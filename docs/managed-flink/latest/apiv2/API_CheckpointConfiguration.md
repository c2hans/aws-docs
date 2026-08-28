---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CheckpointConfiguration.html
---

# CheckpointConfiguration
<a name="API_CheckpointConfiguration"></a>

Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see [ Checkpoints for Fault Tolerance](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/fault-tolerance/checkpointing/#enabling-and-configuring-checkpointing) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/).

## Contents
<a name="API_CheckpointConfiguration_Contents"></a>

 ** ConfigurationType **   <a name="APIReference-Type-CheckpointConfiguration-ConfigurationType"></a>
Describes whether the application uses Managed Service for Apache Flink' default checkpointing behavior. You must set this property to `CUSTOM` in order to set the `CheckpointingEnabled`, `CheckpointInterval`, or `MinPauseBetweenCheckpoints` parameters.
If this value is set to `DEFAULT`, the application will use the following values, even if they are set to other values using APIs or application code:
+  **CheckpointingEnabled:** true
+  **CheckpointInterval:** 60000
+  **MinPauseBetweenCheckpoints:** 5000
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: Yes

 ** CheckpointingEnabled **   <a name="APIReference-Type-CheckpointConfiguration-CheckpointingEnabled"></a>
Describes whether checkpointing is enabled for a Managed Service for Apache Flink application.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointingEnabled` value of `true`, even if this value is set to another value using this API or in application code.
Type: Boolean
Required: No

 ** CheckpointInterval **   <a name="APIReference-Type-CheckpointConfiguration-CheckpointInterval"></a>
Describes the interval in milliseconds between checkpoint operations.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointInterval` value of 60000, even if this value is set to another value using this API or in application code.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** MinPauseBetweenCheckpoints **   <a name="APIReference-Type-CheckpointConfiguration-MinPauseBetweenCheckpoints"></a>
Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the `CheckpointInterval`, the application otherwise performs continual checkpoint operations. For more information, see [ Tuning Checkpointing](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/large_state_tuning/#tuning-checkpointing) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/).
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `MinPauseBetweenCheckpoints` value of 5000, even if this value is set using this API or in application code.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CheckpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CheckpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CheckpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CheckpointConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
