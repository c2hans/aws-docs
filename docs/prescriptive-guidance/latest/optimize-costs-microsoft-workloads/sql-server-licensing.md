---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-licensing.html
---

# Understand SQL Server licensing
<a name="sql-server-licensing"></a>

## Overview
<a name="sql-server-licensing-overview"></a>

As businesses move more workloads to the cloud, optimizing cloud costs has become a top priority. Licensing is one of the most significant costs of running Microsoft workloads on AWS. This section explains how to reduce costs on AWS by optimizing Microsoft licensing for SQL Server.

## AWS licensing options
<a name="sql-server-aws-licensing-options"></a>

AWS offers a range of flexible cost optimization choices for licensing. These licensing options are designed to help you reduce costs, maintain compliance, and meet your business needs.

![Review licensing options, such as purchasing or bringing licenses.](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/d4e0e89d-6a10-49c8-890e-8aec5b49de98.png)

AWS categorizes licenses into three main types:

1. **License included** – This licensing option enables you to purchase and use licenses on demand, paying only for what you use. The license-included option is designed for scenarios where you require flexibility in your licensing usage and want to avoid upfront costs. You can choose from a range of Windows Server, SQL Server, and other Microsoft products.

1. **Bring Your Own License (BYOL) products with license mobility** – This licensing option is designed for scenarios where you already have existing licenses and want to use them in the cloud. You can bring your own licenses to the cloud through Microsoft's [License Mobility](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility) program. You can bring products that have License Mobility, such as SQL Server with Software Assurance (SA), to either shared or dedicated tenancy to help reduce your Amazon EC2 instance costs.

1. **BYOL products without license mobility** – For Microsoft products that don't have License Mobility, such as Windows Server, AWS offers dedicated options to use these products in the cloud. Additionally, Amazon EC2 Dedicated Hosts let you license at the physical core level, which can help reduce the number of licenses required to run your workloads. Dedicated Hosts are well suited for stable, predictable workloads that run most of the time.

## Cost impact of bringing licenses
<a name="sql-server-cost-bringing-licenses"></a>

Bringing your own licenses can help reduce the cost of running Microsoft workloads on AWS. If you bring your own licenses, you don't pay additional licensing costs for the instances that run in the cloud.

The following comparison shows example on-demand monthly costs of running a single c5.xlarge instance 24/7. Prices vary by AWS Region and change over time, so check current pricing before you plan your costs:
+ Windows Server and SQL Server Enterprise edition: $1,353/month (license included)
+ Windows Server and SQL Server Standard edition: $609/month (license included)
+ Windows Server only: $259/month (license included)
+ Compute only (Linux): $127/month

By using your existing licenses, you can reduce licensing costs and lower your overall AWS bill.

## License optimization
<a name="sql-server-license-optimization"></a>

An AWS Optimization and Licensing Assessment (AWS OLA) can help you optimize your licensing by reducing compute and licensing costs. AWS OLA is designed to evaluate your licensing requirements for workloads running on AWS or for workloads that are planned for migration. AWS OLA provides recommendations on optimizing license usage.

One of the key strategies for optimizing licensing usage is [rightsizing instances](rightsize.md). Rightsizing involves selecting the instance type that matches your workload's CPU, memory, and storage requirements. By choosing an instance size that fits your workload, you can use resources in a cost-efficient manner. This can help reduce costs.

With Microsoft software licensing, the number of cores that the software runs on is a critical factor in determining licensing costs. For example, Windows Server and SQL Server are typically licensed based on the number of cores. By rightsizing instances, you can lower the number of cores that the Microsoft software runs on and, in turn, reduce both the cost of the instance and the number of licenses required.

## Cost optimization recommendations
<a name="sql-server-lic-opt-rec"></a>

Optimizing licenses is a key component of cost optimization on AWS. By implementing the right strategies, you can reduce licensing costs, maintain compliance, and increase the value of your licensing investment. This section outlines several strategies for license optimization.

### Bring your eligible Windows Server licenses
<a name="bring-your-eligible-windows-server-licenses.1d31f0eb-0177-5bed-b3ae-376d9997662b"></a>

Bringing your own Windows Server licenses is an effective strategy for license optimization. This strategy enables you to use your existing investments to reduce your AWS spending.

For example, you can deploy Windows Server 2019 and earlier versions on [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) if you purchased the licenses before October 1, 2019, or purchased the licenses as true-ups under active Enterprise Agreements signed before that date. This rule is based on a change that Microsoft made in 2019 to its licensing terms and conditions for products without License Mobility, such as Windows Server, when deployed on [Listed Providers](https://www.microsoft.com/licensing/docs/view/Listed-Providers) (for example, Alibaba, AWS, or Google Cloud). Under the new terms, you can't bring your own Windows Server licenses to AWS but must instead use license-included instances. However, if you purchased perpetual licenses before that date, you can still deploy those Windows Server licenses on Amazon EC2 Dedicated Hosts.

### Physical-level licenses
<a name="physical-level-licenses.c10b8f97-41cc-5a43-8d81-a9d389536928"></a>

Licensing at the physical core level enables you to license just the physical cores of a host, so that you can then deploy a maximum number of instances without impacting the number of licenses required. This is typically done by using Windows Server Datacenter and SQL Server Enterprise edition.

As an example, consider an R5 dedicated host with 48 cores, which translates to 96 vCPUs. If you use Windows Server Datacenter edition, you only need 48 licenses. This enables you to deploy a combination of instances with up to 96 vCPUs, as the following diagram shows.

![Physical-level licenses](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/e6a6f8fe-522f-4558-8a66-00d2ac4a0f09.png)

This approach can be cost-effective if you have enough workloads to maximize the number of instances that you can run on a host. By licensing at the physical core level, you can avoid additional licensing costs for each instance and increase the value of your licensing investment.

### License at the physical core level of SQL Server
<a name="license-at-the-physical-core-level-of-sql-server.e7540bf3-6818-5f66-a575-21421d293b89"></a>

In shared tenancy, SQL Server licensing is based on the number of vCPUs allocated to the instance. In contrast, with dedicated hosts, you can license SQL Server Enterprise edition at the physical core level or at the vCPU level.

As with the previous example of the R5 dedicated host, if you license SQL Server Enterprise edition at the physical core level, then you only need 48 SQL Server Enterprise edition licenses to license the hosts. In contrast, in shared tenancy, where the only option is to license by vCPU, you must have 96 SQL Server Enterprise edition licenses for the same workload. Therefore, dedicated hosts can save you up to 50 percent on SQL Server licensing costs compared to shared tenancy. This is in addition to saving on instance costs by bringing eligible Windows licenses.

### Consolidate SQL Server instances
<a name="consolidate-sql-server-instances.d02602da-5d0a-53ff-a85a-f5aa1bfc00ab"></a>

[SQL Server consolidation](consolidate-instances.md) is the process of combining multiple SQL Server instances onto one server. SQL Server requires a minimum of four core licenses per instance, even if the instance only has two vCPUs. This means that running SQL Server on servers with less than four cores can cause you to over-license these instances and use more licenses than necessary.

![SQL Server consolidation](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/8869e137-c586-4733-a781-b73865658e34.png)

For example, consolidating two instances with two vCPUs each into a single instance with four vCPUs can reduce the licensing requirement by 50 percent. This is because only four core licenses are required instead of eight.

For more information about consolidation, see the [SQL Server consolidation](consolidate-instances.md) section of this guide.

### Downgrade SQL Server editions
<a name="downgrade-sql-server-editions.cd5a1411-f6a3-503d-a3c2-f5f7185cb3c9"></a>

[Changing SQL Server editions](sql-server-editions.md) can be a key strategy for optimizing licensing usage and reducing costs. The Enterprise edition of SQL Server is considerably more expensive than the Standard edition, so downgrading can result in significant cost savings.

Transparent Data Encryption (TDE) and Always On availability groups are two popular features in SQL Server Enterprise edition. There are, however, cost-effective alternatives to these features that you can consider if you don't require the full feature set of SQL Server Enterprise edition. For example, you could get TDE in SQL Server Standard edition starting with SQL Server 2019. In place of Always On availability groups, you could use failover clustering with shared storage on FSx for Windows File Server for high availability with SQL Server Standard edition.

By downgrading from SQL Server Enterprise edition to SQL Server Standard edition, you can significantly reduce your licensing costs. For more information, see the [Optimizing cost for your high availability SQL Server deployments on AWS](https://aws.amazon.com/blogs/storage/optimizing-cost-for-your-high-availability-sql-server-deployments-on-aws/) post on the AWS Storage Blog.

In addition to reducing licensing costs, downgrading SQL Server editions can help reduce your Software Assurance spending and help you avoid future true-ups. If you retire unused licenses, you can avoid additional licensing costs and increase the value of your licensing investment.

Evaluate your SQL Server workloads carefully and determine which features are critical for your business needs. To determine whether your Microsoft SQL Server database uses SQL Server Enterprise edition-specific features, see [Assessing your environment](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/assess-environment.html) in AWS Prescriptive Guidance.

If you choose the right edition of SQL Server and use alternatives to SQL Server Enterprise edition features, you can achieve significant cost savings while maintaining compliance and meeting your business needs. For more information about downgrading options, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide.

### Use SQL Server Developer edition in non-production environments
<a name="use-sql-server-developer-edition-in-non-production-environments.75ccbe1f-60f4-5010-8673-6f58dc76a580"></a>

In non-production environments, you can deploy licensable editions of SQL Server, such as Enterprise or Standard edition, by using MSDN subscriptions in on-premises environments. However, the MSDN subscription doesn't have License Mobility. So, if you migrate to AWS, you can't bring those licenses over. You must use SQL Server Developer edition instead.

SQL Server Developer edition is a fully featured edition of SQL Server that's available for free. This edition is available for SQL Server versions 2016 and later. You can download it from the Microsoft website. You can use SQL Server Developer edition in non-production environments, such as development, testing, and staging, as long as it doesn't connect to live production data.

If you use SQL Server Developer edition in non-production environments, you can avoid additional licensing costs. For more information, see the [Evaluate SQL Server Developer edition](sql-server-dev.md) section of this guide.

### Optimize CPU for SQL Server workloads
<a name="sql-server-rec-cpu-sql"></a>

In some cases, you might need to choose an instance type with more CPUs than your workload requires because of other factors, such as RAM or networking limits. In these situations, you can use the Optimize CPUs feature in AWS to help reduce your licensing costs.

If you bring SQL Server core licenses, you can turn off hyperthreading or CPUs on the EC2 instance to limit the number of available CPUs. This option enables you to use other instance capabilities, such as RAM, while still saving on the cost of purchasing extra licenses.

For example, if you deploy an r5.4xlarge instance because your workload requires 128 GB of memory but you need only eight cores of SQL Server, you can disable hyperthreading so that the instance has only eight active CPUs. This approach can save 50 percent on required SQL Server licenses, because you license only the eight cores that you actively use.

|
|
| Instance type | Total vCPUs | Active vCPU with Optimize CPUs feature | SQL Server license savings |
| --- |--- |--- |--- |
| r5.4xlarge | 16 | 8 | 50% |
| r5.12xlarge | 48 | 8 | 83% |

You can configure the Optimize CPUs feature during the Amazon EC2 launch configuration or by modifying an existing instance. You can apply it to both bring your own license (BYOL) and license-included Amazon EC2 instances. This flexibility helps you rightsize your CPUs to your workload's needs while also reducing Windows Server and SQL Server licenses. For license-included Amazon EC2 instances, reducing CPUs can immediately reduce licensing costs.

If you rightsize your instances, you can use more cost-effective instance types for your workloads. As AWS introduces new instance types, evaluate whether these new instances can meet workload requirements with fewer cores.

## Additional resources
<a name="additional-resources"></a>
+ [Amazon Web Services and Microsoft: Frequently Asked Questions](https://aws.amazon.com/windows/faq/) (AWS documentation)
