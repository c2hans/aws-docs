---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/library-management-best-practices.html
---

# Enforce library version management
<a name="library-management-best-practices"></a>

Lifecycle management is a significant challenge when you're maintaining AWS CDK code bases. For example, assume that you start an AWS CDK project with version 1.97 and then version 1.169 becomes available later on. Version 1.169 offers new features and bug fixes, but you have deployed your infrastructure by using the old version. Now, updating the constructs becomes challenging as this gap increases because of the breaking changes that could be introduced in new versions. This can be a challenge if you have many resources in your environment. The pattern introduced in this section can help you manage your AWS CDK library version using automation. Here's the workflow of this pattern:

1. When you launch a new AWS Service Catalog product, the AWS CDK library versions and its dependencies are stored in the `package.json` file.

1. You deploy a common pipeline that keeps track of all the repositories so that you can apply automatic upgrades to them if there are no breaking changes.

1. An AWS CodeBuild stage checks for the dependency tree and looks for the breaking changes.

1. The pipeline creates a feature branch and then runs `cdk synth` with the new version to confirm there are no errors.

1. The new version is deployed in the test environment and finally runs an integration test to make sure the deployment is healthy.

1. You can use two Amazon Simple Queue Service (Amazon SQS) queues to keep track of the stacks. Users can review the stacks manually in the exception queue and address breaking changes. Items that pass the integration test are allowed to be merged and released.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
