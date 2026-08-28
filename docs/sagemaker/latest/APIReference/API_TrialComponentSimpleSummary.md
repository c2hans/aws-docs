---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentSimpleSummary.html
---

# TrialComponentSimpleSummary
<a name="API_TrialComponentSimpleSummary"></a>

A short summary of a trial component.

## Contents
<a name="API_TrialComponentSimpleSummary_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-TrialComponentSimpleSummary-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-TrialComponentSimpleSummary-CreationTime"></a>
When the component was created.
Type: Timestamp
Required: No

 ** TrialComponentArn **   <a name="sagemaker-Type-TrialComponentSimpleSummary-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`
Required: No

 ** TrialComponentName **   <a name="sagemaker-Type-TrialComponentSimpleSummary-TrialComponentName"></a>
The name of the trial component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** TrialComponentSource **   <a name="sagemaker-Type-TrialComponentSimpleSummary-TrialComponentSource"></a>
The Amazon Resource Name (ARN) and job type of the source of a trial component.
Type: [TrialComponentSource](API_TrialComponentSource.md) object
Required: No

## See Also
<a name="API_TrialComponentSimpleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentSimpleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentSimpleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentSimpleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
