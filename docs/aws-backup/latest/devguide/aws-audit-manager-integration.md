---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-audit-manager-integration.html
---

# Using AWS Backup Audit Manager with AWS Audit Manager
<a name="aws-audit-manager-integration"></a>

AWS Backup Audit Manager controls map to prebuilt, standard controls in AWS Audit Manager, allowing you to import your AWS Backup Audit Manager compliance findings to your AWS Audit Manager reports. You might want to do so to help a compliance officer, audit manager, or other colleague who reports on backup activity as part of your organization’s overall compliance posture.

You can import the compliance results of your AWS Backup Audit Manager controls to your AWS Audit Manager frameworks. To enable AWS Audit Manager to automatically collect data from your AWS Backup Audit Manager controls, create a custom control in AWS Audit Manager using the instructions for [Customizing an existing control](https://docs.aws.amazon.com/audit-manager/latest/userguide/customize-control-from-existing.html) in the *AWS Audit Manager User Guide*. As you follow those instructions, note that the **Data source** for AWS Backup controls is **AWS Config**.

For a list of AWS Backup controls, see [Choosing your controls](https://docs.aws.amazon.com/aws-backup/latest/devguide/choosing-controls.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
