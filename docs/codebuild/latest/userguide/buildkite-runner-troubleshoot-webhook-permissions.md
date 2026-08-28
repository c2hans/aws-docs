---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner-troubleshoot-webhook-permissions.html
---

# Troubleshoot the webhook permission issues
<a name="buildkite-runner-troubleshoot-webhook-permissions"></a>

 **Issue: **

The Buildkite job fails to checkout the job's source repository due to permission issues.

 **Possible causes: **
+ CodeBuild does not have sufficient permissions to checkout the job's source repository.
+ The pipeline's repository settings are set to check out using SSH for CodeBuild managed credentials.

 **Recommended solutions: **
+ Verify that CodeBuild has sufficient permissions configured to check out the job's source repository. Additionally, verify that your CodeBuild project's service role has sufficient permissions to access the configured source permission option.
+ Verify that your Buildkite pipeline is configured to use checkout using HTTPS if you are using CodeBuild managed source repository credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
