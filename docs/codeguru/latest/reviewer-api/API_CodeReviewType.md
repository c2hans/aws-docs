---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html
---

# CodeReviewType
<a name="API_CodeReviewType"></a>

The type of a code review. There are two code review types:
+  `PullRequest` - A code review that is automatically triggered by a pull request on an associated repository.
+  `RepositoryAnalysis` - A code review that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN in [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview).

## Contents
<a name="API_CodeReviewType_Contents"></a>

 ** RepositoryAnalysis **   <a name="reviewer-Type-CodeReviewType-RepositoryAnalysis"></a>
A code review that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN in [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview).
Type: [RepositoryAnalysis](API_RepositoryAnalysis.md) object
Required: Yes

 ** AnalysisTypes **   <a name="reviewer-Type-CodeReviewType-AnalysisTypes"></a>
They types of analysis performed during a repository analysis or a pull request review. You can specify either `Security`, `CodeQuality`, or both.
Type: Array of strings
Valid Values: `Security | CodeQuality`
Required: No

## See Also
<a name="API_CodeReviewType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CodeReviewType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CodeReviewType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CodeReviewType)
