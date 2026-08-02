---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-aws-managed.html
---

# AWS Managed Microsoft AD
<a name="active-directory-aws-managed"></a>

## Overview
<a name="active-directory-aws-managed-overview"></a>

AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, is powered by a Windows Server Active Directory and managed by AWS. You can use AWS Managed Microsoft AD to migrate a broad range of Active Directory–aware applications to the AWS Cloud. AWS Managed Microsoft AD works with a variety of native Active Directory applications and services. It also supports [AWS managed applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_app_compatibility.html). While there are not many cost optimization levers for AWS Managed Microsoft AD due to the service and its billing mechanisms, there are some design tenets that can help you keep costs at a minimum.

## Cost impact
<a name="active-directory-aws-managed-cost"></a>

Since AWS Managed Microsoft AD is a managed service based on present SKUs, sizing is a relatively straightforward process. Currently there are two sizing SKUs available: Standard and Enterprise editions. Other SKUs include directory sharing, adding additional domain controllers (including additional Regions), and cross-Region data transfer.

## Cost optimization recommendations
<a name="active-directory-aws-managed-rec"></a>

There are differences between AWS Managed Microsoft AD Standard Edition and AWS Managed Microsoft AD Enterprise Edition. Enterprise Edition supports up to 500,000 Active Directory objects, 500 account shares (soft limit), and has multi-Region support. Standard Edition supports up to 30,000 Active Directory objects, five account shares (soft limit to approximately 25 maximum), and doesn't have multi-Region support.

**Note**
The upper limits of Active Directory objects are approximations. Your directory might support more or fewer objects depending on their size and the behavior and performance needs of your applications.

The questions to consider prior to selecting your directory type are:
+ Is multi-Region support required?
+ Is the directory going to be shared with over 25 accounts?
+ Is the Active Directory object count going to be over 30,000?

If the answer is yes to any of the above questions, then Enterprise Edition is required. If the answer to all the questions is no, we recommend that you start with Standard Edition.

**Note**
You can upgrade a directory from Standard Edition to Enterprise Edition but a directory cannot be downgraded. Deploying Standard Edition isn't going through a one-way door. If you desire to upgrade your directory to Enterprise Edition, contact AWS.

There is a cost for each share when you share directories in AWS Managed Microsoft AD Enterprise Edition. This is less than the cost of deploying a directory in each account, but keep in mind that sharing costs can creep up if left unchecked. We recommend that you only share directories with accounts containing Amazon Relational Database Service (Amazon RDS) and Amazon FSx for Windows File Server, since only those services support this feature. Keep in mind that you have the option to integrate FSx for Windows File Server with your self-managed Active Directory, including an AWS Managed Microsoft AD. If only Amazon FSx is required in another account, then you can do a self-managed Amazon FSx deployment against the AWS Managed Microsoft AD without the need to share the directory.

When deciding when to deploy additional domain controllers, keep in mind that AWS Managed Microsoft AD supports only two subnets in separate Availability Zones in the same VPC. Adding additional domain controllers doesn't allow you to add additional subnets. To determine if you must add additional domain controllers due to performance issues, review the [domain controller performance metrics in CloudWatch](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_monitor_dc_performance.html). This tells you if one or all domain controllers are being overwhelmed. If you determine that only one domain controller is being overwhelmed, adding additional domain controllers won't alleviate the load and you'll need to dig deeper into applications not load balancing across the currently available domain controllers. If all domain controllers are being heavily used, adding an additional domain controller could reduce the load on the existing domain controllers. For instructions on how to automate scaling, see [How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/) in the AWS Security Blog.

If you extended your directory to multiple Regions, we recommend that you don't use the directory NETLOGON or SYSVOL shares for file storage. All domain controllers replicate the contents of those shares. Not using the shares for file storage keeps data transfer costs to a minimum.

You also have the option to enroll in an Enterprise Agreement with AWS. Enterprise Agreements give you the option to tailor agreements that best suit your needs. For more information, see [Enterprise Customers](https://aws.amazon.com/pricing/enterprise/).

## Additional resources
<a name="active-directory-aws-managed-resources"></a>
+ [AWS Managed Microsoft AD quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html) (AWS Directory Service documentation)
+ [AWS Directory Service Pricing](https://aws.amazon.com/directoryservice/pricing/) (AWS website)
+ [Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/active-directory-domain-services.html) (AWS Whitepapers)
