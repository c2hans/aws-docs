---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_batch_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Batch examples using SDK for Python (Boto3)
<a name="python_3_batch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with AWS Batch.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello AWS Batch
<a name="batch_Hello_python_3_topic"></a>

The following code example shows how to get started using AWS Batch.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
def hello_batch() -> None:
    """
    Lists compute environments using the AWS Batch service.
    """
    batch_client = boto3.client("batch")
    print("Hello, AWS Batch! Let's list your compute environments:\n")
    try:
        response = batch_client.describe_compute_environments()
        environments = response.get("computeEnvironments", [])
        if environments:
            print(f"Found {len(environments)} compute environment(s):")
            for env in environments:
                print(
                    f"  - Name: {env['computeEnvironmentName']} | "
                    f"Type: {env.get('type', 'N/A')} | "
                    f"State: {env.get('state', 'N/A')} | "
                    f"Status: {env.get('status', 'N/A')}"
                )
        else:
            print("No compute environments found in your account.")
    except ClientError as err:
        logger.error(
            "Error listing compute environments: %s",
            err.response["Error"]["Message"],
        )
        raise

    print("\nHello example complete.")
```
+  For API details, see [listJobsPaginator](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/listJobsPaginator) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="batch_Scenario_python_3_topic"></a>

The following code example shows how to:
+ Create an AWS Batch compute environment.
+ Check the status of the compute environment.
+ Set up an AWS Batch job queue and job definition.
+ Register a job definition.
+ Submit an AWS Batch Job.
+ Get a list of jobs applicable to the job queue.
+ Check the status of job.
+ Delete AWS Batch resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).
Run an interactive scenario at a command prompt.

```
class BatchScenario:
    """Runs the AWS Batch Basics scenario."""

    def __init__(
        self,
        batch_wrapper: BatchWrapper,
        iam_client=None,
        ec2_client=None,
    ) -> None:
        """
        Initializes the scenario.

        The scenario self-provisions the networking (default VPC subnet and
        security group) and the ECS task execution role that Fargate jobs
        require, so it can be run with only AWS credentials. All provisioned
        resources are removed in ``cleanup``.

        :param batch_wrapper: A BatchWrapper instance for Batch operations.
        :param iam_client: A Boto3 IAM client (created if not supplied).
        :param ec2_client: A Boto3 EC2 client (created if not supplied).
        """
        self.batch_wrapper = batch_wrapper
        self.iam_client = iam_client or boto3.client("iam")
        self.ec2_client = ec2_client or boto3.client("ec2")
        self.ce_name = None
        self.ce_arn = None
        self.jq_name = None
        self.jq_arn = None
        self.jd_name = None
        self.jd_arn = None
        self.jd_revision = None
        self.job_id = None
        self.subnet_ids = None
        self.security_group_ids = None
        self.execution_role_name = None
        self.execution_role_arn = None

    def discover_networking(self) -> None:
        """
        Finds a subnet and security group in the default VPC.

        This lets the scenario run without the user supplying networking IDs,
        matching the self-contained behavior of the other Batch Basics examples.

        :raises RuntimeError: If no default VPC or no subnet is found.
        """
        vpcs = self.ec2_client.describe_vpcs(
            Filters=[{"Name": "isDefault", "Values": ["true"]}]
        ).get("Vpcs", [])
        if not vpcs:
            raise RuntimeError(
                "No default VPC found. Create a default VPC or run this scenario "
                "in a region that has one."
            )
        vpc_id = vpcs[0]["VpcId"]

        subnets = self.ec2_client.describe_subnets(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        ).get("Subnets", [])
        if not subnets:
            raise RuntimeError(f"No subnets found in default VPC {vpc_id}.")
        # Prefer a subnet that assigns public IPs so the Fargate task can pull
        # its public ECR image; fall back to the first subnet otherwise. One
        # subnet is sufficient for the Basics scenario.
        public_subnets = [s for s in subnets if s.get("MapPublicIpOnLaunch")]
        chosen = public_subnets[0] if public_subnets else subnets[0]
        self.subnet_ids = [chosen["SubnetId"]]

        groups = self.ec2_client.describe_security_groups(
            Filters=[
                {"Name": "vpc-id", "Values": [vpc_id]},
                {"Name": "group-name", "Values": ["default"]},
            ]
        ).get("SecurityGroups", [])
        if not groups:
            raise RuntimeError(f"No default security group found in VPC {vpc_id}.")
        self.security_group_ids = [groups[0]["GroupId"]]

    def create_execution_role(self) -> None:
        """
        Creates an ECS task execution role for Fargate jobs.

        Fargate requires an execution role that trusts ecs-tasks.amazonaws.com
        and has the AmazonECSTaskExecutionRolePolicy so the agent can pull the
        container image and write logs. The role is deleted in ``cleanup``.
        """
        response = self.iam_client.create_role(
            RoleName=self.execution_role_name,
            AssumeRolePolicyDocument=json.dumps(ECS_TASKS_TRUST_POLICY),
            Description="ECS task execution role for the Batch Basics scenario.",
        )
        self.execution_role_arn = response["Role"]["Arn"]
        self.iam_client.attach_role_policy(
            RoleName=self.execution_role_name,
            PolicyArn=ECS_EXECUTION_POLICY_ARN,
        )
        # IAM is eventually consistent; give the role a moment to propagate
        # before Batch/Fargate tries to assume it.
        time.sleep(10)
        print(f"Created execution role: {self.execution_role_arn}")

    def setup(self, timestamp: str) -> None:
        """
        Provisions all prerequisites: networking discovery and the ECS task
        execution role, and derives the resource names.

        :param timestamp: A unique timestamp string for naming resources.
        """
        self.ce_name = f"batch-basics-fargate-ce-{timestamp}"
        self.jq_name = f"batch-basics-job-queue-{timestamp}"
        self.jd_name = f"batch-basics-job-def-{timestamp}"
        self.execution_role_name = f"batch-basics-exec-role-{timestamp}"

        print("\nDiscovering default VPC networking...")
        self.discover_networking()
        print(
            f"  Subnets: {', '.join(self.subnet_ids)}\n"
            f"  Security Group: {', '.join(self.security_group_ids)}"
        )
        print("Creating ECS task execution role...")
        self.create_execution_role()

    def create_compute_environment(self) -> None:
        """Step 1: Create a Fargate compute environment."""
        print("\n" + "-" * 80)
        print("Step 1: Create a Fargate compute environment")
        print(f"Creating compute environment: {self.ce_name}")

        response = self.batch_wrapper.create_compute_environment(
            compute_environment_name=self.ce_name,
            subnet_ids=self.subnet_ids,
            security_group_ids=self.security_group_ids,
        )
        self.ce_arn = response["computeEnvironmentArn"]
        print(f"Compute environment ARN: {self.ce_arn}")

        print("Waiting for compute environment to become VALID...")
        env = self.batch_wrapper.wait_for_compute_environment_valid(self.ce_name)
        print(
            f"Compute environment is VALID.\n"
            f"  Name: {env['computeEnvironmentName']}\n"
            f"  Type: {env.get('type', 'N/A')}\n"
            f"  State: {env.get('state', 'N/A')}\n"
            f"  Status: {env.get('status', 'N/A')}"
        )
        print("-" * 80)

    def create_job_queue(self) -> None:
        """Step 2: Create a job queue."""
        print("\n" + "-" * 80)
        print("Step 2: Create a job queue")
        print(f"Creating job queue: {self.jq_name}")

        response = self.batch_wrapper.create_job_queue(
            job_queue_name=self.jq_name,
            compute_environment_name=self.ce_name,
        )
        self.jq_arn = response["jobQueueArn"]
        print(f"Job queue ARN: {self.jq_arn}")
        # A newly created job queue is briefly in CREATING status; submit_job
        # requires it to be VALID, so wait before continuing.
        print("Waiting for job queue to become VALID...")
        self.batch_wrapper.wait_for_job_queue_valid(self.jq_name)
        print("Job queue is ready.")
        print("-" * 80)

    def register_job_definition(self) -> None:
        """Step 3: Register a job definition."""
        print("\n" + "-" * 80)
        print("Step 3: Register a job definition")
        print(f"Registering job definition: {self.jd_name}")

        response = self.batch_wrapper.register_job_definition(
            job_definition_name=self.jd_name,
            execution_role_arn=self.execution_role_arn,
        )
        self.jd_arn = response["jobDefinitionArn"]
        self.jd_revision = response["revision"]
        print(f"Job definition ARN: {self.jd_arn}")
        print(f"Revision: {self.jd_revision}")
        print("-" * 80)

    def submit_job(self) -> None:
        """Step 4: Submit a job."""
        print("\n" + "-" * 80)
        print("Step 4: Submit a job")

        job_name = "batch-basics-hello-job"
        print(f"Submitting job: {job_name}")
        response = self.batch_wrapper.submit_job(
            job_name=job_name,
            job_queue=self.jq_name,
            job_definition=f"{self.jd_name}:{self.jd_revision}",
        )
        self.job_id = response["jobId"]
        print(
            f"Job submitted successfully.\n"
            f"  Job Name: {response['jobName']}\n"
            f"  Job ID: {self.job_id}\n"
            f"  Job ARN: {response.get('jobArn', 'N/A')}"
        )
        print("-" * 80)

    def monitor_job(self) -> None:
        """Step 5: Monitor the job."""
        print("\n" + "-" * 80)
        print("Step 5: Monitor the job")
        print(f"Waiting for job {self.job_id} to complete...")

        job = self.batch_wrapper.wait_for_job_complete(self.job_id)
        status = job.get("status", "UNKNOWN")
        if status == "SUCCEEDED":
            print("Job completed successfully!")
        else:
            print(f"Job ended with status: {status}")
            reason = job.get("statusReason", "No reason provided")
            print(f"  Status Reason: {reason}")

        print(f"  Final Status: {status}")
        container = job.get("container", {})
        exit_code = container.get("exitCode", "N/A")
        print(f"  Exit Code: {exit_code}")
        print("-" * 80)

    def list_jobs(self) -> None:
        """Step 6: List jobs in the queue."""
        print("\n" + "-" * 80)
        print("Step 6: List jobs in the queue")
        print(f"Listing SUCCEEDED jobs in queue: {self.jq_name}")

        job_summaries = self.batch_wrapper.list_jobs(
            job_queue=self.jq_name, job_status="SUCCEEDED"
        )
        if job_summaries:
            print(f"Found {len(job_summaries)} job(s):")
            for js in job_summaries:
                print(
                    f"  - Job ID: {js['jobId']} | "
                    f"Name: {js['jobName']} | "
                    f"Status: {js.get('status', 'N/A')}"
                )
        else:
            print("No SUCCEEDED jobs found.")
        print("-" * 80)

    def cleanup(self) -> None:
        """
        Cleans up all resources in reverse dependency order.

        Uses only Batch service operations (no CloudFormation). Each resource
        is waited into a stable state before the next transition so deletes do
        not fail with "resource is being modified". A success message is only
        printed when every step succeeds; otherwise the resources that could
        not be removed are listed so the user can delete them manually.
        """
        print("\n" + "-" * 80)
        print("Cleaning up resources...")

        leftovers = []

        # Deregister job definition.
        if self.jd_arn:
            try:
                print(f"Deregistering job definition: {self.jd_arn} ... ", end="")
                self.batch_wrapper.deregister_job_definition(self.jd_arn)
                print("done.")
            except Exception as e:
                logger.error("Error deregistering job definition: %s", e)
                print(f"error: {e}")
                leftovers.append(f"job definition {self.jd_arn}")

        # Disable and delete the job queue. The queue must be VALID before it
        # can be updated, and DISABLED/VALID before it can be deleted.
        if self.jq_name:
            queue_deleted = False
            try:
                print(f"Disabling job queue: {self.jq_name} ... ", end="")
                self.batch_wrapper.wait_for_job_queue_valid(self.jq_name)
                self.batch_wrapper.update_job_queue(self.jq_name, state="DISABLED")
                self.batch_wrapper.wait_for_job_queue_disabled(self.jq_name)
                print("done.")
            except Exception as e:
                logger.error("Error disabling job queue: %s", e)
                print(f"error: {e}")

            try:
                print(f"Deleting job queue: {self.jq_name} ... ", end="")
                self.batch_wrapper.delete_job_queue(self.jq_name)
                # The queue is fully gone only after it leaves the DELETING
                # state; wait so the compute environment can be deleted next.
                self.batch_wrapper.wait_for_job_queue_disabled(self.jq_name)
                print("done.")
                queue_deleted = True
            except Exception as e:
                logger.error("Error deleting job queue: %s", e)
                print(f"error: {e}")
            if not queue_deleted:
                leftovers.append(f"job queue {self.jq_name}")

        # Disable and delete the compute environment. It must be DISABLED and
        # VALID before deletion, otherwise AWS Batch rejects the delete.
        if self.ce_name:
            ce_deleted = False
            try:
                print(f"Disabling compute environment: {self.ce_name} ... ", end="")
                self.batch_wrapper.wait_for_compute_environment_valid(self.ce_name)
                self.batch_wrapper.update_compute_environment(
                    self.ce_name, state="DISABLED"
                )
                self.batch_wrapper.wait_for_compute_environment_disabled(self.ce_name)
                print("done.")
            except Exception as e:
                logger.error("Error disabling compute environment: %s", e)
                print(f"error: {e}")

            try:
                print(f"Deleting compute environment: {self.ce_name} ... ", end="")
                self.batch_wrapper.delete_compute_environment(self.ce_name)
                print("done.")
                ce_deleted = True
            except Exception as e:
                logger.error("Error deleting compute environment: %s", e)
                print(f"error: {e}")
            if not ce_deleted:
                leftovers.append(f"compute environment {self.ce_name}")

        # Delete the ECS task execution role the scenario created. Detach the
        # managed policy first; a role cannot be deleted while policies are
        # attached.
        if self.execution_role_name:
            role_deleted = False
            try:
                print(
                    f"Deleting execution role: {self.execution_role_name} ... ",
                    end="",
                )
                self.iam_client.detach_role_policy(
                    RoleName=self.execution_role_name,
                    PolicyArn=ECS_EXECUTION_POLICY_ARN,
                )
                self.iam_client.delete_role(RoleName=self.execution_role_name)
                print("done.")
                role_deleted = True
            except ClientError as e:
                logger.error("Error deleting execution role: %s", e)
                print(f"error: {e}")
            if not role_deleted:
                leftovers.append(f"IAM role {self.execution_role_name}")

        if leftovers:
            print(
                "\nCleanup incomplete. The following resources were NOT deleted "
                "and must be removed manually to avoid charges:"
            )
            for item in leftovers:
                print(f"  - {item}")
        else:
            print("All resources cleaned up successfully.")
        print("-" * 80)

    def run(self) -> None:
        """Runs the full scenario."""
        print("=" * 80)
        print("Welcome to the AWS Batch Basics scenario!")
        print("=" * 80)

        self.create_compute_environment()
        self.create_job_queue()
        self.register_job_definition()
        self.submit_job()
        self.monitor_job()
        self.list_jobs()
```
Create a class that wraps Batch operations.

```
class BatchWrapper:
    """Encapsulates AWS Batch operations."""

    def __init__(self, batch_client: Any) -> None:
        """
        Initializes the BatchWrapper with an AWS Batch client.

        :param batch_client: A Boto3 AWS Batch client.
        """
        self.batch_client = batch_client
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateComputeEnvironment)
  + [CreateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateJobQueue)
  + [DeleteComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteComputeEnvironment)
  + [DeleteJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteJobQueue)
  + [DeregisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeregisterJobDefinition)
  + [DescribeComputeEnvironments](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeComputeEnvironments)
  + [DescribeJobQueues](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobQueues)
  + [DescribeJobs](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobs)
  + [ListJobsPaginator](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListJobsPaginator)
  + [RegisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/RegisterJobDefinition)
  + [SubmitJob](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/SubmitJob)
  + [UpdateComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateComputeEnvironment)
  + [UpdateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateJobQueue)

## Actions
<a name="actions"></a>

### `CreateComputeEnvironment`
<a name="batch_CreateComputeEnvironment_python_3_topic"></a>

The following code example shows how to use `CreateComputeEnvironment`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def create_compute_environment(
        self,
        compute_environment_name: str,
        subnet_ids: list,
        security_group_ids: list,
        max_vcpus: int = 4,
    ) -> dict:
        """
        Creates a managed Fargate compute environment.

        :param compute_environment_name: The name for the compute environment.
        :param subnet_ids: A list of subnet IDs for the compute resources.
        :param security_group_ids: A list of security group IDs.
        :param max_vcpus: Maximum number of vCPUs (default 4).
        :return: A dictionary with the compute environment name and ARN.
        """
        try:
            response = self.batch_client.create_compute_environment(
                computeEnvironmentName=compute_environment_name,
                type="MANAGED",
                state="ENABLED",
                computeResources={
                    "type": "FARGATE",
                    "maxvCpus": max_vcpus,
                    "subnets": subnet_ids,
                    "securityGroupIds": security_group_ids,
                },
            )
            logger.info(
                "Created compute environment %s: %s",
                response["computeEnvironmentName"],
                response["computeEnvironmentArn"],
            )
            return response
        except ClientError as err:
            logger.error(
                "Error creating compute environment %s: %s",
                compute_environment_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [CreateComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateComputeEnvironment) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateJobQueue`
<a name="batch_CreateJobQueue_python_3_topic"></a>

The following code example shows how to use `CreateJobQueue`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def create_job_queue(
        self,
        job_queue_name: str,
        compute_environment_name: str,
        priority: int = 1,
    ) -> dict:
        """
        Creates a job queue associated with a compute environment.

        :param job_queue_name: The name for the job queue.
        :param compute_environment_name: The compute environment to associate.
        :param priority: The priority of the job queue (default 1).
        :return: A dictionary with the job queue name and ARN.
        """
        try:
            response = self.batch_client.create_job_queue(
                jobQueueName=job_queue_name,
                state="ENABLED",
                priority=priority,
                computeEnvironmentOrder=[
                    {
                        "order": 1,
                        "computeEnvironment": compute_environment_name,
                    }
                ],
            )
            logger.info(
                "Created job queue %s: %s",
                response["jobQueueName"],
                response["jobQueueArn"],
            )
            return response
        except ClientError as err:
            logger.error(
                "Error creating job queue %s: %s",
                job_queue_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [CreateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateJobQueue) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteComputeEnvironment`
<a name="batch_DeleteComputeEnvironment_python_3_topic"></a>

The following code example shows how to use `DeleteComputeEnvironment`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def delete_compute_environment(self, compute_environment: str) -> None:
        """
        Deletes a compute environment.

        :param compute_environment: The compute environment name or ARN to delete.
        """
        try:
            self.batch_client.delete_compute_environment(
                computeEnvironment=compute_environment
            )
            logger.info("Deleted compute environment %s.", compute_environment)
        except ClientError as err:
            logger.error(
                "Error deleting compute environment %s: %s",
                compute_environment,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteComputeEnvironment) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteJobQueue`
<a name="batch_DeleteJobQueue_python_3_topic"></a>

The following code example shows how to use `DeleteJobQueue`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def delete_job_queue(self, job_queue: str) -> None:
        """
        Deletes a job queue. The queue must be disabled first.

        :param job_queue: The job queue name or ARN to delete.
        """
        try:
            self.batch_client.delete_job_queue(jobQueue=job_queue)
            logger.info("Deleted job queue %s.", job_queue)
        except ClientError as err:
            logger.error(
                "Error deleting job queue %s: %s",
                job_queue,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeleteJobQueue) in *AWS SDK for Python (Boto3) API Reference*.

### `DeregisterJobDefinition`
<a name="batch_DeregisterJobDefinition_python_3_topic"></a>

The following code example shows how to use `DeregisterJobDefinition`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def deregister_job_definition(self, job_definition: str) -> None:
        """
        Deregisters a job definition.

        :param job_definition: The job definition name:revision or ARN.
        """
        try:
            self.batch_client.deregister_job_definition(jobDefinition=job_definition)
            logger.info("Deregistered job definition %s.", job_definition)
        except ClientError as err:
            logger.error(
                "Error deregistering job definition %s: %s",
                job_definition,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeregisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DeregisterJobDefinition) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeComputeEnvironments`
<a name="batch_DescribeComputeEnvironments_python_3_topic"></a>

The following code example shows how to use `DescribeComputeEnvironments`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def describe_compute_environments(
        self, compute_environment_names: Optional[list] = None
    ) -> list:
        """
        Describes one or more compute environments.

        :param compute_environment_names: Optional list of compute environment names
            or ARNs to describe. If None, describes all compute environments.
        :return: A list of compute environment detail dictionaries.
        """
        try:
            params = {}
            if compute_environment_names is not None:
                params["computeEnvironments"] = compute_environment_names
            response = self.batch_client.describe_compute_environments(**params)
            environments = response.get("computeEnvironments", [])
            logger.info("Described %d compute environment(s).", len(environments))
            return environments
        except ClientError as err:
            logger.error(
                "Error describing compute environments: %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeComputeEnvironments](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeComputeEnvironments) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeJobs`
<a name="batch_DescribeJobs_python_3_topic"></a>

The following code example shows how to use `DescribeJobs`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def describe_jobs(self, job_ids: list) -> list:
        """
        Describes one or more jobs.

        :param job_ids: A list of job IDs to describe.
        :return: A list of job detail dictionaries.
        """
        try:
            response = self.batch_client.describe_jobs(jobs=job_ids)
            jobs = response.get("jobs", [])
            logger.info("Described %d job(s).", len(jobs))
            return jobs
        except ClientError as err:
            logger.error(
                "Error describing jobs: %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeJobs](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobs) in *AWS SDK for Python (Boto3) API Reference*.

### `ListJobs`
<a name="batch_ListJobs_python_3_topic"></a>

The following code example shows how to use `ListJobs`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def list_jobs(self, job_queue: str, job_status: str = "SUCCEEDED") -> list:
        """
        Lists jobs in a job queue with a specific status.

        :param job_queue: The job queue name or ARN.
        :param job_status: The job status to filter by (default SUCCEEDED).
        :return: A list of job summary dictionaries.
        """
        try:
            paginator = self.batch_client.get_paginator("list_jobs")
            job_summaries = []
            for page in paginator.paginate(jobQueue=job_queue, jobStatus=job_status):
                job_summaries.extend(page.get("jobSummaryList", []))
            logger.info(
                "Listed %d %s job(s) in queue %s.",
                len(job_summaries),
                job_status,
                job_queue,
            )
            return job_summaries
        except ClientError as err:
            logger.error(
                "Error listing jobs in queue %s: %s",
                job_queue,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListJobs](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListJobs) in *AWS SDK for Python (Boto3) API Reference*.

### `RegisterJobDefinition`
<a name="batch_RegisterJobDefinition_python_3_topic"></a>

The following code example shows how to use `RegisterJobDefinition`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def register_job_definition(
        self,
        job_definition_name: str,
        execution_role_arn: str,
        image: str = "public.ecr.aws/amazonlinux/amazonlinux:2023",
        command: Optional[list] = None,
        vcpus: str = "0.25",
        memory: str = "512",
    ) -> dict:
        """
        Registers a Fargate job definition.

        :param job_definition_name: The name for the job definition.
        :param execution_role_arn: The ARN of the IAM execution role that grants
            the Fargate agent permission to pull the container image and write
            logs. This is required for Fargate jobs; without it the API call
            fails with "executionRoleArn is required for Fargate jobs."
        :param image: The container image to use.
        :param command: The command to run in the container.
        :param vcpus: The number of vCPUs (as a string). Fargate accepts
            fractional values such as "0.25".
        :param memory: The memory in MiB (as a string).
        :return: A dictionary with the job definition name, ARN, and revision.
        """
        if command is None:
            command = ["echo", "Hello from AWS Batch!"]
        try:
            container_properties = {
                "image": image,
                "command": command,
                "resourceRequirements": [
                    {"type": "VCPU", "value": vcpus},
                    {"type": "MEMORY", "value": memory},
                ],
                "networkConfiguration": {"assignPublicIp": "ENABLED"},
                "fargatePlatformConfiguration": {"platformVersion": "LATEST"},
                "executionRoleArn": execution_role_arn,
            }
            response = self.batch_client.register_job_definition(
                jobDefinitionName=job_definition_name,
                type="container",
                # platformCapabilities must be FARGATE; otherwise Batch treats
                # this as an EC2 job definition and rejects fractional vCPUs.
                platformCapabilities=["FARGATE"],
                containerProperties=container_properties,
            )
            logger.info(
                "Registered job definition %s revision %d: %s",
                response["jobDefinitionName"],
                response["revision"],
                response["jobDefinitionArn"],
            )
            return response
        except ClientError as err:
            logger.error(
                "Error registering job definition %s: %s",
                job_definition_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [RegisterJobDefinition](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/RegisterJobDefinition) in *AWS SDK for Python (Boto3) API Reference*.

### `SubmitJob`
<a name="batch_SubmitJob_python_3_topic"></a>

The following code example shows how to use `SubmitJob`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def submit_job(self, job_name: str, job_queue: str, job_definition: str) -> dict:
        """
        Submits a job to a job queue.

        :param job_name: A descriptive name for the job.
        :param job_queue: The job queue name or ARN.
        :param job_definition: The job definition name:revision or ARN.
        :return: A dictionary with the job name, ID, and ARN.
        """
        try:
            response = self.batch_client.submit_job(
                jobName=job_name,
                jobQueue=job_queue,
                jobDefinition=job_definition,
            )
            logger.info(
                "Submitted job %s (ID: %s): %s",
                response["jobName"],
                response["jobId"],
                response.get("jobArn", ""),
            )
            return response
        except ClientError as err:
            logger.error(
                "Error submitting job %s: %s",
                job_name,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [SubmitJob](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/SubmitJob) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateComputeEnvironment`
<a name="batch_UpdateComputeEnvironment_python_3_topic"></a>

The following code example shows how to use `UpdateComputeEnvironment`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def update_compute_environment(self, compute_environment: str, state: str) -> dict:
        """
        Updates a compute environment, such as disabling it before deletion.

        A compute environment must be DISABLED before it can be deleted;
        calling ``delete_compute_environment`` on an ENABLED environment raises
        "Cannot delete an enabled compute environment, set the state to
        DISABLED first."

        :param compute_environment: The compute environment name or ARN.
        :param state: The new state (ENABLED or DISABLED).
        :return: The response dictionary.
        """
        try:
            response = self.batch_client.update_compute_environment(
                computeEnvironment=compute_environment, state=state
            )
            logger.info(
                "Updated compute environment %s to state %s.",
                compute_environment,
                state,
            )
            return response
        except ClientError as err:
            logger.error(
                "Error updating compute environment %s: %s",
                compute_environment,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [UpdateComputeEnvironment](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateComputeEnvironment) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateJobQueue`
<a name="batch_UpdateJobQueue_python_3_topic"></a>

The following code example shows how to use `UpdateJobQueue`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def update_job_queue(self, job_queue: str, state: str) -> dict:
        """
        Updates a job queue, such as disabling it before deletion.

        :param job_queue: The job queue name or ARN.
        :param state: The new state (ENABLED or DISABLED).
        :return: The response dictionary.
        """
        try:
            response = self.batch_client.update_job_queue(
                jobQueue=job_queue, state=state
            )
            logger.info("Updated job queue %s to state %s.", job_queue, state)
            return response
        except ClientError as err:
            logger.error(
                "Error updating job queue %s: %s",
                job_queue,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [UpdateJobQueue](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateJobQueue) in *AWS SDK for Python (Boto3) API Reference*.
