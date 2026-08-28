---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAnalysis.html
---

# RepositoryAnalysis
<a name="API_RepositoryAnalysis"></a>

A code review type that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN when you call [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview).

## Contents
<a name="API_RepositoryAnalysis_Contents"></a>

 ** RepositoryHead **   <a name="reviewer-Type-RepositoryAnalysis-RepositoryHead"></a>
A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies the tip of a branch in an associated repository.
Type: [RepositoryHeadSourceCodeType](API_RepositoryHeadSourceCodeType.md) object
Required: No

 ** S3BucketRepository **   <a name="reviewer-Type-RepositoryAnalysis-S3BucketRepository"></a>
Information about an associated repository in an S3 bucket. The associated repository contains a source code .zip file and a build artifacts .zip file that contains .jar or .class files.
Type: [S3BucketRepository](API_S3BucketRepository.md) object
Required: No

 ** SourceCodeType **   <a name="reviewer-Type-RepositoryAnalysis-SourceCodeType"></a>
Specifies the source code that is analyzed in a code review.
Type: [SourceCodeType](API_SourceCodeType.md) object
Required: No

## See Also
<a name="API_RepositoryAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/RepositoryAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/RepositoryAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/RepositoryAnalysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
