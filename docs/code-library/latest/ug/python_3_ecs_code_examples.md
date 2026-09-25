---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_ecs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon ECS examples using SDK for Python (Boto3)
<a name="python_3_ecs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Amazon ECS.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello Amazon ECS
<a name="ecs_Hello_python_3_topic"></a>

The following code example shows how to get started using Amazon ECS.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def hello_ecs():
    """
    Lists the Amazon ECS clusters in the current AWS region.
    Uses a paginator to handle large numbers of clusters.
    """
    ecs_client = boto3.client("ecs")
    try:
        paginator = ecs_client.get_paginator("list_clusters")
        cluster_arns = list()
        for page in paginator.paginate():
            cluster_arns.extend(page.get("clusterArns", list()))
        if cluster_arns:
            print(f"Found {len(cluster_arns)} ECS cluster(s):")
            for arn in cluster_arns:
                print(f"  - {arn}")
        else:
            print("No ECS clusters found in the current region.")
    except ClientError as err:
        logger.error(
            "Error listing ECS clusters: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise

if __name__ == "__main__":
    hello_ecs()
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListClusters) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn Amazon ECS basics
<a name="ecs_Scenario_python_3_topic"></a>

The following code example shows how to learn Amazon ECS basics.
+ Create an ECS cluster.
+ Register a Fargate task definition.
+ Run a standalone task.
+ Create a service.
+ List tasks in the service.
+ Describe and update the service.
+ Clean up all resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).
Run an interactive scenario at a command prompt.

```
import json
import logging
import os
import sys

import boto3
from botocore.exceptions import ClientError, WaiterError

# The EcsWrapper lives in the parent directory (python/example_code/ecs/).
# Add it to the path so this scenario can be run directly from the scenarios/ folder.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ecs_wrapper import EcsWrapper

logger = logging.getLogger(__name__)

CLUSTER_NAME = "ecs-basics-cluster"
TASK_FAMILY = "ecs-basics-task-def"
SERVICE_NAME = "ecs-basics-service"
STACK_NAME = "ecs-basics-prerequisites"

def get_cfn_template():
    """Returns the CloudFormation template as a JSON string."""
    template = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "ECS Basics - VPC, subnets, security group, and task execution role.",
        "Resources": {
            "EcsTaskExecutionRole": {
                "Type": "AWS::IAM::Role",
                "Properties": {
                    "AssumeRolePolicyDocument": {
                        "Version":"2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Principal": {"Service": "ecs-tasks.amazonaws.com"},
                                "Action": "sts:AssumeRole",
                            }
                        ],
                    },
                    "ManagedPolicyArns": [
                        "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
                    ],
                },
            },
            "Vpc": {
                "Type": "AWS::EC2::VPC",
                "Properties": {
                    "CidrBlock": "10.0.0.0/16",
                    "EnableDnsSupport": True,
                    "EnableDnsHostnames": True,
                },
            },
            "InternetGateway": {"Type": "AWS::EC2::InternetGateway"},
            "AttachGateway": {
                "Type": "AWS::EC2::VPCGatewayAttachment",
                "Properties": {
                    "VpcId": {"Ref": "Vpc"},
                    "InternetGatewayId": {"Ref": "InternetGateway"},
                },
            },
            "PublicSubnetOne": {
                "Type": "AWS::EC2::Subnet",
                "Properties": {
                    "VpcId": {"Ref": "Vpc"},
                    "CidrBlock": "10.0.1.0/24",
                    "AvailabilityZone": {"Fn::Select": ["0", {"Fn::GetAZs": ""}]},
                    "MapPublicIpOnLaunch": True,
                },
            },
            "PublicSubnetTwo": {
                "Type": "AWS::EC2::Subnet",
                "Properties": {
                    "VpcId": {"Ref": "Vpc"},
                    "CidrBlock": "10.0.2.0/24",
                    "AvailabilityZone": {"Fn::Select": ["1", {"Fn::GetAZs": ""}]},
                    "MapPublicIpOnLaunch": True,
                },
            },
            "RouteTable": {
                "Type": "AWS::EC2::RouteTable",
                "Properties": {"VpcId": {"Ref": "Vpc"}},
            },
            "DefaultRoute": {
                "Type": "AWS::EC2::Route",
                "DependsOn": "AttachGateway",
                "Properties": {
                    "RouteTableId": {"Ref": "RouteTable"},
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "GatewayId": {"Ref": "InternetGateway"},
                },
            },
            "SubnetOneRouteTableAssoc": {
                "Type": "AWS::EC2::SubnetRouteTableAssociation",
                "Properties": {
                    "SubnetId": {"Ref": "PublicSubnetOne"},
                    "RouteTableId": {"Ref": "RouteTable"},
                },
            },
            "SubnetTwoRouteTableAssoc": {
                "Type": "AWS::EC2::SubnetRouteTableAssociation",
                "Properties": {
                    "SubnetId": {"Ref": "PublicSubnetTwo"},
                    "RouteTableId": {"Ref": "RouteTable"},
                },
            },
            "SecurityGroup": {
                "Type": "AWS::EC2::SecurityGroup",
                "Properties": {
                    "GroupDescription": "ECS Basics security group",
                    "VpcId": {"Ref": "Vpc"},
                    "SecurityGroupEgress": [
                        {
                            "IpProtocol": "-1",
                            "CidrIp": "0.0.0.0/0",
                        }
                    ],
                },
            },
        },
        "Outputs": {
            "TaskExecutionRoleArn": {
                "Value": {"Fn::GetAtt": ["EcsTaskExecutionRole", "Arn"]},
            },
            "SubnetIdOne": {"Value": {"Ref": "PublicSubnetOne"}},
            "SubnetIdTwo": {"Value": {"Ref": "PublicSubnetTwo"}},
            "SecurityGroupId": {"Value": {"Ref": "SecurityGroup"}},
        },
    }
    return json.dumps(template)

# Stack states that cannot be reused or updated in place. A stack in one of
# these states is the residue of a failed create/rollback and must be deleted
# before a fresh stack can be created with the same name.
_UNUSABLE_STACK_STATES = frozenset(
    {"ROLLBACK_COMPLETE", "ROLLBACK_FAILED", "CREATE_FAILED", "DELETE_FAILED"}
)

def _delete_stack_if_unusable(cfn_client):
    """
    Deletes the stack if it exists in an unusable state from a prior failed run.

    CloudFormation will not let you create a stack whose name is already taken,
    and a stack stuck in ROLLBACK_COMPLETE (or similar) can neither be updated
    nor reused. Removing it first makes the scenario safely re-entrant.
    """
    try:
        response = cfn_client.describe_stacks(StackName=STACK_NAME)
    except ClientError as err:
        # No existing stack (or we can't read it): nothing to clean up.
        if "does not exist" in err.response["Error"]["Message"]:
            return
        raise

    status = response["Stacks"][0]["StackStatus"]
    if status in _UNUSABLE_STACK_STATES:
        print(
            f"Stack '{STACK_NAME}' is in an unusable state ({status}) from a "
            "previous run; deleting it before redeploying..."
        )
        delete_stack(cfn_client)

def deploy_stack(cfn_client):
    """Deploys the CloudFormation stack and returns outputs as a dict."""
    print(f"\nDeploying CloudFormation stack '{STACK_NAME}'...")
    # A stack left over from a previous failed run (e.g. ROLLBACK_COMPLETE or
    # CREATE_FAILED) cannot be reused or updated in place; it has no usable
    # outputs and must be deleted before we can create a fresh one. Clean it up
    # first so the scenario is re-entrant.
    _delete_stack_if_unusable(cfn_client)

    try:
        cfn_client.create_stack(
            StackName=STACK_NAME,
            TemplateBody=get_cfn_template(),
            Capabilities=["CAPABILITY_IAM"],
        )
        waiter = cfn_client.get_waiter("stack_create_complete")
        print("Waiting for stack creation to complete...")
        waiter.wait(
            StackName=STACK_NAME, WaiterConfig={"Delay": 15, "MaxAttempts": 60}
        )
    except ClientError as err:
        if err.response["Error"]["Code"] == "AlreadyExistsException":
            # The stack already exists in a usable (complete) state. Reuse its
            # outputs rather than failing, so repeated runs are graceful.
            print(
                f"Stack '{STACK_NAME}' already exists; reusing its outputs. "
                "Delete it manually if you need a clean deployment."
            )
        else:
            raise

    stack = cfn_client.describe_stacks(StackName=STACK_NAME)["Stacks"][0]

    # Only a stack in a complete state exposes usable outputs. If it ended up in
    # any other state (e.g. ROLLBACK_COMPLETE), "Outputs" is absent and blindly
    # reading stack_outputs["TaskExecutionRoleArn"] later would raise a
    # confusing KeyError. Fail fast here with a clear message instead.
    status = stack["StackStatus"]
    if status not in ("CREATE_COMPLETE", "UPDATE_COMPLETE"):
        raise RuntimeError(
            f"Stack '{STACK_NAME}' is in state '{status}', which has no usable "
            "outputs. Delete the stack and re-run the scenario."
        )

    # CloudFormation omits the "Outputs" key entirely when a stack has none, so
    # default to an empty list rather than indexing directly.
    outputs = stack.get("Outputs", list())
    result = dict()
    for output in outputs:
        result[output["OutputKey"]] = output["OutputValue"]
    print(f"Stack outputs: {result}")
    return result

def delete_stack(cfn_client):
    """Deletes the CloudFormation stack."""
    print(f"\nDeleting CloudFormation stack '{STACK_NAME}'...")
    try:
        cfn_client.delete_stack(StackName=STACK_NAME)
        waiter = cfn_client.get_waiter("stack_delete_complete")
        waiter.wait(StackName=STACK_NAME, WaiterConfig={"Delay": 15, "MaxAttempts": 60})
        print("Stack deleted.")
    except ClientError as err:
        logger.error("Failed to delete stack: %s", err)

def run_scenario():
    """Runs the ECS Basics scenario."""
    ecs_client = boto3.client("ecs")
    cfn_client = boto3.client("cloudformation")
    wrapper = EcsWrapper(ecs_client)

    cluster_name = None
    task_def_arn = None
    standalone_task_arn = None
    service_name = None

    try:
        # --- Setup: Deploy CloudFormation stack ---
        stack_outputs = deploy_stack(cfn_client)
        execution_role_arn = stack_outputs["TaskExecutionRoleArn"]
        subnets = [stack_outputs["SubnetIdOne"], stack_outputs["SubnetIdTwo"]]
        security_groups = [stack_outputs["SecurityGroupId"]]

        # --- Setup: Create ECS cluster ---
        print(f"\nCreating ECS cluster '{CLUSTER_NAME}'...")
        cluster = wrapper.create_cluster(CLUSTER_NAME)
        cluster_name = cluster["clusterName"]
        print(f"  Cluster: {cluster['clusterName']} (ARN: {cluster['clusterArn']})")
        print(f"  Status: {cluster['status']}")

        # --- Step 1: Register task definition ---
        print(f"\nRegistering task definition '{TASK_FAMILY}'...")
        task_def = wrapper.register_task_definition(
            family=TASK_FAMILY,
            execution_role_arn=execution_role_arn,
        )
        task_def_arn = f"{task_def['family']}:{task_def['revision']}"
        print(f"  Family: {task_def['family']}, Revision: {task_def['revision']}")
        print(f"  ARN: {task_def['taskDefinitionArn']}")

        # --- Step 2: Describe the cluster ---
        print(f"\nDescribing cluster '{cluster_name}'...")
        clusters = wrapper.describe_clusters([cluster_name])
        if clusters:
            c = clusters[0]
            print(f"  Name: {c['clusterName']}, Status: {c['status']}")
            print(f"  Active services: {c['activeServicesCount']}")
            print(f"  Running tasks: {c['runningTasksCount']}")

        # --- Step 3: Run a standalone task ---
        print(f"\nRunning standalone task with '{task_def_arn}'...")
        tasks = wrapper.run_task(
            cluster=cluster_name,
            task_definition=task_def_arn,
            subnets=subnets,
            security_groups=security_groups,
        )
        if tasks:
            standalone_task_arn = tasks[0]["taskArn"]
            print(f"  Task ARN: {standalone_task_arn}")
            print(f"  Status: {tasks[0]['lastStatus']}")
        else:
            # run_task can return an empty task list when every task fails to
            # start (see the 'failures' entry in the run_task response). Surface
            # this clearly so the reader knows Step 4 was skipped intentionally
            # rather than assuming the task launched successfully.
            logger.warning(
                "No tasks were started for '%s'. The task may have failed to "
                "launch (check the 'failures' field in the run_task response). "
                "Skipping the wait-and-describe step.",
                task_def_arn,
            )
            print("  No tasks were started; skipping the wait-and-describe step.")

        # --- Step 4: Wait for task to run, then describe it ---
        if standalone_task_arn:
            print("\nWaiting for task to reach RUNNING state...")
            try:
                waiter = ecs_client.get_waiter("tasks_running")
                waiter.wait(
                    cluster=cluster_name,
                    tasks=[standalone_task_arn],
                    WaiterConfig={"Delay": 6, "MaxAttempts": 100},
                )
            except WaiterError:
                print("  Task did not reach RUNNING state within timeout.")

            task_details = wrapper.describe_tasks(cluster_name, [standalone_task_arn])
            if task_details:
                t = task_details[0]
                print(f"  Task status: {t['lastStatus']}")
                for container in t.get("containers", list()):
                    print(f"  Container '{container['name']}': {container['lastStatus']}")

        # --- Step 5: Create a service ---
        print(f"\nCreating service '{SERVICE_NAME}'...")
        service = wrapper.create_service(
            cluster=cluster_name,
            service_name=SERVICE_NAME,
            task_definition=task_def_arn,
            desired_count=1,
            subnets=subnets,
            security_groups=security_groups,
        )
        service_name = service["serviceName"]
        print(f"  Service: {service['serviceName']} (ARN: {service['serviceArn']})")
        print(f"  Desired count: {service['desiredCount']}")

        # --- Step 6: List tasks in the service ---
        print("\nWaiting for the service to reach a steady state...")
        try:
            services_waiter = ecs_client.get_waiter("services_stable")
            services_waiter.wait(
                cluster=cluster_name,
                services=[service_name],
                WaiterConfig={"Delay": 15, "MaxAttempts": 40},
            )
        except WaiterError:
            print("  Service did not stabilize within the timeout; continuing.")
        task_arns = wrapper.list_tasks(
            cluster=cluster_name, service_name=service_name
        )
        print(f"  Service tasks: {task_arns}")

        # --- Step 7: Describe the service ---
        print(f"\nDescribing service '{service_name}'...")
        services = wrapper.describe_services(cluster_name, [service_name])
        if services:
            s = services[0]
            print(f"  Name: {s['serviceName']}, Status: {s['status']}")
            print(f"  Desired: {s['desiredCount']}, Running: {s['runningCount']}")
            events = s.get("events", list())
            if events:
                print(f"  Latest event: {events[0].get('message', 'N/A')}")

        # --- Step 8: Update the service (scale up) ---
        print(f"\nScaling service '{service_name}' to 2 tasks...")
        updated = wrapper.update_service(
            cluster=cluster_name,
            service=service_name,
            desired_count=2,
        )
        print(f"  Updated desired count: {updated['desiredCount']}")

    except Exception:
        logger.exception("Scenario encountered an error.")
        raise

    finally:
        # --- Cleanup ---
        print("\n--- Cleanup ---")

        # Stop standalone task
        if standalone_task_arn and cluster_name:
            try:
                print(f"Stopping standalone task '{standalone_task_arn}'...")
                ecs_client.stop_task(
                    cluster=cluster_name,
                    task=standalone_task_arn,
                    reason="Scenario cleanup",
                )
                stopped_waiter = ecs_client.get_waiter("tasks_stopped")
                stopped_waiter.wait(
                    cluster=cluster_name,
                    tasks=[standalone_task_arn],
                    WaiterConfig={"Delay": 6, "MaxAttempts": 100},
                )
                print("  Standalone task stopped.")
            except (ClientError, WaiterError) as err:
                logger.warning("Could not stop standalone task: %s", err)

        # Scale down and delete service
        if service_name and cluster_name:
            try:
                print(f"Scaling down service '{service_name}' to 0...")
                wrapper.update_service(
                    cluster=cluster_name,
                    service=service_name,
                    desired_count=0,
                )
                # Wait for tasks to drain before deleting the service.
                try:
                    drain_waiter = ecs_client.get_waiter("services_stable")
                    drain_waiter.wait(
                        cluster=cluster_name,
                        services=[service_name],
                        WaiterConfig={"Delay": 15, "MaxAttempts": 40},
                    )
                except WaiterError:
                    logger.warning(
                        "Service '%s' did not drain within the timeout; "
                        "attempting force delete.",
                        service_name,
                    )
                print(f"Deleting service '{service_name}'...")
                wrapper.delete_service(cluster=cluster_name, service=service_name)
                print("  Service deleted.")
            except ClientError as err:
                logger.warning("Could not delete service: %s", err)

        # Deregister task definition
        if task_def_arn:
            try:
                print(f"Deregistering task definition '{task_def_arn}'...")
                wrapper.deregister_task_definition(task_def_arn)
                print("  Task definition deregistered.")
            except ClientError as err:
                logger.warning("Could not deregister task definition: %s", err)

        # Delete cluster
        if cluster_name:
            try:
                print(f"Deleting cluster '{cluster_name}'...")
                wrapper.delete_cluster(cluster_name)
                print("  Cluster deleted.")
            except ClientError as err:
                logger.warning("Could not delete cluster: %s", err)

        # Delete CloudFormation stack
        delete_stack(cfn_client)

    print("\nECS Basics scenario complete!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_scenario()
```
Create a class that wraps ECS operations.

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateCluster](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateCluster)
  + [CreateService](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateService)
  + [DeleteCluster](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteCluster)
  + [DeleteService](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteService)
  + [DeregisterTaskDefinition](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeregisterTaskDefinition)
  + [DescribeClusters](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeClusters)
  + [DescribeServices](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeServices)
  + [DescribeTasks](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeTasks)
  + [ListTasks](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListTasks)
  + [RegisterTaskDefinition](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RegisterTaskDefinition)
  + [RunTask](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RunTask)
  + [UpdateService](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateService)

## Actions
<a name="actions"></a>

### `CreateCluster`
<a name="ecs_CreateCluster_python_3_topic"></a>

The following code example shows how to use `CreateCluster`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def create_cluster(self, cluster_name: str) -> Dict[str, Any]:
        """
        Creates a new Amazon ECS cluster.

        :param cluster_name: The name of the cluster to create.
        :return: The cluster details from the response.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        try:
            response = self.ecs_client.create_cluster(
                clusterName=cluster_name,
                settings=[
                    {"name": "containerInsights", "value": "enabled"},
                ],
            )
            cluster = response["cluster"]
            logger.info(
                "Created cluster '%s' with ARN: %s",
                cluster["clusterName"],
                cluster["clusterArn"],
            )
            return cluster
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when creating cluster '%s': %s",
                    cluster_name,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateCluster](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateCluster) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateService`
<a name="ecs_CreateService_python_3_topic"></a>

The following code example shows how to use `CreateService`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def create_service(
        self,
        cluster: str,
        service_name: str,
        task_definition: str,
        desired_count: int,
        subnets: List[str],
        security_groups: List[str],
    ) -> Dict[str, Any]:
        """
        Creates a service that maintains a desired count of running tasks.

        :param cluster: The cluster name or ARN.
        :param service_name: The name for the service.
        :param task_definition: The task definition family or family:revision.
        :param desired_count: The number of task instances to maintain.
        :param subnets: List of subnet IDs.
        :param security_groups: List of security group IDs.
        :return: The service details from the response.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        try:
            response = self.ecs_client.create_service(
                cluster=cluster,
                serviceName=service_name,
                taskDefinition=task_definition,
                desiredCount=desired_count,
                launchType="FARGATE",
                networkConfiguration={
                    "awsvpcConfiguration": {
                        "subnets": subnets,
                        "securityGroups": security_groups,
                        "assignPublicIp": "ENABLED",
                    }
                },
            )
            service = response["service"]
            logger.info(
                "Created service '%s' (ARN: %s) with desired count %s",
                service["serviceName"],
                service["serviceArn"],
                service["desiredCount"],
            )
            return service
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when creating service '%s': %s",
                    service_name,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateService](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateService) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteCluster`
<a name="ecs_DeleteCluster_python_3_topic"></a>

The following code example shows how to use `DeleteCluster`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def delete_cluster(self, cluster: str) -> Dict[str, Any]:
        """
        Deletes an ECS cluster.

        :param cluster: The cluster name or ARN.
        :return: The deleted cluster details.
        :raises ClientError: If the request fails (e.g., ClusterContainsServicesException).
        """
        try:
            response = self.ecs_client.delete_cluster(
                cluster=cluster,
            )
            cluster_info = response["cluster"]
            logger.info(
                "Deleted cluster '%s' (status: %s)",
                cluster_info["clusterName"],
                cluster_info["status"],
            )
            return cluster_info
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterContainsServicesException":
                logger.error(
                    "Cluster '%s' still contains services. Delete services first: %s",
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteCluster](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteCluster) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteService`
<a name="ecs_DeleteService_python_3_topic"></a>

The following code example shows how to use `DeleteService`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def delete_service(
        self,
        cluster: str,
        service: str,
        force: bool = True,
    ) -> Dict[str, Any]:
        """
        Deletes a service from a cluster.

        :param cluster: The cluster name or ARN.
        :param service: The service name or ARN.
        :param force: If True, deletes the service even if it has active tasks.
        :return: The deleted service details.
        :raises ClientError: If the request fails (e.g., ServiceNotFoundException).
        """
        try:
            response = self.ecs_client.delete_service(
                cluster=cluster,
                service=service,
                force=force,
            )
            svc = response["service"]
            logger.info(
                "Deleted service '%s' from cluster '%s'",
                svc["serviceName"],
                cluster,
            )
            return svc
        except ClientError as err:
            if err.response["Error"]["Code"] == "ServiceNotFoundException":
                logger.error(
                    "Service '%s' not found (may already be deleted): %s",
                    service,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteService](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteService) in *AWS SDK for Python (Boto3) API Reference*.

### `DeregisterTaskDefinition`
<a name="ecs_DeregisterTaskDefinition_python_3_topic"></a>

The following code example shows how to use `DeregisterTaskDefinition`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def deregister_task_definition(self, task_definition: str) -> Dict[str, Any]:
        """
        Deregisters a task definition.

        :param task_definition: The family:revision of the task definition.
        :return: The deregistered task definition details.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        try:
            response = self.ecs_client.deregister_task_definition(
                taskDefinition=task_definition,
            )
            task_def = response["taskDefinition"]
            logger.info(
                "Deregistered task definition '%s' (status: %s)",
                task_def["taskDefinitionArn"],
                task_def["status"],
            )
            return task_def
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when deregistering task definition '%s': %s",
                    task_definition,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeregisterTaskDefinition](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeregisterTaskDefinition) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeClusters`
<a name="ecs_DescribeClusters_python_3_topic"></a>

The following code example shows how to use `DescribeClusters`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def describe_clusters(self, cluster_names: List[str]) -> List[Dict[str, Any]]:
        """
        Describes one or more ECS clusters.

        :param cluster_names: A list of cluster names or ARNs.
        :return: A list of cluster details.
        :raises ClientError: If the request fails (e.g., ClusterNotFoundException).
        """
        try:
            response = self.ecs_client.describe_clusters(
                clusters=cluster_names,
                include=["STATISTICS"],
            )
            clusters = response.get("clusters", list())
            for cluster in clusters:
                logger.info(
                    "Cluster '%s': status=%s, active_services=%s, running_tasks=%s",
                    cluster["clusterName"],
                    cluster["status"],
                    cluster["activeServicesCount"],
                    cluster["runningTasksCount"],
                )
            return clusters
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterNotFoundException":
                logger.error(
                    "Cluster(s) not found: %s. %s",
                    cluster_names,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DescribeClusters](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeClusters) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeServices`
<a name="ecs_DescribeServices_python_3_topic"></a>

The following code example shows how to use `DescribeServices`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def describe_services(
        self, cluster: str, service_names: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Describes the specified services running in a cluster.

        :param cluster: The cluster name or ARN.
        :param service_names: A list of service names or ARNs.
        :return: A list of service details.
        :raises ClientError: If the request fails (e.g., ClusterNotFoundException).
        """
        try:
            response = self.ecs_client.describe_services(
                cluster=cluster,
                services=service_names,
            )
            services = response.get("services", list())
            for svc in services:
                logger.info(
                    "Service '%s': status=%s, desired=%s, running=%s",
                    svc["serviceName"],
                    svc["status"],
                    svc["desiredCount"],
                    svc["runningCount"],
                )
            return services
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterNotFoundException":
                logger.error(
                    "Cluster '%s' not found when describing services: %s",
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeServices) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeTasks`
<a name="ecs_DescribeTasks_python_3_topic"></a>

The following code example shows how to use `DescribeTasks`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def describe_tasks(
        self, cluster: str, task_arns: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Describes the specified tasks.

        :param cluster: The cluster name or ARN.
        :param task_arns: A list of task ARNs.
        :return: A list of task details.
        :raises ClientError: If the request fails (e.g., ClusterNotFoundException).
        """
        try:
            response = self.ecs_client.describe_tasks(
                cluster=cluster,
                tasks=task_arns,
            )
            tasks = response.get("tasks", list())
            for task in tasks:
                logger.info(
                    "Task '%s': status=%s, desired_status=%s",
                    task["taskArn"],
                    task["lastStatus"],
                    task["desiredStatus"],
                )
            return tasks
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterNotFoundException":
                logger.error(
                    "Cluster '%s' not found when describing tasks: %s",
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DescribeTasks](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeTasks) in *AWS SDK for Python (Boto3) API Reference*.

### `ListTasks`
<a name="ecs_ListTasks_python_3_topic"></a>

The following code example shows how to use `ListTasks`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def list_tasks(
        self,
        cluster: str,
        service_name: Optional[str] = None,
    ) -> List[str]:
        """
        Lists task ARNs for a cluster, optionally filtered by service.
        Uses paginator to handle large result sets.

        :param cluster: The cluster name or ARN.
        :param service_name: The service name to filter by (optional).
        :return: A list of task ARN strings.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        try:
            task_arns = list()
            paginator = self.ecs_client.get_paginator("list_tasks")
            params = dict()
            params["cluster"] = cluster
            if service_name is not None:
                params["serviceName"] = service_name
            for page in paginator.paginate(**params):
                task_arns.extend(page.get("taskArns", list()))
            logger.info(
                "Listed %d tasks for cluster '%s'%s",
                len(task_arns),
                cluster,
                f" (service='{service_name}')" if service_name else "",
            )
            return task_arns
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when listing tasks: %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListTasks](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListTasks) in *AWS SDK for Python (Boto3) API Reference*.

### `RegisterTaskDefinition`
<a name="ecs_RegisterTaskDefinition_python_3_topic"></a>

The following code example shows how to use `RegisterTaskDefinition`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def register_task_definition(
        self,
        family: str,
        execution_role_arn: str,
        container_definitions: Optional[List[Dict[str, Any]]] = None,
        cpu: str = "256",
        memory: str = "512",
    ) -> Dict[str, Any]:
        """
        Registers a new task definition for Fargate.

        :param family: The family name for the task definition.
        :param execution_role_arn: The ARN of the task execution IAM role.
        :param container_definitions: List of container definitions. If None, a
            default httpd container is used.
        :param cpu: The task-level CPU units (e.g., '256').
        :param memory: The task-level memory in MiB (e.g., '512').
        :return: The task definition details from the response.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        if container_definitions is None:
            container_definitions = [
                {
                    "name": "sample-app",
                    "image": "public.ecr.aws/docker/library/httpd:2.4",
                    "essential": True,
                    "portMappings": [
                        {
                            "containerPort": 80,
                            "hostPort": 80,
                            "protocol": "tcp",
                        }
                    ],
                    "cpu": 256,
                    "memory": 512,
                }
            ]
        try:
            response = self.ecs_client.register_task_definition(
                family=family,
                networkMode="awsvpc",
                requiresCompatibilities=["FARGATE"],
                cpu=cpu,
                memory=memory,
                executionRoleArn=execution_role_arn,
                containerDefinitions=container_definitions,
            )
            task_def = response["taskDefinition"]
            logger.info(
                "Registered task definition '%s' revision %s, ARN: %s",
                task_def["family"],
                task_def["revision"],
                task_def["taskDefinitionArn"],
            )
            return task_def
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when registering task definition '%s': %s",
                    family,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [RegisterTaskDefinition](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RegisterTaskDefinition) in *AWS SDK for Python (Boto3) API Reference*.

### `RunTask`
<a name="ecs_RunTask_python_3_topic"></a>

The following code example shows how to use `RunTask`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def run_task(
        self,
        cluster: str,
        task_definition: str,
        subnets: List[str],
        security_groups: List[str],
        count: int = 1,
    ) -> List[Dict[str, Any]]:
        """
        Runs a standalone Fargate task.

        :param cluster: The cluster name or ARN.
        :param task_definition: The task definition family or family:revision.
        :param subnets: List of subnet IDs.
        :param security_groups: List of security group IDs.
        :param count: Number of tasks to run.
        :return: A list of task details.
        :raises ClientError: If the request fails (e.g., ClusterNotFoundException).
        """
        try:
            response = self.ecs_client.run_task(
                cluster=cluster,
                taskDefinition=task_definition,
                launchType="FARGATE",
                count=count,
                networkConfiguration={
                    "awsvpcConfiguration": {
                        "subnets": subnets,
                        "securityGroups": security_groups,
                        "assignPublicIp": "ENABLED",
                    }
                },
            )
            tasks = response.get("tasks", list())
            failures = response.get("failures", list())
            if failures:
                logger.warning("Task run failures: %s", failures)
            for task in tasks:
                logger.info(
                    "Started task '%s' with status '%s'",
                    task["taskArn"],
                    task["lastStatus"],
                )
            return tasks
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterNotFoundException":
                logger.error(
                    "Cluster '%s' not found: %s",
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [RunTask](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RunTask) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateService`
<a name="ecs_UpdateService_python_3_topic"></a>

The following code example shows how to use `UpdateService`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def update_service(
        self,
        cluster: str,
        service: str,
        desired_count: int,
    ) -> Dict[str, Any]:
        """
        Updates the desired count for a service.

        :param cluster: The cluster name or ARN.
        :param service: The service name or ARN.
        :param desired_count: The new desired task count.
        :return: The updated service details.
        :raises ClientError: If the request fails (e.g., ServiceNotFoundException).
        """
        try:
            response = self.ecs_client.update_service(
                cluster=cluster,
                service=service,
                desiredCount=desired_count,
            )
            svc = response["service"]
            logger.info(
                "Updated service '%s' desired count to %s",
                svc["serviceName"],
                svc["desiredCount"],
            )
            return svc
        except ClientError as err:
            if err.response["Error"]["Code"] == "ServiceNotFoundException":
                logger.error(
                    "Service '%s' not found in cluster '%s': %s",
                    service,
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [UpdateService](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateService) in *AWS SDK for Python (Boto3) API Reference*.
