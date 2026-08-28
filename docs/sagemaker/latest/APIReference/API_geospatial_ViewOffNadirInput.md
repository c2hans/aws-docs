---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ViewOffNadirInput.html
---

# ViewOffNadirInput
<a name="API_geospatial_ViewOffNadirInput"></a>

The input structure for specifying ViewOffNadir property filter. ViewOffNadir refers to the angle from the sensor between nadir (straight down) and the scene center. Measured in degrees (0-90).

## Contents
<a name="API_geospatial_ViewOffNadirInput_Contents"></a>

 ** LowerBound **   <a name="sagemaker-Type-geospatial_ViewOffNadirInput-LowerBound"></a>
The minimum value for ViewOffNadir property filter. This filters items having ViewOffNadir greater than or equal to this value.
Type: Float
Required: Yes

 ** UpperBound **   <a name="sagemaker-Type-geospatial_ViewOffNadirInput-UpperBound"></a>
The maximum value for ViewOffNadir property filter. This filters items having ViewOffNadir lesser than or equal to this value.
Type: Float
Required: Yes

## See Also
<a name="API_geospatial_ViewOffNadirInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ViewOffNadirInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ViewOffNadirInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ViewOffNadirInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
