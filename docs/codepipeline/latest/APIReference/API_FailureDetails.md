---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_FailureDetails.html
---

# FailureDetails
<a name="API_FailureDetails"></a>

Represents information about failure details.

## Contents
<a name="API_FailureDetails_Contents"></a>

 ** message **   <a name="CodePipeline-Type-FailureDetails-message"></a>
The message about the failure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: Yes

 ** type **   <a name="CodePipeline-Type-FailureDetails-type"></a>
The type of the failure.
Type: String
Valid Values: `JobFailed | ConfigurationError | PermissionError | RevisionOutOfSync | RevisionUnavailable | SystemUnavailable`
Required: Yes

 ** externalExecutionId **   <a name="CodePipeline-Type-FailureDetails-externalExecutionId"></a>
The external ID of the run of the action that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1500.
Required: No

## See Also
<a name="API_FailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/FailureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/FailureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/FailureDetails)
