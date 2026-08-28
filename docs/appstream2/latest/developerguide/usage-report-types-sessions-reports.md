---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-report-types-sessions-reports.html
---

# WorkSpaces Applications Sessions Reports
<a name="usage-report-types-sessions-reports"></a>

For each day that users launch at least one streaming session in your Amazon Web Services account, WorkSpaces Applications exports a sessions report to your Amazon S3 bucket. The report, named **daily-session-report-[YYYY]-[MM]-[DD].csv**, is stored in a nested folder structure in your Amazon S3 account, using the following folder path:

[bucket\_name]/sessions/schedule=DAILY/year=[YYYY]/month=[MM]/day=[DD]/

This nesting structure facilitates partitioning if you choose to query your reports by using Amazon Athena. Athena is a serverless, interactive query service that you can use to analyze data stored in your S3 buckets using standard SQL. For more information, see [Create Custom Reports and Analyze WorkSpaces Applications Usage Data](configure-custom-reports-analyze-usage-data.md).

Each user session is described in a single record in a sessions report. Sessions reports are generated daily according to UTC time within 24 hours of the close of the day that is the subject of the report. If a session spans more than one day, the session record appears in the sessions report corresponding to the day in which the session ends. For information about the data included in sessions reports, see [Sessions Report Fields](usage-reports-fields-sessions-reports.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
