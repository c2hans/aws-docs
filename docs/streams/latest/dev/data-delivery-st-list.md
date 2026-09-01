---
source_url: https://docs.aws.amazon.com/streams/latest/dev/data-delivery-st-list.html
---

# List streaming table deliveries
<a name="data-delivery-st-list"></a>

 List the deliveries in your account, optionally filtered to the deliveries attached to a specific stream. Use this to find deliveries before deleting a stream, or to audit the deliveries configured in a AWS Region.

## Using the AWS Management Console
<a name="data-delivery-st-list-console"></a>

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Streaming tables** to view the list of deliveries, with columns such as name, status, source stream, and destination table.

## Using the AWS CLI
<a name="data-delivery-st-list-cli"></a>

 Use the `list-channels` command to list deliveries in the current AWS Region:

```
aws kinesis list-channels
```

 To list only the deliveries attached to a specific stream, provide a stream filter:

```
aws kinesis list-channels \
    --stream-filter StreamARN="arn:aws:kinesis:us-east-1:123456789012:stream/my-stream"
```

 The response returns up to 100 deliveries per page. Use the pagination token in the response to retrieve additional results.

 **API reference** – see `ListChannels` in the *Amazon Kinesis Data Streams API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
