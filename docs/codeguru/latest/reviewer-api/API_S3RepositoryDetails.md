---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_S3RepositoryDetails.html
---

# S3RepositoryDetails
<a name="API_S3RepositoryDetails"></a>

Specifies the name of an S3 bucket and a `CodeArtifacts` object that contains the S3 object keys for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.

## Contents
<a name="API_S3RepositoryDetails_Contents"></a>

 ** BucketName **   <a name="reviewer-Type-S3RepositoryDetails-BucketName"></a>
The name of the S3 bucket used for associating a new S3 repository. It must begin with `codeguru-reviewer-`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?=^.{3,63}$)(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)`
Required: No

 ** CodeArtifacts **   <a name="reviewer-Type-S3RepositoryDetails-CodeArtifacts"></a>
A `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object key for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.
Type: [CodeArtifacts](API_CodeArtifacts.md) object
Required: No

## See Also
<a name="API_S3RepositoryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/S3RepositoryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/S3RepositoryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/S3RepositoryDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
