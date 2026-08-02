---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainedModelArtifactMaxSize.html
---

# TrainedModelArtifactMaxSize
<a name="API_TrainedModelArtifactMaxSize"></a>

Specifies the maximum size limit for trained model artifacts. This configuration helps control storage costs and ensures that trained models don't exceed specified size constraints. The size limit applies to the total size of all artifacts produced by the training job.

## Contents
<a name="API_TrainedModelArtifactMaxSize_Contents"></a>

 ** unit **   <a name="API-Type-TrainedModelArtifactMaxSize-unit"></a>
The unit of measurement for the maximum artifact size. Valid values include common storage units such as bytes, kilobytes, megabytes, gigabytes, and terabytes.
Type: String
Valid Values: `GB`
Required: Yes

 ** value **   <a name="API-Type-TrainedModelArtifactMaxSize-value"></a>
The numerical value for the maximum artifact size limit. This value is interpreted according to the specified unit.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 100.0.
Required: Yes

## See Also
<a name="API_TrainedModelArtifactMaxSize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainedModelArtifactMaxSize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainedModelArtifactMaxSize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainedModelArtifactMaxSize)
