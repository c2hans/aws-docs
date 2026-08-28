---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-deploy-test-fork-pipelines-sample-application.html
---

# Deploying and testing the Amazon SNS event fork pipelines sample application
<a name="sns-deploy-test-fork-pipelines-sample-application"></a>

To accelerate the development of your event-driven applications, you can subscribe event-handling pipelines—powered by AWS Event Fork Pipelines—to Amazon SNS topics. AWS Event Fork Pipelines is a suite of open-source [nested applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html), based on the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) (AWS SAM), which you can deploy directly from the [AWS Event Fork Pipelines suite](https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines) (choose **Show apps that create custom IAM roles or resource policies**) into your AWS account. For more information, see [How AWS Event Fork Pipelines works](sns-fork-pipeline-as-subscriber.md#how-sns-fork-works).

This page shows how you can use the AWS Management Console to deploy and test the AWS Event Fork Pipelines sample application.

**Important**
To avoid incurring unwanted costs after you finish deploying the AWS Event Fork Pipelines sample application, delete its CloudFormation stack. For more information, see [Deleting a Stack on the CloudFormation Console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) in the *AWS CloudFormation User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
