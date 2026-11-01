---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_batch_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Batch examples using AWS CLI
<a name="cli_2_batch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Batch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `cancel-job`
<a name="batch_CancelJob_cli_2_topic"></a>

The following code example shows how to use `cancel-job`.

**AWS CLI**
**To cancel a job**
The following `cancel-job` example cancels a job with the specified job ID.

```
aws batch cancel-job \
    --job-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --reason {{"Cancelling job."}}
```
This command produces no output.
For more information, see [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html) in the *AWS Batch User Guide*.
+  For API details, see [CancelJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/cancel-job.html) in *AWS CLI Command Reference*.

### `create-compute-environment`
<a name="batch_CreateComputeEnvironment_cli_2_topic"></a>

The following code example shows how to use `create-compute-environment`.

**AWS CLI**
**Example 1: To create a managed compute environment with On-Demand instances**
The following `create-compute-environment` example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand.

```
aws batch create-compute-environment \
    --cli-input-json {{file://<path_to_json_file>/C4OnDemand.json}}
```
Contents of `C4OnDemand.json`:

```
{
    "computeEnvironmentName": "C4OnDemand",
    "type": "MANAGED",
    "state": "ENABLED",
    "computeResources": {
        "type": "EC2",
        "minvCpus": 0,
        "maxvCpus": 128,
        "desiredvCpus": 48,
        "instanceTypes": [
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge"
        ],
        "subnets": [
            "subnet-220c0e0a",
            "subnet-1a95556d",
            "subnet-978f6dce"
        ],
        "securityGroupIds": [
            "sg-cf5093b2"
        ],
        "ec2KeyPair": "id_rsa",
        "instanceRole": "ecsInstanceRole",
        "tags": {
            "Name": "Batch Instance - C4OnDemand"
        }
    },
    "serviceRole": "arn:aws:iam::123456789012:role/AWSBatchServiceRole"
}
```
Output:

```
{
    "computeEnvironmentName": "C4OnDemand",
    "computeEnvironmentArn": "arn:aws:batch:us-west-2:123456789012:compute-environment/C4OnDemand"
}
```
For more information, see [Create a compute environment](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment.html) in the *AWS Batch User Guide*.
**Example 2: To create a managed compute environment with Spot Instances**
The following `create-compute-environment` example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot.

```
aws batch create-compute-environment \
    --cli-input-json {{file://<path_to_json_file>/M4Spot.json}}
```
Contents of `M4Spot.json`:

```
{
    "computeEnvironmentName": "M4Spot",
    "type": "MANAGED",
    "state": "ENABLED",
    "computeResources": {
        "type": "SPOT",
        "spotIamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-role",
        "minvCpus": 0,
        "maxvCpus": 128,
        "desiredvCpus": 4,
        "instanceTypes": [
            "m4"
        ],
        "bidPercentage": 20,
        "subnets": [
            "subnet-220c0e0a",
            "subnet-1a95556d",
            "subnet-978f6dce"
        ],
        "securityGroupIds": [
            "sg-cf5093b2"
        ],
        "ec2KeyPair": "id_rsa",
        "instanceRole": "ecsInstanceRole",
        "tags": {
            "Name": "Batch Instance - M4Spot"
        }
    },
    "serviceRole": "arn:aws:iam::123456789012:role/AWSBatchServiceRole"
}
```
Output:

```
{
    "computeEnvironmentName": "M4Spot",
    "computeEnvironmentArn": "arn:aws:batch:us-west-2:123456789012:compute-environment/M4Spot"
}
```
For more information, see [Create a compute environment](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment.html) in the *AWS Batch User Guide*.
+  For API details, see [CreateComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html) in *AWS CLI Command Reference*.

### `create-job-queue`
<a name="batch_CreateJobQueue_cli_2_topic"></a>

The following code example shows how to use `create-job-queue`.

**AWS CLI**
**Example 1: To create a low priority job queue with a single compute environment**
The following `create-job-queue` example creates a job queue called LowPriority that uses the M4Spot compute environment.

```
aws batch create-job-queue \
    --cli-input-json {{file://<path_to_json_file>/LowPriority.json}}
```
Contents of `LowPriority.json`:

```
{
    "jobQueueName": "LowPriority",
    "state": "ENABLED",
    "priority": 10,
    "computeEnvironmentOrder": [
        {
            "order": 1,
            "computeEnvironment": "M4Spot"
        }
    ]
}
```
Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-west-2:123456789012:job-queue/LowPriority",
    "jobQueueName": "LowPriority"
}
```
For more information, see [Create a job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue.html) in the *AWS Batch User Guide*.
**Example 2: To create a high priority job queue with two compute environments**
The following `create-job-queue` example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2. The scheduler will attempt to place jobs on the C4OnDemand compute environment first.

```
aws batch create-job-queue \
    --cli-input-json {{file://<path_to_json_file>/HighPriority.json}}
```
Contents of `HighPriority.json`:

```
{
    "jobQueueName": "HighPriority",
    "state": "ENABLED",
    "priority": 1,
    "computeEnvironmentOrder": [
        {
            "order": 1,
            "computeEnvironment": "C4OnDemand"
        },
        {
            "order": 2,
            "computeEnvironment": "M4Spot"
        }
    ]
}
```
Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-west-2:123456789012:job-queue/HighPriority",
    "jobQueueName": "HighPriority"
}
```
For more information, see [Create a job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue.html) in the *AWS Batch User Guide*.
+  For API details, see [CreateJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html) in *AWS CLI Command Reference*.

### `delete-compute-environment`
<a name="batch_DeleteComputeEnvironment_cli_2_topic"></a>

The following code example shows how to use `delete-compute-environment`.

**AWS CLI**
**To delete a compute environment**
The following `delete-compute-environment` example deletes the P2OnDemand compute environment.

```
aws batch delete-compute-environment \
    --compute-environment {{P2OnDemand}}
```
This command produces no output.
For more information, see [Compute environments for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the *AWS Batch User Guide*.
+  For API details, see [DeleteComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-compute-environment.html) in *AWS CLI Command Reference*.

### `delete-job-queue`
<a name="batch_DeleteJobQueue_cli_2_topic"></a>

The following code example shows how to use `delete-job-queue`.

**AWS CLI**
**To delete a job queue**
The following `delete-job-queue` example deletes the GPGPU job queue.

```
aws batch delete-job-queue \
    --job-queue {{GPGPU}}
```
This command produces no output.
For more information, see [Delete a job queue in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/delete-job-queue.html) in the *AWS Batch User Guide*.
+  For API details, see [DeleteJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-job-queue.html) in *AWS CLI Command Reference*.

### `deregister-job-definition`
<a name="batch_DeregisterJobDefinition_cli_2_topic"></a>

The following code example shows how to use `deregister-job-definition`.

**AWS CLI**
**To deregister a job definition**
The following `deregister-job-definition` example deregisters a job definition called sleep10.

```
aws batch deregister-job-definition \
    --job-definition {{sleep10}}
```
This command produces no output.
For more information, see [Job definitions](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html) in the *AWS Batch User Guide*.
+  For API details, see [DeregisterJobDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/deregister-job-definition.html) in *AWS CLI Command Reference*.

### `describe-compute-environments`
<a name="batch_DescribeComputeEnvironments_cli_2_topic"></a>

The following code example shows how to use `describe-compute-environments`.

**AWS CLI**
**To describe a compute environment**
The following `describe-compute-environments` example describes the P2OnDemand compute environment.

```
aws batch describe-compute-environments \
    --compute-environments {{P2OnDemand}}
```
Output:

```
{
    "computeEnvironments": [
        {
            "status": "VALID",
            "serviceRole": "arn:aws:iam::123456789012:role/AWSBatchServiceRole",
            "computeEnvironmentArn": "arn:aws:batch:us-west-2:123456789012:compute-environment/P2OnDemand",
            "computeResources": {
                "subnets": [
                    "subnet-220c0e0a",
                    "subnet-1a95556d",
                    "subnet-978f6dce"
                ],
                "tags": {
                    "Name": "Batch Instance - P2OnDemand"
                },
                "desiredvCpus": 48,
                "minvCpus": 0,
                "instanceTypes": [
                    "p2"
                ],
                "securityGroupIds": [
                    "sg-cf5093b2"
                ],
                "instanceRole": "ecsInstanceRole",
                "maxvCpus": 128,
                "type": "EC2",
                "ec2KeyPair": "id_rsa"
            },
            "statusReason": "ComputeEnvironment Healthy",
            "ecsClusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/P2OnDemand_Batch_2c06f29d-d1fe-3a49-879d-42394c86effc",
            "state": "ENABLED",
            "computeEnvironmentName": "P2OnDemand",
            "type": "MANAGED"
        }
    ]
}
```
For more information, see [Compute environments for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the *AWS Batch User Guide*.
+  For API details, see [DescribeComputeEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-compute-environments.html) in *AWS CLI Command Reference*.

### `describe-job-definitions`
<a name="batch_DescribeJobDefinitions_cli_2_topic"></a>

The following code example shows how to use `describe-job-definitions`.

**AWS CLI**
**To describe active job definitions**
The following `describe-job-definitions` example describes all of your active job definitions.

```
aws batch describe-job-definitions \
    --status {{ACTIVE}}
```
Output:

```
{
    "jobDefinitions": [
        {
            "status": "ACTIVE",
            "jobDefinitionArn": "arn:aws:batch:us-west-2:123456789012:job-definition/sleep60:1",
            "containerProperties": {
                "mountPoints": [],
                "image": "busybox",
                "environment": [],
                "vcpus": 1,
                "command": [
                    "sleep",
                    "60"
                ],
                "volumes": [],
                "memory": 128,
                "ulimits": []
            },
            "parameters": {},
            "type": "container",
            "jobDefinitionName": "sleep60",
            "revision": 1
        }
    ]
}
```
For more information, see [Job definitions](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html) in the *AWS Batch User Guide*.
+  For API details, see [DescribeJobDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-definitions.html) in *AWS CLI Command Reference*.

### `describe-job-queues`
<a name="batch_DescribeJobQueues_cli_2_topic"></a>

The following code example shows how to use `describe-job-queues`.

**AWS CLI**
**To describe a job queue**
The following `describe-job-queues` example describes the HighPriority job queue.

```
aws batch describe-job-queues \
    --job-queues {{HighPriority}}
```
Output:

```
{
    "jobQueues": [
        {
            "status": "VALID",
            "jobQueueArn": "arn:aws:batch:us-west-2:123456789012:job-queue/HighPriority",
            "computeEnvironmentOrder": [
                {
                    "computeEnvironment": "arn:aws:batch:us-west-2:123456789012:compute-environment/C4OnDemand",
                    "order": 1
                }
            ],
            "statusReason": "JobQueue Healthy",
            "priority": 1,
            "state": "ENABLED",
            "jobQueueName": "HighPriority"
        }
    ]
}
```
For more information, see [Job queues](https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html) in the *AWS Batch User Guide*.
+  For API details, see [DescribeJobQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-queues.html) in *AWS CLI Command Reference*.

### `describe-jobs`
<a name="batch_DescribeJobs_cli_2_topic"></a>

The following code example shows how to use `describe-jobs`.

**AWS CLI**
**To describe a job**
The following `describe-jobs` example describes a job with the specified job ID.

```
aws batch describe-jobs \
    --jobs {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "jobs": [
        {
            "status": "SUBMITTED",
            "container": {
                "mountPoints": [],
                "image": "busybox",
                "environment": [],
                "vcpus": 1,
                "command": [
                    "sleep",
                    "60"
                ],
                "volumes": [],
                "memory": 128,
                "ulimits": []
            },
            "parameters": {},
            "jobDefinition": "arn:aws:batch:us-west-2:123456789012:job-definition/sleep60:1",
            "jobQueue": "arn:aws:batch:us-west-2:123456789012:job-queue/HighPriority",
            "jobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "dependsOn": [],
            "jobName": "example",
            "createdAt": 1480483387803
        }
    ]
}
```
For more information, see [Jobs](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html) in the *AWS Batch User Guide*.
+  For API details, see [DescribeJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html) in *AWS CLI Command Reference*.

### `list-jobs`
<a name="batch_ListJobs_cli_2_topic"></a>

The following code example shows how to use `list-jobs`.

**AWS CLI**
**Example 1: To list running jobs**
The following `list-jobs` example lists the running jobs in the HighPriority job queue.

```
aws batch list-jobs \
    --job-queue {{HighPriority}}
```
Output:

```
{
    "jobSummaryList": [
        {
            "jobName": "example",
            "jobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
    ]
}
```
For more information, see [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html) in the *AWS Batch User Guide*.
**Example 2: To list submitted jobs**
The following `list-jobs` example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.

```
aws batch list-jobs \
    --job-queue {{HighPriority}} \
    --job-status {{SUBMITTED}}
```
Output:

```
{
    "jobSummaryList": [
        {
            "jobName": "example",
            "jobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
    ]
}
```
For more information, see [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html) in the *AWS Batch User Guide*.
+  For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html) in *AWS CLI Command Reference*.

### `register-job-definition`
<a name="batch_RegisterJobDefinition_cli_2_topic"></a>

The following code example shows how to use `register-job-definition`.

**AWS CLI**
**To register a job definition**
The following `register-job-definition` example registers a job definition for a simple container job.

```
aws batch register-job-definition \
    --job-definition-name {{sleep30}} \
    --type {{container}} \
    --container-properties '{{{ "image": "busybox", "vcpus": 1, "memory": 128, "command": [ "sleep", "30"]}}}'
```
Output:

```
{
    "jobDefinitionArn": "arn:aws:batch:us-west-2:123456789012:job-definition/sleep30:1",
    "jobDefinitionName": "sleep30",
    "revision": 1
}
```
For more information, see [Create a single-node job definition](https://docs.aws.amazon.com/batch/latest/userguide/create-job-definition.html) in the *AWS Batch User Guide*.
+  For API details, see [RegisterJobDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html) in *AWS CLI Command Reference*.

### `submit-job`
<a name="batch_SubmitJob_cli_2_topic"></a>

The following code example shows how to use `submit-job`.

**AWS CLI**
**To submit a job**
The following `submit-job` example submits a simple container job called example to the HighPriority job queue.

```
aws batch submit-job \
    --job-name {{example}} \
    --job-queue {{HighPriority}} \
    --job-definition {{sleep60}}
```
Output:

```
{
    "jobName": "example",
    "jobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Tutorial: submit a job](https://docs.aws.amazon.com/batch/latest/userguide/submit_job.html) in the *AWS Batch User Guide*.
+  For API details, see [SubmitJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html) in *AWS CLI Command Reference*.

### `terminate-job`
<a name="batch_TerminateJob_cli_2_topic"></a>

The following code example shows how to use `terminate-job`.

**AWS CLI**
**To terminate a job**
The following `terminate-job` example terminates a job with the specified job ID.

```
aws batch terminate-job \
    --job-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --reason {{"Terminating job."}}
```
This command produces no output.
For more information, see [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html) in the *AWS Batch User Guide*.
+  For API details, see [TerminateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/terminate-job.html) in *AWS CLI Command Reference*.

### `update-compute-environment`
<a name="batch_UpdateComputeEnvironment_cli_2_topic"></a>

The following code example shows how to use `update-compute-environment`.

**AWS CLI**
**To update a compute environment**
The following `update-compute-environment` example disables the P2OnDemand compute environment so it can be deleted.

```
aws batch update-compute-environment \
    --compute-environment {{P2OnDemand}} \
    --state {{DISABLED}}
```
Output:

```
{
    "computeEnvironmentName": "P2OnDemand",
    "computeEnvironmentArn": "arn:aws:batch:us-west-2:123456789012:compute-environment/P2OnDemand"
}
```
For more information, see [Update a compute environment in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html) in the *AWS Batch User Guide*.
+  For API details, see [UpdateComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html) in *AWS CLI Command Reference*.

### `update-job-queue`
<a name="batch_UpdateJobQueue_cli_2_topic"></a>

The following code example shows how to use `update-job-queue`.

**AWS CLI**
**To update a job queue**
The following `update-job-queue` example disables a job queue so that it can be deleted.

```
aws batch update-job-queue \
    --job-queue {{GPGPU}} \
    --state {{DISABLED}}
```
Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-west-2:123456789012:job-queue/GPGPU",
    "jobQueueName": "GPGPU"
}
```
For more information, see [Delete a job queue in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/delete-job-queue.html) in the *AWS Batch User Guide*.
+  For API details, see [UpdateJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-job-queue.html) in *AWS CLI Command Reference*.
