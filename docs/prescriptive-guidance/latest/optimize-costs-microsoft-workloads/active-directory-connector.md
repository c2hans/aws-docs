---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-connector.html
---

# AD Connector
<a name="active-directory-connector"></a>

## Overview
<a name="active-directory-connector-overview"></a>

[AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) is a proxy service that connects your existing on-premises Microsoft Active Directory to compatible [AWS applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_app_compatibility.html), such as Amazon WorkSpaces, AWS Quick, and domain join for Amazon Elastic Compute Cloud (Amazon EC2) instances, without caching any information in the cloud. You can use AD Connector to add one service account to your Active Directory. AD Connector eliminates the need for directory synchronization or the cost and complexity of hosting a federation infrastructure. Because of the nature of the service and its billing mechanisms, AD Connector has few cost optimization levers. You can follow the design recommendations in this section to help manage costs.

## Cost impact
<a name="active-directory-connector-cost"></a>

AD Connector is a managed service based on preset SKUs, which simplifies sizing. AD Connector offers two sizes: small and large. You can use the [AWS Pricing Calculator](https://calculator.aws/#/addService/DirectoryService) to estimate costs for AD Connector.

## Cost optimization recommendations
<a name="active-directory-connector-rec"></a>

Other than backend compute resources, there is no difference between the small and large connector sizes.

Before you select a connector size, consider the following questions:
+ Do you have a large number (10,000\+) of active users who access AWS applications integrated with the AD Connector?
+ Are your users members of many, deep, or circular nested groups?

If you answer no to both questions, we recommend that you start with the small size. If you answer yes to either question, consider the large size. You can start with a small AD Connector and, if performance degrades, request an upgrade to the large size.

|
|
| Note: You can upgrade an AD Connector from small to large, but you can't downgrade it. |
| --- |

Most performance issues don't originate from the AD Connector. They occur when on-premises Active Directory domain controllers are overwhelmed because many users are members of many, deep, or circular nested groups.

You can also enroll in an Enterprise Agreement with AWS. Enterprise Agreements let you tailor agreements to your needs. For more information, see [Enterprise Customers](https://aws.amazon.com/pricing/enterprise/).

## Additional resources
<a name="active-directory-connector-resources"></a>
+ [AD Connector quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_limits.html) (AWS Directory Service documentation)
+ [Other directory types pricing](https://aws.amazon.com/directoryservice/other-directories-pricing/) (AWS website)
+ [Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/active-directory-domain-services.html) (AWS Whitepapers)
