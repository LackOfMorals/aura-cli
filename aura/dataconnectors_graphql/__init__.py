import click
from .update import update_dataconnector_graphql
from .get import get_dataconnector_graphql

@click.group(help="Manage your GraphQL Data connectors")
def dataconnectors_graphql():
    pass

dataconnectors_graphql.add_command(update_dataconnector_graphql)
dataconnectors_graphql.add_command(get_dataconnector_graphql)

