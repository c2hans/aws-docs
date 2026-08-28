---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/network-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network requirements
<a name="network-requirements"></a>

 To use AWS Direct Connect, your network must meet the following conditions:
+  Your network is collocated with an existing AWS DX POP.
+  You are working with an AWS Direct Connect partner who is a member of the [AWS Partner Network](https://partners.amazonaws.com/) (APN).
+  You are working with an independent service provider to connect to AWS Direct Connect.
+  The AWS Direct Connect network segment is configured to support:
  +  802.1Q VLAN encapsulation must be supported across the entire connection, including intermediate devices.
  +  BGP and BGP MD5 authentication.

 AWS Direct Connect supports both the IPv4 and IPv6 communication protocols. IPv6 addresses provided by public AWS services are accessible through AWS Direct Connect Public VIF.

 To access public resources in a remote Region, you must set up a public VIF and establish a BGP session. After you have created a public VIF and established a BGP session to it, your router learns the routes of the other public AWS Regions.

 AWS Direct Connect applies inbound (from your on-premises data center) and outbound (from your AWS Region) routing policies for a public AWS Direct Connect connection. You can also use BGP community tags on routes advertised by Amazon and apply BGP community tags on the routes you advertise to Amazon.

 AWS Direct Connect locations in Regions or AWS GovCloud (US) can access public services in any other Region excluding China (Beijing and Ningxia). In addition, AWS Direct Connect connections in Regions or AWS GovCloud (US) can be configured to access a VPC in your account in any other Region excluding China (Beijing and Ningxia). You can, therefore, use a single AWS Direct Connect connection to build multi-Region services.

 There are SLA implications of this design. All networking traffic remains on the AWS global network backbone, regardless of whether you access public AWS services or a VPC in another Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
