import click
from aura.api_command import api_command
from aura.api_repository import make_api_call
from aura.util.get_instance_id import get_instance_id


@api_command(name="get", help_text="Get graphql details for a data connector")
@click.option("--data-connector-id", "-dcid", prompt=True, help="Mandatory. The ID of the data connector to get the details")

def get_dataconnector_graphql(data_connector_id: str):
    """
    Get details of a data connectors.

    Makes "GET /data-connectors/:data connector id/graphql" API request.
    """



    path = f"/data-connectors/{data_connector_id}/graphql"

    return make_api_call("GET", path)
