---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmStatusItem.html
---

# AlgorithmStatusItem
<a name="API_AlgorithmStatusItem"></a>

Represents the overall status of an algorithm.

## Contents
<a name="API_AlgorithmStatusItem_Contents"></a>

 ** Name **   <a name="sagemaker-Type-AlgorithmStatusItem-Name"></a>
The name of the algorithm for which the overall status is being reported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** Status **   <a name="sagemaker-Type-AlgorithmStatusItem-Status"></a>
The current status.
Type: String
Valid Values: `NotStarted | InProgress | Completed | Failed`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-AlgorithmStatusItem-FailureReason"></a>
if the overall status is `Failed`, the reason for the failure.
Type: String
Required: No

## See Also
<a name="API_AlgorithmStatusItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AlgorithmStatusItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AlgorithmStatusItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AlgorithmStatusItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
