import argparse
import sys
from typing import Mapping, Sequence

import pandas as pd

from exabel_data_sdk import ExabelClient
from exabel_data_sdk.client.api.data_classes.entity import Entity
from exabel_data_sdk.scripts.base_script import BaseScript


class CreateEntitiesFromCsv(BaseScript):
    """
    Processes an input CSV file containing entity names and types to create entities.

    The CSV file should have a header line with the following fields
        entity_resource_name;display_name;description
    subsequently followed by rows of values. The separator is configurable using the
    script argument '--sep' and defaults to ';'. The description field is optional.

    The entity_resource_name is on the following format:
    entityTypes/<entity_type>/entities/<entity_id>

    <entity_type>: an entity type defined in the Exabel platform. May be prefixed with a namespace.
    <entity_id>: must match the regex \w[\w-]{0,63}. May be prefixed with a namespace

    The display_name field is an Entity display_name.

    The description field is one or more paragraphs of text description.

    Example:
        entity_resource_name;display_name;description
        entityTypes/brand/entities/shazam;Shazam;Shazam description
        entityTypes/test.company_and_brand/entities/test.Apple-Shazam;Apple - Shazam;Apple and Shazam description

    """

    def __init__(self, argv: Sequence[str], description: str):
        super().__init__(argv, description)
        self.parser.add_argument(
            "--filename-input",
            required=True,
            type=str,
            help="The URL of the file to parse.",
        )
        self.parser.add_argument(
            "--sep", required=False, type=str, default=";", help="Delimiter to use between cells."
        )

    def check_entity_format(self, entity_name: str) -> None:
        name_parts = entity_name.split("/")
        if len(name_parts) != 4:
            raise ValueError(f"Invalid resource name: {entity_name}")

    def load_entities(
        self, client: ExabelClient, entities_input: pd.DataFrame
    ) -> Mapping[str, Entity]:

        for c in ["entity_resource_name", "display_name"]:
            if c not in entities_input.columns:
                raise ValueError(f"Missing required column in input: {c}")

        result = {}
        for i, entity in entities_input.iterrows():
            entity_name = entity["entity_resource_name"]
            try:
                self.check_entity_format(entity_name)
                name_parts = entity_name.split("/")
                entity_type = f"{name_parts[0]}/{name_parts[1]}"
                if not client.entity_api.entity_exists(entity_name):
                    entity = client.entity_api.create_entity(
                        entity=Entity(
                            name=entity_name,
                            display_name=entity["display_name"],
                            description=entity["description"]
                            if "description" in entities_input.columns
                            else "",
                            properties={},
                        ),
                        entity_type=entity_type,
                    )
                    result[entity_name] = entity
            except Exception as e:
                result[entity_name] = None
        return dict(result)

    def run_script(self, client: ExabelClient, args: argparse.Namespace) -> Mapping[str, Entity]:

        entities_input = pd.read_csv(args.filename_input, header=0, sep=args.sep)
        try:
            res = self.load_entities(client, entities_input)
            return res
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    CreateEntitiesFromCsv(sys.argv, "Create entity mapping.").run()