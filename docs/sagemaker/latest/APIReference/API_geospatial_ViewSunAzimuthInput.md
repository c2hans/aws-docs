---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ViewSunAzimuthInput.html
---

# ViewSunAzimuthInput
<a name="API_geospatial_ViewSunAzimuthInput"></a>

The input structure for specifying ViewSunAzimuth property filter. ViewSunAzimuth refers to the Sun azimuth angle. From the scene center point on the ground, this is the angle between truth north and the sun. Measured clockwise in degrees (0-360).

## Contents
<a name="API_geospatial_ViewSunAzimuthInput_Contents"></a>

 ** LowerBound **   <a name="sagemaker-Type-geospatial_ViewSunAzimuthInput-LowerBound"></a>
The minimum value for ViewSunAzimuth property filter. This filters items having ViewSunAzimuth greater than or equal to this value.
Type: Float
Required: Yes

 ** UpperBound **   <a name="sagemaker-Type-geospatial_ViewSunAzimuthInput-UpperBound"></a>
The maximum value for ViewSunAzimuth property filter. This filters items having ViewSunAzimuth lesser than or equal to this value.
Type: Float
Required: Yes

## See Also
<a name="API_geospatial_ViewSunAzimuthInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ViewSunAzimuthInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ViewSunAzimuthInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ViewSunAzimuthInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
