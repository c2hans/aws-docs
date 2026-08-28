---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GeoMosaicConfigInput.html
---

# GeoMosaicConfigInput
<a name="API_geospatial_GeoMosaicConfigInput"></a>

Input configuration information for the geomosaic.

## Contents
<a name="API_geospatial_GeoMosaicConfigInput_Contents"></a>

 ** AlgorithmName **   <a name="sagemaker-Type-geospatial_GeoMosaicConfigInput-AlgorithmName"></a>
The name of the algorithm being used for geomosaic.
Type: String
Valid Values: `NEAR | BILINEAR | CUBIC | CUBICSPLINE | LANCZOS | AVERAGE | RMS | MODE | MAX | MIN | MED | Q1 | Q3 | SUM`
Required: No

 ** TargetBands **   <a name="sagemaker-Type-geospatial_GeoMosaicConfigInput-TargetBands"></a>
The target bands for geomosaic.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_geospatial_GeoMosaicConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/GeoMosaicConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/GeoMosaicConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/GeoMosaicConfigInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
