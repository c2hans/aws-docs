---
source_url: https://docs.aws.amazon.com/vpc/latest/mirroring/modify-traffic-mirroring-targets.html
---

# View traffic mirror targets and modify target tags
<a name="modify-traffic-mirroring-targets"></a>

A traffic mirror target is the destination for mirrored traffic. For more information, see [Understand traffic mirror target concepts](traffic-mirroring-targets.md).

Complete the steps in this section to view traffic mirror targets or modify target tags.

**To view your traffic mirror targets and modify tags using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Traffic Mirroring**, **Mirror targets**.

1. To view a target, select the ID of the traffic mirror target to open its details page.

1. To modify the tags, on the **Tags** tab, choose **Manage tags**.

1. (Optional) For each tag to add, choose **Add new tag** and enter the tag key and tag value. For each tag to remove, choose **Remove**.

1. Choose **Save**.

**To view your traffic mirror targets using the AWS CLI**
Use the [describe-traffic-mirror-targets](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-traffic-mirror-targets.html) command.

**To modify your traffic mirror target tags using the AWS CLI**
Use the [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) command to add a tag. Use the [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) command to remove a tag.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
