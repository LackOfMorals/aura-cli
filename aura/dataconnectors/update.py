import json
import click
from aura.api_command import api_command
from aura.api_repository import make_api_call, make_api_call_and_wait_for_instance_status
from aura.util.get_instance_id import get_instance_id


@api_command(name="update", help_text="Update an instance")
@click.option("--data-connector-id", "-dcid", prompt=True, help="Mandatory. The ID of the data connector to modify")
@click.option("--name", "-n", prompt=True, default="", help="The new data connector name")
@click.option("--instance-id", "-id", prompt=True, default="", help="New Aura instance ID to use with this data connector")
@click.option("--username", "-u", prompt=True, default="", help="New Aura instance DB username")
@click.option("--password", "-p", prompt=True, default="", help="New Aura instance DB username")


def update_dataconnector(data_connector_id: str,
                         name: str,
                         instance_id: str,
                         username : str,
                         password : str):
    """
    Update a data connector.

    Only memory and name can be updated.

    Makes "PATCH /data-connectors/:data connector ID" API request.
    """

    data = {}
    if name:
        data["name"] = name

    if instance_id:
        data["aura_instance"]["id"] = instance_id

    if username:
        data["aura_instance"]["username"] = username

    if password:
        data["aura_instance"]["password"] = password

    path = f"/data-connectors/{data_connector_id}"


    return make_api_call("PATCH", path, data=json.dumps(data))
