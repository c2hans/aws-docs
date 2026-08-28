---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-github-personal-access-token-expired.html
---

# Problem: GitHub personal access token expired
<a name="problem-github-personal-access-token-expired"></a>

The solution uses a GitHub personal access token to access the Landing Zone Accelerator on AWS code repository. If you have set an expiration date on the access token, the token’s privilege is revoked when it expires. You will see an error when trying to run the **Source** stage and action of the [Installer](deployment-pipelines.md#awsaccelerator-installerstack) or [Core](deployment-pipelines.md#awsaccelerator-pipelinestack) pipeline. For example:

 `Could not access the GitHub repository: "landing-zone-accelerator-on-aws". The access token might be invalid or has been revoked. Edit the pipeline to reconnect with GitHub.`

## Resolution
<a name="resolution-7"></a>

## Option 1 (releases as of version 1.3.1): Use the Landing Zone Accelerator automated GitHub token update functionality
<a name="option-1-releases-as-of-version-1.3.1-use-the-landing-zone-accelerator-automated-github-token-update-functionality"></a>

1.  [Create a new GitHub personal access token](prerequisites.md#create-a-github-personal-access-token-and-store-in-secrets-manager) and update the secret value in AWS Secrets Manager.
**Note**
Saving the updated value in Secrets Manager will invoke the `UpdatePipelineGithubToken` Lambda function, which automates the process of updating the GitHub Personal Access Token in CodePipeline.

1. Retry the failed **Source** stage of the affected pipeline.

## Option 2 : (releases before version 1.3.1): Update access token in AWS CodePipeline
<a name="option-2-releases-before-version-1.3.1-update-access-token-in-aws-codepipeline"></a>

1. Create a new GitHub personal access token and update the pipeline structure with the new token. For step-by-step instructions, see [Configure authentication](https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html#action-reference-GitHub) (Github version 1 source actions) in the *AWS CodePipeline User Guide*.

1. Retry the failed **Source** stage of the affected pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
