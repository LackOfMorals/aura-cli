import json
import click
from aura.api_command import api_command
from aura.api_repository import make_api_call, make_api_call_and_wait_for_instance_status
from aura.util.get_instance_id import get_instance_id


@api_command(name="update", help_text="Update an instance")
@click.option("--data-connector-id", "-dcid", prompt=True, help="Mandatory. The ID of the data connector to modify")
@click.option("--type-defs", "-td", prompt=True, help="The GraphQL type definitions to use with the data connector")


def update_dataconnector_graphql(data_connector_id: str,
                         type_defs: str):
    """
    Update type defs for a graphql data connector.

    Makes "PATCH /data-connectors/:data connector ID/graphql" API request.
    """

    data = {}

    if type_defs:
        data["type_definitions"] = type_defs

        path = f"/data-connectors/{data_connector_id}"

        return make_api_call("PATCH", path, data=json.dumps(data))

    else:
        return { "No type defs given"}

