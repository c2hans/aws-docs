---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam-resources-console.html
---

# Viewing resources in the console
<a name="security-iam-resources-console"></a>

The console requires the `ListRepositories` permission to display a list of repositories for your AWS account in the AWS Region where you are signed in. The console also includes a **Go to resource** function to quickly perform a case insensitive search for resources. This search is performed in your AWS account in the AWS Region where you are signed in. The following resources are displayed across the following services:
+ AWS CodeBuild: Build projects
+ AWS CodeCommit: Repositories
+ AWS CodeDeploy: Applications
+ AWS CodePipeline: Pipelines

To perform this search across resources in all services, you must have the following permissions:
+ AWS CodeBuild: `ListProjects`
+ CodeCommit: `ListRepositories`
+ CodeDeploy: `ListApplications`
+ CodePipeline: `ListPipelines`

Results are not returned for a service's resources if you do not have permissions for that service. Even if you have permissions for viewing resources, some resources are not returned if there is an explicit `Deny` to view those resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
