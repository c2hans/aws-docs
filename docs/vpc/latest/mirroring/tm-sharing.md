---
source_url: https://docs.aws.amazon.com/vpc/latest/mirroring/tm-sharing.html
---

# Share a traffic mirror target
<a name="tm-sharing"></a>

A traffic mirror target can be owned by an AWS account that is different from the traffic mirror source.

You can use AWS Resource Access Manager (RAM) to share a traffic mirror target across accounts. Use the following procedure to share a traffic mirror target that you own.

You must create a traffic mirror target before you share it. For more information, see [Create or delete a traffic mirror target](create-traffic-mirroring-target.md).

**To share a traffic mirror target**

1. Open the AWS Resource Access Manager console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/).

1. Choose **Create a resource share**.

1. Under **Description**, for **Name**, enter a descriptive name for the resource share.

1. For **Select resource type**, choose **Traffic Mirror Targets**. Select the traffic mirror target.

1. For **Principals**, add principals to the resource share. For each AWS account, OU, or organization, specify its ID and choose **Add**.

   For **Allow external accounts**, choose whether to allow sharing for this resource with AWS accounts that are external to your organization.

1. (Optional) Under **Tags**, enter a tag key and tag value pair for each tag. These tags are applied to the resource share but not to the traffic mirror target.

1. Choose **Create resource share**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
