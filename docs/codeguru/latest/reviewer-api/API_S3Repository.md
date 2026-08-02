---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_S3Repository.html
---

# S3Repository
<a name="API_S3Repository"></a>

Information about a repository in an S3 bucket.

## Contents
<a name="API_S3Repository_Contents"></a>

 ** BucketName **   <a name="reviewer-Type-S3Repository-BucketName"></a>
The name of the S3 bucket used for associating a new S3 repository. It must begin with `codeguru-reviewer-`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?=^.{3,63}$)(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)`
Required: Yes

 ** Name **   <a name="reviewer-Type-S3Repository-Name"></a>
The name of the repository in the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S[\w.-]*$`
Required: Yes

## See Also
<a name="API_S3Repository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/S3Repository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/S3Repository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/S3Repository)
