---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_CloudRemovalConfigInput.html
---

# CloudRemovalConfigInput
<a name="API_geospatial_CloudRemovalConfigInput"></a>

Input structure for Cloud Removal Operation type

## Contents
<a name="API_geospatial_CloudRemovalConfigInput_Contents"></a>

 ** AlgorithmName **   <a name="sagemaker-Type-geospatial_CloudRemovalConfigInput-AlgorithmName"></a>
The name of the algorithm used for cloud removal.
Type: String
Valid Values: `INTERPOLATION`
Required: No

 ** InterpolationValue **   <a name="sagemaker-Type-geospatial_CloudRemovalConfigInput-InterpolationValue"></a>
The interpolation value you provide for cloud removal.
Type: String
Required: No

 ** TargetBands **   <a name="sagemaker-Type-geospatial_CloudRemovalConfigInput-TargetBands"></a>
TargetBands to be returned in the output of CloudRemoval operation.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_geospatial_CloudRemovalConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/CloudRemovalConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/CloudRemovalConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/CloudRemovalConfigInput)
