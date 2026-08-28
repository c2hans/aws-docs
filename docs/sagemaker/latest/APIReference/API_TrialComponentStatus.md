---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentStatus.html
---

# TrialComponentStatus
<a name="API_TrialComponentStatus"></a>

The status of the trial component.

## Contents
<a name="API_TrialComponentStatus_Contents"></a>

 ** Message **   <a name="sagemaker-Type-TrialComponentStatus-Message"></a>
If the component failed, a message describing why.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** PrimaryStatus **   <a name="sagemaker-Type-TrialComponentStatus-PrimaryStatus"></a>
The status of the trial component.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: No

## See Also
<a name="API_TrialComponentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
