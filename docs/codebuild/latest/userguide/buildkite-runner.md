---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner.html
---

# Self-managed Buildkite runner in AWS CodeBuild
<a name="buildkite-runner"></a>

You can configure your project to set up self-hosted Buildkite runners in CodeBuild containers to process your Buildkite jobs. This can be done by setting up a webhook using your CodeBuild project, and updating your Buildkite pipeline YAML steps to use self-hosted runners hosted on CodeBuild machines.

The high-level steps to configure a CodeBuild project to run Buildkite jobs are as follows:
+ Navigate to the CodeBuild console and create a CodeBuild project with the Buildkite runner project runner type configuration
+ Add a `job.scheduled` webhook to your Buildkite organization.
+ Update your Buildkite pipeline YAML steps in Buildkite to configure your build environment.

For a more detailed procedure, see [Tutorial: Configure a CodeBuild-hosted Buildkite runner](sample-runner-buildkite.md). This feature allows your Buildkite jobs to get native integration with AWS, which provides security and convenience through features like IAM, AWS Secrets Manager, AWS CloudTrail, and Amazon VPC. You can access the latest instance types, including ARM-based instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
