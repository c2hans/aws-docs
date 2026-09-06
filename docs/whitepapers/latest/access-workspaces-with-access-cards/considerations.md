---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Considerations
<a name="considerations"></a>

 You should consider and understand the following information prior to starting the instructions included in this guide.
+ **Skill level** — Prior experience with Amazon Web Services (AWS) is required to complete this implementation. An understanding of core AWS technologies, including [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html), [AWS Directory Service AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html), [Amazon WorkSpaces](https://aws.amazon.com/workspaces/), [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI), Microsoft Active Directory, and Microsoft Certificate Authorities.
+ **Increase service limits** — By default, AWS sets quotas (also referred to as limits) for the resources that you can create and the number of users who can use the service. You can request a quota increase using [Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) and [AWS Support Center](https://console.aws.amazon.com/support/home#/). If a service is not yet available in AWS Service Quotas, use AWS Support Center instead. Increases are not granted immediately. It might take a couple of days for your increase to become effective. For the service limit quotas for WorkSpaces, see the [Amazon WorkSpaces endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/wsp.html) page.
+ **Supported Availability Zones** — Amazon Workspaces support for smart card pre-session authentication is available in the WorkSpaces AWS GovCloud (US-West) [Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) at this time. WorkSpaces support for smart card in-session authentication is available in all Regions where [WorkSpaces Streaming Protocol](https://aws.amazon.com/workspaces/wsp/) (WSP) is supported.
