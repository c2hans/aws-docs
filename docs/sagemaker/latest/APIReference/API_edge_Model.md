---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_Model.html
---

# Model
<a name="API_edge_Model"></a>

Information about a model deployed on an edge device that is registered with SageMaker Edge Manager.

## Contents
<a name="API_edge_Model_Contents"></a>

 ** LatestInference **   <a name="sagemaker-Type-edge_Model-LatestInference"></a>
The timestamp of the last inference that was made.
Type: Timestamp
Required: No

 ** LatestSampleTime **   <a name="sagemaker-Type-edge_Model-LatestSampleTime"></a>
The timestamp of the last data sample taken.
Type: Timestamp
Required: No

 ** ModelMetrics **   <a name="sagemaker-Type-edge_Model-ModelMetrics"></a>
Information required for model metrics.
Type: Array of [EdgeMetric](API_edge_EdgeMetric.md) objects
Required: No

 ** ModelName **   <a name="sagemaker-Type-edge_Model-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 255.
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
Required: No

 ** ModelVersion **   <a name="sagemaker-Type-edge_Model-ModelVersion"></a>
The version of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: No

## See Also
<a name="API_edge_Model_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/Model)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/Model)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/Model)
