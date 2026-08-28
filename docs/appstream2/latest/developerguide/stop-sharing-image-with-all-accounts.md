---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/stop-sharing-image-with-all-accounts.html
---

# Stop Sharing an Image That You Own in Amazon WorkSpaces Applications
<a name="stop-sharing-image-with-all-accounts"></a>

Follow these steps to stop sharing an image that you own with any other AWS account.

**To stop sharing an image that you own with any other AWS account**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the navigation pane, choose **Images**, **Image Registry**.

1. In the image list, select the image that you want to change the permissions for.

1. Below the image list, choose the **Permissions** tab for the image you selected, then choose **Edit**.

1. In the **Edit image permissions** dialog box, in the row for all AWS accounts that the image is shared with, choose the X icon to the right of the **Use for fleet **option.

1. Choose **Update image sharing permissions**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
