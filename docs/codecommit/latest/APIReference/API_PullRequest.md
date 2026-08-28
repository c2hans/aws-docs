---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PullRequest.html
---

# PullRequest
<a name="API_PullRequest"></a>

Returns information about a pull request.

## Contents
<a name="API_PullRequest_Contents"></a>

 ** approvalRules **   <a name="CodeCommit-Type-PullRequest-approvalRules"></a>
The approval rules applied to the pull request.
Type: Array of [ApprovalRule](API_ApprovalRule.md) objects
Required: No

 ** authorArn **   <a name="CodeCommit-Type-PullRequest-authorArn"></a>
The Amazon Resource Name (ARN) of the user who created the pull request.
Type: String
Required: No

 ** clientRequestToken **   <a name="CodeCommit-Type-PullRequest-clientRequestToken"></a>
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.
Type: String
Required: No

 ** creationDate **   <a name="CodeCommit-Type-PullRequest-creationDate"></a>
The date and time the pull request was originally created, in timestamp format.
Type: Timestamp
Required: No

 ** description **   <a name="CodeCommit-Type-PullRequest-description"></a>
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** lastActivityDate **   <a name="CodeCommit-Type-PullRequest-lastActivityDate"></a>
The day and time of the last user or system activity on the pull request, in timestamp format.
Type: Timestamp
Required: No

 ** pullRequestId **   <a name="CodeCommit-Type-PullRequest-pullRequestId"></a>
The system-generated ID of the pull request.
Type: String
Required: No

 ** pullRequestStatus **   <a name="CodeCommit-Type-PullRequest-pullRequestStatus"></a>
The status of the pull request. Pull request status can only change from `OPEN` to `CLOSED`.
Type: String
Valid Values: `OPEN | CLOSED`
Required: No

 ** pullRequestTargets **   <a name="CodeCommit-Type-PullRequest-pullRequestTargets"></a>
The targets of the pull request, including the source branch and destination branch for the pull request.
Type: Array of [PullRequestTarget](API_PullRequestTarget.md) objects
Required: No

 ** revisionId **   <a name="CodeCommit-Type-PullRequest-revisionId"></a>
The system-generated revision ID for the pull request.
Type: String
Required: No

 ** title **   <a name="CodeCommit-Type-PullRequest-title"></a>
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.
Type: String
Length Constraints: Maximum length of 150.
Required: No

## See Also
<a name="API_PullRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PullRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PullRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PullRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
