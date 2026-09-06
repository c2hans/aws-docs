---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/byol-ded-hosts.html
---

# Bring licenses for Windows and SQL Server workloads
<a name="byol-ded-hosts"></a>

## Overview
<a name="byol-ded-hosts-overview"></a>

If you have significant investments in Microsoft workloads and existing enterprise licensing agreements, you can choose from several AWS options to support these workloads, including [license included (provided by AWS)](https://aws.amazon.com/windows/faq/#buy-win-serv-inc) and [Bring Your Own License (BYOL)](https://aws.amazon.com/windows/faq/#byol) options. You can use [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) to fully take advantage of existing Microsoft licensing agreements and bring Windows Server to AWS. This can save you up to 50 percent on Amazon EC2 instance costs. Since Windows licenses account for approximately half of the instance costs, bringing Windows Server to AWS on Dedicated Hosts can result in substantial cost savings. Because Windows Server can't be brought to [default (shared) tenancy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html), Dedicated Hosts is the ideal choice if you want to use your existing licenses for Windows Server on AWS.

Dedicated Hosts are not just for Windows Server BYOL instances. They also offer you the flexibility to match your on-premises licensing for existing SQL Server workloads. Dedicated Hosts expose the physical cores of the underlying server, and enable you to license SQL Server at the physical core level. This isn't possible in default (shared) tenancy where SQL Server licensing is based on the number of virtual CPUs allocated to the instance. This feature enables you to license SQL Server workloads on AWS in a way that's consistent with your on-premises licensing strategy. Consequently, you can save up to 50 percent on SQL Server licensing costs compared to default (shared) tenancy, in addition to cost savings on instance costs, by using eligible Windows licenses. For more information about this scenario, see the [Understand SQL Server licensing](sql-server-licensing.md) section of this guide.

## Amazon EC2 Dedicated Hosts
<a name="byol-ded-hosts-ec2"></a>

An Amazon EC2 Dedicated Host is essentially the same EC2 host that AWS uses to run its EC2 compute offerings. The difference is that these hosts are fully dedicated to a single customer and provide exclusive access to the underlying physical infrastructure. You can use Dedicated Hosts to run your instances on hardware that's entirely dedicated to your use, instead of sharing resources with other AWS customers. This gives you greater control over cloud resources and enables you to reduce costs by bringing your own software licenses, such as Windows Server and SQL Server, to AWS.

Keep in mind the following:
+ A Dedicated Host is a physical server fully dedicated to a single customer. You get visibility into the sockets and physical cores of the Dedicated Host so that you can address licensing compliance requirements, such as per-socket, per-core, or per-VM software licensing agreements.
+ Dedicated Hosts that can support multiple instance sizes of the same instance family are known as heterogeneous Dedicated Hosts. These [instance families](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html?icmpid=docs_ec2_console#dedicated-hosts-allocating) include T3, A1, C5, M5, R5, C5n, R5n, and M5n. In contrast, other instance families support only one instance size on the same Dedicated Host. These are called homogeneous Dedicated Hosts.
+ Dedicated Hosts are billed on a per-host basis. This means that you are charged per Dedicated Host regardless of how many instances are running on it. Dedicated Host pricing varies based on the instance family, Region, and payment option selected. You can choose the optimal configuration for your workload to achieve your desired performance and cost outcomes.

This diagram illustrates the differences between shared tenancy instances and Dedicated Hosts.

![Comparison of shared tenancy and Dedicated Hosts](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/48a38dd7-be5d-479a-89ae-550423687e68.png)

### Homogenous Dedicated Hosts
<a name="homogenous-dedicated-hosts.4b602fa9-043f-508b-a408-19fe80a38e40"></a>

Consider a scenario where an M6i Dedicated Host is used. M6i and R6i Dedicated Hosts have two sockets, 64 physical cores, and support instance types of the same size. These are called homogenous Dedicated Hosts. This means that the number of instances that you can launch on a single M6i Dedicated Host depends on the instance size.

For example:
+ In the case of xlarge (4 vCPUs), you can launch a maximum of 32 m6i.xlarge instances on this Dedicated Host.
+ In the case of 8xlarge (32 vCPUs), you can launch a maximum of 4 m6i.8xlarge instances on this Dedicated Host.
+ In the case of metal (128 vCPUs), you can launch a maximum of 1 m6i.metal instance on this Dedicated Host.

The following diagram shows the Dedicated Host options for M6 instances.

![Dedicated Host options for M6 instances](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/4ac40d2c-9bdf-4185-8a63-9c7f0f29ad66.png)

### Heterogenous Dedicated Hosts
<a name="heterogenous-dedicated-hosts.fc7e13b9-bdfe-51da-b24e-3d7baeaf7aca"></a>

Dedicated Hosts that support multiple instance sizes on the same host are referred to as a heterogenous Amazon EC2 Dedicated Hosts. The following diagram shows an example of C5, M5, and R5 Dedicated Hosts with various instance sizes, such as 2xlarge, xlarge, and 4xlarge.

![C5, M5, and R5 Dedicated Host examples](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/1ee795af-7f97-4f49-a060-b5aefda7ad7e.png)

### Dedicated Host management
<a name="dedicated-host-management.1d7e60d0-1403-5da0-8791-ec6628d60a68"></a>

We recommend that you consider the following in regard to managing Amazon EC2 Dedicated Hosts:
+ To take full advantage of Dedicated Hosts, you can [share a single host between multiple accounts within your organization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dh-sharing.html). Host sharing enables resource optimization and can result in cost savings by using every available slot on the host. By sharing a Dedicated Host between business units, you can centralize your IT infrastructure and improve resource utilization, while still maintaining separation between workloads. If you're part of an organization in AWS Organizations and sharing is enabled within your organization, then consumers in your organization are automatically granted access to the shared Dedicated Host. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared Dedicated Host after accepting the invitation.
+ You can run Windows Server 2022 on Dedicated Hosts under the license-included model, as Windows Server 2019 is the latest version where you can BYOL. If you want to use Windows Server 2022 on Dedicated Hosts, you must use Windows Server 2022 license-included instances.
+ [AWS License Manager](https://aws.amazon.com/license-manager/) is a comprehensive solution for managing software licenses from various vendors across AWS and on-premises environments. If you [use License Manager](https://catalog.us-east-1.prod.workshops.aws/workshops/c7d505a0-b48b-4178-922a-9ee675dfb81c/en-US/license-manager), you can gain greater visibility and control over how software licenses are used, leading to cost savings and improved compliance. You can use License Manager to set rules to emulate your unique licensing terms. This enables you to enforce those rules and prevent license misuse. This can reduce the risk of noncompliance and improve license management processes.
+ You can use License Manager to automate the placement, release, and recovery of hosts by using [host resource groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html). This can increase productivity and reduce management overhead. License Manager also provides a centralized view of license usage across AWS and on-premises environments based on licensing rules, making it easy to manage incremental licensing purchases, compliance, and vendor audits across your organization. Furthermore, License Manager integrates with AWS Organizations and AWS Resource Access Manager (AWS RAM) to share license configurations across accounts and Regions. This enables you to create reports for your entire environment based on a schedule and manage licensing rules centrally in one AWS account. Ultimately, this can improve governance and reduce complexity.
+ When designing high availability for Dedicated Hosts within a single Region, make sure that you've allocated a minimum of two Dedicated Hosts in a minimum of two Availability Zones for production-critical workloads. For more information, see the [Amazon EC2 Dedicated Hosts for Microsoft Windows on AWS](https://aws.amazon.com/quickstart/architecture/microsoft-dedicated-host/) reference deployment.
+ For each Dedicated Host instance family, there is a limit on the number of instances that you can run for each instance size. For more information, see [Dedicated Hosts Configuration Table](https://aws.amazon.com/ec2/dedicated-hosts/pricing/?nc1=h_ls#Dedicated_Hosts_Configuration_Table) in the Amazon EC2 documentation.

## AWS licensing options
<a name="byol-licensing-options"></a>

Licenses are classified into the following primary categories:
+ **License included **– This licensing option enables you to purchase and use licenses on demand, paying solely for what you use. It's ideal for use cases where you're seeking flexibility in your licensing usage and wish to avoid upfront costs. You can choose from a variety of Windows Server, SQL Server, and other Microsoft products.
+ **BYOL products with License Mobility **– If you already have existing licenses and want to use them in the cloud, this licensing option allows you to bring your own licenses to the cloud through the [Microsoft License Mobility program](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility). Products with license mobility, such as SQL Server with Software Assurance (SA), can be brought to either shared or dedicated tenancy. This reduces AWS instance costs.
+ **BYOL products without License Mobility **– For Microsoft products like Windows Server that lack License Mobility, AWS provides dedicated options for using these products in the cloud. Additionally, Dedicated Hosts enable licensing at the physical core level, making it possible to save 50 percent or more on the licenses needed to run your workloads. Dedicated Hosts are an excellent choice for stable and predictable workloads that run most of the time.

## Bringing Windows Server licenses
<a name="byol-licensing-windows"></a>

Bringing your own Windows licenses is one of the most effective strategies for license optimization because it enables you to take advantage of existing investments and reduce your AWS expenses. Specific BYOL scenarios don't require SA or License Mobility benefits, but Amazon EC2 dedicated infrastructure is always necessary. To be eligible, you must have purchased perpetual licenses before October 1, 2019 or added them as a true-up under an active Enterprise Enrollment effective before October 1, 2019. In these specific BYOL scenarios, you can upgrade only licenses to versions available prior to October 1, 2019. For example, if you dropped SA in 2017, you have the rights to deploy only up to Windows Server 2016, not 2019. However, 2019 is the last version eligible for BYOL to AWS. For more information, see [Licensing – Windows Server](https://aws.amazon.com/windows/faq/#licensing-winserv) in the AWS documentation.

Bringing licenses can significantly impact the cost of running Microsoft workloads on AWS. When you bring your own licenses, you're not required to pay additional licensing costs for the instances running in the cloud, which can lead to considerable cost savings.

The following table show the on-demand monthly cost of running a single c5.xlarge instance 24/7 on various configurations.

|
|
| Configuration | Monthly cost (USD) |
| --- |--- |
| Windows Server \+ SQL Server Enterprise edition | $1,353.00 (LI) |
| Windows Server \+ SQL Server Standard edition | $609.00 (LI) |
| Windows Server only | $259.00 (LI) |
| Compute only (Linux) | $127.00 |

You  can use your existing licenses to reduce licensing costs and save money on your overall AWS bill.

To be eligible for BYOL on Amazon EC2 Dedicated Hosts, you must bring your own software licenses, such as for Windows Server and SQL Server. BYOL allows you to use your existing licenses on AWS and can result in cost savings. To bring your own licenses, you must have the license entitlements from the software vendor and must also provide the installation media or image for the software. The installation media or image can be used to launch instances on Dedicated Hosts. To learn more about creating a BYOL AMI, see [How to create Windows Server Bring-Your-Own-License AMIs from on-premises with VM Import/Export](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-create-windows-server-bring-your-own-license-amis-from-on-premises-with-vm-import-export/) in the Microsoft Workloads on AWS blog.

**Note**
A license type set to **Auto** is the equivalent of an [AWS license-included option](https://docs.aws.amazon.com/vm-import/latest/userguide/licensing.html). This option can result in unwanted on-demand spending. You will need to switch [licensing types](https://aws.amazon.com/blogs/mt/use-aws-flexible-licensing-options-to-optimize-cost/).

## Cost optimization scenarios
<a name="byol-licensing-opt-scenarios"></a>

Right sizing and optimizing licenses is a key component of cost optimization on AWS. If you implement the right strategies, you can reduce licensing costs, maintain compliance, and achieve the best possible value from your licensing investment by using Amazon EC2 Dedicated Hosts and the BYOL option.

This section covers the following example scenarios:
+ Cost savings with T3 Dedicated Hosts
+ Comparing shared tenancy to Dedicated Hosts with SQL Server BYOL
+ Highly available SQL Server deployments

### Cost savings with T3 Dedicated Hosts
<a name="cost-savings-with-t3-dedicated-hosts.a0f97dea-da6f-5370-b7b2-afb9c2045c2a"></a>

T3 Dedicated Hosts differ from other Amazon EC2 Dedicated Hosts that traditionally provide fixed CPU resources. T3 Dedicated Hosts, in contrast, support burstable instances that are capable of sharing CPU resources, providing baseline CPU performance, and bursting when needed. Sharing CPU resources, also known as oversubscription, is what enables a single T3 Dedicated Host to support up to four times more instances than comparable general-purpose Dedicated Hosts.

T3 Dedicated Hosts drive a lower TCO by delivering higher instance density than any other Amazon EC2 Dedicated Host. Burstable T3 instances enable you to consolidate a higher number of instances with low-to-moderate average CPU utilization on fewer hosts than ever before. T3 Dedicated Hosts also offer smaller instance sizes in a greater number of vCPU and memory combinations than other Amazon EC2 Dedicated Hosts. Smaller instance sizes can contribute to lower TCO and help deliver consolidation ratios equivalent to or greater than on-premises hosts.

T3 Dedicated Hosts are best suited for running BYOL software with low-to-moderate CPU utilization and eligible per-socket, per-core, or per-VM software licenses, including Microsoft Windows desktop, Windows Server, SQL Server, and Oracle Databases.

#### Use T3 Dedicated Hosts to reduce Windows Server Datacenter licenses (per core)
<a name="use-t3-dedicated-hosts-to-reduce-windows-server-datacenter-licenses--per-core-.17f7bd9c-8ea9-5e2f-b1fb-0901d62afdda"></a>

In on-premises environments, you're taking advantage of the fact that you can easily oversubscribe your physical CPUs on VMware hosts and achieve high levels of consolidation.

Consider the following example. You're currently using 10x36 core, 384 GB RAM VMware hosts in an on-premises environment. Additionally, each host is running 96x2 vCPU, 4 GB RAM Windows Server virtual machines with low average CPU utilization.

You can now achieve much higher levels of consolidation by moving your virtual machines to T3 Dedicated Hosts, which have twice the amount of RAM compared to your current on-premises VMware hosts. You can run the same number of servers on T3 Dedicated Hosts with 50 percent less host cost. This can help you reduce Windows Server licensing costs by 33 percent. The following table highlights the savings of using T3 Dedicated Hosts.

|  |
| --- |
|  | On-premises VMware hosts | T3 Dedicated Hosts | Savings |
| --- |--- |--- |--- |
| Physical servers | 10 | 5 |  |
| Physical cores per host | 36 | 48 |  |
| RAM per host (GB) | 384 | 768 |  |
| 2 vCPU, 4 GB RAM VMs per host | 96 | 192 |  |
| Total number of VMs | 960 | 960 |  |
| Total Windows Server Datacenter licenses (per core) = (Number of servers \* Physical core count) | 10 \* 36 = 360 | 5 \* 48 = 240 | 33% |

### Comparing shared tenancy to Dedicated Hosts with SQL Server BYOL
<a name="comparing-shared-tenancy-to-dedicated-hosts-with-sql-server-byol.ff17b4ce-a045-5a8e-a2fa-bb1a1ebecf80"></a>

Consider a practical example to demonstrate the value of Amazon EC2 Dedicated Hosts. In this scenario, an organization runs a SQL Server workload in on-premises environment with 240 cores and wants to deploy the same workload cost-effectively on AWS. If this organization brings their own licenses (BYOL), they continue to pay for SA and reducing the number of cores directly affects their costs.

The following diagram compares AWS savings between Microsoft entitlements and SQL Server.

![Comparison of Microsoft entitlement to SQL Server savings](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/b1406ad9-a8cc-4d18-8ad2-43554d5adb1b.png)

By right sizing the instances on AWS shared tenancy, you can reduce SQL Server licenses down to 140 cores. This results in SA costs of $197,000.

Amazon EC2 Dedicated Hosts enable you to license SQL Server at the physical core level. This isn't possible in shared tenancy where SQL Server licensing is based on the number of vCPUs allocated to the instance. Consequently, by using two R5 Dedicated Hosts with 48 cores each, you only need to cover 96 cores instead of the 140 vCPUs required on shared tenancy. By deploying R5 Dedicated Hosts and licensing the workloads at the physical level, you can bring the required number of SQL Server Enterprise edition licenses down to 96 cores. This means that you can deploy as many as 192 cores (accounting for hyper-threading) of SQL Server workloads, while still meeting licensing requirements and achieving significant cost savings.

In this case, the organization pays approximately $341,000 annually in SA costs. After right sizing on shared tenancy, they reduce costs to $197,000 with 140 vCPUs. Amazon EC2 Dedicated Hosts further reduces costs to $151,000 (an approximately 56 percent decrease).

### Highly available SQL Server deployments
<a name="highly-available-sql-server-deployments.8f8aa58e-d75a-5a41-a4d7-23b01abf53ef"></a>

This example analyzes how cost can influence a SQL Server deployment on AWS with various licensing considerations. Suppose an organization needs to deploy six SQL Server Enterprise servers on AWS to support three applications. These servers require high availability and have 16 vCPUs and 256 GB of RAM each. See the following scenario details:
+ **Server** – SQL Server
+ **Operating system edition** – Windows Server Datacenter 2019
+ **SQL Server edition** – SQL Server Enterprise 2019
+ **vCPU** – 16
+ **Memory (GB)** – 256
+ **Quantity **– 6

To optimize costs on AWS without sacrificing performance, we recommend that you right size instances based on CPU, memory, network, and disk (IOPS/BW) utilization. After right sizing the workloads, place them on the x2iedn.4xlarge instance type, which offers 16 vCPUs. However, this instance type also includes twice the necessary memory for the workloads. Further optimization is still possible.

#### Scenario 1
<a name="scenario-1.a90df4b8-75be-5781-9352-bc7d394f3f1d"></a>

An organization deploys six SQL Server Enterprise servers on AWS shared tenancy by using the license-included option for both Windows and SQL Server. With this option, the cost of the Windows and SQL Server licenses is incorporated into the instance price. See the following scenario details:
+ **Shared tenancy (instance)** – x2iedn.4xlarge
+ **Hourly cost (USD)** – $10.0705
+ **Monthly cost per unit (USD)** – $7,351.47
+ **Number of servers** – 6
+ **CPU** – 16
+ **Memory** – 512
+ **Monthly cost for 6 servers **– $44,108

#### Scenario 2
<a name="scenario-2.51a54bec-3e54-5458-8140-4ddd0487009e"></a>

An organization has SA and BYOL for SQL Server on shared tenancy. This means that the organization uses the license-included option for Windows, but provides their own SQL Server licenses based on the number of vCPUs allocated to the instance. Since the organization has six SQL Server Enterprise servers with 16 vCPUs each, a total of 96 vCPUs is required. See the following scenario details:
+ **Shared tenancy (instance)** – x2iedn.4xlarge
+ **Hourly cost (USD)** – $4.0705
+ **Monthly cost per unit (USD)** – $2971.47
+ **Number of servers** – 6
+ **CPU** – 16
+ **Memory** – 512
+ **BYOL cores** – 96
+ **Monthly cost for 6 servers **– $17,828

By bringing their own SQL Server licenses with SA, the organization in this scenario can achieve cost savings compared to using the license-included option for SQL Server. The precise cost savings depend on the specific licensing agreement's pricing and terms. In this scenario, AWS costs decrease by $26,280 per month when bringing SQL Server Enterprise licenses to AWS.

#### Scenario 3
<a name="scenario-3.08dbc2a9-3c31-53b5-9cce-7f81745d501c"></a>

An organization has BYOL for both Windows and SQL Server on Amazon EC2 Dedicated Hosts. This means that the organization will assign licenses at the physical core level, enabling them to license only the host's physical cores. Licensing at the physical core level allows you to deploy the maximum number of instances without affecting the required licenses. This licensing model is commonly used with Windows Server Datacenter and SQL Server Enterprise edition.

This scenario uses two X2iezn Amazon EC2 Dedicated Hosts. Each host has 24 physical cores and 48 vCPUs. This provides adequate capacity for the six SQL Server Enterprise servers with 16 vCPUs and 256 GB of RAM each. See the following scenario details:
+ **Number of dedicated hosts** – 2
+ **Instance family** – x2iezn
+ **Hourly cost (USD)** – $11.009
+ **Monthly cost per unit (USD)**  – $8,036
+ **Physical core** – 48
+ **Available vCPU** – 96
+ **Windows Server core licenses required** – 24
+ **Licenses required for SQL Server Enterprise cores **– 24
+ **Monthly cost **– 16,073

The total cost for two X2iezn family Amazon EC2 Dedicated Hosts is $16,073 per month. For more information about pricing, see the AWS Pricing Calculator [estimate](https://calculator.aws/#/estimate) for this scenario. The organization in this scenario can save $1,755.65 per month by bringing their Windows licenses. If they use Amazon EC2 Dedicated Hosts, they can also reduce the number of required SQL Server licenses. In shared tenancy, they would need 96 SQL Server Enterprise licenses to cover the six SQL Server Enterprise servers with 16 vCPUs each. However, by using Amazon EC2 Dedicated Hosts and licensing at the physical core level, they can reduce the number of required licenses to 48 cores.

The following details compare the costs from example 3 and show how much you can save by deploying workloads on Amazon EC2 Dedicated Hosts with the BYOL option compared to other scenarios.
+ **On-premises server** – SQL Server
+ **vCPU** – 16
+ **Memory**  – 256
+ **Number of servers** – 6
+ **Monthly cost for scenario 1: Windows (LI) \+ SQL Server Enterprise (LI)** – $44,108
+ **Monthly cost for scenario 2: Windows (LI) \+ SQL Server Enterprise (BYOL)** – $17,828
+ **Monthly cost for scenario 3: Windows (LI) \+ SQL Server Enterprise (BYOL) on Amazon EC2 Dedicated Host** – $16,073

**Note**
Cost is based on on-demand pricing. You can further reduce costs by using Savings Plans or Dedicated Reserved Instances. These options offer a flexible pricing model with significant cost savings compared to on-demand pricing. With these plans, you can commit to a term of one or three years. For more information, see the [Optimize spending for Windows on Amazon EC2](savings-plans.md) section of this guide.

Consider the following payment options for Amazon EC2 Dedicated Hosts:
+ [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html#on-demand-dedicated-hosts) (Amazon EC2 documentation)
+ [Dedicated Host Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-billing.html#dedicated-host-reservations) (Amazon EC2 documentation)
+ [Savings Plans](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-billing.html#dedicated-hosts-savings-plans) (Amazon EC2 documentation)

The [AWS Pricing Calculator](https://aws.amazon.com/about-aws/whats-new/2023/01/aws-pricing-calculator-optimized-pricing-estimation-ec2-dedicated-hosts/) now supports Dedicated Host pricing. This can help you choose the appropriate underlying Dedicated Host.

## Cost optimization recommendations
<a name="byol-ded-hosts-next-steps"></a>

We recommend that you take the following next steps to optimize your costs by using the AWS Cost Explorer:

1. [Enable Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html).

1. Use Cost Explorer to [view and analyze the costs and usage](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) of your Amazon EC2 Dedicated Host deployments.

1. Validate that you're running BYOL. You can display the following platform details and usage operation values on the instances or AMI pages in the Amazon EC2 console, or in the response that's returned by the `describe-images` or `describe-instances` command.
   + **Platform details: **Windows , **Usage operation:** RunInstances:0002  (License included)
   + **Platform details**: Windows BYOL, **Usage operation:** RunInstances:0800

## Additional resources
<a name="byol-ded-hosts-resources"></a>
+ [Eligible license types for license type conversion](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-types.html) (AWS License Manager documentation)
+ [AWS License Manager & Dedicated Host workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c7d505a0-b48b-4178-922a-9ee675dfb81c/en-US/license-manager) (AWS License Manager Workshop)
+ [Amazon EC2 Dedicated Hosts FAQs](https://www.amazonaws.cn/en/ec2/dedicated-hosts/faqs/) (AWS documentation)
+ [How to create Windows Server Bring-Your-Own-License AMIs from on-premises with VM Import/Export](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-create-windows-server-bring-your-own-license-amis-from-on-premises-with-vm-import-export/) (Microsoft Workloads on AWS blog)
+ [VM Import/Export](https://aws.amazon.com/ec2/vm-import/) (AWS documentation)
+ [Amazon Web Services and Microsoft: Frequently Asked Questions](https://aws.amazon.com/windows/faq/) (AWS documentation)
+ [License type conversions in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-conversion.html) (AWS License Manager documentation)
+ [Deploying highly-available SQL Server on Amazon EC2 Dedicated Hosts](https://aws.amazon.com/blogs/mt/deploying-highly-available-sql-server-on-amazon-ec2-dedicated-hosts/) (AWS Cloud Operations & Migrations Blog)
