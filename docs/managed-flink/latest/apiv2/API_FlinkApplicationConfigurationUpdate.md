---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkApplicationConfigurationUpdate.html
---

# FlinkApplicationConfigurationUpdate
<a name="API_FlinkApplicationConfigurationUpdate"></a>

Describes updates to the configuration parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_FlinkApplicationConfigurationUpdate_Contents"></a>

 ** CheckpointConfigurationUpdate **   <a name="APIReference-Type-FlinkApplicationConfigurationUpdate-CheckpointConfigurationUpdate"></a>
Describes updates to an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.
Type: [CheckpointConfigurationUpdate](API_CheckpointConfigurationUpdate.md) object
Required: No

 ** MonitoringConfigurationUpdate **   <a name="APIReference-Type-FlinkApplicationConfigurationUpdate-MonitoringConfigurationUpdate"></a>
Describes updates to the configuration parameters for Amazon CloudWatch logging for an application.
Type: [MonitoringConfigurationUpdate](API_MonitoringConfigurationUpdate.md) object
Required: No

 ** ParallelismConfigurationUpdate **   <a name="APIReference-Type-FlinkApplicationConfigurationUpdate-ParallelismConfigurationUpdate"></a>
Describes updates to the parameters for how an application executes multiple tasks simultaneously.
Type: [ParallelismConfigurationUpdate](API_ParallelismConfigurationUpdate.md) object
Required: No

## See Also
<a name="API_FlinkApplicationConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfigurationUpdate)
