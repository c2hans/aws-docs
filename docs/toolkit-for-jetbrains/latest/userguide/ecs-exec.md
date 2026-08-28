---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/ecs-exec.html
---

# Amazon Elastic Container Service (Amazon ECS) Exec in AWS Toolkit
<a name="ecs-exec"></a>

You can use the Amazon ECS Exec feature to issue single commands or run a shell in an Amazon Elastic Container Service (Amazon ECS) container, directly from the AWS Toolkit.

**Important**
Enabling and Disabling Amazon ECS Exec changes the state of resources in your AWS account. This includes stopping and restarting the service. Altering the state of resources while the Amazon ECS Exec is enabled can lead to unpredictable results. For more information about Amazon ECS Exec, see the developer guide [Using Amazon ECS Exec for Debugging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-considerations).

## Amazon ECS Exec prerequisites
<a name="ecs-exec-prereq"></a>

Before you can use the Amazon ECS Exec feature, there are prerequisite conditions that need to be met.

**Important**
In order to enable Amazon ECS Exec for a particular service, Amazon ECS Cloud Debugging must be disbled for that service.

### Amazon ECS requirements
<a name="w2aac17c25b8c11b7"></a>

Depending on whether your tasks are hosted on Amazon EC2 or AWS Fargate, Amazon ECS Exec has different version requirements.
+ If you're using Amazon EC2, you must use an Amazon ECS optimized AMI that was released after January 20th, 2021, with an agent version of 1.50.2 or greater. Additional information is available for you in the developer guide [Amazon ECS optimized AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html).
+ If you're using AWS Fargate, you must use platform version 1.4.0 or higher. Additional information about Fargate requirements is available to you in the developer guide [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

### AWS account configuration and IAM permissions
<a name="w2aac17c25b8c11b9"></a>

To use the Amazon ECS Exec feature, you need to have an existing Amazon ECS cluster associated with your AWS account. Amazon ECS Exec uses Systems Manager to establish a connection with the containers on your cluster and requires specific Task IAM Role Permissions to communicate with the SSM service.

You can find IAM role and policy information, specific to Amazon ECS Exec, in the [IAM permissions required for ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-enabling-and-using) developer guide.

## Working with the Amazon ECS Exec
<a name="w2aac17c25b8c15"></a>

You can enable or disable Amazon ECS Exec directly from the AWS Explorer in the AWS Toolkit for JetBrains. When Amazon ECS Exec is enabled, you can choose containers from the Amazon ECS menu and then run commands against them.

### Enabling Amazon ECS Exec
<a name="w2aac17c25b8c15b5"></a>

1. From the AWS Explorer, expand the Amazon ECS menu.

1. Expand the **Clusters** section, and choose the cluster your want to modify.

1. Open the context menu for (right-click) the service you want to modify and choose **Enable Command Execution**.
**Note**
If Amazon ECS Cloud Debugging is enabled for this service, the **Enable Command Execution** option will not be available. Disabling Cloud Debugging will restore the option, but it will stop and restart your service.

**Important**
This will start a new deployment of your Service and may take a few minutes. For more information, see the note at the beginning of this section.)

### Disabling Amazon ECS Exec
<a name="w2aac17c25b8c15b7"></a>

1. From the AWS Explorer, expand the Amazon ECS menu.

1. Expand the **Clusters** section, and choose the cluster your want to modify.

1. Open the context menu for (right-click) the service you want to modify and choose **Disable Command Execution**.

**Important**
This will start a new deployment of your Service and may take a few minutes. For more information, see the note at the beginning of this section.

### Running commands against a Container
<a name="w2aac17c25b8c15b9"></a>

To run commands against a container using the AWS Explorer, Amazon ECS Exec must be enabled. If it's not enabled, see the **Enabling Amazon ECS Exec** procedure in this section.

1. From the AWS Explorer, expand the Amazon ECS menu.

1. Expand the **Clusters** section, and choose the cluster your want to modify.

1. Expand a service to list its containers.

1. Open the context menu for (right-click) the container you want to modify and choose **Run Command in Container**.

1. In the **Run Command in Container** dialog box, choose the **Task ARN** that you want.

1. You can type the command you want to run or select it from a list of commands that were run during the same session.

1. Choose **Execute**

### Running commands from within a shell
<a name="w2aac17c25b8c15c11"></a>

To run commands against a container from within a shell, using the AWS Explorer, Amazon ECS Exec must be enabled. If it's not enabled, see the **Enabling Amazon ECS Exec** procedure in this section.

1. From the AWS Explorer, expand the Amazon ECS menu.

1. Expand the **Clusters** section, and choose the cluster your want to modify.

1. Expand the service to list its containers.

1. Open the context menu for (right-click) the container you want to modify and choose **Open Interactive Shell**.

1. In the **Interactive Shell** dialog box, choose the **Task ARN** that you want.

1. Choose a shell from the corresponding drop down, or enter the name of the shell you want to interact with.

1. When you are satisfied with your settings, choose **Execute**.

1. When the shell opens in a terminal, you can enter commands to interact with the container.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
