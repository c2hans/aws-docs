---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkApplicationConfigurationDescription.html
---

# FlinkApplicationConfigurationDescription
<a name="API_FlinkApplicationConfigurationDescription"></a>

Describes configuration parameters for a Managed Service for Apache Flink application.

## Contents
<a name="API_FlinkApplicationConfigurationDescription_Contents"></a>

 ** CheckpointConfigurationDescription **   <a name="APIReference-Type-FlinkApplicationConfigurationDescription-CheckpointConfigurationDescription"></a>
Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.
Type: [CheckpointConfigurationDescription](API_CheckpointConfigurationDescription.md) object
Required: No

 ** JobPlanDescription **   <a name="APIReference-Type-FlinkApplicationConfigurationDescription-JobPlanDescription"></a>
The job plan for an application. For more information about the job plan, see [Jobs and Scheduling](https://nightlies.apache.org/flink/flink-docs-release-1.20/internals/job_scheduling.html) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/). To retrieve the job plan for the application, use the [DescribeApplication:IncludeAdditionalDetails](API_DescribeApplication.md#APIReference-DescribeApplication-request-IncludeAdditionalDetails) parameter of the [DescribeApplication](API_DescribeApplication.md) operation.
Type: String
Required: No

 ** MonitoringConfigurationDescription **   <a name="APIReference-Type-FlinkApplicationConfigurationDescription-MonitoringConfigurationDescription"></a>
Describes configuration parameters for Amazon CloudWatch logging for an application.
Type: [MonitoringConfigurationDescription](API_MonitoringConfigurationDescription.md) object
Required: No

 ** ParallelismConfigurationDescription **   <a name="APIReference-Type-FlinkApplicationConfigurationDescription-ParallelismConfigurationDescription"></a>
Describes parameters for how an application executes multiple tasks simultaneously.
Type: [ParallelismConfigurationDescription](API_ParallelismConfigurationDescription.md) object
Required: No

## See Also
<a name="API_FlinkApplicationConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/FlinkApplicationConfigurationDescription)
