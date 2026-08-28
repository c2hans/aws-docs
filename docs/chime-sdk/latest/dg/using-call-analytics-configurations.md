---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/using-call-analytics-configurations.html
---

# Using call analytics configurations for the Amazon Chime SDK
<a name="using-call-analytics-configurations"></a>

To process audio using a call analytics configuration, you must create a call analytics pipeline, also known as a media insights pipeline. The pipeline is created during a call to handle the audio and is terminated at the end of the call. Call analytics pipelines require the ARN of a call analytics configuration, and information about the audio source. The call analytics configuration includes details about audio processors, insight destinations, and alert event configurations, *but not the audio source*. This allows you to reuse the configuration across different call analytics workflows, such as with different Voice Connectors or KVS sources. The call analytics pipeline invokes the machine learning services specified in the configuration and records the audio. You can manually or automatically stop the pipeline when the call ends.

You can use call analytics pipelines in a wide variety use cases. The following workflows show potential ways to use a call analytics configuration and pipeline.

**Topics**
+ [Understanding workflows for recording calls for the Amazon Chime SDK](recording-workflows.md)
+ [Understanding workflows for machine-learning based analytics for the Amazon Chime SDK](ml-based-analytics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
