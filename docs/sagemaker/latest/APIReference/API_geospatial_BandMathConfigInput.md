---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_BandMathConfigInput.html
---

# BandMathConfigInput
<a name="API_geospatial_BandMathConfigInput"></a>

Input structure for the BandMath operation type. Defines Predefined and CustomIndices to be computed using BandMath.

## Contents
<a name="API_geospatial_BandMathConfigInput_Contents"></a>

 ** CustomIndices **   <a name="sagemaker-Type-geospatial_BandMathConfigInput-CustomIndices"></a>
CustomIndices that are computed.
Type: [CustomIndicesInput](API_geospatial_CustomIndicesInput.md) object
Required: No

 ** PredefinedIndices **   <a name="sagemaker-Type-geospatial_BandMathConfigInput-PredefinedIndices"></a>
One or many of the supported predefined indices to compute. Allowed values: `NDVI`, `EVI2`, `MSAVI`, `NDWI`, `NDMI`, `NDSI`, and `WDRVI`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_geospatial_BandMathConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/BandMathConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/BandMathConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/BandMathConfigInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
