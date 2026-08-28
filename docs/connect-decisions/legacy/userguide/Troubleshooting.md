---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/Troubleshooting.html
---

# Troubleshooting
<a name="Troubleshooting"></a>

This section contains information about how to troubleshoot order planning and tracking issues that may occur.

| Issue | Resolution |
| --- | --- |
| Order planning and tracking page is blank |  + Make sure data ingestion is complete.<br />+ Check the data quality tab under *Data Lake* for missing required entities or any specific errors. For information on required entities for order planning and tracking, see [Order Planning and Tracking](entities-work-order-insights.md).<br />+ Make sure the order planning and tracking configuration is complete. For more information, see [Orders settings](work-order-settings.md).  |
| A specific column is not displayed under orders or order lines | Hover over on any column name and select the three vertical dots. Choose *Manage columns* and make sure the required column is selected. |
| Column or field values are not displayed under orders or orders insights |  + Make sure the column name has a value in the dataset.<br />+ Check the data mapping between the source and destination fields in the data lake page. For more information, see [Uploading files for the first time](uploading_files.md).  |
| A column or field is not displayed under Material Summary |  + Make sure the column name has a value in the dataset.<br />+ Check the data mapping between the source and destination fields in the data lake page. For more information, see [Uploading files for the first time](uploading_files.md).<br />+ Choose **Edit** on the material summary page to see if the data entity is enabled to view on the material summary page.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
