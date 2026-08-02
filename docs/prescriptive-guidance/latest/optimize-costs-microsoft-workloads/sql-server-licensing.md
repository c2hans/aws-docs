---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-licensing.html
---

# Understand SQL Server licensing
<a name="sql-server-licensing"></a>

## Overview
<a name="sql-server-licensing-overview"></a>

As more and more businesses move their workloads to the cloud, optimizing costs on cloud platforms has become a top priority. Licensing is one of the most significant costs associated with running Microsoft workloads on AWS. This section explains how to optimize costs on AWS by optimizing Microsoft licensing for SQL Server.

## AWS licensing options
<a name="sql-server-aws-licensing-options"></a>

AWS offers a range of flexible cost optimization choices for licensing. These licensing options are designed to help you reduce costs, maintain compliance, and meet your business needs.

![Review licensing options, such as purchasing or bringing licenses.](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/d4e0e89d-6a10-49c8-890e-8aec5b49de98.png)

AWS categorizes licenses into three main types:

1. **License included** – This licensing option enables you to purchase and use licenses on demand, paying only for what you use. The license-included option is ideal for scenarios where you require flexibility in your licensing usage and want to avoid upfront costs. You can choose from a range of Windows Server, SQL Server, and other Microsoft products.

1. **Bring Your Own License (BYOL) products with license mobility** – This licensing option is designed for scenarios where you already have existing licenses and want to use them in the cloud. AWS allows customers to bring their own licenses to the cloud through Microsoft's [License Mobility](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility) program. You can bring products that have License Mobility, such as SQL Server with Software Assurance (SA), to either shared or dedicated tenancy to reduce your AWS instance costs.

1. **BYOL products without license mobility** – For Microsoft products that don't have License Mobility, such as Windows Server, AWS offers dedicated options to use these products in the cloud. Additionally, dedicated hosts offer an opportunity to license at the physical core level. This can save you 50 percent or more on the licenses required to run your workloads. Dedicated hosts are a great option for stable and predictable workloads running most of the time.

## Cost impact of bringing licenses
<a name="sql-server-cost-bringing-licenses"></a>

Bringing licenses can have a significant impact on the cost of running Microsoft workloads on AWS. If you bring your own licenses, you aren't required to pay additional licensing costs for the instances running in the cloud. This can lead to significant cost savings.

The following comparison shows the on-demand monthly cost of running a single c5.xlarge instance 24/7:
+ Windows Server \+ SQL Server Enterprise edition: $1353/month (License included)
+ Windows Server \+ SQL Server Standard edition: $609/month (License included)
+ Windows Server only: $259/month (License included)
+ Compute only (Linux): $127/month

Ultimately, bringing your own licenses can have a significant impact on the cost of running Microsoft workloads on AWS. If you use your existing licenses, you can reduce licensing costs and save money on your overall AWS bill.

## License optimization
<a name="sql-server-license-optimization"></a>

An AWS Optimization and Licensing Assessment (AWS OLA) can help you optimize your licensing by reducing compute and licensing costs. AWS OLA is designed to evaluate your licensing requirements for workloads running on AWS or for workloads that are planned for migration. AWS OLA provides recommendations on optimizing license usage.

One of the key strategies for optimizing licensing usage is [right sizing instances](rightsize.md). Right sizing involves selecting the right instance type for your workload based on its CPU, memory, and storage requirements. By choosing the appropriate instance size, you can ensure that you're using resources in a cost-efficient manner. This can lead to significant cost savings.

With Microsoft software licensing, the number of cores that the software runs on is a critical factor in determining licensing costs. For example, Windows Server and SQL Server licenses are typically licensed on the number of cores. By right sizing instances, you can lower the number of cores that the Microsoft software runs on and, in turn, reduce both the cost of the instance and the number of licenses required.

## Cost optimization recommendations
<a name="sql-server-lic-opt-rec"></a>

Optimizing licenses is a key component of cost optimization on AWS. By implementing the right strategies, you can reduce licensing costs, maintain compliance, and achieve the best possible value from your licensing investment. This section outlines several strategies for license optimization.

### Bring your eligible Windows Server licenses
<a name="bring-your-eligible-windows-server-licenses.6e668423-cdd3-55db-b120-e585d182eb93"></a>

Bringing your own Windows Server licenses is one of the most effective strategies for license optimization. This strategy enables you to take advantage of your existing investments to reduce your AWS spending.

For example, you can deploy Windows Server 2019 and earlier versions on [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) if you purchased the licenses before 1/10/2019 or purchased the licenses as true-ups under active Enterprise Agreements signed before that date. This rule is based on a change that Microsoft made in 2019 to its licensing terms and conditions for products without License Mobility, such as Windows Server, when deployed on [Listed Providers](https://www.microsoft.com/licensing/docs/view/Listed-Providers) (for example, Alibaba, AWS, or Google Cloud). Under the new terms, you can't bring your own Windows Server licenses to AWS but must instead use license-included instances. However, if you purchased perpetual licenses prior to that date, then you can still deploy those Windows Server licenses on Amazon EC2 Dedicated Hosts.

### Physical-level licenses
<a name="physical-level-licenses.754886a5-15f1-54e5-8ebb-c0c9c14aee5d"></a>

Licensing at the physical core level enables you to license just the physical cores of a host, so that you can then deploy a maximum number of instances without impacting the number of licenses required. This is typically done by using Windows Server Datacenter and SQL Server Enterprise edition.

As an example, consider an R5 dedicated host with 48 cores, which translates to 96 vCPUs. If you use Windows Server Datacenter edition, you only need 48 licenses. This enables you to deploy a combination of instances with up to 96 vCPUs, as the following diagram shows.

![Physical-level licenses](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/e6a6f8fe-522f-4558-8a66-00d2ac4a0f09.png)

This approach can be especially cost-effective if you have enough workloads to maximize the number of instances that you can run on a host. By licensing at the physical core level, you can avoid additional licensing costs for each instance and achieve the best possible value for your licensing investment.

### License at the physical core level of SQL Server
<a name="license-at-the-physical-core-level-of-sql-server.e7540bf3-6818-5f66-a575-21421d293b89"></a>

In shared tenancy, SQL Server licensing is based on the number of vCPUs allocated to the instance. In contrast, with dedicated hosts, you can license SQL Server Enterprise edition at the physical core level or at the vCPU level.

As with the previous example of the R5 dedicated host, if you license SQL Server Enterprise edition at the physical core level, then you only need 48 SQL Server Enterprise edition licenses to license the hosts. In contrast, in shared tenancy, where the only option is to license by vCPU, you must have 96 SQL Server Enterprise edition licenses for the same workload. Therefore, dedicated hosts can save you up to 50 percent on SQL Server licensing costs compared to shared tenancy. This is in addition to saving on instance costs by bringing eligible Windows licenses.

### Consolidate SQL Server instances
<a name="consolidate-sql-server-instances.d02602da-5d0a-53ff-a85a-f5aa1bfc00ab"></a>

[SQL Server consolidation](consolidate-instances.md) is the process of combining multiple SQL Server instances onto one server. SQL Server requires a minimum of four core licenses per instance, even if the instance only has two vCPUs. This means that running SQL Server on servers with less than four cores can cause you to over-license these instances and use more licenses than necessary.

![SQL Server consolidation](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/8869e137-c586-4733-a781-b73865658e34.png)

For example, consolidating two instances with two vCPUs each into a single instance with four vCPUs can reduce the licensing requirement by 50 percent. This is because only four core licenses are required instead of eight.

For more information about consolidation, see the [SQL Server consolidation](consolidate-instances.md) section of this guide.

### Downgrade SQL Server editions
<a name="downgrade-sql-server-editions.83c4eb15-ff27-56c6-bdaa-d28f5c0d2feb"></a>

[Changing SQL Server editions](sql-server-editions.md) can be a key strategy for optimizing licensing usage and reducing costs. The Enterprise edition of SQL Server is considerably more expensive than the Standard edition, so the downgrading can result in significant cost savings.

Transparent Data Encryption (TDE) and Always On availability groups are two popular features in SQL Server Enterprise edition. There are, however, cost-effective alternatives to these features that you can consider if you don't require the full feature set of SQL Server Enterprise edition. For example, you could get TDE in SQL Server Standard edition starting with SQL Server 2019. In place of Always On availability groups, you could use failover clustering with shared storage on FSx for Windows File Server for high availability with SQL Server Standard edition.

By downgrading from SQL Server Enterprise edition to SQL Server Standard edition, you can significantly reduce your licensing costs. For more information, see the [Optimizing cost for your high availability SQL Server deployments on AWS](https://aws.amazon.com/blogs/storage/optimizing-cost-for-your-high-availability-sql-server-deployments-on-aws/) post on the AWS Storage Blog.

In addition to reducing licensing costs, downgrading SQL Server editions can help reduce your Software Assurance spending and help you avoid future true-ups. If you return unused licenses to the shelf, you can avoid additional licensing costs and achieve the best possible value from your licensing investment.

It's important to evaluate your SQL Server workloads carefully and determine which features are critical for your business needs. For more information, see [Assessing your environment](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/assess-environment.html) in AWS Prescriptive Guidance, and determine whether your Microsoft SQL Server database uses SQL Server Enterprise edition-specific features.

If you choose the right edition of SQL Server and use alternatives to SQL Server Enterprise edition features, you can achieve significant cost savings while maintaining compliance and meeting your business needs. For more information about downgrading options, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide.

### Use SQL Server Developer edition in non-production environments
<a name="use-sql-server-developer-edition-in-non-production-environments.12b42a38-9fcf-5a57-9110-9168dab525b4"></a>

In non-production environments, you can deploy licensable editions of SQL Server, such as Enterprise or Standard edition, by using MSDN subscriptions in on-premises environments. However, the MSDN subscription doesn't have License Mobility. So, if you migrate to AWS, you can't bring those licenses over. You must use SQL Server Developer edition instead.

SQL Server Developer edition is a fully-featured edition of SQL Server that's available for free. This edition is available for SQL Server versions 2016 and later. You can download it from the Microsoft website. SQL Server Developer edition is intended to be used in all non-production environments, such as development, testing, and staging, as long as it's not connecting to live production data.

If you use SQL Server Developer edition in non-production environments, you can avoid additional licensing costs. For more information, see the [Evaluate SQL Server Developer edition](sql-server-dev.md) section of this guide.

### Optimize CPU for SQL Server workloads
<a name="sql-server-rec-cpu-sql"></a>

In some cases, you could be required to choose an instance type with more CPUs than are required for your workload due to other factors such as RAM or networking limits. However, AWS provides a solution to help you optimize your licensing costs in these situations.

You can, like most customers who bring SQL Server core licenses, disable hyperthreading or turn off CPUs on the EC2 instance to limit the number of available CPUs to the host. This option enables you to take advantage of other instance capabilities, such as RAM, while still saving on the cost of purchasing extra licenses.

For example, if you deploy an r5.4xlarge instance because your workload requires 128 GB of memory but you only need eight cores of SQL Server, then you can disable hyperthreading of an instance with just eight active CPUs. By doing this, you can save 50 percent on required SQL Server licenses, as you only need to license the eight cores that are actively being used.

|
|
| Instance type | Total vCPUs | Active vCPU with Optimize CPUs feature | SQL Server license savings |
| --- |--- |--- |--- |
| r5.4xlarge | 16 | 8 | 50% |
| r5.12xlarge | 48 | 8 | 83% |

The Optimize CPU feature can be configured during the Amazon EC2 launch configuration or by modifying an existing instance. It can also be applied to both BYOL and license-included Amazon EC2 instances. This flexibility helps you to rightsize your CPU to your workload's needs, while also reducing Windows Server and SQL Server licenses. For license-included Amazon EC2 instances, reducing CPUs provides an instant savings on licensing costs.

If you rightsize your instances, you can ensure that you're using the most cost-effective instance types for your workloads. As AWS introduces new instance types, it's important to evaluate whether these new instances can satisfy workload requirements with fewer cores.

## Additional resources
<a name="additional-resources"></a>
+ [Amazon Web Services and Microsoft: Frequently Asked Questions](https://aws.amazon.com/windows/faq/) (AWS documentation)
