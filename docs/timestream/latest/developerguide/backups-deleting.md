---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/backups-deleting.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Deleting backups
<a name="backups-deleting"></a>

This section describes how to delete a backup of a Timestream for LiveAnalytics table.

To delete a backup from Timestream console, follow these steps.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/timestream).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. Choose the radio button next to the recovery point ID of the resource. In the upper-right corner of the pane, select **Actions** and choose **Delete**.

1. Select **Continue to AWS Backup** and follow the steps for deleting backups at [Deleting backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html).

**Note**
When you delete a backup that is incremental, only the incremental backup is deleted and the underlying full backup is not deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
