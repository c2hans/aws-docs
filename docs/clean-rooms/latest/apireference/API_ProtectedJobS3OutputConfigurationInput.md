---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobS3OutputConfigurationInput.html
---

# ProtectedJobS3OutputConfigurationInput
<a name="API_ProtectedJobS3OutputConfigurationInput"></a>

Contains input information for protected jobs with an S3 output type.

## Contents
<a name="API_ProtectedJobS3OutputConfigurationInput_Contents"></a>

 ** bucket **   <a name="API-Type-ProtectedJobS3OutputConfigurationInput-bucket"></a>
 The S3 bucket for job output.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `.*(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
Required: Yes

 ** keyPrefix **   <a name="API-Type-ProtectedJobS3OutputConfigurationInput-keyPrefix"></a>
The S3 prefix to unload the protected job results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\w!.=*/-]*`
Required: No

## See Also
<a name="API_ProtectedJobS3OutputConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobS3OutputConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobS3OutputConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobS3OutputConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
