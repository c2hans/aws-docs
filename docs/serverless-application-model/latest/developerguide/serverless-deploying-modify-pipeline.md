---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying-modify-pipeline.html
---

# Automate the deployment of your AWS SAM application
<a name="serverless-deploying-modify-pipeline"></a>

In AWS SAM, how you automate the deployment of your AWS SAM application varies depending on the CI/CD system you are using. For this reason, the examples in this section show you how to configure various CI/CD systems to automate building serverless applications in an AWS SAM build container image. These build container images make it easier to build and package serverless applications using the AWS SAM CLI.

The procedures for your existing CI/CD pipeline to deploy serverless applications using AWS SAM are slightly different depending on which CI/CD system you are using.

The following topics provide examples for configuring your CI/CD system to build serverless applications within an AWS SAM build container image:

**Topics**
+ [Using AWS CodePipeline to deploy with AWS SAM](deploying-using-codepipeline.md)
+ [Using Bitbucket Pipelines to deploying with AWS SAM](deploying-using-bitbucket.md)
+ [Using Jenkins to deploy with AWS SAM](deploying-using-jenkins.md)
+ [Using GitLab CI/CD to deploy with AWS SAM](deploying-using-gitlab.md)
+ [Using GitHub Actions to deploy with AWS SAM](deploying-using-github.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
