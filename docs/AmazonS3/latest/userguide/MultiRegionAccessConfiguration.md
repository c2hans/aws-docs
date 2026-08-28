---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessConfiguration.html
---

# Configuring a Multi-Region Access Point for use with AWS PrivateLink
<a name="MultiRegionAccessConfiguration"></a>

You can use Multi-Region Access Points to route Amazon S3 request traffic between AWS Regions. Each Multi-Region Access Point global endpoint routes Amazon S3 data request traffic from multiple sources without your having to build complex networking configurations with separate endpoints. These data-request traffic sources include:
+ Traffic originating in a virtual private cloud (VPC)
+ Traffic from on-premises data centers traveling over AWS PrivateLink
+ Traffic from the public internet

If you establish an AWS PrivateLink connection to an S3 Multi-Region Access Point, you can route S3 requests into AWS, or across multiple AWS Regions, over a private connection by using a simple network architecture and configuration. When you use AWS PrivateLink, you don't need to configure a VPC peering connection.

**Topics**
+ [Configuring Multi-Region Access Point opt-in Regions](ConfiguringMrapOptInRegions.md)
+ [Configuring a Multi-Region Access Point for use with AWS PrivateLink](MultiRegionAccessPointsPrivateLink.md)
+ [Removing access to a Multi-Region Access Point from a VPC endpoint](RemovingMultiRegionAccessPointAccess.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
