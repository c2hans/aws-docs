---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-managing-rebooting-db.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Rebooting a DB instance
<a name="timestream-for-influx-managing-rebooting-db"></a>

You can reboot a DB instance using the AWS Management Console, the AWS Command Line Interface, or the Timestream API. You must provide the ID of the DB instance:

**Using the AWS Management Console**

1. Sign in to the AWS Management Console and open the [Amazon Timestream for InfluxDB console](https://console.aws.amazon.com/timestream/).

1. In the navigation pane, choose **InfluxDB Databases**, and then choose the DB instance that you want to reboot.

1. Choose **Restart database**.

1. Choose **Confirm and Restart**.

**Using the AWS Command Line Interface**

To reboot a DB instance by using the AWS CLI, call the `reboot-db-instance` command with the following options:

**Example Commands**

For Linux, macOS, or Unix:

```
aws timestream-influxdb reboot-db-instance \
    --region YOUR_REGION \
    --identifier YOUR_INSTANCE_ID
```

For Windows:

```
aws timestream-influxdb reboot-db-instance ^
    --region YOUR_REGION ^
    --identifier YOUR_INSTANCE_ID
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
