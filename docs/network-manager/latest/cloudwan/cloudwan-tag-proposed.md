---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tag-proposed.html
---

# Add or update an AWS Cloud WAN resource attachment tag
<a name="cloudwan-tag-proposed"></a>

Add a tag to a Cloud WAN core network attachment or modify an existing tag.

**To add or update attachment tags**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1.  Select the check box for the specific attachment that you want to view or update. Details about the attachment are displayed in the lower part of the page. Choose the **Tags** tab.

1. Choose **Add/Update tags**.

1. Choose **Add tags**, and then choose **Add tag** to add a new key-value pair. Or edit the **Value** of any existing tag. Choose** Edit tags** when finished.

   If the change that you made to the tags requires a tag acceptance from the core network owner, you will see the new proposed tags in the **Proposed Tags** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
