---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/requirements.html
---

# Prerequisites and limitations
<a name="requirements"></a>

Before you follow this guide, work with your AWS account team or AWS Partner to review the prerequisites and limitations for implementing edge architectures with AWS Outposts and Local Zones.

## Prerequisites
<a name="prerequisites"></a>

### AWS Outposts
<a name="9999999999999999out-.5fc1d7aa-175d-5077-9174-59f12ae3db4a"></a>
+ Your existing data center must meet the [AWS Outposts requirements](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html) for facilities, networking, and power. AWS Outposts is designed to operate in a data center environment that has  5-15 kVA redundant power inputs, 145.8 times the kVA of cubic feet per minute (CFM) airflow, and an ambient temperature between 41° F (5° C) and 95° F (35° C), among other requirements.
+ Confirm that the AWS Outposts service is available in your country by consulting the [AWS Outposts rack FAQs.](https://aws.amazon.com/outposts/rack/faqs/) See the question: *In which countries and territories is Outposts rack available?*
+ If your organization requires four or more [AWS Outposts racks](https://aws.amazon.com/outposts/rack/), your data center must meet the [Aggregation, Core, Edge (ACE) rack requirements](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-ace-requirements.html).
+ An internet or AWS Direct Connect link of at least 500 Mbps (1 Gbps is better) must be provided and sustained to connect [AWS Outposts to the AWS Region](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html), with appropriate backup connectivity if your use case requires it. The round-trip time latency from AWS Outposts to the Region must be 175 milliseconds at the maximum.
+ You must have an active contract for an [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) or an [AWS Unified Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/) plan.

### AWS Local Zones
<a name="9999999999999999lzslong-.3867a3cc-11ff-5c86-841b-a7f1a24c66cf"></a>
+ An AWS Local Zone must be available close to your data centers or users. See [AWS Local Zones locations](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/).
+ Confirm that you have network connectivity from your on-premises infrastructure to the Local Zone:
  + Option 1: An Direct Connect link from your data center to the [Direct Connect point of presence (PoP)](https://aws.amazon.com/directconnect/locations/) that's closest to the Local Zone. For more information, see [Direct Connect](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity-direct-connect.html) in the Local Zones documentation.
  + Option 2: An internet link in addition to an on-premises virtual private network (VPN) appliance and the necessary licensing to launch a software-based VPN appliance on Amazon EC2 in the Local Zone. For more information, see [VPN connection](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity-ec2-vpn.html) in the Local Zones documentation.

For additional connectivity options, see the [Local Zones documentation](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity.html).

## Limitations
<a name="limitations"></a>

### AWS Outposts
<a name="9999999999999999out-.e01ea251-a3e2-5be3-88cc-ed2cc0c2e116"></a>
+ Amazon Relational Database Service (Amazon RDS) on AWS Outposts Multi-AZ deployments require customer-owned IP (CoIP) address pools. For more information, see [Customer-owned IP addresses for Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.coip.html).
+ Multi-AZ on AWS Outposts is available for all supported versions of MySQL and PostgreSQL on Amazon RDS on AWS Outposts. For more information, see [Amazon RDS on AWS Outposts support for Amazon RDS features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.features.html). [Amazon RDS on AWS Outposts supports ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html)SQL Server, Amazon RDS for MySQL, and Amazon RDS for PostgreSQL databases.
+ AWS Outposts isn't designed to operate when it's disconnected from an AWS Region. For more information, see the [Thinking in terms of failure modes](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/thinking-in-terms-of-failure-modes.html) section in the AWS whitepaper *AWS Outposts High Availability Design and Architecture Considerations*.
+ Amazon Simple Storage Service (Amazon S3) on AWS Outposts has some limitations. These are discussed in the [How is Amazon S3 on Outposts different from Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OnOutpostsRestrictionsLimitations.html) section of the *Amazon S3 on Outposts User Guide*.
+ Application Load Balancers on AWS Outposts don't support mutual TLS (mTLS) or sticky sessions.
+ The ACE racks aren't fully enclosed and don't include front or rear doors.
+ The instance capacity tool is applicable only for new orders.

### AWS Local Zones
<a name="9999999999999999lzslong-.71f5bb8e-9cad-5466-9728-a5c9638e2f3c"></a>
+ Local Zones don't have an AWS Site-to-Site VPN endpoint. Instead, use a software-based VPN on Amazon EC2.
+ Local Zones don't support AWS Transit Gateway. Instead, connect to the Local Zone by using a Direct Connect Private virtual interface (VIF).
+ Not all Local Zones support services such as Amazon RDS, Amazon FSx, Amazon EMR, or Amazon ElastiCache, or NAT gateways. For more information, see [AWS Local Zones features](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/?nc=sn&loc=2).
+ Application Load Balancers in Local Zones don't support mTLS or sticky sessions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
