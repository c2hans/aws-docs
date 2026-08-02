---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RequestMetadata.html
---

# RequestMetadata
<a name="API_RequestMetadata"></a>

Metadata that is associated with a code review. This applies to both pull request and repository analysis code reviews.

## Contents
<a name="API_RequestMetadata_Contents"></a>

 ** EventInfo **   <a name="reviewer-Type-RequestMetadata-EventInfo"></a>
Information about the event associated with a code review.
Type: [EventInfo](API_EventInfo.md) object
Required: No

 ** Requester **   <a name="reviewer-Type-RequestMetadata-Requester"></a>
An identifier, such as a name or account ID, that is associated with the requester. The `Requester` is used to capture the `author/actor` name of the event request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** RequestId **   <a name="reviewer-Type-RequestMetadata-RequestId"></a>
The ID of the request. This is required for a pull request code review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S+`
Required: No

 ** VendorName **   <a name="reviewer-Type-RequestMetadata-VendorName"></a>
The name of the repository vendor used to upload code to an S3 bucket for a CI/CD code review. For example, if code and artifacts are uploaded to an S3 bucket for a CI/CD code review by GitHub scripts from a GitHub repository, then the repository association's `ProviderType` is `S3Bucket` and the CI/CD repository vendor name is GitHub. For more information, see the definition for `ProviderType` in [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html).
Type: String
Valid Values: `GitHub | GitLab | NativeS3`
Required: No

## See Also
<a name="API_RequestMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/RequestMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/RequestMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/RequestMetadata)
