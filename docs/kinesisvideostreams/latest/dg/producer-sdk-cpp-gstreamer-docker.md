---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp-gstreamer-docker.html
---

# Use the C\+\+ producer SDK as a GStreamer plugin in a Docker container
<a name="producer-sdk-cpp-gstreamer-docker"></a>

[GStreamer](https://gstreamer.freedesktop.org/) is a popular media framework used by multiple cameras and video sources to create custom media pipelines by combining modular plugins. The Kinesis Video Streams GStreamer plugin streamlines the integration of your existing GStreamer media pipeline with Kinesis Video Streams.

In addition, using [Docker]() to create the GStreamer pipeline standardizes the operating environment for Kinesis Video Streams, which streamlines building and running the application.

For information about using the C\+\+ producer SDK as a GStreamer plugin in a Docker container, see [Run the GStreamer element in a Docker container](examples-gstreamer-plugin.md#examples-gstreamer-plugin-docker).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
