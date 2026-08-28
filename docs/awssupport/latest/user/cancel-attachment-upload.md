---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/cancel-attachment-upload.html
---

# Cancelling an in-progress upload
<a name="cancel-attachment-upload"></a>

You can cancel a file upload while it is in progress.

**To cancel an upload**

1. While a file is uploading, the **Status** column shows a progress bar and the **Action** column shows **Cancel**.

1. Choose **Cancel** in the **Action** column.

1. The upload is aborted and the file status changes to **Failed to upload**. You can then retry or remove the file.

**Note**
Any partially uploaded data is automatically cleaned up. No additional action is required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
