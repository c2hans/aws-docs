---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CheckpointConfigurationDescription.html
---

# CheckpointConfigurationDescription
<a name="API_CheckpointConfigurationDescription"></a>

Describes checkpointing parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_CheckpointConfigurationDescription_Contents"></a>

 ** CheckpointingEnabled **   <a name="APIReference-Type-CheckpointConfigurationDescription-CheckpointingEnabled"></a>
Describes whether checkpointing is enabled for a Managed Service for Apache Flink application.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointingEnabled` value of `true`, even if this value is set to another value using this API or in application code.
Type: Boolean
Required: No

 ** CheckpointInterval **   <a name="APIReference-Type-CheckpointConfigurationDescription-CheckpointInterval"></a>
Describes the interval in milliseconds between checkpoint operations.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointInterval` value of 60000, even if this value is set to another value using this API or in application code.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ConfigurationType **   <a name="APIReference-Type-CheckpointConfigurationDescription-ConfigurationType"></a>
Describes whether the application uses the default checkpointing behavior in Managed Service for Apache Flink.
If this value is set to `DEFAULT`, the application will use the following values, even if they are set to other values using APIs or application code:
+  **CheckpointingEnabled:** true
+  **CheckpointInterval:** 60000
+  **MinPauseBetweenCheckpoints:** 5000
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** MinPauseBetweenCheckpoints **   <a name="APIReference-Type-CheckpointConfigurationDescription-MinPauseBetweenCheckpoints"></a>
Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `MinPauseBetweenCheckpoints` value of 5000, even if this value is set using this API or in application code.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CheckpointConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CheckpointConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CheckpointConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CheckpointConfigurationDescription)
