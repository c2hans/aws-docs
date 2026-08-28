---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PlatformInput.html
---

# PlatformInput
<a name="API_geospatial_PlatformInput"></a>

The input structure for specifying Platform. Platform refers to the unique name of the specific platform the instrument is attached to. For satellites it is the name of the satellite, eg. landsat-8 (Landsat-8), sentinel-2a.

## Contents
<a name="API_geospatial_PlatformInput_Contents"></a>

 ** Value **   <a name="sagemaker-Type-geospatial_PlatformInput-Value"></a>
The value of the platform.
Type: String
Required: Yes

 ** ComparisonOperator **   <a name="sagemaker-Type-geospatial_PlatformInput-ComparisonOperator"></a>
The ComparisonOperator to use with PlatformInput.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | STARTS_WITH`
Required: No

## See Also
<a name="API_geospatial_PlatformInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/PlatformInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/PlatformInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/PlatformInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
