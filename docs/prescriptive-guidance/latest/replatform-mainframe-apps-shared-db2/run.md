---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/run.html
---

# Running
<a name="run"></a>

To ensure optimal performance and low latency between your cloud-based application and your on-premises database, we recommend that you implement [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html). This service provides a dedicated network connection between AWS and your organization's data center, and offers more consistent network performance and reduced latency compared with internet-based connections. This is particularly crucial for database operations that require quick response times.

To achieve high availability (HA) and elasticity for the application that's running on AWS, you can implement a robust architecture by using the following components:
+ **Elastic Load Balancing (ELB)**: You can deploy a load balancer to distribute incoming traffic across multiple Amazon Elastic Compute Cloud (Amazon EC2) instances that your application runs on. This ensures even distribution of the workload and provides a single entry point for client requests.
+ **Auto Scaling group**: EC2 instances that host the application can be organized into an Auto Scaling group. This allows the infrastructure to automatically adjust the number of instances based on predefined metrics such as CPU utilization or network traffic. During peak times, additional instances can be launched to handle increased load, whereas during quieter periods, unnecessary instances can be terminated to optimize costs.
+ **EC2 instances**: The application can be deployed on EC2 instances within the Auto Scaling group. These instances should be distributed across multiple Availability Zones to enhance fault tolerance and ensure high availability.
+ **Multi-AZ deployment**: By spreading the application instances across multiple Availability Zones, the system can withstand the failure of a single Availability Zone without significant impact on overall availability.

This architecture enables the application to scale seamlessly based on demand while maintaining high availability. The load balancer ensures that traffic is distributed evenly across healthy instances, and the Auto Scaling group manages the number of instances based on actual workload.

To further enhance reliability, you can implement a robust monitoring and alerting system by using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to help detect and respond to any performance issues or failures promptly. Additionally, regular testing of the automatic scaling capabilities and failover scenarios will ensure that the system behaves as expected during various load conditions and potential failures.

By adopting this approach, you can benefit from the scalability and flexibility of the AWS Cloud while maintaining a secure connection to your on-premises Db2 database. This hybrid setup serves as an excellent path toward a full cloud migration, and provides gradual transition and risk mitigation throughout the process.

## Two-phase commit (2PC)
<a name="2pc"></a>

[AWS Mainframe Modernization Replatform with Rocket Software](https://aws.amazon.com/mainframe-modernization/capabilities/replatform-rocketsoftware/) offers support for two-phase commit (2PC) transactions through its implementation of extended architecture (XA). This capability is crucial for maintaining data integrity across distributed systems, particularly in mainframe environments where complex transactions often span multiple resources.

The XA architecture, which is integrated into AWS Replatform with Rocket Software, enables the coordination of transactions across diverse resources such as databases and message queues. This integration ensures that all parts of a distributed transaction either commit or roll back in unison, to maintain consistency across the system.

The 2PC process consists of two phases:
+ Prepare phase: The transaction manager queries all resource managers involved in the transaction to ensure that they're ready to commit.
+ Commit phase: If all resource managers respond positively, the transaction manager instructs them to commit the changes. If any of the resource managers cannot commit, all managers are instructed to roll back changes.

By using XA, AWS Replatform with Rocket Software provides a reliable and scalable solution for managing complex, distributed transactions in modernized mainframe environments. This feature is essential for organizations that want to migrate their mainframe applications to the cloud without compromising on transactional integrity or performance.

## Runtime infrastructure
<a name="running-architecture"></a>

The following diagram shows a highly available and elastic environment in the AWS Cloud that includes two Availability Zones, EC2 instances in an Auto Scaling group, a Network Load Balancer, and a dedicated connection between the AWS and mainframe environments through AWS Direct Connect.

![2PC architecture for replatforming mainframe applications.](https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/images/guide-img/b5c7b078-cfe6-46c4-b120-94b5824d3c88/images/ef1d449e-ee57-4664-ac6b-fc581a9af36d.png)

In this architecture:

1. When the AWS Mainframe Modernization runtime starts, it retrieves Db2 credentials from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) and opens a persistent connection with Db2 for z/OS.
**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

1. Clients bind the Network Load Balancer address in [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).

1. Route 53 redirects transactions to the the Network Load Balancer.

1. The Network Load Balancer distributes transactions across multiple EC2 instances.

1. The workload that's running on AWS Mainframe Modernization interacts with Db2 for z/OS by using a persistent connection through AWS Direct Connect.
