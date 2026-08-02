---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/architecture.html
---

# Architecture
<a name="architecture"></a>

AWS Mainframe Modernization Replatform with Micro Focus is available in two modes:
+ AWS Replatform with Micro Focus is a serverless managed runtime environment that is dynamically deployed with a Micro Focus backend and is fully managed by AWS. AWS Replatform with Micro Focus provides a cloud-native API layer for interacting with Micro Focus. In this managed approach, only Micro Focus is available for replatforming. The UniKix solution isn't available.
+ AWS Replatform with Micro Focus on Amazon Elastic Compute Cloud (Amazon EC2) is delivered as an Amazon Machine Image (AMI) of a preinstalled Micro Focus environment that you launch on the EC2 instance type that you choose. This custom deployment exposes native Micro Focus directly.

Both modes include transaction managers, data mapping tools, screen and maps readers, and batch job run environments. You can use either mode to run mainframe applications on distributed servers with minimal changes to the source code.

The following diagram shows workflow integration where Control-M is hosted on an Amazon EC2 instance. An Amazon Aurora database is used for maintaining the data required to manage and run batch jobs. The architecture is a Multi-Availability Zone (Multi-AZ) deployment for high availability. Applications' batch jobs and data are orchestrated in the AWS Replatform with Micro Focus runtime environment. The diagram shows both AWS Replatform with Micro Focus modes: fully managed and custom on Amazon EC2.

![Diagram showing both configurations.](http://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/images/guide-img/ca7d4793-feac-4eba-a6cd-6ca4d6395925/images/f868f8cf-4803-4508-8660-ca2bf1eee3f9.png)

The diagram shows the following resources:

1. In the on-premises environment, the Control-M Agent is installed to control workloads still running on IBM Z/OS or other workload. The workloads that are running on x86 connect to the AWS environment through AWS Direct Connect.

1. Control-M Server is installed on a pair of EC2 instances in an active-passive mode in a Multi-AZ environment for high availability and disaster recovery.

1. The Amazon Aurora backend database used by Control-M (running on an EC2 instance) is deployed with a replica in the secondary Availability Zone for high availability and disaster recovery.

1. A separate VPC contains an EC2 instance that has AWS Replatform with Micro Focus delivered as an AMI of a preinstalled Micro Focus environment. Control-M Agent is installed on this instance to interact with Micro Focus utilities that provide extended job management capabilities.

During the migration project, you might still be managing workload in non AWS locations on both mainframe and distributed servers. The architecture shown isn't intended to be prescriptive but to provide a general direction. We recommend that a detailed configuration, including disaster recovery options, is constructed as part of the Control-M implementation.
