---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/view-reports.html
---

# Viewing audit reports
<a name="view-reports"></a>

You can open, view, and analyze AWS Backup Audit Manager reports using the programs that you ordinarily use to work with CSV or JSON files. Note that reports for multiple regions or multiple accounts are only available in CSV format.

Large files are broken up into multiple reports if the total file size exceeds 50 MB. If the resulting files are over 50 MB, AWS Backup Audit Manager will create additional CSV files with the remainder of the report.

**To view a report**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation pane, choose **Reports**.

1. Under **Report plan name**, select a report plan by choosing its name.

1. Under **Report jobs**, click on the report link to view the report.

1. If your report's **Report status** has a dotted underline, choose it for information about your report.

1. Choose which report to view by its **Completion time**.

1. Choose the **S3 link**. This opens your destination S3 bucket.

1. Under **Name**, choose the name of the report that you want to view.

1. To save the report to your computer, choose **Download**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
