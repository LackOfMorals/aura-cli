import json
import click
from aura.api_command import api_command
from aura.api_repository import make_api_call, make_api_call_and_wait_for_instance_status
from aura.config_repository import CLIConfig
from aura.decorators import pass_config


# pylint: disable=redefined-builtin
@api_command(name="create", help_text="Create a new data connector")
@click.option("--name", "-n", prompt=True, help="The data connector name")
@click.option("--type", "-t", prompt=True, help="The data connector type - graphql")
@click.option("--instance-id", "-id", prompt=True, help="The Aura instance ID to use with this data connector")
@click.option("--username", "-u", prompt=True, help="The Aura instance DB username")
@click.option("--password", "-p", prompt=True, help="The Aura instance DB username")
@click.option("--type-defs", "-td", help="The GraphQL type definitions to use with the data connector")

@pass_config
def create_dc(
    config: CLIConfig,
    name: str,
    type: str,
    instance_id : str,
    username : str,
    password : str,
    type_defs : str,
    wait: bool,
):
    """
    Create a new data connector with the specified options.

    Makes "POST /data-connectors" API request.
    """

    path = "/data-connectors"

    data = {
        {
            "name": name,
            "type": type,
            "aura_instance": {
                "id": instance_id,
                "username": username,
                "password": password
            },
            "data_connector": {
                "graphql": {
                    "type_definitions": type_defs
                }
            }
        }
    }

    if wait:
        return make_api_call_and_wait_for_instance_status(
            "POST", path, "running", data=json.dumps(data)
        )

    return make_api_call("POST", path, data=json.dumps(data))
