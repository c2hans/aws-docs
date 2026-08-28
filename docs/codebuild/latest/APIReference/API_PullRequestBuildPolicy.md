---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PullRequestBuildPolicy.html
---

# PullRequestBuildPolicy
<a name="API_PullRequestBuildPolicy"></a>

A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.

## Contents
<a name="API_PullRequestBuildPolicy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** requiresCommentApproval **   <a name="CodeBuild-Type-PullRequestBuildPolicy-requiresCommentApproval"></a>
Specifies when comment-based approval is required before triggering a build on pull requests. This setting determines whether builds run automatically or require explicit approval through comments.
+  *DISABLED*: Builds trigger automatically without requiring comment approval
+  *ALL\_PULL\_REQUESTS*: All pull requests require comment approval before builds execute (unless contributor is one of the approver roles)
+  *FORK\_PULL\_REQUESTS*: Only pull requests from forked repositories require comment approval (unless contributor is one of the approver roles)
Type: String
Valid Values: `DISABLED | ALL_PULL_REQUESTS | FORK_PULL_REQUESTS`
Required: Yes

 ** approverRoles **   <a name="CodeBuild-Type-PullRequestBuildPolicy-approverRoles"></a>
List of repository roles that have approval privileges for pull request builds when comment approval is required. Only users with these roles can provide valid comment approvals. If a pull request contributor is one of these roles, their pull request builds will trigger automatically. This field is only applicable when `requiresCommentApproval` is not *DISABLED*.
Type: Array of strings
Valid Values: `GITHUB_READ | GITHUB_TRIAGE | GITHUB_WRITE | GITHUB_MAINTAIN | GITHUB_ADMIN | GITLAB_GUEST | GITLAB_PLANNER | GITLAB_REPORTER | GITLAB_DEVELOPER | GITLAB_MAINTAINER | GITLAB_OWNER | BITBUCKET_READ | BITBUCKET_WRITE | BITBUCKET_ADMIN`
Required: No

## See Also
<a name="API_PullRequestBuildPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/PullRequestBuildPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/PullRequestBuildPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/PullRequestBuildPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
