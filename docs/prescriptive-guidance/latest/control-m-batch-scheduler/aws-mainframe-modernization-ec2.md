---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/aws-mainframe-modernization-ec2.html
---

# AWS Mainframe Modernization on Amazon EC2 integration with Control-M
<a name="aws-mainframe-modernization-ec2"></a>

This section describes how Control-M integrates with and supports batch jobs that run in a custom AWS Mainframe Modernization runtime environment deployed on an EC2 instance. If you are implementing the fully managed AWS Replatform with Micro Focus runtime environment, see the [Managed AWS Mainframe Modernization integration with Control-M](aws-mainframe-modernization-managed.md) section.

This section assumes the following prerequisites:
+ An active AWS account.
+ A virtual private cloud (VPC) where the EC2 instances will be created.
+ The mainframe application is migrated and running in an AWS Replatform with Micro Focus environment on an EC2 instance and is supporting the Micro Focus runtime engine with multiple defined batch jobs. For this pilot, follow the instructions at [Replatforming applications with Micro Focus](https://docs.aws.amazon.com/m2/latest/userguide/replatforming-m2.html). The documentation includes all tasks and additional information on configuring and operating the AWS Replatform with Micro Focus runtime environment on Amazon EC2.

This following topics cover the setup required for integration between Control-M and the AWS Replatform with Micro Focus environment:
+ [Deploy Control-M and Micro Focus resources](deploy-resources-environment.md)
+ [Create a Control-M connection profile](create-control-m-connection-profile.md)
+ [Create jobs and schedules in Control-M Planning](create-jobs-schedules-control-m-planning.md)
+ [Manage job runs in Control-M by using Monitoring](monitor.md)
