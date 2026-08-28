---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_OutputResolutionStackInput.html
---

# OutputResolutionStackInput
<a name="API_geospatial_OutputResolutionStackInput"></a>

The input structure representing Output Resolution for Stacking Operation.

## Contents
<a name="API_geospatial_OutputResolutionStackInput_Contents"></a>

 ** Predefined **   <a name="sagemaker-Type-geospatial_OutputResolutionStackInput-Predefined"></a>
A string value representing Predefined Output Resolution for a stacking operation. Allowed values are `HIGHEST`, `LOWEST`, and `AVERAGE`.
Type: String
Valid Values: `HIGHEST | LOWEST | AVERAGE`
Required: No

 ** UserDefined **   <a name="sagemaker-Type-geospatial_OutputResolutionStackInput-UserDefined"></a>
The structure representing User Output Resolution for a Stacking operation defined as a value and unit.
Type: [UserDefined](API_geospatial_UserDefined.md) object
Required: No

## See Also
<a name="API_geospatial_OutputResolutionStackInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/OutputResolutionStackInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/OutputResolutionStackInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/OutputResolutionStackInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
