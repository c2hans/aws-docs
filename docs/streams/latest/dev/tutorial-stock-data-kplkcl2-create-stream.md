---
source_url: https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-create-stream.html
---

# Create a data stream
<a name="tutorial-stock-data-kplkcl2-create-stream"></a>

First, you must create the data stream that you will use in subsequent steps of this tutorial.

**To create a stream**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Choose **Data Streams** in the navigation pane.

1. In the navigation bar, expand the Region selector and choose a Region.

1. Choose **Create Kinesis stream**.

1. Enter a name for your data stream (for example, **StockTradeStream**).

1. Enter **1** for the number of shards, but keep **Estimate the number of shards you'll need** collapsed.

1. Choose **Create Kinesis stream**.

On the **Kinesis streams** list page, the status of your stream appears as `CREATING` while the stream is being created. When the stream is ready to use, the status changes to `ACTIVE`.

If you choose the name of your stream, in the page that appears, the **Details** tab displays a summary of your data stream configuration. The **Monitoring** section displays monitoring information for the stream.

## Next steps
<a name="tutorial-stock-data-kplkcl2-create-stream-next"></a>

[Create an IAM policy and user](tutorial-stock-data-kplkcl2-iam.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
