import click
from aura.api_command import api_command
from aura.api_repository import make_api_call

@api_command(name="get", help_text="Get details for a data connector")
@click.option("--data-connector-id", "-id", prompt=True, help="Mandatory. The ID of the data connector to get the details")
@click.option("--type-defs", "-td", is_flag=True, prompt=False, help="Optional.  If given, returns type definitions for a graphql data connector")

def get_dataconnector(data_connector_id: str, type_defs: bool):
    """
    Get details of a data connectors.

    Makes "GET /data-connectors/:data connector id" API request.
    """

    if type_defs:
            path = f"/data-connectors/{data_connector_id}/graphql"
    else:
        path = f"/data-connectors/{data_connector_id}"

    return make_api_call("GET", path)
