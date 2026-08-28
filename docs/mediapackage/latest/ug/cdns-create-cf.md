---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/cdns-create-cf.html
---

# Creating a Distribution from Amazon CloudFront
<a name="cdns-create-cf"></a>

After you create a channel and its endpoints in AWS Elemental MediaPackage, note the URLs for each of the endpoints. These URLs are what you use for the origin domain names for your CloudFront distribution. You need one origin for each endpoint on the channel in MediaPackage.

For detailed steps about creating a distribution in Amazon CloudFront with AWS Elemental MediaPackage endpoints as the origins, see [Delivering Live Streaming Video](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html) in the *Amazon CloudFront Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
