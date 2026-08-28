---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_StackConfigInput.html
---

# StackConfigInput
<a name="API_geospatial_StackConfigInput"></a>

The input structure for Stacking Operation.

## Contents
<a name="API_geospatial_StackConfigInput_Contents"></a>

 ** OutputResolution **   <a name="sagemaker-Type-geospatial_StackConfigInput-OutputResolution"></a>
The structure representing output resolution (in target georeferenced units) of the result of stacking operation.
Type: [OutputResolutionStackInput](API_geospatial_OutputResolutionStackInput.md) object
Required: No

 ** TargetBands **   <a name="sagemaker-Type-geospatial_StackConfigInput-TargetBands"></a>
A list of bands to be stacked in the specified order. When the parameter is not provided, all the available bands in the data collection are stacked in the alphabetical order of their asset names.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_geospatial_StackConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/StackConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/StackConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/StackConfigInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
