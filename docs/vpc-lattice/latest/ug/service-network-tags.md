---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-tags.html
---

# Manage tags for a VPC Lattice service network
<a name="service-network-tags"></a>

Tags help you to categorize your service network in different ways, for example, by purpose, owner, or environment.

You can add multiple tags to each service network. Tag keys must be unique for each service network. If you add a tag with a key that is already associated with the service network, it updates the value of that tag. You can use characters such as letters, spaces, numbers (in UTF-8), and the following special characters: \+ - = . \_ : / @. Do not use leading or trailing spaces. Tag values are case sensitive.

**To add or delete tags using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the name of the service network to open its details page.

1. Choose the **Tags** tab.

1. To add a tag, choose **Add tags** and enter the tag key and tag value. To add another tag, choose **Add new tag**. When you are finished adding tags, choose **Save changes**.

1. To delete a tag, select the check box for the tag and choose **Delete**. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To add or delete tags using the AWS CLI**
Use the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/untag-resource.html) commands.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
