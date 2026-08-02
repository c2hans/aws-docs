---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_WorkerComputeConfiguration.html
---

# WorkerComputeConfiguration
<a name="API_WorkerComputeConfiguration"></a>

Configuration information about the compute workers that perform the transform job.

## Contents
<a name="API_WorkerComputeConfiguration_Contents"></a>

 ** number **   <a name="API-Type-WorkerComputeConfiguration-number"></a>
The number of compute workers that are used.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 1024.
Required: No

 ** properties **   <a name="API-Type-WorkerComputeConfiguration-properties"></a>
The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your Clean Rooms workloads.
Type: [WorkerComputeConfigurationProperties](API_WorkerComputeConfigurationProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** type **   <a name="API-Type-WorkerComputeConfiguration-type"></a>
The instance type of the compute workers that are used.
Type: String
Valid Values: `CR.1X | CR.4X | CR.8X`
Required: No

## See Also
<a name="API_WorkerComputeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/WorkerComputeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/WorkerComputeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/WorkerComputeConfiguration)
