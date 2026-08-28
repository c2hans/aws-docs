---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/licensing-microsoft-workloads.html
---

# Microsoft licensing on AWS
<a name="licensing-microsoft-workloads"></a>

This section describes how Microsoft licensing works on AWS, provides licensing best practices and strategies for deployment of Microsoft workloads on AWS, and helps you remain compliant with Microsoft's licensing terms while optimizing costs. Due to the impact of licensing on the cost of a migration, Microsoft licensing and Bring Your Own License (BYOL) options often influence the deployment options available. That's why it's important to understand how licensing works before you start the migration process.

## Assess
<a name="licensing-assess"></a>

When assessing your Microsoft workloads for migration to AWS, it's important to consider licensing requirements. For Microsoft workloads, we recommend that you take advantage of an [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) to assess on-premises or cloud workloads and build a right-sized and optimized roadmap for running workloads in AWS. An AWS OLA will not only make optimized suggestions for the right Amazon Elastic Compute Cloud (Amazon EC2) instances for your workloads, but it will also look at your Microsoft licensing position. The result will be recommendations for the best path forward to save on compute and licensing costs. An AWS OLA is available for new and existing customers, and is fully funded and obligation-free. For more information, contact the [AWS OLA team](https://pages.awscloud.com/windows-ola-contact-us.html).

If an AWS OLA is not an option for you at this time, it's still important to understand how Microsoft licensing works in AWS. If you're looking to BYOL, we recommend that you request an updated copy of your Microsoft License Statement (MLS) from your Microsoft licensing purchasing contact. Use this to review what licensing you have and any purchase dates and SA quantities where applicable. For assistance with your MLS, reach out to your AWS representative. Your representative can connect you with a Microsoft specialist.

Different Microsoft products have different licensing requirements, so it's important to have a clear picture of what Microsoft products you have deployed. AWS has different options available to meet the needs of different Microsoft products, including shared/default tenancy for Amazon EC2 for products with License Mobility and dedicated options for products without License Mobility. AWS also has license included options, where the cost of the licensing is included in the Amazon EC2 compute costs. You could benefit from a mixed licensing model when migrating to AWS. A mixed licensing model is where shared-tenancy EC2 instances are used with all or some license included options. The mixed licensing model is best for variable workloads and when dedicated Amazon EC2 options are used for stable, predictable workloads—especially when Windows Server Datacenter or SQL Server Enterprise BYOL is an option.

For more information about current Microsoft licensing terms for products purchased through Microsoft's Volume Licensing programs, see the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage) site.

### License included options
<a name="license-included-options.0d8e89bf-d644-5ca5-a141-c68a2f3eb1df"></a>

*License included* refers to Amazon EC2 instances that include the cost of the license in the compute costs. For Microsoft server workloads, AWS currently offers Windows Server ([Amazon EC2](https://aws.amazon.com/ec2/instance-types/), [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/pricing/), [Amazon EC2 Dedicated Instances](https://aws.amazon.com/ec2/pricing/dedicated-instances/), [AWS Outposts](https://aws.amazon.com/outposts/)) and SQL Server Enterprise, Standard, and Web editions ([Amazon EC2](https://aws.amazon.com/ec2/instance-types/)). These server licenses are offered per vCPU per second with the pay-as-you-go model as a benefit of license included Amazon EC2 instances. If the Amazon EC2 instance is scheduled to stop, or if it scales up or down based on demand, you only pay for the licensing for the time the instance is running. With on-demand pricing there are no long-term commitments, which is ideal for future modernization plans.

License included is available for current and legacy versions with Amazon Machine Images (AMIs) available for all supported versions. End-of-support versions, such as Windows Server 2008 or SQL Server 2012, can still be licensed with license included, but you must bring your own media.

There are no software upgrade fees with the license included option. As soon as a new version of the product is released by Microsoft, the new version is made available in the Amazon EC2 console right away for no additional cost above the current license included costs. Most importantly, AWS is responsible for the licensing compliance for license included Amazon EC2 instances. This can save a lot of time and effort for you because licensing compliance can be complex and difficult.

The SQL Server license included options offer core-based licenses with no client access licenses (CALs) required. An unlimited number of users can access a license included Windows Server EC2 instance without counting or licensing CALs. Windows Server license included EC2 instances also include two Microsoft Remote Desktop connections for administrative purposes only. If you need additional Microsoft Remote Desktop connections, you can buy Remote Desktop Services User CALs with Software Assurance (SA) from Microsoft and bring them to AWS through License Mobility benefits.

AWS also offers some user-based license included options. Visual Studio 2022 Enterprise and Professional editions ([Amazon EC2](https://aws.amazon.com/ec2/instance-types/) and [AWS Lambda](https://aws.amazon.com/lambda/)) and Office LTSC Professional Plus 2021 ([Amazon EC2](https://aws.amazon.com/ec2/instance-types/)) are charged per user, per month. These include Microsoft Remote Desktop connections for each user. [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/) also offers Office Professional Plus 2016 or 2019 as an add-on, charged per user, per month.

AWS offers the following license included options for Microsoft workloads:

|
|
| **Product** | **Availability** | **Versions available** |
| --- |--- |--- |
| Windows Server | Amazon EC2, Amazon EC2 Dedicated Instances, Amazon EC2 Dedicated Hosts, AWS Outposts | All\* |
| SQL Server Enterprise | Amazon EC2, Amazon EC2 Dedicated Instances, AWS Outposts | All\* |
| SQL Server Standard | Amazon EC2, Amazon EC2 Dedicated Instances, AWS Outposts | All\* |
| SQL Server Web\*\* | Amazon EC2, Amazon EC2 Dedicated Instances, AWS Outposts | All\* |
| Visual Studio Enterprise | Amazon EC2, AWS Lambda, Amazon WorkSpaces | 2022 |
| Visual Studio Professional | Amazon EC2, AWS Lambda, Amazon WorkSpaces | 2022 |
| Office Professional Plus | Amazon WorkSpaces | 2019, 2016 |
| Office LTSC Professional Plus | Amazon EC2, Amazon WorkSpaces | 2021, 2024 |
| Visio LTSC Professional | Amazon WorkSpaces | 2021, 2024 |
| Visio LTSC Standard | Amazon WorkSpaces | 2021, 2024 |
| Project Professional | Amazon WorkSpaces | 2021, 2024 |
| Project Standard | Amazon WorkSpaces | 2021, 2024 |
| Remote Desktop Services SAL | Amazon EC2, Amazon WorkSpaces | — |

\*Out-of-support and supported versions require your own media.

\*\*SQL Server Web edition has a restricted use case based on Microsoft's licensing terms. SQL Server Web edition may be used only to support public and internet accessible webpages, websites, web applications, and web services. It may not be used to support line-of-business applications (for example, customer relationship management, enterprise resource management, and other similar applications).

License included options are best for variable workloads. For example, this is when workloads don't need to run most of the time or when workloads frequently need to scale up and down.

### BYOL options
<a name="byol-options.2ac49263-58bf-5795-8dd6-912ff80c0e4c"></a>

Using the Bring Your Own License (BYOL) model is a great way to capitalize on your existing investments in on-premises software while benefiting from the efficiencies of the AWS Cloud. BYOL allows you to extend the lifecycle of prior software versions and purchases, and deploy products not offered by AWS as license included. Whenever you bring your own licenses, you must also bring your own media. This means that you must create your own Amazon Machine Image (AMI) with your own media, rather than using Amazon-provided AMIs. The [VM Import/Export](https://aws.amazon.com/ec2/vm-import/) tool is free to use and enables you to create your own AMIs. Alternatively, you can use [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) to create your own media and AMIs.

#### Microsoft products with License Mobility through Software Assurance
<a name="microsoft-products-with-license-mobility-through-software-assurance.574b05ec-08b0-5121-971a-44a5fb781e80"></a>

Because AWS is an [Authorized Mobility Partner](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/Authorized_Mobility_Partners.pdf) any Microsoft products with License Mobility that are covered by active SA can be brought to AWS on shared or dedicated tenant environments. Products eligible for License Mobility through SA include SQL Server, SharePoint Server, Exchange Server, Project Server, Skype for Business Server, BizTalk Server, Remote Desktop Services User CALs, and System Center Server. Microsoft products that have License Mobility Rights are not affected by the October 1, 2019 [licensing changes](https://www.microsoft.com/en-us/licensing/news/updated-licensing-rights-for-dedicated-cloud) made by Microsoft. As a result, products with License Mobility don't have any purchase date or version restrictions. They are eligible for BYOL to AWS as long as the licenses have active SA. For example, SQL Server 2022 licenses with active SA can be brought to shared-tenancy (default) EC2 instances (doesn't required Dedicated Instances) as long as SA is maintained.

Products with License Mobility through SA are licensed on AWS the same way they would be within a virtualized on-premises environment, with the exception of System Center Server. System Center Server licenses have specialized license counting applied when being brought to the AWS Cloud. For every 16 cores of System Center Server Datacenter edition, you can manage up to 10 EC2 instances (of any size). For every 16 cores of System Center Server Standard edition, you can manage up to two EC2 instances (of any size). SQL Server is the most commonly brought product with License Mobility to AWS. SQL Server core licenses with active SA or subscription licenses (except those purchased through the Cloud Solution Provider, or CSP, program) are licensed per vCPU on shared-tenancy (default) EC2 instances, with a minimum Microsoft licensing requirement of four vCPUs per EC2 instance. SQL Server/CAL licenses with active SA are licensed with one server license per EC2 instance. Plus, all users or devices with access must have the corresponding CALs assigned to them. SQL Server also has a passive failover benefit with active SA and subscriptions. For every active, licensed SQL Server on Amazon EC2, you're eligible for a secondary, passive SQL Server instance on Amazon EC2 without having to license the SQL Server portion on the passive instance. For more information, see the [Microsoft SQL Server 2022 Licensing guide](https://download.microsoft.com/download/9/3/d/93d32de6-f268-45ed-ba25-2f9a6756b6af/SQL_Server_2022_Licensing_guide.pdf) (downloadable PDF) on the Microsoft website. AWS is an [Authorized Mobility Partner](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/Authorized_Mobility_Partners.pdf) (downloadable PDF). If you bring Microsoft products with [License Mobility](https://aws.amazon.com/windows/resources/licensemobility/) to AWS, you must fill out and submit a License Mobility Verification Form to Microsoft. This form is a brief Microsoft Word document that asks for the following:
+ Your name and contact information
+ Microsoft agreement number
+ Your cloud partner
+ Products being brought through License Mobility
+ Number of licenses that you're bringing

You must submit the form to Microsoft directly or through your Microsoft reseller within 10 days of bringing the products to AWS. To learn more about the verification process, see [License Mobility through Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility.aspx) in the Microsoft documentation. The License Mobility Verification Form has a section to provide information about the Authorized Mobility Partner. You can use `microsoft@amazon.com` as the email address, *Amazon Web Services* as the Partner name, and `aws.amazon.com` as the Partner website. For more guidance, see Microsoft's [Verification Guide for Customers](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/License_Mobility_Customer_Verification_Guide.pdf) (downloadable PDF) in the Microsoft documentation. To download a copy of the License Mobility Verification Form, see [Licensing Resources and Documents](https://www.microsoft.com/licensing/docs/view/Forms?lang=1&year=2016) in the Microsoft documentation.

**Note**
The Flexible Virtualization Program offered by Microsoft isn't available on AWS because AWS has been named a Listed Provider\* cloud by Microsoft. Microsoft named Alibaba, Amazon, and Google Cloud as [Listed Providers](https://www.microsoft.com/licensing/docs/view/Listed-Providers) as part of the October 1, 2019 [licensing changes](https://www.microsoft.com/en-us/licensing/news/updated-licensing-rights-for-dedicated-cloud). Beginning October 1, 2019, on-premises licenses purchased without SA and License Mobility rights can't be deployed hosted cloud services offered by Listed Providers.

#### Microsoft products without License Mobility
<a name="microsoft-products-without-license-mobility.82f30e97-bc74-51e2-9af5-cb6a108acd23"></a>

Windows Server, Visual Studio, Microsoft Developer Network (MSDN), Windows desktop operating systems, Microsoft Office, and Microsoft 365 apps (formerly Office 365) don't have License Mobility rights granted to them in the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage), even if the licenses have SA or are active subscription licenses. As a result, bringing licenses for these products requires dedicated infrastructure: Amazon EC2 Dedicated Hosts, Amazon EC2 Dedicated Instances, Amazon Elastic VMware Service (Amazon EVS), and Dedicated Hosts on AWS Outposts. You must also follow other specific requirements to be eligible for BYOL to AWS. These requirements are a result of changes Microsoft made to the license terms for products without License Mobility when deployed on Listed Provider clouds, effective October 1, 2019. For more information, see [Updated Microsoft licensing terms for dedicated hosted cloud services](https://www.microsoft.com/en-us/licensing/news/updated-licensing-rights-for-dedicated-cloud) in the Microsoft documentation.

To be eligible for BYOL to AWS, licenses for products without License Mobility must meet the following requirements from Microsoft:
+ Licenses must be purchased as perpetual use rights (not subscription).
+ The purchase date of the licenses must be before October 1, 2019, or the licenses must be purchased within a Microsoft Enterprise Agreement term that started before October 1, 2019.
+ The version deployed must have been publicly available prior to October 1, 2019.
+ The product must be deployed on dedicated infrastructure.

Subscription licenses for products without License Mobility will lose BYOL once purchased or renewed on or after October 1, 2019.

**Note**
Products without License Mobility don't require active SA for BYOL on AWS, as long as the licenses meet the requirements above.

**Note**
Windows Server BYOL requires dedicated host tenancy (such as Amazon EC2 Dedicated Hosts, Amazon Elastic VMware Service (Amazon EVS), and Dedicated Hosts on AWS Outposts) because Windows Server BYOL must be licensed by physical core.

#### Microsoft 365 and Office 365 BYOL
<a name="microsoft-365-and-office-365-byol.19c78c4f-bd43-595d-bd13-51451aae7bf3"></a>

Microsoft 365 and Office 365 are subscription licenses and are not eligible for License Mobility benefits. As a result, these products were impacted by the October 1, 2019 licensing changes from Microsoft and are not eligible for BYOL on AWS. The exception to this is on Amazon WorkSpaces offerings, where Microsoft allows BYOL of the Microsoft 365 apps for enterprise or business with the following eligible plans, effective August 1, 2023:
+ Microsoft 365 E3/E5
+ Microsoft 365 A3/A5
+ Microsoft 365 G3/G5
+ Microsoft 365 Business Premium

The following are also included in this update for BYOL on Amazon WorkSpaces:
+ Microsoft Project licensed under Planner and Project Plan 3 or 5
+ Microsoft Visio, licensed under Visio Online Plan 2
+ Microsoft Teams, licensed under Microsoft Teams EEA, Enterprise, Essentials, or Premium
+ Microsoft Power Automate, licensed under Microsoft Power Automate Premium
+ Microsoft 365 app, licensed under Microsoft 365 Copilot

For confirmation on this, see the [Microsoft Product Terms for Amazon WorkSpaces Deployments](https://www.microsoft.com/licensing/terms/en-US/product/AmazonWorkspacesDeployments/EAEAS).

#### Windows Desktop Operating System (Windows 11) BYOL
<a name="windows-desktop-operating-system--windows-11--byol.69067d14-bc6c-5b5e-bb61-ba1525cca832"></a>

As a result of Microsoft's October 1, 2019 licensing changes, Windows Desktop OS BYOL on listed provider clouds, such as AWS, requires the following:
+ VDA E3/E5 user subscription license for each user with access to the virtual desktop instances
+ Dedicated infrastructure, such as BYOL WorkSpaces, Amazon EC2 Dedicated Instances, Amazon EC2 Dedicated Hosts, Amazon Elastic VMware Service (Amazon EVS), or AWS Outposts

If using Microsoft 365 BYOL on Amazon WorkSpaces, VDA E3/E5 user subscription licenses (or VDA Add-Ons) are still required according to the Microsoft Product Terms.

#### Services Provider License Agreement (SPLA) BYOL
<a name="services-provider-license-agreement--spla--byol.a7220039-2737-574f-951b-b1a22f258481"></a>

Effective October 1, 2025, Microsoft no longer allows BYOL of licenses purchased under the SPLA program on [listed provider clouds](https://www.microsoft.com/licensing/docs/view/Listed-Providers). As a result, the recommendation is to move to license included offerings available from AWS.

#### Windows Server BYOL on Amazon EC2 Dedicated Hosts
<a name="windows-server-byol-on-9999999999999999ec2dedicatedhosts-.319ab917-005f-550d-879e-343cd50baa7d"></a>

Windows Server BYOL is available for version 2019 or earlier with eligible licenses on Amazon EC2 Dedicated Hosts, Amazon EVS, Dedicated Hosts on AWS Outposts, Dedicated Host tenancy on bare metal (including Nutanix on EC2 (NC2) and Red Hat OpenShift (ROSA)). If you bring BYOL-eligible Windows Server licenses to Amazon EC2 Dedicated Hosts, you must license all physical cores (not vCPUs) of the host. For example, an R5 Amazon EC2 Dedicated Host has 48 physical cores. Bringing 48 cores of Windows Server Datacenter edition to an R5 allows for as many Amazon EC2 instances to be deployed on the host as technically possible. Bringing 48 cores of Windows Server Standard edition allows up to two Amazon EC2 instances of any size on the host. You can stack Windows Server Standard edition licenses to allow for additional Amazon EC2 instances on the same host, where all of the physical cores of the host licensed a second time allows for two additional Amazon EC2 instances (and so on).

On Amazon EVS, Standard edition is not recommended due to having multiple hosts in a cluster, and instead Datacenter edition is recommended. For example, the minimum number of hosts on Amazon EVS is four `i4i.metal` hosts, each with 64 physical cores, totaling 256 cores. This configuration would require 256 cores of BYOL-eligible Windows Server Datacenter licenses, and it allows for unlimited virtualization for virtual machines running version 2019 or earlier. Because licensing can be complex, see the [Amazon Web Services and Microsoft FAQ site](https://aws.amazon.com/windows/faq/) to determine if your licenses are eligible for the BYOL to AWS option. If you don't find the information you need in the FAQ or are unsure where to start with migrating your Microsoft workloads to AWS, contact `Microsoft@Amazon.com`. AWS has Microsoft workload and licensing specialists available to help make sure you have all the information that you need.

## Mobilize
<a name="licensing-mobilize"></a>

### AWS License Manager
<a name="9999999999999999liclong-.91b27ade-2222-5786-a2f3-e68511ac4218"></a>

As part of the mobilize phase for Microsoft licensing considerations, we recommend that you input the licenses you're planning to allocate to your workloads in AWS in [AWS License Manager](https://aws.amazon.com/license-manager/). License Manager is a free tool that makes it easier for you to manage your software licenses from vendors such as Microsoft, Oracle, IBM, and SAP across not only AWS but workloads on-premises or in other clouds, too.

To learn more about License Manager, see [Working with AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/using-license-manager.html) in the License Manager documentation.

### Licensing optimization
<a name="licensing-optimization.9a0a1999-9107-58b9-ae88-5ac9b63feb3b"></a>

[Optimize CPU](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) is an Amazon EC2 feature that allows you to turn off simultaneous multithreading (SMT) or hyperthreading or decrease to a specific number of vCPUs, while retaining all of the memory associated with the Amazon EC2 instance type. This helps you reduce the number of Microsoft SQL Server Core licenses that you need to bring (subject to a 4-core licensing minimum set by Microsoft), or lower the license included costs for Windows Server and SQL Server. To learn more, see the [Optimize CPU Best Practices for SQL Server Workloads](https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpus-best-practices-for-sql-server-workloads-continued/) blog post.

[High Availability for SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-high-availability.html) is another option to lower license included SQL Server costs for active-passive failover clusters. With this feature, you pay for SQL Server license included on only the active SQL Server Amazon EC2 instance, where the secondary passive instance is the same size or smaller in terms of vCPUs. For more information, see the [Reduce Microsoft SQL Server High Availability costs running on Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/amazon-ec2-reduces-costs-for-microsoft-sql-server-high-availability-deployments/) blog post.

### Licensing considerations
<a name="licensing-considerations.19a5816f-e359-5d23-84c2-77f385dc6ef4"></a>

We recommend completing a fully-funded [Optimization and Licensing Assessment (OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/), which can help you right-size your instances and provides multiple pricing and migration options within a business case. It can also review your specific licensing and provide customized recommendations.

Consider planning your migration around the licenses currently assigned to the workloads prior to migration. For example, if you're bringing several on-premises hosts to AWS, consider migrating by host rather than by grouping workloads that fall across several different hosts. This is because as you decommission an on-premises host, you free up the licenses associated to that host for use in AWS. Alternatively, you can use license included instances for Windows Server or SQL Server during your migration and switch over to the BYOL option after the migration is complete. However, this option requires using your own media and AMI from the beginning (even for license included options). The [license conversion feature](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html) available with AWS License Manager only allows you to switch to BYOL from license included if the Amazon EC2 instances were originally created from your own media and AMIs.

## Migrate
<a name="licensing-migrate"></a>

Within 10 days of deploying your Microsoft workloads on AWS, be sure to submit the [License Mobility Verification Form](https://aws.amazon.com/windows/resources/licensemobility/) to Microsoft for any licenses with License Mobility that you're bringing to AWS. You can submit this form multiple times, based on the different stages of your migration. The form asks for the following:
+ Your name and contact information
+ Microsoft agreement number
+ Your cloud partner
+ Products being brought through License Mobility
+ Number of licenses that you're bringing

The **License Mobility Verification** form has a section to provide information about the authorized mobility partner. Use `microsoft@amazon.com` as the email address, `Amazon Web Services` as the partner name, and `aws.amazon.com` as the partner website.

To learn more about the verification process, see [License Mobility through Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility.aspx) in the Microsoft documentation. For more guidance, see Microsoft's [Verification Guide for Customers](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/License_Mobility_Customer_Verification_Guide.pdf) (downloadable PDF) in the Microsoft documentation. To download a copy of the **License Mobility Verification** form, see [Licensing Resources and Documents](https://www.microsoft.com/licensing/docs/view/Forms?lang=1&year=2016) in the Microsoft documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
