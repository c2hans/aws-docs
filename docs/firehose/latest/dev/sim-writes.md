---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/sim-writes.html
---

# Configure multiple file directories and streams
<a name="sim-writes"></a>

By specifying multiple flow configuration settings, you can configure the agent to monitor multiple file directories and send data to multiple streams. In the following configuration example, the agent monitors two file directories and sends data to a Kinesis data stream and a Firehose stream respectively. You can specify different endpoints for Kinesis Data Streams and Amazon Data Firehose so that your data stream and Firehose stream don’t need to be in the same Region.

```
{
    "cloudwatch.emitMetrics": {{true}},
    "kinesis.endpoint": "{{https://your/kinesis/endpoint}}",
    "firehose.endpoint": "{{https://your/firehose/endpoint}}",
    "flows": [
        {
            "filePattern": "{{/tmp/app1.log*}}",
            "kinesisStream": "{{yourkinesisstream}}"
        },
        {
            "filePattern": "{{/tmp/app2.log*}}",
            "deliveryStream": "{{yourfirehosedeliverystream}}"
        }
    ]
}
```

For more detailed information about using the agent with Amazon Kinesis Data Streams, see [Writing to Amazon Kinesis Data Streams with Kinesis Agent](https://docs.aws.amazon.com/kinesis/latest/dev/writing-with-agents.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
