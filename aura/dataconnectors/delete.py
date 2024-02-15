import click
from aura.api_command import api_command
from aura.api_repository import make_api_call
from aura.util.get_instance_id import get_instance_id


# pylint: disable=unused-argument
def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@api_command(name="delete", help_text="Delete a data connector")
@click.option("--data-connector-id", "-dcid", prompt=True, help="Mandatory. The ID of the data connector to delete")
@click.option(
    "--yes",
    is_flag=True,
    callback=abort_if_false,
    expose_value=False,
    prompt="Are you sure you want to delete the dataconnector?",
    help="Confirmation flag",
)
def delete_dc(data_connector_id: str):
    """
    Delete a data connector
    Makes "DELETE /data-connectors/:dataConnectorID

    """
    path = f"/data-connectors/{data_connector_id}"

    print("At make_api_call")
    api_response = make_api_call("DELETE", path)

    print(api_response)

    return api_response

