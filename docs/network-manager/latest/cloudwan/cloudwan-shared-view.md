---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-shared-view.html
---

# View shared AWS Cloud WAN attachments
<a name="cloudwan-shared-view"></a>

View details about your shared VPC and transit gateway attachments.

**To view shared VP and transit gateway attachments**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, under **Shared by me**, choose **Attachments**.

1. The **Attachment** page displays the following information about your shared attachments:
   + **Attachment ID**
   + **Name**
   + **Edge location**
   + **Resource Type**
   + **Resource ID**
   + **State**
   + **Core network**
   + **Core network status**

1. Select the check box for the specific attachment that you want to view. Details about the attachment are displayed on the lower part of the page.

1. (Optional) You can edit some of the attachment information:

   1. Choose the attachment, and then choose **Edit**.

   1. On the **Edit attachment** page, you can edit the subnet configuration and the tags.

   1. If you made any changes to update the attachment, choose **Edit attachment**. The **Attachments** page displays a confirmation that the attachment was modified successfully.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
