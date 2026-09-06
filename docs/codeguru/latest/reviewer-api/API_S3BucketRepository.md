---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_S3BucketRepository.html
---

# S3BucketRepository
<a name="API_S3BucketRepository"></a>

Information about an associated repository in an S3 bucket. The associated repository contains a source code .zip file and a build artifacts .zip file that contains .jar or .class files.

## Contents
<a name="API_S3BucketRepository_Contents"></a>

 ** Name **   <a name="reviewer-Type-S3BucketRepository-Name"></a>
The name of the repository when the `ProviderType` is `S3Bucket`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S[\w.-]*$`
Required: Yes

 ** Details **   <a name="reviewer-Type-S3BucketRepository-Details"></a>
An `S3RepositoryDetails` object that specifies the name of an S3 bucket and a `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object keys for a source code .zip file and for a build artifacts .zip file.
Type: [S3RepositoryDetails](API_S3RepositoryDetails.md) object
Required: No

## See Also
<a name="API_S3BucketRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/S3BucketRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/S3BucketRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/S3BucketRepository)
