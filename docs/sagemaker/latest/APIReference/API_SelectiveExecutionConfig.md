---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SelectiveExecutionConfig.html
---

# SelectiveExecutionConfig
<a name="API_SelectiveExecutionConfig"></a>

The selective execution configuration applied to the pipeline run.

## Contents
<a name="API_SelectiveExecutionConfig_Contents"></a>

 ** SelectedSteps **   <a name="sagemaker-Type-SelectiveExecutionConfig-SelectedSteps"></a>
A list of pipeline steps to run. All step(s) in all path(s) between two selected steps should be included.
Type: Array of [SelectedStep](API_SelectedStep.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** SourcePipelineExecutionArn **   <a name="sagemaker-Type-SelectiveExecutionConfig-SourcePipelineExecutionArn"></a>
The ARN from a reference execution of the current pipeline. Used to copy input collaterals needed for the selected steps to run. The execution status of the pipeline can be either `Failed` or `Success`.
This field is required if the steps you specify for `SelectedSteps` depend on output collaterals from any non-specified pipeline steps. For more information, see [Selective Execution for Pipeline Steps](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-selective-ex.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: No

## See Also
<a name="API_SelectiveExecutionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SelectiveExecutionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SelectiveExecutionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SelectiveExecutionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
