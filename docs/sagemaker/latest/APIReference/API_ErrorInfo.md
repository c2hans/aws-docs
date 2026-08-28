---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ErrorInfo.html
---

# ErrorInfo
<a name="API_ErrorInfo"></a>

This is an error field object that contains the error code and the reason for an operation failure.

## Contents
<a name="API_ErrorInfo_Contents"></a>

 ** Code **   <a name="sagemaker-Type-ErrorInfo-Code"></a>
The error code for an invalid or failed operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`
Required: No

 ** Reason **   <a name="sagemaker-Type-ErrorInfo-Reason"></a>
The failure reason for the operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!\s*$).+`
Required: No

## See Also
<a name="API_ErrorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ErrorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ErrorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ErrorInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
