---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs.html
---

# Create an Amazon ECS task definition and mount a file system on EC2 instances using Amazon EFS
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs"></a>

*Durga Prasad Cheepuri, Amazon Web Services*

## Summary
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs-summary"></a>

This pattern provides code samples and steps to create an Amazon Elastic Container Service (Amazon ECS) task definition that runs on Amazon Elastic Compute Cloud (Amazon EC2) instances in the Amazon Web Services (AWS) Cloud, while using Amazon Elastic File System (Amazon EFS) to mount a file system on those EC2 instances. Amazon ECS tasks that use Amazon EFS automatically mount the file systems that you specify in the task definition and make these file systems available to the task’s containers across all Availability Zones in an AWS Region.

To meet your persistent storage and shared storage requirements, you can use Amazon ECS and Amazon EFS together. For example, you can use Amazon EFS to store persistent user data and application data for your applications with active and standby ECS container pairs running in different Availability Zones for high availability. You can also use Amazon EFS to store shared data that can be accessed in parallel by ECS containers and distributed job workloads.

To use Amazon EFS with Amazon ECS, you can add one or more volume definitions to a task definition. A volume definition includes an Amazon EFS file system ID, access point ID, and a configuration for AWS Identity and Access Management (IAM) authorization or Transport Layer Security (TLS) encryption in transit. You can use container definitions within task definitions to specify the task definition volumes that get mounted when the container runs. When a task that uses an Amazon EFS file system runs, Amazon ECS ensures that the file system is mounted and available to the containers that need access to it.

## Prerequisites and limitations
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A virtual private cloud (VPC) with a virtual private network (VPN) endpoint or a router
+ (Recommended) [Amazon ECS container agent 1.38.0 or later](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-versions.html) for compatibility with Amazon EFS access points and IAM authorization features (For more information, see the AWS blog post [New for Amazon EFS – IAM Authorization and Access Points](https://aws.amazon.com/blogs/aws/new-for-amazon-efs-iam-authorization-and-access-points/).)

**Limitations**
+ Amazon ECS container agent versions earlier than 1.35.0 don’t support Amazon EFS file systems for tasks that use the EC2 launch type.

## Architecture
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs-architecture"></a>

The following diagram shows an example of an application that uses Amazon ECS to create a task definition and mount an Amazon EFS file system on EC2 instances in ECS containers.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/090a3f03-a4c6-47e3-b1ae-b0eb5c5b269c/images/343e0f1d-44ee-4ec2-8392-aeddc0e48b83.png)

The diagram shows the following workflow:

1. Create an Amazon EFS file system.

1. Create a task definition with a container.

1. Configure the container instances to mount the Amazon EFS file system. The task definition references the volume mounts, so the container instance can use the Amazon EFS file system. ECS tasks have access to the same Amazon EFS file system, regardless of which container instance those tasks are created on.

1. Create an Amazon ECS service with three instances of the task definition.

**Technology stack**
+ Amazon EC2
+ Amazon ECS
+ Amazon EFS

## Tools
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs-tools"></a>
+ [Amazon EC2](https://docs.aws.amazon.com/ec2/?id=docs_gateway) – Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud. You can use Amazon EC2 to launch as many or as few virtual servers as you need, and you can scale out or scale in.
+ [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) – Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast container management service for running, stopping, and managing containers on a cluster. You can run your tasks and services on a serverless infrastructure that is managed by AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of EC2 instances that you manage.
+ [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) – Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources.
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) – The AWS Command Line Interface (AWS CLI) is an open-source tool for interacting with AWS services through commands in your command-line shell. With minimal configuration, you can run AWS CLI commands that implement functionality equivalent to that provided by the browser-based AWS Management Console from a command prompt.

## Epics
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs-epics"></a>

### Create an Amazon EFS file system
<a name="create-an-amazon-efs-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EFS file system by using the AWS Management Console. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs.html) | AWS DevOps |

### Create an Amazon ECS task definition by using either an Amazon EFS file system or the AWS CLI
<a name="create-an-amazon-ecs-task-definition-by-using-either-an-amazon-efs-file-system-or-the-aws-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a task definition using an Amazon EFS file system. | Create a task definition by using the [new Amazon ECS console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html) or [classic Amazon ECS console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition-classic.html) with the following configurations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs.html) | AWS DevOps |
| Create a task definition using the AWS CLI. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs.html) | AWS DevOps |

## Related resources
<a name="create-an-amazon-ecs-task-definition-and-mount-a-file-system-on-ec2-instances-using-amazon-efs-resources"></a>
+ [Amazon ECS task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
+ [Amazon EFS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html)

## Attachments
<a name="attachments-090a3f03-a4c6-47e3-b1ae-b0eb5c5b269c"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/090a3f03-a4c6-47e3-b1ae-b0eb5c5b269c/attachments/attachment.zip)
