---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ResamplingConfigInput.html
---

# ResamplingConfigInput
<a name="API_geospatial_ResamplingConfigInput"></a>

The structure representing input for resampling operation.

## Contents
<a name="API_geospatial_ResamplingConfigInput_Contents"></a>

 ** OutputResolution **   <a name="sagemaker-Type-geospatial_ResamplingConfigInput-OutputResolution"></a>
The structure representing output resolution (in target georeferenced units) of the result of resampling operation.
Type: [OutputResolutionResamplingInput](API_geospatial_OutputResolutionResamplingInput.md) object
Required: Yes

 ** AlgorithmName **   <a name="sagemaker-Type-geospatial_ResamplingConfigInput-AlgorithmName"></a>
The name of the algorithm used for resampling.
Type: String
Valid Values: `NEAR | BILINEAR | CUBIC | CUBICSPLINE | LANCZOS | AVERAGE | RMS | MODE | MAX | MIN | MED | Q1 | Q3 | SUM`
Required: No

 ** TargetBands **   <a name="sagemaker-Type-geospatial_ResamplingConfigInput-TargetBands"></a>
Bands used in the operation. If no target bands are specified, it uses all bands available in the input.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_geospatial_ResamplingConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ResamplingConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ResamplingConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ResamplingConfigInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
