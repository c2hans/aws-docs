---
source_url: https://docs.aws.amazon.com/streams/latest/dev/data-delivery-st-describe.html
---

# Describe a streaming table delivery
<a name="data-delivery-st-describe"></a>

 Retrieve the configuration and current status of a streaming table delivery, including its state (`ChannelStatus`) and status reason (`ChannelStatusReason`). Use this to verify that a delivery reached the ACTIVE state after creation, or to diagnose a delivery in the FAILED state.

## Using the AWS Management Console
<a name="data-delivery-st-describe-console"></a>

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Streaming tables**. From the list of deliveries, choose the delivery that you want to view.

1. The delivery details page shows the delivery status, source stream, destination table, data freshness, service access role, and dead-letter queue configuration. Use the **Configurations** tab to view source and destination settings, and the **Logs and tags** tab to view log delivery and tags.

## Using the AWS CLI
<a name="data-delivery-st-describe-cli"></a>

 Use the `describe-channel` command and pass the channel ARN (`ChannelARN`) returned by `create-channel`:

```
aws kinesis describe-channel \
    --channel-arn "arn:aws:kinesis:us-east-1:123456789012:channel/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

 The response includes the delivery's `ChannelStatus` (CREATING, ACTIVE, UPDATING, DELETING, or FAILED), the source stream configuration, the destination table configuration, and the data freshness setting. A delivery is ready to receive records when `ChannelStatus` is ACTIVE.

 **API reference** – see `DescribeChannel` in the *Amazon Kinesis Data Streams API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
