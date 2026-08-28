---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewSummary.html
---

# CodeReviewSummary
<a name="API_CodeReviewSummary"></a>

Information about the summary of the code review.

## Contents
<a name="API_CodeReviewSummary_Contents"></a>

 ** CodeReviewArn **   <a name="reviewer-Type-CodeReviewSummary-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: No

 ** CreatedTimeStamp **   <a name="reviewer-Type-CodeReviewSummary-CreatedTimeStamp"></a>
The time, in milliseconds since the epoch, when the code review was created.
Type: Timestamp
Required: No

 ** LastUpdatedTimeStamp **   <a name="reviewer-Type-CodeReviewSummary-LastUpdatedTimeStamp"></a>
The time, in milliseconds since the epoch, when the code review was last updated.
Type: Timestamp
Required: No

 ** MetricsSummary **   <a name="reviewer-Type-CodeReviewSummary-MetricsSummary"></a>
The statistics from the code review.
Type: [MetricsSummary](API_MetricsSummary.md) object
Required: No

 ** Name **   <a name="reviewer-Type-CodeReviewSummary-Name"></a>
The name of the code review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** Owner **   <a name="reviewer-Type-CodeReviewSummary-Owner"></a>
The owner of the repository. For an AWS CodeCommit repository, this is the AWS account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** ProviderType **   <a name="reviewer-Type-CodeReviewSummary-ProviderType"></a>
The provider type of the repository association.
Type: String
Valid Values: `CodeCommit | GitHub | Bitbucket | GitHubEnterpriseServer | S3Bucket`
Required: No

 ** PullRequestId **   <a name="reviewer-Type-CodeReviewSummary-PullRequestId"></a>
The pull request ID for the code review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S+`
Required: No

 ** RepositoryName **   <a name="reviewer-Type-CodeReviewSummary-RepositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** SourceCodeType **   <a name="reviewer-Type-CodeReviewSummary-SourceCodeType"></a>
Specifies the source code that is analyzed in a code review.
Type: [SourceCodeType](API_SourceCodeType.md) object
Required: No

 ** State **   <a name="reviewer-Type-CodeReviewSummary-State"></a>
The state of the code review.
The valid code review states are:
+  `Completed`: The code review is complete.
+  `Pending`: The code review started and has not completed or failed.
+  `Failed`: The code review failed.
+  `Deleting`: The code review is being deleted.
Type: String
Valid Values: `Completed | Pending | Failed | Deleting`
Required: No

 ** Type **   <a name="reviewer-Type-CodeReviewSummary-Type"></a>
The type of the code review.
Type: String
Valid Values: `PullRequest | RepositoryAnalysis`
Required: No

## See Also
<a name="API_CodeReviewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CodeReviewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CodeReviewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CodeReviewSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
