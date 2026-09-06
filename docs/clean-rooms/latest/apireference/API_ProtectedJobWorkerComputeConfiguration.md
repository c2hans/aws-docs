---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobWorkerComputeConfiguration.html
---

# ProtectedJobWorkerComputeConfiguration
<a name="API_ProtectedJobWorkerComputeConfiguration"></a>

The configuration of the compute resources for a PySpark job.

## Contents
<a name="API_ProtectedJobWorkerComputeConfiguration_Contents"></a>

 ** number **   <a name="API-Type-ProtectedJobWorkerComputeConfiguration-number"></a>
The number of workers for a PySpark job.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 1024.
Required: Yes

 ** type **   <a name="API-Type-ProtectedJobWorkerComputeConfiguration-type"></a>
The worker compute configuration type.
Type: String
Valid Values: `CR.1X | CR.4X`
Required: Yes

 ** properties **   <a name="API-Type-ProtectedJobWorkerComputeConfiguration-properties"></a>
The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your AWS Clean Rooms workloads.
Type: [WorkerComputeConfigurationProperties](API_WorkerComputeConfigurationProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ProtectedJobWorkerComputeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobWorkerComputeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobWorkerComputeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobWorkerComputeConfiguration)
