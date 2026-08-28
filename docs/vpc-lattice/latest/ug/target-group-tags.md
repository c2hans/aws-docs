---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-group-tags.html
---

# Tags for your VPC Lattice target group
<a name="target-group-tags"></a>

Tags help you to categorize your target groups in different ways, for example, by purpose, owner, or environment.

You can add multiple tags to each target group. Tag keys must be unique for each target group. If you add a tag with a key that is already associated with the target group, it updates the value of that tag.

When you are finished with a tag, you can remove it.

**Restrictions**
+ Maximum number of tags per resource—50
+ Maximum key length—127 Unicode characters
+ Maximum value length—255 Unicode characters
+ Tag keys and values are case sensitive. Allowed characters are letters, spaces, and numbers representable in UTF-8, plus the following special characters: \+ - = . \_ : / @. Do not use leading or trailing spaces.
+ Do not use the `aws:` prefix in your tag names or values because it is reserved for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

**To update the tags for a target group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Target groups**.

1. Select the name of the target group to open its details page.

1. Choose the **Tags** tab.

1. To add a tag, choose **Add tags** and enter the tag key and tag value. To add another tag, choose **Add new tag**. When you are finished adding tags, choose **Save changes**.

1. To delete a tag, select the check box for the tag and choose **Delete**. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To update the tags for a target group using the AWS CLI**
Use the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/untag-resource.html) commands.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
