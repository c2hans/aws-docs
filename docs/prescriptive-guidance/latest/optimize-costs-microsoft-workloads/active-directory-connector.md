---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-connector.html
---

# AD Connector
<a name="active-directory-connector"></a>

## Overview
<a name="active-directory-connector-overview"></a>

[AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) is a proxy service that provides an easy way to connect your existing on-premises Microsoft Active Directory to compatible [AWS applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_app_compatibility.html), such as Amazon WorkSpaces, Amazon Quick, and seamless domain join for Amazon Elastic Compute Cloud (Amazon EC2) instances, without caching any information in the cloud. You can use AD Connector to add one service account to your Active Directory. AD Connector eliminates the need for directory synchronization or the cost and complexity of hosting a federation infrastructure. While there are not many cost optimization levers for AD Connector due to the nature of the service and its billing mechanisms, you can follow the design recommendations in this section to keep costs to a minimum.

## Cost impact
<a name="active-directory-connector-cost"></a>

AD Connector is a managed service based on preset SKUs. This makes sizing a straightforward process. There are two sizing SKUs available: small and large sizes. You can use the [AWS Pricing Calculator](https://calculator.aws/#/addService/DirectoryService) for cost estimations involving AD Connector.

## Cost optimization recommendations
<a name="active-directory-connector-rec"></a>

Other than backend compute resources there is no difference between the small and large connector sizes.

The questions to consider prior to selecting your directory type are:
+ Is there a large number (10,000\+) of active users using AWS applications integrated with the AD Connector?
+ Is the user a member of many, deep, or circular nested groups?

If the answer to both questions is no, we recommend you start with the small size. If you answer yes to any of the above questions, then a large size might be worth considering. You can start with a small size AD Connector and, if the directory becomes impaired due to performance, you can request the directory be upgraded to the large size.

|
|
| Note: You can upgrade an AD Connector from small to large, but an AD Connector cannot be downgraded. |
| --- |

Most of the performance issues are not related to the AD Connector, but the on-premises Active Directory domain controllers being overwhelmed due to many users being a member of many, deep, or circular nested groups.

You also have the option to enroll in an Enterprise Agreement with AWS. Enterprise Agreements give you the option to tailor agreements that best suit your needs. For more information, see [Enterprise Customers](https://aws.amazon.com/pricing/enterprise/).

## Additional resources
<a name="active-directory-connector-resources"></a>
+ [AD Connector quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_limits.html) (AWS Directory Service documentation)
+ [Other directory types pricing](https://aws.amazon.com/directoryservice/other-directories-pricing/) (AWS website)
+ [Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/active-directory-domain-services.html) (AWS Whitepapers)
