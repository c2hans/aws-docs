---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/cost-optimization-journey.html
---

# Cost optimization journey
<a name="cost-optimization-journey"></a>

The scope, timing, and specific path of your cloud migration journey depends on your business objectives, technical requirements, and other factors. This section provides an example of a cloud migration journey that's focused on [Cloud Financial Management with AWS](https://aws.amazon.com/aws-cost-management/) and adheres to MACO recommendations and best practices. You can use this example to gain an understanding of how to design a cloud migration journey for Microsoft workloads.

The following high-level tasks illustrate the approach that an organization could take to implement MACO recommendations and best practices:
+ Establish a tagging strategy and enable user-defined cost allocation tags. For more information, see the AWS Whitepaper [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html).
+ Define budgets based on applications, teams, or departments. For more information, see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) in the *AWS Billing and Cost Management User Guide*.
+ Perform an AWS Optimization and Licensing Assessment (AWS OLA) to accelerate savings. For more information, see [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) in the AWS documentation.
+ Bring Your Own License (BYOL) for Windows and SQL Server workloads by using Amazon Elastic Compute Cloud Dedicated Hosts. For more information, see the [Bring licenses for Windows and SQL Server workloads](byol-ded-hosts.md) section of this guide.
+ Optimize your SQL Server licensing on AWS. For more information, see the [Understand SQL Server licensing](sql-server-licensing.md) section of this guide.
+ Select the right instance type for Windows workloads. For more information, see the [Select the right instance type for Windows workloads](right-size-selection.md) section of this guide.
+ Select the right instance type for SQL workloads. For more information, see the [Select the right EC2 instance for SQL Server workloads](right-ec2-instance.md) section of this guide.
+ Migrate Amazon Elastic Block Store (Amazon EBS) from gp2 to gp3. For more information, see the [Migrate Amazon EBS volumes from gp2 to gp3](ebs-migrate-gp2-gp3.md) section of this guide.
+ Control workloads with EC2 Instance Scheduler on AWS. For more information, see the [Automate stop and start schedules](windows-ec2-schedules.md) section of this guide.
+ Remove SQL Server costs for non-production workloads by using SQL Server Developer Edition. For more information, see the [Assess SQL Server Developer edition](sql-server-dev.md) section of this guide.
+ Use a single Availability Zone for Amazon FSx for Windows File Server for development and testing workloads. For more information, see the [Use a single Availability Zone](storage-fsx-single-az.md) section of this guide.
+ Rightsize your Windows workloads by using AWS Compute Optimizer. For more information, see the [Right size Windows workloads](rightsize.md) section of this guide.
+ Optimize spending on Windows on Amazon EC2 by using Savings Plans. For more information, see the [Optimize spending for Windows on Amazon EC2](savings-plans.md) section of this guide.
+ Enable data deduplication on FSx for Windows File Server. For more information, see the [Enable data deduplication in Amazon FSx](storage-fsx-deduplication.md) section of this guide.
+ Use data sharding for file systems on FSx for Windows File Server. For more information, see the [Understand data sharding in Amazon FSx for Windows File Server](storage-fsx-data-sharding.md) section of this guide.
+ Optimize your SQL Server backup strategies. For more information, see the [Optimize SQL Server backup strategies](sql-server-backup.md) section of this guide.
+ Make static .NET framework apps support dynamic scaling. For more information, see the [Support dynamic scaling for static .NET Framework apps section](net-static.md) of this guide.
+ Use serverless .NET microservices. For more information, see the [Consider serverless .NET](net-serverless.md) section of this guide.
+ Move your Windows apps to containers. For more information, see the [Containerize .NET apps](net-containerize.md) section of this guide.
+ Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to rightsize Windows containers running on AWS Fargate for Amazon Elastic Container Service (Amazon ECS). For more information, see the [Enable AWS Compute Optimizer](optimizer-ecs-fargate.md#optimizer-ecs-fargate-rec) section of this guide.
+ Refactor to modern .NET and move to Linux. For more information, see the [Refactor to modern .NET and move to Linux](net-refactor-linux.md) section of this guide.
+ Leverage Graviton instances and containers. For more information, see the [Use Graviton instances and containers](net-graviton.md) section of this guide.
+ Modernize SQL Server databases. For more information, see the [Modernize SQL Server databases](modernize-sql-server.md) section of this guide.
+ Design Active Directory infrastructure. For more information, see the [Active Directory](active-directory-main.md) section of this guide.

For more information about a customer journey focused on Cloud Financial Management with AWS, see the AWS Whitepaper [Cloud Financial Management capability](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/cloud-financial-management-capability.html).
