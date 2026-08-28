---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType.html
---

# SourceCodeType
<a name="API_SourceCodeType"></a>

Specifies the source code that is analyzed in a code review.

## Contents
<a name="API_SourceCodeType_Contents"></a>

 ** BranchDiff **   <a name="reviewer-Type-SourceCodeType-BranchDiff"></a>
A type of [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a source branch name and a destination branch name in an associated repository.
Type: [BranchDiffSourceCodeType](API_BranchDiffSourceCodeType.md) object
Required: No

 ** CommitDiff **   <a name="reviewer-Type-SourceCodeType-CommitDiff"></a>
A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a commit diff created by a pull request on an associated repository.
Type: [CommitDiffSourceCodeType](API_CommitDiffSourceCodeType.md) object
Required: No

 ** RepositoryHead **   <a name="reviewer-Type-SourceCodeType-RepositoryHead"></a>
A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies the tip of a branch in an associated repository.
Type: [RepositoryHeadSourceCodeType](API_RepositoryHeadSourceCodeType.md) object
Required: No

 ** RequestMetadata **   <a name="reviewer-Type-SourceCodeType-RequestMetadata"></a>
Metadata that is associated with a code review. This applies to any type of code review supported by CodeGuru Reviewer. The `RequestMetadaa` field captures any event metadata. For example, it might capture metadata associated with an event trigger, such as a push or a pull request.
Type: [RequestMetadata](API_RequestMetadata.md) object
Required: No

 ** S3BucketRepository **   <a name="reviewer-Type-SourceCodeType-S3BucketRepository"></a>
Information about an associated repository in an S3 bucket that includes its name and an `S3RepositoryDetails` object. The `S3RepositoryDetails` object includes the name of an S3 bucket, an S3 key for a source code .zip file, and an S3 key for a build artifacts .zip file. `S3BucketRepository` is required in [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) for `S3BucketRepository` based code reviews.
Type: [S3BucketRepository](API_S3BucketRepository.md) object
Required: No

## See Also
<a name="API_SourceCodeType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/SourceCodeType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/SourceCodeType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/SourceCodeType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
