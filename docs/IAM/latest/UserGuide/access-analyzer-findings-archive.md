---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-archive.html
---

# Archive IAM Access Analyzer findings
<a name="access-analyzer-findings-archive"></a>

When you get a finding for access to a resource that is intentional, you can archive the findings. For example, an external or internal access finding for an Amazon S3 bucket that is accessed for approved workflows or an unused access finding for an access key that may still be necessary. When you archive a finding, it is cleared from active findings list. Archived findings aren't deleted. You can filter the **Findings** page to display your archived findings, and unarchive them at any time.

**To archive findings from the **Findings** page**

1. Select the checkbox next to one or more findings to archive.

1. Choose **Actions** and then choose **Archive**.

   A confirmation is displayed at the top of the screen.

**To archive findings from the **Findings Details** page**

1. Choose the **Finding ID** for the finding to archive.

1. Choose **Archive**.

   A confirmation is displayed at the top of the screen.

To unarchive findings, repeat the preceding steps, but choose **Unarchive** instead of **Archive**. When you unarchive a finding, the status is set to Active.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
