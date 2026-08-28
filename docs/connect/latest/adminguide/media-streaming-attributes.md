---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/media-streaming-attributes.html
---

# Contact attributes for live media streaming in Kinesis Video Streams
<a name="media-streaming-attributes"></a>

The attributes are displayed when you select **Media streams** for the **Type** in a flow block that supports attributes, such as the **Start media streaming** block. They include the following:

Customer audio stream ARN
The ARN of the Kinesis video stream that includes the customer data to reference.
**JSONPath format: **$.MediaStreams.Customer.Audio.StreamARN

Customer audio start timestamp
The time at which the customer audio stream started.
**JSONPath format: **$.MediaStreams.Customer.Audio.StartTimestamp

Customer audio stop timestamp
The time at which the customer audio stream stopped.
**JSONPath format: **$.MediaStreams.Customer.Audio.StopTimestamp

Customer audio start fragment number
The number that identifies the Kinesis Video Streams fragment in which the customer audio stream started.
**JSONPath format: **$.MediaStreams.Customer.Audio.StartFragmentNumber

For more information about Amazon Kinesis Video Streams fragments, see [Fragment](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html) in the * Amazon Kinesis Video Streams Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
