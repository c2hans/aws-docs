---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/continuous-delivery.html
---

# Continuous delivery
<a name="continuous-delivery"></a>

Continuous delivery (CD) is a software development practice where code changes are automatically prepared for a release to production. A pillar of modern application development, continuous delivery expands upon continuous integration by deploying all code changes to a testing environment and/or a production environment after the build stage. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process.

Continuous delivery lets developers automate testing beyond just unit tests so they can verify application updates across multiple dimensions before deploying to customers.

These tests might include UI testing, load testing, integration testing, API reliability testing, and more. This helps developers more thoroughly validate updates and preemptively discover issues. Using the cloud, it is easy and cost-effective to automate the creation and replication of multiple environments for testing, which was previously difficult to do on-premises.

AWS offers the following services for continuous delivery:
+ [AWS CodeBuild](aws-codebuild.md)
+ [AWS CodeDeploy](aws-codedeploy.md)
+ [AWS CodePipeline](aws-codepipeline.md)

**Topics**
+ [AWS CodeDeploy](aws-codedeploy.md)
+ [AWS CodePipeline](aws-codepipeline.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
