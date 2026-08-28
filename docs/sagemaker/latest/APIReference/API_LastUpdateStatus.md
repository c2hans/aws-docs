---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LastUpdateStatus.html
---

# LastUpdateStatus
<a name="API_LastUpdateStatus"></a>

A value that indicates whether the update was successful.

## Contents
<a name="API_LastUpdateStatus_Contents"></a>

 ** Status **   <a name="sagemaker-Type-LastUpdateStatus-Status"></a>
A value that indicates whether the update was made successful.
Type: String
Valid Values: `Successful | Failed | InProgress`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-LastUpdateStatus-FailureReason"></a>
If the update wasn't successful, indicates the reason why it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_LastUpdateStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LastUpdateStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LastUpdateStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LastUpdateStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
