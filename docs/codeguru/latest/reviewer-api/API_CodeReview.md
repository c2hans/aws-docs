---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html
---

# CodeReview
<a name="API_CodeReview"></a>

Information about a code review. A code review belongs to the associated repository that contains the reviewed code.

## Contents
<a name="API_CodeReview_Contents"></a>

 ** AnalysisTypes **   <a name="reviewer-Type-CodeReview-AnalysisTypes"></a>
The types of analysis performed during a repository analysis or a pull request review. You can specify either `Security`, `CodeQuality`, or both.
Type: Array of strings
Valid Values: `Security | CodeQuality`
Required: No

 ** AssociationArn **   <a name="reviewer-Type-CodeReview-AssociationArn"></a>
The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) that contains the reviewed source code. You can retrieve associated repository ARNs by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:association:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** CodeReviewArn **   <a name="reviewer-Type-CodeReview-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: No

 ** ConfigFileState **   <a name="reviewer-Type-CodeReview-ConfigFileState"></a>
The state of the `aws-codeguru-reviewer.yml` configuration file that allows the configuration of the CodeGuru Reviewer analysis. The file either exists, doesn't exist, or exists with errors at the root directory of your repository.
Type: String
Valid Values: `Present | Absent | PresentWithErrors`
Required: No

 ** CreatedTimeStamp **   <a name="reviewer-Type-CodeReview-CreatedTimeStamp"></a>
The time, in milliseconds since the epoch, when the code review was created.
Type: Timestamp
Required: No

 ** LastUpdatedTimeStamp **   <a name="reviewer-Type-CodeReview-LastUpdatedTimeStamp"></a>
The time, in milliseconds since the epoch, when the code review was last updated.
Type: Timestamp
Required: No

 ** Metrics **   <a name="reviewer-Type-CodeReview-Metrics"></a>
The statistics from the code review.
Type: [Metrics](API_Metrics.md) object
Required: No

 ** Name **   <a name="reviewer-Type-CodeReview-Name"></a>
The name of the code review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** Owner **   <a name="reviewer-Type-CodeReview-Owner"></a>
The owner of the repository. For an AWS CodeCommit repository, this is the AWS account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** ProviderType **   <a name="reviewer-Type-CodeReview-ProviderType"></a>
The type of repository that contains the reviewed code (for example, GitHub or Bitbucket).
Type: String
Valid Values: `CodeCommit | GitHub | Bitbucket | GitHubEnterpriseServer | S3Bucket`
Required: No

 ** PullRequestId **   <a name="reviewer-Type-CodeReview-PullRequestId"></a>
The pull request ID for the code review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\S+`
Required: No

 ** RepositoryName **   <a name="reviewer-Type-CodeReview-RepositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** SourceCodeType **   <a name="reviewer-Type-CodeReview-SourceCodeType"></a>
The type of the source code for the code review.
Type: [SourceCodeType](API_SourceCodeType.md) object
Required: No

 ** State **   <a name="reviewer-Type-CodeReview-State"></a>
The valid code review states are:
+  `Completed`: The code review is complete.
+  `Pending`: The code review started and has not completed or failed.
+  `Failed`: The code review failed.
+  `Deleting`: The code review is being deleted.
Type: String
Valid Values: `Completed | Pending | Failed | Deleting`
Required: No

 ** StateReason **   <a name="reviewer-Type-CodeReview-StateReason"></a>
The reason for the state of the code review.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** Type **   <a name="reviewer-Type-CodeReview-Type"></a>
The type of code review.
Type: String
Valid Values: `PullRequest | RepositoryAnalysis`
Required: No

## See Also
<a name="API_CodeReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CodeReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CodeReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CodeReview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
