---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EcsSettings.html
---

# EcsSettings
<a name="API_EcsSettings"></a>

The Amazon ECS settings for a compute environment, including the CloudWatch Container Insights mode. Use this structure with `CreateComputeEnvironment` and `UpdateComputeEnvironment`.

## Contents
<a name="API_EcsSettings_Contents"></a>

 ** containerInsights **   <a name="Batch-Type-EcsSettings-containerInsights"></a>
Specifies the CloudWatch Container Insights mode for the compute environment. Valid values are:
ENABLED
Turns on standard Container Insights, which collects CPU, memory, disk, and network utilization metrics for the compute environment.
ENHANCED
Turns on enhanced Container Insights, which collects the standard metrics along with additional per-task observability metrics.
DISABLED
Turns off Container Insights for the compute environment.
If you don't specify a value, the default is `DISABLED`. For more information, see [Container Insights](https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights.html) in the * AWS Batch User Guide*.
Type: String
Valid Values: `ENABLED | ENHANCED | DISABLED`
Required: No

## See Also
<a name="API_EcsSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EcsSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EcsSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EcsSettings)
