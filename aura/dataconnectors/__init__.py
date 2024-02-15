import click
from .create import create_dc
from .list import list_dataconnectors
from .update import update_dataconnector, update_dataconnector_graphql
from .get import get_dataconnector
from .delete import delete_dc

@click.group(help="Manage your Data connectors")
def dataconnectors():
    pass


dataconnectors.add_command(create_dc)
dataconnectors.add_command(list_dataconnectors)
dataconnectors.add_command(update_dataconnector)
dataconnectors.add_command(get_dataconnector)
dataconnectors.add_command(update_dataconnector_graphql)
dataconnectors.add_command(delete_dc)


