import os
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants


# client->database->container->item
def get_db_object():
    url = os.getenv("ACCOUNT_URL")
    key = os.getenv("ACCOUNT_KEY")
    client = cosmos_client.CosmosClient(url, {"masterKey": key})
    database = client.get_database_client("punchd")
    container = database.get_container_client("punchdnew")
    return container


def verify_user_unique(user):
    db = get_db_object()
    try:
        item = None
        item = db.read_item(item=user.user_id, partition_key=user.user_id)
    except errors.CosmosResourceNotFoundError:
        # We expect not to find the user
        pass
    if item:
        raise errors.HTTPFailure(
            http_constants.StatusCodes.BAD_REQUEST,
            "User already exists",
            {"message": "User already exists"},)
