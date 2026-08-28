---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/access-media-stream-data.html
---

# Develop live media streaming in Connect Customer
<a name="access-media-stream-data"></a>

To help you get started with development using live media streaming, Connect Customer includes the following Kinesis Video Streams repository that contains a basic example of how to consume audio data from your Kinesis Video Streams: [https://github.com/amazon-connect/connect-kvs-consumer-demo](https://github.com/amazon-connect/connect-kvs-consumer-demo)

This demo builds upon the high level abstractions provided by the Kinesis Video Streams Parser Library to read the `AUDIO_TO_CUSTOMER` and `AUDIO_FROM_CUSTOMER` tracks published by Connect Customer. It stores this data as a raw PCM file. This file can be transformed, transcoded, or played back.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
