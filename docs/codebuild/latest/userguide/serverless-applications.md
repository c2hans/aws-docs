---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/serverless-applications.html
---

# Use AWS CodeBuild with serverless applications
<a name="serverless-applications"></a>

The AWS Serverless Application Model (AWS SAM) is an open-source framework for building serverless applications. For more information, see the [AWS serverless application model](https://github.com/awslabs/serverless-application-model) repository on GitHub.

You can use AWS CodeBuild to package and deploy serverless applications that follow the AWS SAM standard. For the deployment step, CodeBuild can use AWS CloudFormation. To automate the building and deployment of serverless applications with CodeBuild and CloudFormation, you can use AWS CodePipeline.

For more information, see [Deploying Serverless Applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying.html) in the *AWS Serverless Application Model Developer Guide*.

## Related resources
<a name="acb-more-info"></a>
+ For information about getting started with AWS CodeBuild, see [Getting started with AWS CodeBuild using the console](getting-started-overview.md#getting-started).
+ For information about troubleshooting issues in CodeBuild, see [Troubleshooting AWS CodeBuild](troubleshooting.md).
+ For information about quotas in CodeBuild, see [Quotas for AWS CodeBuild](limits.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
