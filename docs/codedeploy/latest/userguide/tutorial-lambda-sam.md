---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam.html
---

# Tutorial: Deploy an updated Lambda function with CodeDeploy and the AWS Serverless Application Model
<a name="tutorial-lambda-sam"></a>

AWS SAM is an open-source framework for building serverless applications. It transforms and expands YAML syntax in a AWS SAM template into CloudFormation syntax to build serverless applications, such as a Lambda function. For more information, see [What is the AWS Serverless Application Model?](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

 In this tutorial, you use AWS SAM to create a solution that does the following:
+  Creates your Lambda function.
+  Creates your CodeDeploy application and deployment group.
+  Creates two Lambda functions that execute deployment validation tests during CodeDeploy lifecycle hooks.
+  Detects when your Lambda function is updated. The updating of the Lambda function triggers a deployment by CodeDeploy that incrementally shifts production traffic from the original version of your Lambda function to the updated version.

**Note**
This tutorial requires you to create resources that might result in charges to your AWS account. These include possible charges for CodeDeploy, Amazon CloudWatch, and AWS Lambda. For more information, see [CodeDeploy pricing](https://aws.amazon.com/codedeploy/pricing/), [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/), and [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

**Topics**
+ [Prerequisites](tutorial-lambda-sam-prereqs.md)
+ [Step 1: Set up your infrastructure](tutorial-lambda-sam-setup-infrastructure.md)
+ [Step 2: Update the Lambda function](tutorial-lambda-sam-update-function.md)
+ [Step 3: Deploy the updated Lambda function](tutorial-lambda-sam-deploy-update.md)
+ [Step 4: View your deployment results](tutorial-lambda-sam-deploy-view-results.md)
+ [Step 5: Clean up](tutorial-lambda-clean-up.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
