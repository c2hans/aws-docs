---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Retention.html
---

# CloudWatch investigations data retention
<a name="Investigations-Retention"></a>

The retention period that you set for an investigation group determines how long that investigation data is kept. Valid values are seven days to 90 days.

After you first create an investigation, if you don't end it manually, it moves to a CLOSED state automatically after seven days. Then, the retention period determines how long the data is kept after the investigation moves to the CLOSED state. The data that is kept during the retention period includes the data in the investigation, accepted and discarded findings, and AI assistant audit log messages.

When this retention period expires, the investigation data is deleted.

If you manually end an investigation, that also moves the investigation to the CLOSED state and the retention period time begins to be in effect.

**Note**
Investigations conducted without configuring your CloudWatch investigations settings are linked to individual user sessions and are deleted after 24 hours, with no recovery option available.

## Incident report retention
<a name="Investigations-Retention-IncidentReports"></a>

Incident reports generated from investigations follow the same retention policy as their parent investigations.

We recommend copying important incident reports to external systems if you need to retain them beyond the investigation retention period.

For more information, see [Generate incident reports](Investigations-Incident-Reports.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
