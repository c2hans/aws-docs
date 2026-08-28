---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-reports-fields-applications-reports.html
---

# Applications Report Fields
<a name="usage-reports-fields-applications-reports"></a>

The following table describes the fields included in WorkSpaces Applications applications reports.

| Field name | Description |
| --- | --- |
| user\_session\_id | The unique identifier (ID) for the session. |
| application\_name | The name of the application, as specified in Image Assistant. This value is provided when a user launches an application through the WorkSpaces Applications interface.  |
| schedule | The frequency with which reports are generated.<br />Possible value: DAILY |
| year | The year of the report.  |
| month | The month of the report.  |
| day | The day of the report.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
