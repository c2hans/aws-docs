---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/time-to-deploy.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Time to deploy
<a name="time-to-deploy"></a>

## Definition
<a name="definition"></a>

 Time to deploy can be an important factor in selecting a suitable connectivity type for a workload. Depending on the type of connectivity and on-premises locations, connectivity can be established within hours, however, it may take weeks or months if additional circuits must be installed. This will influence your decision to use an internet-based connection, a private dedicated connection, or a private hosted connection provided as a managed service by an AWS Direct Connect Partner.

## Key questions
<a name="key-questions"></a>
+  What is the required timeline for the deployment – hours, days, weeks, or months?
+  How long will the connection be needed – will it be a short-lived project or permanent infrastructure?

## Capabilities to consider
<a name="capabilities-to-consider"></a>

 When you require AWS connectivity within hours or days, you will most likely need to use an existing network connection. This often means establishing a VPN connection to AWS over the public internet. If an existing AWS DX partner is providing you with private AWS connectivity, a new hosted connection could be provisioned within hours.

 When you have days to weeks, you can work with an AWS Direct Connect Partner to establish private connectivity to AWS. AWS Direct Connect Partners help you establish network connectivity between AWS Direct Connect locations and your data center, office, or co-location environment. Certain [AWS Direct Connect Partners](https://aws.amazon.com/directconnect/partners/) are approved to offer [Direct Connect Hosted Connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html). Hosted Connections can often be provisioned faster than Dedicated Connections. AWS Direct Connect Partner will provision each Hosted Connection using their existing infrastructure that is connected to the AWS backbone.

 When you have several weeks to months, you can investigate establishing a dedicated private connection with AWS. Service providers and AWS Direct Connect Partners facilitate AWS Direct Connect Dedicated Connections. It’s common for service providers to install networking equipment at the customer’s premises to facilitate a Direct Connect Dedicated Connection. Depending on the service provider, location of your site, and other physical factors, the installation of a Direct Connect Dedicated Connection can take from several weeks to a few months.

 If you already have your network equipment installed in the same colocation facility where the AWS Direct Connect location exists, then you can quickly establish an AWS Direct Connect Dedicated Connection via a cross-connect at the co-location site. After you request the connection, AWS makes a Letter of Authorization and Connecting Facility Assignment (LOA-CFA) available to you to download, or emails you with a request for more information. The LOA-CFA is the authorization to connect to AWS, and is required by your network provider to order a cross connect for you.

*Table 1 – Cost effectiveness comparison*

|   |  Internet-based connectivity  |  DX Dedicated Connection (existing equipment within DX location)  |  DX Dedicated Connection (net-new)  |  DX Hosted Connection (existing port with DX Partner)  |  DX Hosted Connection (net-new)  |
| --- | --- | --- | --- | --- | --- |
|  Provisioning time  |  Hours to days  |  Days  |  Several weeks to months  |  Hours to days  |  Several days to weeks to months  |

**Note**
The provided provision time guidelines are based on real-world observation and only serve as an illustration. When taking into considerations your site location, proximity to direct connect locations, and pre-existing infrastructure, and will all impact provisioning time. Your AWS Direct Connect Partner will advise you on the precise provisioning time.
