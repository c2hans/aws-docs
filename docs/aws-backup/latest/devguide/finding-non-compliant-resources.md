---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/finding-non-compliant-resources.html
---

# Finding non-compliant resources
<a name="finding-non-compliant-resources"></a>

AWS Backup Audit Manager helps you find which resources are non-compliant in two ways.
+ When [Viewing framework compliance status](https://docs.aws.amazon.com/aws-backup/latest/devguide/viewing-frameworks.html), choose the control name in the **Details section**. Doing so takes you to the AWS Config console, where you can view a list of your of your `Non-Compliant` resources.
+ After you [Create a report plan with the resource compliance template](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-report-plan-console.html) that includes your framework, you can [View your report](https://docs.aws.amazon.com/aws-backup/latest/devguide/view-reports.html) to identify all your `Non-Compliant` resources across all your controls.

  Furthermore, your `Resource compliance report` shows the last time AWS Backup Audit Manager last evaluated each of your controls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
