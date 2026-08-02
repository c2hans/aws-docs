---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-sizing-compute-optimizer.html
---

# Optimize SQL Server sizing by using Compute Optimizer
<a name="sql-server-sizing-compute-optimizer"></a>

## Overview
<a name="sql-server-sizing-compute-optimizer-overview"></a>

[AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) helps database administrators (DBAs) discover Microsoft SQL Server workloads on Amazon Elastic Compute Cloud (Amazon EC2) and rightsize EC2 instances to reduce license costs by up to 25%. The [inferred workload type](https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-type.html) feature in Compute Optimizer uses machine learning (ML) and automatically detects the applications that might be running on your AWS resources. Compute Optimizer includes support for SQL Server as an inferred workload type. By using the inferred workload type feature, you can pinpoint cost-saving opportunities based on the specific workload running on your Amazon EC2 instances.

With this feature, you can categorize cost-saving opportunities by supported inferred workload types, such as SQL Server.  Compute Optimizer can automatically discover SQL Server EC2 instances that are over-provisioned. You can switch to the EC2 console to downsize the instance, which helps reduce the licensing and infrastructure costs.

You can also use Compute Optimizer to make SQL Server licensing recommendations. For more information, see [Optimize SQL Server licensing by using Compute Optimizer](sql-server-compute-optimizer.md) in this guide.

## Configure Compute Optimizer
<a name="sql-server-sizing-compute-optimizer-configuration"></a>

For instructions for using Compute Optimizer with SQL Server inferred workloads, see [Optimizing performance and reducing licensing costs: Leveraging AWS Compute Optimizer for Amazon EC2 SQL Server instances](https://aws.amazon.com/blogs/modernizing-with-aws/optimizing-performance-and-reducing-licensing-costs-leveraging-aws-compute-optimizer-for-ec2-sql-server-instances/) (AWS Blog). You can opt in for standalone accounts, accounts that are a member of an organization, and management accounts of an organization. For standalone and member accounts, opting in enables Compute Optimizer for that account only. For an organization management account, you can choose whether to enable Compute Optimizer in that account only or for all member accounts of the organization.

The Compute Optimizer opt-in process automatically creates an AWS Identity and Access Management (IAM) service-linked role. For more information, see [Using service-linked roles for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/using-service-linked-roles.html).

Compute Optimizer analyzes your resources based on Amazon CloudWatch metrics, such as CPU, I/O, network, and Amazon Elastic Block Store (Amazon EBS) usage. To generate recommendations, at least 30 consecutive hours of CloudWatch metric data is required in the past 14 days. If you enable the enhanced infrastructure metrics feature, it extends the utilization metrics to 93 days. For more information, see [CloudWatch metric requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-metrics) and [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the Compute Optimizer documentation.

Compute Optimizer provides options and the savings associated with each option, based on vCPU, memory, storage, network, risk, and migration effort. You can use the CloudWatch metrics dashboard to analyze the data being used to make the recommendation. With this data, you can rightsize your EC2 instances that are running SQL Server workloads. For more information about how to change your instance type, see [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the Amazon EC2 documentation.

## Additional resources
<a name="sql-server-sizing-compute-optimizer-resources"></a>
+ [AWS Compute Optimizer identifies and filters Microsoft SQL Server workloads](https://aws.amazon.com/about-aws/whats-new/2023/05/aws-compute-optimizer-identifies-filters-sql-server-workloads/) (AWS)
+ [Optimizing performance and reducing licensing costs: Leveraging AWS Compute Optimizer for Amazon EC2 SQL Server instances](https://aws.amazon.com/blogs/modernizing-with-aws/optimizing-performance-and-reducing-licensing-costs-leveraging-aws-compute-optimizer-for-ec2-sql-server-instances/) (AWS Blog)
+ [What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) (AWS documentation)
+ [Viewing EC2 instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html) (AWS documentation)
