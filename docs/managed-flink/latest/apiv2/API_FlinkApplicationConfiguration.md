---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkApplicationConfiguration.html
---

# FlinkApplicationConfiguration
<a name="API_FlinkApplicationConfiguration"></a>

Describes configuration parameters for a Managed Service for Apache Flink application or a Studio notebook.

## Contents
<a name="API_FlinkApplicationConfiguration_Contents"></a>

 ** CheckpointConfiguration **   <a name="APIReference-Type-FlinkApplicationConfiguration-CheckpointConfiguration"></a>
Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see [ Checkpoints for Fault Tolerance](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/fault-tolerance/checkpointing/#enabling-and-configuring-checkpointing) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/).
Type: [CheckpointConfiguration](API_CheckpointConfiguration.md) object
Required: No

 ** MonitoringConfiguration **   <a name="APIReference-Type-FlinkApplicationConfiguration-MonitoringConfiguration"></a>
Describes configuration parameters for Amazon CloudWatch logging for an application.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** ParallelismConfiguration **   <a name="APIReference-Type-FlinkApplicationConfiguration-ParallelismConfiguration"></a>
Describes parameters for how an application executes multiple tasks simultaneously.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

## See Also
<a name="API_FlinkApplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
