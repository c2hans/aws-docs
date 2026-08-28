---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CheckpointConfigurationUpdate.html
---

# CheckpointConfigurationUpdate
<a name="API_CheckpointConfigurationUpdate"></a>

Describes updates to the checkpointing parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_CheckpointConfigurationUpdate_Contents"></a>

 ** CheckpointingEnabledUpdate **   <a name="APIReference-Type-CheckpointConfigurationUpdate-CheckpointingEnabledUpdate"></a>
Describes updates to whether checkpointing is enabled for an application.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointingEnabled` value of `true`, even if this value is set to another value using this API or in application code.
Type: Boolean
Required: No

 ** CheckpointIntervalUpdate **   <a name="APIReference-Type-CheckpointConfigurationUpdate-CheckpointIntervalUpdate"></a>
Describes updates to the interval in milliseconds between checkpoint operations.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointInterval` value of 60000, even if this value is set to another value using this API or in application code.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ConfigurationTypeUpdate **   <a name="APIReference-Type-CheckpointConfigurationUpdate-ConfigurationTypeUpdate"></a>
Describes updates to whether the application uses the default checkpointing behavior of Managed Service for Apache Flink. You must set this property to `CUSTOM` in order to set the `CheckpointingEnabled`, `CheckpointInterval`, or `MinPauseBetweenCheckpoints` parameters.
If this value is set to `DEFAULT`, the application will use the following values, even if they are set to other values using APIs or application code:
+  **CheckpointingEnabled:** true
+  **CheckpointInterval:** 60000
+  **MinPauseBetweenCheckpoints:** 5000
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** MinPauseBetweenCheckpointsUpdate **   <a name="APIReference-Type-CheckpointConfigurationUpdate-MinPauseBetweenCheckpointsUpdate"></a>
Describes updates to the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `MinPauseBetweenCheckpoints` value of 5000, even if this value is set using this API or in application code.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CheckpointConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CheckpointConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CheckpointConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CheckpointConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
