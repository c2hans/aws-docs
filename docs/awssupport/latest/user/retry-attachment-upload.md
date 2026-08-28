---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/retry-attachment-upload.html
---

# Retrying a failed upload
<a name="retry-attachment-upload"></a>

If a file upload fails, you can retry the upload.

**To retry a failed upload**

1. In the attachments table, identify the file showing **Failed to upload** in the **Status** column.

1. Choose **Retry** in the **Action** column.

1. The upload restarts. Monitor the **Status** column for progress.

**Important**
You cannot submit a case while any attachment has a **Failed to upload** status. An error banner appears if you attempt to submit. You must either retry or remove the failed attachment before submitting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
