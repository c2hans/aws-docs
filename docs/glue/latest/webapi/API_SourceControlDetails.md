---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SourceControlDetails.html
---

# SourceControlDetails
<a name="API_SourceControlDetails"></a>

The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository.

## Contents
<a name="API_SourceControlDetails_Contents"></a>

 ** AuthStrategy **   <a name="Glue-Type-SourceControlDetails-AuthStrategy"></a>
The type of authentication, which can be an authentication token stored in AWS Secrets Manager, or a personal access token.
Type: String
Valid Values: `PERSONAL_ACCESS_TOKEN | AWS_SECRETS_MANAGER`
Required: No

 ** AuthToken **   <a name="Glue-Type-SourceControlDetails-AuthToken"></a>
The value of an authorization token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Branch **   <a name="Glue-Type-SourceControlDetails-Branch"></a>
An optional branch in the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Folder **   <a name="Glue-Type-SourceControlDetails-Folder"></a>
An optional folder in the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** LastCommitId **   <a name="Glue-Type-SourceControlDetails-LastCommitId"></a>
The last commit ID for a commit in the remote repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Owner **   <a name="Glue-Type-SourceControlDetails-Owner"></a>
The owner of the remote repository that contains the job artifacts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Provider **   <a name="Glue-Type-SourceControlDetails-Provider"></a>
The provider for the remote repository.
Type: String
Valid Values: `GITHUB | GITLAB | BITBUCKET | AWS_CODE_COMMIT`
Required: No

 ** Repository **   <a name="Glue-Type-SourceControlDetails-Repository"></a>
The name of the remote repository that contains the job artifacts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_SourceControlDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SourceControlDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SourceControlDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SourceControlDetails)
