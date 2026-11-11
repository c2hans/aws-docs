---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-aws-managed.html
---

# AWS Managed Microsoft AD
<a name="active-directory-aws-managed"></a>

## Overview
<a name="active-directory-aws-managed-overview"></a>

AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, is powered by Windows Server Active Directory, and AWS manages it. You can use AWS Managed Microsoft AD to migrate a broad range of Active Directory–aware applications to the AWS Cloud. AWS Managed Microsoft AD works with a variety of native Active Directory applications and services. It also supports [AWS managed applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_app_compatibility.html). Although the service and its billing mechanisms offer few cost optimization levers for AWS Managed Microsoft AD, you can follow several design tenets to help reduce your costs.

## Cost impact
<a name="active-directory-aws-managed-cost"></a>

Because AWS Managed Microsoft AD is a managed service based on predefined SKUs, sizing is a straightforward process. Two sizing SKUs are available: Standard Edition and Enterprise Edition. Other SKUs include directory sharing, additional domain controllers (including in additional Regions), and cross-Region data transfer.

## Cost optimization recommendations
<a name="active-directory-aws-managed-rec"></a>

There are differences between AWS Managed Microsoft AD Standard Edition and AWS Managed Microsoft AD Enterprise Edition. Enterprise Edition supports up to 500,000 Active Directory objects, 500 account shares (soft limit), and has multi-Region support. Standard Edition supports up to 30,000 Active Directory objects, 25 account shares (soft limit), and doesn't have multi-Region support.

**Note**
The upper limits of Active Directory objects are approximations. Your directory might support more or fewer objects depending on their size and the behavior and performance needs of your applications.

Before you select your directory type, consider the following questions:
+ Is multi-Region support required?
+ Is the directory going to be shared with over 25 accounts?
+ Is the Active Directory object count going to be over 30,000?

If the answer is yes to any of the above questions, then Enterprise Edition is required. If the answer to all the questions is no, we recommend that you start with Standard Edition.

**Note**
You can upgrade a directory from Standard Edition to Enterprise Edition, but you can't downgrade it. Deploying Standard Edition doesn't lock you into that edition. If you want to upgrade your directory to Enterprise Edition, you can do so using the AWS Support Management Console, the UpdateDirectorySetup API, the AWS CLI, or AWS Tools for PowerShell.

Each share incurs a cost when you share directories in AWS Managed Microsoft AD Enterprise Edition. This cost is less than deploying a directory in each account, but sharing costs can increase if you don't monitor them. We recommend that you share directories only with accounts that contain Amazon Relational Database Service (Amazon RDS) and Amazon FSx for Windows File Server, because only those services support this feature. You can also integrate FSx for Windows File Server with your self-managed Active Directory, including an AWS Managed Microsoft AD. If you require only Amazon FSx in another account, you can do a self-managed Amazon FSx deployment against the AWS Managed Microsoft AD without sharing the directory.

When you decide whether to deploy more domain controllers, keep in mind that AWS Managed Microsoft AD supports only two subnets in separate Availability Zones in the same [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/). Adding domain controllers doesn't allow you to add subnets. To determine if you must add domain controllers because of performance issues, review the [domain controller performance metrics in CloudWatch](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_monitor_dc_performance.html). These metrics show whether one or all domain controllers are overloaded. If only one domain controller is overloaded, adding domain controllers won't reduce the load. Instead, investigate why your applications aren't load balancing across the available domain controllers. If all domain controllers are heavily used, adding a domain controller could reduce the load on the existing domain controllers. For instructions on how to automate scaling, see [How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/) in the AWS Security Blog.

If you extended your directory to multiple Regions, we recommend that you don't use the directory NETLOGON or SYSVOL shares for file storage. All domain controllers replicate the contents of those shares. Not using the shares for file storage keeps data transfer costs to a minimum.

You can also enroll in an Enterprise Agreement with AWS. Enterprise Agreements allow you to tailor agreements to your needs. For more information, see [Enterprise Customers](https://aws.amazon.com/pricing/enterprise/).

## Additional resources
<a name="active-directory-aws-managed-resources"></a>
+ [AWS Managed Microsoft AD quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html) (AWS Directory Service documentation)
+ [AWS Directory Service Pricing](https://aws.amazon.com/directoryservice/pricing/) (AWS website)
+ [Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/active-directory-domain-services.html) (AWS Whitepapers)
