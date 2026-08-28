---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Disabling.html
---

# Stopping a database activity stream
<a name="DBActivityStreams.Disabling"></a>

You can stop an activity stream using the console or AWS CLI.

If you delete your Amazon RDS database instance, the activity stream is stopped and the underlying Amazon Kinesis stream is deleted automatically.

## Console
<a name="DBActivityStreams.Disabling-collapsible-section-D1"></a>

**To turn off an activity stream**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose a database that you want to stop the database activity stream for.

1. For **Actions**, choose **Stop activity stream**. The **Database Activity Stream** window appears.

   1. Choose **Immediately**.

      When you choose **Immediately**, the RDS instance restarts right away. If you choose **During the next maintenance window**, the RDS instance doesn't restart right away. In this case, the database activity stream doesn't stop until the next maintenance window.

   1. Choose **Continue**.

## AWS CLI
<a name="DBActivityStreams.Disabling-collapsible-section-D2"></a>

To stop database activity streams for your database, configure the DB instance using the AWS CLI command [stop-activity-stream](https://docs.aws.amazon.com/cli/latest/reference/rds/stop-activity-stream.html). Identify the AWS Region for the DB instance using the `--region` parameter. The `--apply-immediately` parameter is optional.

For Linux, macOS, or Unix:

```
aws rds --region {{MY_REGION}} \
    stop-activity-stream \
    --resource-arn {{MY_DB_ARN}} \
    --apply-immediately
```

For Windows:

```
aws rds --region {{MY_REGION}} ^
    stop-activity-stream ^
    --resource-arn {{MY_DB_ARN}} ^
    --apply-immediately
```

## RDS API
<a name="DBActivityStreams.Disabling-collapsible-section-D3"></a>

To stop database activity streams for your database, configure the DB instance using the [StopActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopActivityStream.html) operation. Identify the AWS Region for the DB instance using the `Region` parameter. The `ApplyImmediately` parameter is optional.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
