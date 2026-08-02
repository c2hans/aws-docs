---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/ecs-exec.html
---

# Amazon Elastic Container Service Exec in AWS Toolkit for Visual Studio Code
<a name="ecs-exec"></a>

You can issue single commands in an Amazon Elastic Container Service (Amazon ECS) container with the AWS Toolkit for Visual Studio Code, using the Amazon ECS Exec feature.

**Important**
Enabling and Disabling Amazon ECS Exec changes the state of resources in your AWS account. This includes stopping and restarting the service. Altering the state of resources while the Amazon ECS Exec is enabled can lead to unpredictable results. For more information about Amazon ECS, see the developer guide [Using Amazon ECS Exec for Debugging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-considerations).

## Amazon ECS Exec prerequisites
<a name="ecs-exec-prereq"></a>

Before you can use the Amazon ECS Exec feature, there are some prerequisite conditions that need to be met.

### Amazon ECS requirements
<a name="w2aac17c35c10c11b5"></a>

Depending on whether your tasks are hosted on Amazon EC2 or AWS Fargate, Amazon ECS Exec has different version requirements.
+ If you're using Amazon EC2, you must use an Amazon ECS optimized AMI that was released after January 20th, 2021, with an agent version of 1.50.2 or greater. Additional information is available for you in the developer guide [Amazon ECS optimized AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html).
+ If you're using AWS Fargate, you must use platform version 1.4.0 or higher. Additional information about Fargate requirements is available to you in the developer guide [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

### AWS account configuration and IAM permissions
<a name="w2aac17c35c10c11b7"></a>

To use the Amazon ECS Exec feature, you need to have an existing Amazon ECS cluster associated with your AWS account. Amazon ECS Exec uses Systems Manager to establish a connection with the containers on your cluster and requires specific Task IAM Role Permissions to communicate with the SSM service.

You can find IAM role and policy information, specific to Amazon ECS Exec, in the [IAM permissions required for ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-enabling-and-using) developer guide.

## Working with the Amazon ECS Exec
<a name="w2aac17c35c10c15"></a>

You can enable or disable the Amazon ECS Exec directly from the AWS Explorer in the Toolkit for VS Code. When you have enabled Amazon ECS Exec, you can choose containers from the Amazon ECS menu and then run commands against them.

### Enabling Amazon ECS Exec
<a name="w2aac17c35c10c15b5"></a>

1. From the AWS Explorer, locate and expand the Amazon ECS menu.

1. Expand the cluster with the service that you want to modify.

1. Open the context menu for (right-click) the service and choose **Enable Command Execution**.

**Important**
This will start a new deployment of your Service and may take a few minutes. For more information, see the note at the beginning of this section.

### Disabling Amazon ECS Exec
<a name="w2aac17c35c10c15b7"></a>

1. From the AWS Explorer, locate and expand the Amazon ECS menu.

1. Expand the cluster that houses the service you want.

1. Open the context menu for (right-click) the service and choose **Disable Command Execution**.

**Important**
This will start a new deployment of your Service and may take a few minutes. For more information, see the note at the beginning of this section.)

### Running commands against a Container
<a name="w2aac17c35c10c15b9"></a>

To run commands against a container using the AWS Explorer, Amazon ECS Exec must be enabled. If it's not enabled, see the **Enabling ECS Exec** procedure in this section.

1. From the AWS Explorer, locate and expand the Amazon ECS menu.

1. Expand the cluster that houses the service you want.

1. Expand the service to list the associated containers.

1. Open the context menu for (right-click) the container and choose **Run Command in Container**.

1. A **prompt** will open with a list of running Tasks, choose the **Task ARN** that you want.
**Note**
If only one Task is running for that Service, it will be auto-selected and this step will be skipped.

1. When prompted, type the command that you want to run and press **Enter** to process.
