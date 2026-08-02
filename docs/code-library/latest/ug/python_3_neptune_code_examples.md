---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_neptune_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Neptune examples using SDK for Python (Boto3)
<a name="python_3_neptune_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Neptune.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello Neptune
<a name="neptune_Hello_python_3_topic"></a>

The following code example shows how to get started using Neptune.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
import boto3
from botocore.exceptions import ClientError

def describe_db_clusters(neptune_client):
    """
    Describes the Amazon Neptune DB clusters using a paginator to handle multiple pages.
    Raises ClientError with 'ResourceNotFoundException' if no clusters are found.
    """
    paginator = neptune_client.get_paginator("describe_db_clusters")
    clusters_found = False

    for page in paginator.paginate():
        for cluster in page.get("DBClusters", []):
            clusters_found = True
            print(f"Cluster Identifier: {cluster['DBClusterIdentifier']}")
            print(f"Status: {cluster['Status']}")

    if not clusters_found:
        raise ClientError(
            {
                "Error": {
                    "Code": "ResourceNotFoundException",
                    "Message": "No Neptune DB clusters found."
                }
            },
            operation_name="DescribeDBClusters"
        )

def main():
    """
    Main entry point: creates the Neptune client and calls the describe operation.
    """
    neptune_client = boto3.client("neptune")
    try:
        describe_db_clusters(neptune_client)
    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code == "ResourceNotFoundException":
            print(f"Resource not found: {e.response['Error']['Message']}")
        else:
            print(f"Unexpected ClientError: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [DescribeDBClustersPaginator](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClustersPaginator) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="neptune_Scenario_python_3_topic"></a>

The following code example shows how to:
+ Create an Amazon Neptune Subnet Group.
+ Create an Neptune Cluster.
+ Create an Neptune Instance.
+ Check the status of the Neptune Instance.
+ Show Neptune cluster details.
+ Stop the Neptune cluster.
+ Start the Neptune cluster.
+ Delete the Neptune Assets.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
import boto3
import time
from botocore.exceptions import ClientError

# Constants used in this scenario
POLL_INTERVAL_SECONDS = 10
TIMEOUT_SECONDS = 1200  # 20 minutes

def delete_db_cluster(neptune_client, cluster_id: str):
    """
    Deletes a Neptune DB cluster and throws exceptions to the caller.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        cluster_id (str): The ID of the Neptune DB cluster to be deleted.

    Raises:
        ClientError: If the delete operation fails.
    """
    request = {
        'DBClusterIdentifier': cluster_id,
        'SkipFinalSnapshot': True
    }

    try:
        print(f"Deleting DB Cluster: {cluster_id}")
        neptune_client.delete_db_cluster(**request)

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBClusterNotFoundFault":
            print(f"Cluster '{cluster_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB cluster. {code}: {message}")
        raise

def format_elapsed_time(seconds: int) -> str:
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

def delete_db_instance(neptune_client, instance_id: str):
    """
    Deletes a Neptune DB instance and waits for its deletion to complete.
    Raises exception to be handled by calling code.
    """
    print(f"Initiating deletion of DB Instance: {instance_id}")
    try:
        neptune_client.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=True
        )

        print(f"Waiting for DB Instance '{instance_id}' to be deleted...")
        waiter = neptune_client.get_waiter('db_instance_deleted')
        waiter.wait(
            DBInstanceIdentifier=instance_id,
            WaiterConfig={
                'Delay': 30,
                'MaxAttempts': 40
            }
        )

        print(f"DB Instance '{instance_id}' successfully deleted.")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBInstanceNotFoundFault":
            print(f"Instance '{instance_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB instance. {code}: {message}")
        raise

def delete_db_subnet_group(neptune_client, subnet_group_name):
    """
    Deletes a Neptune DB subnet group synchronously using Boto3.

    Args:
        neptune_client (boto3.client): The Neptune client.
        subnet_group_name (str): The name of the DB subnet group to delete.

    Raises:
        ClientError: If the delete operation fails.
    """
    delete_group_request = {
        'DBSubnetGroupName': subnet_group_name
    }

    try:
        neptune_client.delete_db_subnet_group(**delete_group_request)
        print(f"️ Deleting Subnet Group: {subnet_group_name}")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBSubnetGroupNotFoundFault":
            print(f"Subnet group '{subnet_group_name}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete subnet group. {code}: {message}")
        raise

def wait_for_cluster_status(
        neptune_client,
        cluster_id: str,
        desired_status: str,
        timeout_seconds: int = TIMEOUT_SECONDS,
        poll_interval_seconds: int = POLL_INTERVAL_SECONDS
):
    """
    Waits for a Neptune DB cluster to reach a desired status.

    Args:
        neptune_client (boto3.client): The Amazon Neptune client.
        cluster_id (str): The identifier of the Neptune DB cluster.
        desired_status (str): The target status (e.g., "available", "stopped").
        timeout_seconds (int): Max time to wait in seconds (default: 1200).
        poll_interval_seconds (int): Polling interval in seconds (default: 10).

    Raises:
        RuntimeError: If the desired status is not reached before timeout.
    """
    print(f"Waiting for cluster '{cluster_id}' to reach status '{desired_status}'...")
    start_time = time.time()

    while True:
        # Prepare request object
        describe_cluster_request = {
            'DBClusterIdentifier': cluster_id
        }

        # Call the Neptune API
        response = neptune_client.describe_db_clusters(**describe_cluster_request)
        clusters = response.get('DBClusters', [])
        current_status = clusters[0].get('Status') if clusters else None
        elapsed_seconds = int(time.time() - start_time)

        status_str = current_status if current_status else "Unknown"
        print(
            f"\r Elapsed: {format_elapsed_time(elapsed_seconds):<20}  Cluster status: {status_str:<20}",
            end="", flush=True
        )

        if current_status and current_status.lower() == desired_status.lower():
            print(
                f"\nNeptune cluster reached desired status '{desired_status}' after {format_elapsed_time(elapsed_seconds)}."
            )
            return

        if elapsed_seconds > timeout_seconds:
            raise RuntimeError(f"Timeout waiting for Neptune cluster to reach status: {desired_status}")

        time.sleep(poll_interval_seconds)

def start_db_cluster(neptune_client, cluster_identifier: str):
    """
    Starts an Amazon Neptune DB cluster and waits until it reaches 'available'.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_identifier (str): The DB cluster identifier.

    Raises:
        ClientError: Propagates AWS API issues like resource not found.
        RuntimeError: If cluster doesn't reach 'available' within timeout.
    """
    try:
        # Initial wait in case the cluster was just stopped
        time.sleep(30)
        neptune_client.start_db_cluster(DBClusterIdentifier=cluster_identifier)
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't start DB cluster. Here's why: {code}: {message}")
        raise

    start_time = time.time()
    paginator = neptune_client.get_paginator('describe_db_clusters')

    while True:
        try:
            pages = paginator.paginate(DBClusterIdentifier=cluster_identifier)
            clusters = []
            for page in pages:
                clusters.extend(page.get('DBClusters', []))
        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBClusterNotFound":
                print(f"Cluster '{cluster_identifier}' not found while polling. It may have been deleted.")
            else:
                print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
            raise

        status = clusters[0].get('Status') if clusters else None
        elapsed = time.time() - start_time

        print(f"\rElapsed: {int(elapsed)}s – Cluster status: {status}", end="", flush=True)

        if status and status.lower() == 'available':
            print(f"\n🎉 Cluster '{cluster_identifier}' is available.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for cluster '{cluster_identifier}' to become available.")

        time.sleep(POLL_INTERVAL_SECONDS)

def stop_db_cluster(neptune_client, cluster_identifier: str):
    """
    Stops an Amazon Neptune DB cluster and waits until it's fully stopped.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_identifier (str): The DB cluster identifier.

    Raises:
        ClientError: For AWS API errors (e.g., resource not found).
        RuntimeError: If the cluster doesn't stop within the timeout.
    """
    try:
        neptune_client.stop_db_cluster(DBClusterIdentifier=cluster_identifier)
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't stop DB cluster. Here's why: {code}: {message}")
        raise

    start_time = time.time()
    paginator = neptune_client.get_paginator('describe_db_clusters')

    while True:
        try:
            pages = paginator.paginate(DBClusterIdentifier=cluster_identifier)
            clusters = []
            for page in pages:
                clusters.extend(page.get('DBClusters', []))
        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBClusterNotFound":
                print(f"Cluster '{cluster_identifier}' not found while polling. It may have been deleted.")
            else:
                print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
            raise

        status = clusters[0].get('Status') if clusters else None
        elapsed = time.time() - start_time

        print(f"\rElapsed: {int(elapsed)}s – Cluster status: {status}", end="", flush=True)

        if status and status.lower() == 'stopped':
            print(f"\nCluster '{cluster_identifier}' is now stopped.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for cluster '{cluster_identifier}' to stop.")

        time.sleep(POLL_INTERVAL_SECONDS)

def describe_db_clusters(neptune_client, cluster_id: str):
    """
    Describes details of a Neptune DB cluster, paginating if needed.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_id (str): The ID of the cluster to describe.

    Raises:
        ClientError: If there's an AWS API error (e.g., cluster not found).
    """
    paginator = neptune_client.get_paginator('describe_db_clusters')

    try:
        pages = paginator.paginate(DBClusterIdentifier=cluster_id)

        found = False
        for page in pages:
            for cluster in page.get('DBClusters', []):
                found = True
                print(f"Cluster Identifier: {cluster.get('DBClusterIdentifier')}")
                print(f"Status: {cluster.get('Status')}")
                print(f"Engine: {cluster.get('Engine')}")
                print(f"Engine Version: {cluster.get('EngineVersion')}")
                print(f"Endpoint: {cluster.get('Endpoint')}")
                print(f"Reader Endpoint: {cluster.get('ReaderEndpoint')}")
                print(f"Availability Zones: {cluster.get('AvailabilityZones')}")
                print(f"Subnet Group: {cluster.get('DBSubnetGroup')}")
                print("VPC Security Groups:")
                for vpc_group in cluster.get('VpcSecurityGroups', []):
                    print(f"  - {vpc_group.get('VpcSecurityGroupId')}")
                print(f"Storage Encrypted: {cluster.get('StorageEncrypted')}")
                print(f"IAM Auth Enabled: {cluster.get('IAMDatabaseAuthenticationEnabled')}")
                print(f"Backup Retention Period: {cluster.get('BackupRetentionPeriod')} days")
                print(f"Preferred Backup Window: {cluster.get('PreferredBackupWindow')}")
                print(f"Preferred Maintenance Window: {cluster.get('PreferredMaintenanceWindow')}")
                print("------")

        if not found:
            # Treat empty response as cluster not found
            raise ClientError(
                {"Error": {"Code": "DBClusterNotFound", "Message": f"No cluster found with ID '{cluster_id}'"}},
                "DescribeDBClusters"
            )

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        elif code == "DBClusterNotFound":
            print(f"Cluster '{cluster_id}' not found. Please verify the cluster ID.")
        else:
            print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
        raise

def check_instance_status(neptune_client, instance_id: str, desired_status: str):
    """
    Polls the status of a Neptune DB instance until it reaches desired_status.
    Uses pagination via describe_db_instances — even for a single instance.

    Raises:
      ClientError: If describe_db_instances fails (e.g., instance not found).
      RuntimeError: If timeout expires before reaching desired status.
    """
    paginator = neptune_client.get_paginator('describe_db_instances')
    start_time = time.time()

    while True:
        try:
            pages = paginator.paginate(DBInstanceIdentifier=instance_id)
            instances = []
            for page in pages:
                instances.extend(page.get('DBInstances', []))

        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBInstanceNotFound":
                print(f"Instance '{instance_id}' not found. Please verify the instance ID.")
            else:
                print(f"Failed to describe DB instance. {code}: {message}")
            raise

        current_status = instances[0].get('DBInstanceStatus') if instances else None
        elapsed = int(time.time() - start_time)

        print(f"\rElapsed: {format_elapsed_time(elapsed)}  Status: {current_status}", end="", flush=True)

        if current_status and current_status.lower() == desired_status.lower():
            print(f"\nInstance '{instance_id}' reached '{desired_status}' in {format_elapsed_time(elapsed)}.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for '{instance_id}' to reach '{desired_status}'")

        time.sleep(POLL_INTERVAL_SECONDS)

def create_db_instance(neptune_client, db_instance_id: str, db_cluster_id: str) -> str:
    try:
        request = {
            'DBInstanceIdentifier': db_instance_id,
            'DBInstanceClass': 'db.r5.large',
            'Engine': 'neptune',
            'DBClusterIdentifier': db_cluster_id
        }

        print(f"Creating Neptune DB Instance: {db_instance_id}")
        response = neptune_client.create_db_instance(**request)

        instance = response.get('DBInstance')
        if not instance or 'DBInstanceIdentifier' not in instance:
            raise RuntimeError("Instance creation succeeded but no ID returned.")

        print(f"Waiting for DB Instance '{db_instance_id}' to become available...")
        waiter = neptune_client.get_waiter('db_instance_available')
        waiter.wait(
            DBInstanceIdentifier=db_instance_id,
            WaiterConfig={'Delay': 30, 'MaxAttempts': 40}
        )

        print(f"DB Instance '{db_instance_id}' is now available.")
        return instance['DBInstanceIdentifier']

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't create DB instance. Here's why: {code}: {message}")
        raise

    except Exception as e:
        print(f"Unexpected error creating DB instance '{db_instance_id}': {e}")
        raise RuntimeError(f"Unexpected error creating DB instance '{db_instance_id}': {e}") from e

def create_db_cluster(neptune_client, db_name: str) -> str:
    """
    Creates a Neptune DB cluster and returns its identifier.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        db_name (str): The desired cluster identifier.

    Returns:
        str: The DB cluster identifier.

    Raises:
        RuntimeError: For any failure or AWS error, with a user-friendly message.
    """
    request = {
        'DBClusterIdentifier': db_name,
        'Engine': 'neptune',
        'DeletionProtection': False,
        'BackupRetentionPeriod': 1
    }

    try:
        response = neptune_client.create_db_cluster(**request)
        cluster = response.get('DBCluster') or {}

        cluster_id = cluster.get('DBClusterIdentifier')
        if not cluster_id:
            raise RuntimeError("Cluster created but no ID returned.")

        print(f"DB Cluster created: {cluster_id}")
        return cluster_id

    except ClientError as e:
        code = e.response["Error"]["Code"]
        message = e.response["Error"]["Message"]

        if code in ("ServiceQuotaExceededException", "DBClusterQuotaExceededFault"):
            raise RuntimeError("You have exceeded the quota for Neptune DB clusters.") from e
        else:
            raise RuntimeError(f"AWS error [{code}]: {message}") from e

    except Exception as e:
        raise RuntimeError(f"Unexpected error creating DB cluster '{db_name}': {e}") from e

def get_subnet_ids(vpc_id: str) -> list[str]:
    ec2_client = boto3.client('ec2')

    describe_subnets_request = {
        'Filters': [{'Name': 'vpc-id', 'Values': [vpc_id]}]
    }

    response = ec2_client.describe_subnets(**describe_subnets_request)
    subnets = response.get('Subnets', [])
    subnet_ids = [subnet['SubnetId'] for subnet in subnets if 'SubnetId' in subnet]
    return subnet_ids

def get_default_vpc_id() -> str:
    ec2_client = boto3.client('ec2')
    describe_vpcs_request = {
        'Filters': [{'Name': 'isDefault', 'Values': ['true']}]
    }

    response = ec2_client.describe_vpcs(**describe_vpcs_request)
    vpcs = response.get('Vpcs', [])
    if not vpcs:
        raise RuntimeError("No default VPC found in this region.")

    default_vpc_id = vpcs[0]['VpcId']
    print(f"Default VPC ID: {default_vpc_id}")
    return default_vpc_id

def create_subnet_group(neptune_client, group_name: str):
    """
    Creates a Neptune DB subnet group and returns its name and ARN.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        group_name (str): The desired name of the subnet group.

    Returns:
        tuple(str, str): (subnet_group_name, subnet_group_arn)

    Raises:
        RuntimeError: For quota errors or other AWS-related failures.
    """
    vpc_id = get_default_vpc_id()
    subnet_ids = get_subnet_ids(vpc_id)

    request = {
        'DBSubnetGroupName': group_name,
        'DBSubnetGroupDescription': 'My Neptune subnet group',
        'SubnetIds': subnet_ids,
        'Tags': [{'Key': 'Environment', 'Value': 'Dev'}]
    }

    try:
        response = neptune_client.create_db_subnet_group(**request)
        sg = response.get("DBSubnetGroup", {})
        name = sg.get("DBSubnetGroupName")
        arn = sg.get("DBSubnetGroupArn")

        if not name or not arn:
            raise RuntimeError("Response missing subnet group name or ARN.")

        print(f"Subnet group created: {name}")
        print(f"ARN: {arn}")
        return name, arn

    except ClientError as e:
        code = e.response["Error"]["Code"]
        msg = e.response["Error"]["Message"]

        if code == "ServiceQuotaExceededException":
            print("Subnet group quota exceeded.")
            raise RuntimeError("Subnet group quota exceeded.") from e
        else:
            print(f"AWS error [{code}]: {msg}")
            raise RuntimeError(f"AWS error [{code}]: {msg}") from e

    except Exception as e:
        print(f"Unexpected error creating subnet group '{group_name}': {e}")
        raise RuntimeError(f"Unexpected error creating subnet group '{group_name}': {e}") from e

def wait_for_input_to_continue():
    input("\nPress <ENTER> to continue...")
    print("Continuing with the program...\n")

def run_scenario(neptune_client, subnet_group_name: str, db_instance_id: str, cluster_name: str):
    print("-" * 88)
    print("1. Create a Neptune DB Subnet Group")
    wait_for_input_to_continue()

    try:
        name, arn = create_subnet_group(neptune_client, subnet_group_name)
        print(f"Subnet group successfully created: {name}")

        print("-" * 88)
        print("2. Create a Neptune Cluster")
        wait_for_input_to_continue()
        db_cluster_id = create_db_cluster(neptune_client, cluster_name)

        print("-" * 88)
        print("3. Create a Neptune DB Instance")
        wait_for_input_to_continue()
        create_db_instance(neptune_client, db_instance_id, cluster_name)

        print("-" * 88)
        print("4. Check the status of the Neptune DB Instance")
        print("""
        Even though you're targeting a single DB instance,
        describe_db_instances supports pagination and can return multiple pages.

        Handling paginated responses ensures your method continues to work reliably
        even if AWS returns large or paged results.
        """)
        wait_for_input_to_continue()
        check_instance_status(neptune_client, db_instance_id, "available")

        print("-" * 88)
        print("5. Show Neptune Cluster details")
        wait_for_input_to_continue()
        describe_db_clusters(neptune_client, db_cluster_id)

        print("-" * 88)
        print("6. Stop the Amazon Neptune cluster")
        print("""
            Boto3 doesn't currently offer a
            built-in waiter for stop_db_cluster,
            This example implements a custom polling
            strategy until the cluster is in a stopped state.
        """)
        wait_for_input_to_continue()
        stop_db_cluster(neptune_client, db_cluster_id)
        check_instance_status(neptune_client, db_instance_id, "stopped")

        print("-" * 88)
        print("7. Start the Amazon Neptune cluster")
        print("""
            Boto3 doesn't currently offer a
            built-in waiter for start_db_cluster,
            This example implements a custom polling
            strategy until the cluster is in an available state.
        """)
        wait_for_input_to_continue()
        start_db_cluster(neptune_client, db_cluster_id)
        wait_for_cluster_status(neptune_client, db_cluster_id, "available")
        check_instance_status(neptune_client, db_instance_id, "available")

        print("All Neptune resources are now available.")
        print("-" * 88)

        print("-" * 88)
        print("8. Delete the Neptune Assets")
        print("Would you like to delete the Neptune Assets? (y/n)")
        del_ans = input().strip().lower()

        if del_ans == "y":
            print("You selected to delete the Neptune assets.")

            delete_db_instance(neptune_client, db_instance_id)
            delete_db_cluster(neptune_client, db_cluster_id)
            delete_db_subnet_group(neptune_client, subnet_group_name)

            print("Neptune resources deleted successfully")

    except ClientError as ce:
        code = ce.response["Error"]["Code"]

        if code in ("DBInstanceNotFound", "DBInstanceNotFoundFault", "ResourceNotFound"):
            print(f"Instance '{db_instance_id}' not found.")
        elif code in ("DBClusterNotFound", "DBClusterNotFoundFault", "ResourceNotFoundFault"):
            print(f"Cluster '{cluster_name}' not found.")
        elif code == "DBSubnetGroupNotFoundFault":
            print(f"Subnet group '{subnet_group_name}' not found.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"AWS error [{code}]: {ce.response['Error']['Message']}")
            raise  # re-raise unexpected errors

    except RuntimeError as re:
        print(f"Runtime error or timeout: {re}")

def main():
    neptune_client = boto3.client('neptune')

    # Customize the following names to match your Neptune setup
    # (You must change these to unique values for your environment)
    subnet_group_name = "neptuneSubnetGroup111"
    cluster_name = "neptuneCluster111"
    db_instance_id = "neptuneDB111"

    print("""
    Amazon Neptune is a fully managed graph database service by AWS...
    Let's get started!
    """)
    wait_for_input_to_continue()
    run_scenario(neptune_client, subnet_group_name, db_instance_id, cluster_name)

    print("""
    Thank you for checking out the Amazon Neptune Service Use demo.
    For more AWS code examples, visit:
    https://docs.aws.amazon.com/code-library/latest/ug/what-is-code-library.html
    """)

if __name__ == "__main__":
    main()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBCluster)
  + [CreateDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBInstance)
  + [CreateDBSubnetGroup](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBSubnetGroup)
  + [CreateGraph](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateGraph)
  + [DeleteDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBCluster)
  + [DeleteDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBInstance)
  + [DeleteDBSubnetGroup](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBSubnetGroup)
  + [DescribeDBClusters](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusters)
  + [DescribeDBInstances](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBInstances)
  + [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteGremlinProfileQuery)
  + [ExecuteGremlinQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteGremlinQuery)
  + [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteOpenCypherExplainQuery)
  + [ExecuteQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteQuery)
  + [StartDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StartDBCluster)
  + [StopDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StopDBCluster)

## Actions
<a name="actions"></a>

### `CreateDBCluster`
<a name="neptune_CreateDBCluster_python_3_topic"></a>

The following code example shows how to use `CreateDBCluster`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def create_db_cluster(neptune_client, db_name: str) -> str:
    """
    Creates a Neptune DB cluster and returns its identifier.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        db_name (str): The desired cluster identifier.

    Returns:
        str: The DB cluster identifier.

    Raises:
        RuntimeError: For any failure or AWS error, with a user-friendly message.
    """
    request = {
        'DBClusterIdentifier': db_name,
        'Engine': 'neptune',
        'DeletionProtection': False,
        'BackupRetentionPeriod': 1
    }

    try:
        response = neptune_client.create_db_cluster(**request)
        cluster = response.get('DBCluster') or {}

        cluster_id = cluster.get('DBClusterIdentifier')
        if not cluster_id:
            raise RuntimeError("Cluster created but no ID returned.")

        print(f"DB Cluster created: {cluster_id}")
        return cluster_id

    except ClientError as e:
        code = e.response["Error"]["Code"]
        message = e.response["Error"]["Message"]

        if code in ("ServiceQuotaExceededException", "DBClusterQuotaExceededFault"):
            raise RuntimeError("You have exceeded the quota for Neptune DB clusters.") from e
        else:
            raise RuntimeError(f"AWS error [{code}]: {message}") from e

    except Exception as e:
        raise RuntimeError(f"Unexpected error creating DB cluster '{db_name}': {e}") from e
```
+  For API details, see [CreateDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBCluster) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateDBInstance`
<a name="neptune_CreateDBInstance_python_3_topic"></a>

The following code example shows how to use `CreateDBInstance`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def create_db_instance(neptune_client, db_instance_id: str, db_cluster_id: str) -> str:
    try:
        request = {
            'DBInstanceIdentifier': db_instance_id,
            'DBInstanceClass': 'db.r5.large',
            'Engine': 'neptune',
            'DBClusterIdentifier': db_cluster_id
        }

        print(f"Creating Neptune DB Instance: {db_instance_id}")
        response = neptune_client.create_db_instance(**request)

        instance = response.get('DBInstance')
        if not instance or 'DBInstanceIdentifier' not in instance:
            raise RuntimeError("Instance creation succeeded but no ID returned.")

        print(f"Waiting for DB Instance '{db_instance_id}' to become available...")
        waiter = neptune_client.get_waiter('db_instance_available')
        waiter.wait(
            DBInstanceIdentifier=db_instance_id,
            WaiterConfig={'Delay': 30, 'MaxAttempts': 40}
        )

        print(f"DB Instance '{db_instance_id}' is now available.")
        return instance['DBInstanceIdentifier']

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't create DB instance. Here's why: {code}: {message}")
        raise

    except Exception as e:
        print(f"Unexpected error creating DB instance '{db_instance_id}': {e}")
        raise RuntimeError(f"Unexpected error creating DB instance '{db_instance_id}': {e}") from e
```
+  For API details, see [CreateDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBInstance) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateDBSubnetGroup`
<a name="neptune_CreateDBSubnetGroup_python_3_topic"></a>

The following code example shows how to use `CreateDBSubnetGroup`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def create_subnet_group(neptune_client, group_name: str):
    """
    Creates a Neptune DB subnet group and returns its name and ARN.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        group_name (str): The desired name of the subnet group.

    Returns:
        tuple(str, str): (subnet_group_name, subnet_group_arn)

    Raises:
        RuntimeError: For quota errors or other AWS-related failures.
    """
    vpc_id = get_default_vpc_id()
    subnet_ids = get_subnet_ids(vpc_id)

    request = {
        'DBSubnetGroupName': group_name,
        'DBSubnetGroupDescription': 'My Neptune subnet group',
        'SubnetIds': subnet_ids,
        'Tags': [{'Key': 'Environment', 'Value': 'Dev'}]
    }

    try:
        response = neptune_client.create_db_subnet_group(**request)
        sg = response.get("DBSubnetGroup", {})
        name = sg.get("DBSubnetGroupName")
        arn = sg.get("DBSubnetGroupArn")

        if not name or not arn:
            raise RuntimeError("Response missing subnet group name or ARN.")

        print(f"Subnet group created: {name}")
        print(f"ARN: {arn}")
        return name, arn

    except ClientError as e:
        code = e.response["Error"]["Code"]
        msg = e.response["Error"]["Message"]

        if code == "ServiceQuotaExceededException":
            print("Subnet group quota exceeded.")
            raise RuntimeError("Subnet group quota exceeded.") from e
        else:
            print(f"AWS error [{code}]: {msg}")
            raise RuntimeError(f"AWS error [{code}]: {msg}") from e

    except Exception as e:
        print(f"Unexpected error creating subnet group '{group_name}': {e}")
        raise RuntimeError(f"Unexpected error creating subnet group '{group_name}': {e}") from e
```
+  For API details, see [CreateDBSubnetGroup](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBSubnetGroup) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateGraph`
<a name="neptune_CreateGraph_python_3_topic"></a>

The following code example shows how to use `CreateGraph`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
"""
Running this example.

----------------------------------------------------------------------------------
VPC Networking Requirement:
----------------------------------------------------------------------------------
Amazon Neptune must be accessed from **within the same VPC** as the Neptune cluster.
It does not expose a public endpoint, so this code must be executed from:

  - An **AWS Lambda function** configured to run inside the same VPC
  - An **EC2 instance** or **ECS task** running in the same VPC
  - A connected environment such as a **VPN**, **AWS Direct Connect**, or a **peered VPC**

"""

GRAPH_NAME = "sample-analytics-graph"

def main():
    config = Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)
    client = boto3.client("neptune-graph", config=config)
    execute_create_graph(client, GRAPH_NAME)

def execute_create_graph(client, graph_name):
    try:
        print("Creating Neptune graph...")
        response = client.create_graph(
            graphName=graph_name,
            provisionedMemory = 16
        )

        created_graph_name = response.get("name")
        graph_arn = response.get("arn")
        graph_endpoint = response.get("endpoint")

        print("Graph created successfully!")
        print(f"Graph Name: {created_graph_name}")
        print(f"Graph ARN: {graph_arn}")
        print(f"Graph Endpoint: {graph_endpoint}")

    except ClientError as e:
        print(f"Failed to create graph: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"Failed to create graph: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [CreateGraph](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateGraph) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteDBCluster`
<a name="neptune_DeleteDBCluster_python_3_topic"></a>

The following code example shows how to use `DeleteDBCluster`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def delete_db_cluster(neptune_client, cluster_id: str):
    """
    Deletes a Neptune DB cluster and throws exceptions to the caller.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        cluster_id (str): The ID of the Neptune DB cluster to be deleted.

    Raises:
        ClientError: If the delete operation fails.
    """
    request = {
        'DBClusterIdentifier': cluster_id,
        'SkipFinalSnapshot': True
    }

    try:
        print(f"Deleting DB Cluster: {cluster_id}")
        neptune_client.delete_db_cluster(**request)

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBClusterNotFoundFault":
            print(f"Cluster '{cluster_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB cluster. {code}: {message}")
        raise
```
+  For API details, see [DeleteDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBCluster) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteDBInstance`
<a name="neptune_DeleteDBInstance_python_3_topic"></a>

The following code example shows how to use `DeleteDBInstance`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def delete_db_instance(neptune_client, instance_id: str):
    """
    Deletes a Neptune DB instance and waits for its deletion to complete.
    Raises exception to be handled by calling code.
    """
    print(f"Initiating deletion of DB Instance: {instance_id}")
    try:
        neptune_client.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=True
        )

        print(f"Waiting for DB Instance '{instance_id}' to be deleted...")
        waiter = neptune_client.get_waiter('db_instance_deleted')
        waiter.wait(
            DBInstanceIdentifier=instance_id,
            WaiterConfig={
                'Delay': 30,
                'MaxAttempts': 40
            }
        )

        print(f"DB Instance '{instance_id}' successfully deleted.")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBInstanceNotFoundFault":
            print(f"Instance '{instance_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB instance. {code}: {message}")
        raise
```
+  For API details, see [DeleteDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBInstance) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteDBSubnetGroup`
<a name="neptune_DeleteDBSubnetGroup_python_3_topic"></a>

The following code example shows how to use `DeleteDBSubnetGroup`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def delete_db_subnet_group(neptune_client, subnet_group_name):
    """
    Deletes a Neptune DB subnet group synchronously using Boto3.

    Args:
        neptune_client (boto3.client): The Neptune client.
        subnet_group_name (str): The name of the DB subnet group to delete.

    Raises:
        ClientError: If the delete operation fails.
    """
    delete_group_request = {
        'DBSubnetGroupName': subnet_group_name
    }

    try:
        neptune_client.delete_db_subnet_group(**delete_group_request)
        print(f"️ Deleting Subnet Group: {subnet_group_name}")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBSubnetGroupNotFoundFault":
            print(f"Subnet group '{subnet_group_name}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete subnet group. {code}: {message}")
        raise
```
+  For API details, see [DeleteDBSubnetGroup](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBSubnetGroup) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeDBClusters`
<a name="neptune_DescribeDBClusters_python_3_topic"></a>

The following code example shows how to use `DescribeDBClusters`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def describe_db_clusters(neptune_client, cluster_id: str):
    """
    Describes details of a Neptune DB cluster, paginating if needed.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_id (str): The ID of the cluster to describe.

    Raises:
        ClientError: If there's an AWS API error (e.g., cluster not found).
    """
    paginator = neptune_client.get_paginator('describe_db_clusters')

    try:
        pages = paginator.paginate(DBClusterIdentifier=cluster_id)

        found = False
        for page in pages:
            for cluster in page.get('DBClusters', []):
                found = True
                print(f"Cluster Identifier: {cluster.get('DBClusterIdentifier')}")
                print(f"Status: {cluster.get('Status')}")
                print(f"Engine: {cluster.get('Engine')}")
                print(f"Engine Version: {cluster.get('EngineVersion')}")
                print(f"Endpoint: {cluster.get('Endpoint')}")
                print(f"Reader Endpoint: {cluster.get('ReaderEndpoint')}")
                print(f"Availability Zones: {cluster.get('AvailabilityZones')}")
                print(f"Subnet Group: {cluster.get('DBSubnetGroup')}")
                print("VPC Security Groups:")
                for vpc_group in cluster.get('VpcSecurityGroups', []):
                    print(f"  - {vpc_group.get('VpcSecurityGroupId')}")
                print(f"Storage Encrypted: {cluster.get('StorageEncrypted')}")
                print(f"IAM Auth Enabled: {cluster.get('IAMDatabaseAuthenticationEnabled')}")
                print(f"Backup Retention Period: {cluster.get('BackupRetentionPeriod')} days")
                print(f"Preferred Backup Window: {cluster.get('PreferredBackupWindow')}")
                print(f"Preferred Maintenance Window: {cluster.get('PreferredMaintenanceWindow')}")
                print("------")

        if not found:
            # Treat empty response as cluster not found
            raise ClientError(
                {"Error": {"Code": "DBClusterNotFound", "Message": f"No cluster found with ID '{cluster_id}'"}},
                "DescribeDBClusters"
            )

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        elif code == "DBClusterNotFound":
            print(f"Cluster '{cluster_id}' not found. Please verify the cluster ID.")
        else:
            print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
        raise
```
+  For API details, see [DescribeDBClusters](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBClusters) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeDBInstances`
<a name="neptune_DescribeDBInstances_python_3_topic"></a>

The following code example shows how to use `DescribeDBInstances`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def check_instance_status(neptune_client, instance_id: str, desired_status: str):
    """
    Polls the status of a Neptune DB instance until it reaches desired_status.
    Uses pagination via describe_db_instances — even for a single instance.

    Raises:
      ClientError: If describe_db_instances fails (e.g., instance not found).
      RuntimeError: If timeout expires before reaching desired status.
    """
    paginator = neptune_client.get_paginator('describe_db_instances')
    start_time = time.time()

    while True:
        try:
            pages = paginator.paginate(DBInstanceIdentifier=instance_id)
            instances = []
            for page in pages:
                instances.extend(page.get('DBInstances', []))

        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBInstanceNotFound":
                print(f"Instance '{instance_id}' not found. Please verify the instance ID.")
            else:
                print(f"Failed to describe DB instance. {code}: {message}")
            raise

        current_status = instances[0].get('DBInstanceStatus') if instances else None
        elapsed = int(time.time() - start_time)

        print(f"\rElapsed: {format_elapsed_time(elapsed)}  Status: {current_status}", end="", flush=True)

        if current_status and current_status.lower() == desired_status.lower():
            print(f"\nInstance '{instance_id}' reached '{desired_status}' in {format_elapsed_time(elapsed)}.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for '{instance_id}' to reach '{desired_status}'")

        time.sleep(POLL_INTERVAL_SECONDS)
```
+  For API details, see [DescribeDBInstances](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBInstances) in *AWS SDK for Python (Boto3) API Reference*.

### `ExecuteGremlinProfileQuery`
<a name="neptune_ExecuteGremlinProfileQuery_python_3_topic"></a>

The following code example shows how to use `ExecuteGremlinProfileQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
# Replace this with your actual Neptune endpoint
NEPTUNE_ENDPOINT = "https://[Specify Endpoint]:8182"

def main():
    """
    Entry point of the program. Initializes the Neptune client and executes the Gremlin query.
    """
    config = Config(connect_timeout=10, read_timeout=30, retries={'max_attempts': 3})

    neptune_client = boto3.client(
        "neptunedata",
        endpoint_url=NEPTUNE_ENDPOINT,
        config=config
    )

    execute_gremlin_query(neptune_client)

def execute_gremlin_query(neptune_client):
    """
    Executes a Gremlin query against an Amazon Neptune database.
    """
    try:
        print("Querying Neptune...")

        response = neptune_client.execute_gremlin_explain_query(
            gremlinQuery="g.V().has('code', 'ANC')"
        )

        print("Full Response:")
        print(response['output'].read().decode('UTF-8'))

    except ClientError as e:
        print(f"Error calling Neptune: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCore error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [ExecuteGremlinProfileQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteGremlinProfileQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `ExecuteGremlinQuery`
<a name="neptune_ExecuteGremlinQuery_python_3_topic"></a>

The following code example shows how to use `ExecuteGremlinQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
"""
Running this example.

----------------------------------------------------------------------------------
VPC Networking Requirement:
----------------------------------------------------------------------------------
Amazon Neptune must be accessed from **within the same VPC** as the Neptune cluster.
It does not expose a public endpoint, so this code must be executed from:

  - An **AWS Lambda function** configured to run inside the same VPC
  - An **EC2 instance** or **ECS task** running in the same VPC
  - A connected environment such as a **VPN**, **AWS Direct Connect**, or a **peered VPC**

"""

# Replace with your actual Neptune endpoint
NEPTUNE_ENDPOINT = "https://[Specify-Your-Endpoint]:8182"

def main():
    """
    Entry point of the program. Initializes the Neptune client and runs both EXPLAIN and PROFILE queries.
    """
    config = Config(connect_timeout=10, read_timeout=30, retries={'max_attempts': 3})

    neptune_client = boto3.client(
        "neptunedata",
        endpoint_url=NEPTUNE_ENDPOINT,
        config=config
    )

    try:
        run_profile_query(neptune_client)
    except ClientError as e:
        print(f"Neptune error: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCore error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def run_profile_query(neptune_client):
    """
    Runs a PROFILE query on the Neptune graph database.
    """
    print("Running Gremlin PROFILE query...")

    try:
        response = neptune_client.execute_gremlin_profile_query(
            gremlinQuery="g.V().has('code', 'ANC')"
        )
        print("Profile Query Result:")
        output = response.get("output")
        if output:
            print(output.read().decode('utf-8'))
        else:
            print("No explain output returned.")
    except Exception as e:
        print(f"Failed to execute PROFILE query: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [ExecuteGremlinQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteGremlinQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `ExecuteOpenCypherExplainQuery`
<a name="neptune_ExecuteOpenCypherExplainQuery_python_3_topic"></a>

The following code example shows how to use `ExecuteOpenCypherExplainQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
# Replace with your actual Neptune endpoint URL
NEPTUNE_ENDPOINT = "https://<your-neptune-endpoint>:8182"

def main():
    """
    Entry point: Create Neptune client and execute different OpenCypher queries.
    """
    config = Config(connect_timeout=10, read_timeout=30, retries={'max_attempts': 3})

    neptune_client = boto3.client(
        "neptunedata",
        endpoint_url=NEPTUNE_ENDPOINT,
        config=config
    )

    execute_open_cypher_query_without_params(neptune_client)
    execute_open_cypher_query_with_params(neptune_client)
    execute_open_cypher_explain_query(neptune_client)

def execute_open_cypher_query_without_params(client):
    """
    Executes a simple OpenCypher query without parameters.
    """
    try:
        print("\nRunning OpenCypher query without parameters...")
        resp = client.execute_open_cypher_query(
            openCypherQuery="MATCH (n {code: 'ANC'}) RETURN n"
        )
        print("Results:")
        print(resp['results'])

    except Exception as e:
        print(f"Error in simple OpenCypher query: {str(e)}")

def execute_open_cypher_query_with_params(client):
    """
    Executes an OpenCypher query using parameters.
    """
    try:
        print("\nRunning OpenCypher query with parameters...")
        parameters = {'code': 'ANC'}
        resp = client.execute_open_cypher_query(
            openCypherQuery="MATCH (n {code: $code}) RETURN n",
            parameters=json.dumps(parameters)
        )
        print("Results:")
        print(resp['results'])

    except Exception as e:
        print(f"Error in parameterized OpenCypher query: {str(e)}")

def execute_open_cypher_explain_query(client):
    """
    Runs an OpenCypher EXPLAIN query in debug mode.
    """
    try:
        print("\nRunning OpenCypher EXPLAIN query (debug mode)...")
        resp = client.execute_open_cypher_explain_query(
            openCypherQuery="MATCH (n {code: 'ANC'}) RETURN n",
            explainMode="details"
        )
        results = resp.get('results')
        if results is None:
            print("No explain results returned.")
        else:
            try:
                print("Explain Results:")
                print(results.read().decode('UTF-8'))
            except Exception as e:
                print(f"Error in OpenCypher EXPLAIN query: {str(e)}")

    except ClientError as e:
        print(f"Neptune error: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCore error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteOpenCypherExplainQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `ExecuteQuery`
<a name="neptune_ExecuteQuery_python_3_topic"></a>

The following code example shows how to use `ExecuteQuery`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
"""
Running this example.

----------------------------------------------------------------------------------
VPC Networking Requirement:
----------------------------------------------------------------------------------
Amazon Neptune must be accessed from **within the same VPC** as the Neptune cluster.
It does not expose a public endpoint, so this code must be executed from:

  - An **AWS Lambda function** configured to run inside the same VPC
  - An **EC2 instance** or **ECS task** running in the same VPC
  - A connected environment such as a **VPN**, **AWS Direct Connect**, or a **peered VPC**
"""

GRAPH_ID = "<your-graph-id>"

def main():
    config = Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)
    client = boto3.client("neptune-graph", config=config)

    try:
        print("\n--- Running OpenCypher query without parameters ---")
        run_open_cypher_query(client, GRAPH_ID)

        print("\n--- Running OpenCypher query with parameters ---")
        run_open_cypher_query_with_params(client, GRAPH_ID)

        print("\n--- Running OpenCypher explain query ---")
        run_open_cypher_explain_query(client, GRAPH_ID)

    except Exception as e:
        print(f"Unexpected error in main: {e}")

def run_open_cypher_query(client, graph_id):
    """
    Run an OpenCypher query without parameters.
    """
    try:
        resp = client.execute_query(
            graphIdentifier=graph_id,
            queryString="MATCH (n {code: 'ANC'}) RETURN n",
            language='OPEN_CYPHER'
        )
        print(resp['payload'].read().decode('UTF-8'))

    except client.exceptions.InternalServerException as e:
        print(f"InternalServerException: {e.response['Error']['Message']}")
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
    except Exception as e:  # <--- ADD THIS BLOCK
        print(f"Unexpected error: {e}")

def run_open_cypher_query_with_params(client, graph_id):
    """
    Run an OpenCypher query with parameters.
    """
    try:
        parameters = {'code': 'ANC'}
        resp = client.execute_query(
            graphIdentifier=graph_id,
            queryString="MATCH (n {code: $code}) RETURN n",
            language='OPEN_CYPHER',
            parameters=parameters
        )
        print(resp['payload'].read().decode('UTF-8'))

    except client.exceptions.InternalServerException as e:
        print(f"InternalServerException: {e.response['Error']['Message']}")
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
    except Exception as e:  # <--- ADD THIS BLOCK
        print(f"Unexpected error: {e}")

def run_open_cypher_explain_query(client, graph_id):
    """
    Run an OpenCypher explain query (explainMode = "debug").
    """
    try:
        resp = client.execute_query(
            graphIdentifier=graph_id,
            queryString="MATCH (n {code: 'ANC'}) RETURN n",
            language='OPEN_CYPHER',
            explainMode='DETAILS'
        )
        print(resp['payload'].read().decode('UTF-8'))

    except ClientError as e:
        print(f"Neptune error: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"Unexpected Boto3 error: {str(e)}")
    except Exception as e:  # <-- Add this generic catch
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [ExecuteQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteQuery) in *AWS SDK for Python (Boto3) API Reference*.

### `StartDBCluster`
<a name="neptune_StartDBCluster_python_3_topic"></a>

The following code example shows how to use `StartDBCluster`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def start_db_cluster(neptune_client, cluster_identifier: str):
    """
    Starts an Amazon Neptune DB cluster and waits until it reaches 'available'.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_identifier (str): The DB cluster identifier.

    Raises:
        ClientError: Propagates AWS API issues like resource not found.
        RuntimeError: If cluster doesn't reach 'available' within timeout.
    """
    try:
        # Initial wait in case the cluster was just stopped
        time.sleep(30)
        neptune_client.start_db_cluster(DBClusterIdentifier=cluster_identifier)
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't start DB cluster. Here's why: {code}: {message}")
        raise

    start_time = time.time()
    paginator = neptune_client.get_paginator('describe_db_clusters')

    while True:
        try:
            pages = paginator.paginate(DBClusterIdentifier=cluster_identifier)
            clusters = []
            for page in pages:
                clusters.extend(page.get('DBClusters', []))
        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBClusterNotFound":
                print(f"Cluster '{cluster_identifier}' not found while polling. It may have been deleted.")
            else:
                print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
            raise

        status = clusters[0].get('Status') if clusters else None
        elapsed = time.time() - start_time

        print(f"\rElapsed: {int(elapsed)}s – Cluster status: {status}", end="", flush=True)

        if status and status.lower() == 'available':
            print(f"\n🎉 Cluster '{cluster_identifier}' is available.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for cluster '{cluster_identifier}' to become available.")

        time.sleep(POLL_INTERVAL_SECONDS)
```
+  For API details, see [StartDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StartDBCluster) in *AWS SDK for Python (Boto3) API Reference*.

### `StopDBCluster`
<a name="neptune_StopDBCluster_python_3_topic"></a>

The following code example shows how to use `StopDBCluster`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def stop_db_cluster(neptune_client, cluster_identifier: str):
    """
    Stops an Amazon Neptune DB cluster and waits until it's fully stopped.

    Args:
        neptune_client (boto3.client): The Neptune client.
        cluster_identifier (str): The DB cluster identifier.

    Raises:
        ClientError: For AWS API errors (e.g., resource not found).
        RuntimeError: If the cluster doesn't stop within the timeout.
    """
    try:
        neptune_client.stop_db_cluster(DBClusterIdentifier=cluster_identifier)
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't stop DB cluster. Here's why: {code}: {message}")
        raise

    start_time = time.time()
    paginator = neptune_client.get_paginator('describe_db_clusters')

    while True:
        try:
            pages = paginator.paginate(DBClusterIdentifier=cluster_identifier)
            clusters = []
            for page in pages:
                clusters.extend(page.get('DBClusters', []))
        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBClusterNotFound":
                print(f"Cluster '{cluster_identifier}' not found while polling. It may have been deleted.")
            else:
                print(f"Couldn't describe DB cluster. Here's why: {code}: {message}")
            raise

        status = clusters[0].get('Status') if clusters else None
        elapsed = time.time() - start_time

        print(f"\rElapsed: {int(elapsed)}s – Cluster status: {status}", end="", flush=True)

        if status and status.lower() == 'stopped':
            print(f"\nCluster '{cluster_identifier}' is now stopped.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for cluster '{cluster_identifier}' to stop.")

        time.sleep(POLL_INTERVAL_SECONDS)
```
+  For API details, see [StopDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/StopDBCluster) in *AWS SDK for Python (Boto3) API Reference*.
