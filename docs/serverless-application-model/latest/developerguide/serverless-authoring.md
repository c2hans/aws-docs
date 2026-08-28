---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-authoring.html
---

# Define your infrastructure with AWS SAM
<a name="serverless-authoring"></a>

Now that you have created your project, you are ready to define your application infrastructure with AWS SAM. Do this by configuring your AWS SAM template to define your application's resources and properties, which is the `template.yaml` file in your AWS SAM project.

The topics in this section provide content on defining your infrastructure in your AWS SAM template (your `template.yaml` file). It also contains topics on defining resources for specific use cases, such as working with Lambda layers, using nested applications, controlling access to API Gateway APIs, orchestrating AWS resources with Step Functions, code signing your applications, and validating your AWS SAM template.

**Topics**
+ [Define application resources in your AWS SAM template](authoring-define-resources.md)
+ [Set up and manage resource access in your AWS SAM template](sam-permissions.md)
+ [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md)
+ [Increase efficiency using Lambda layers with AWS SAM](serverless-sam-cli-layers.md)
+ [Reuse code and resources using nested applications in AWS SAM](serverless-sam-template-nested-applications.md)
+ [Manage time-based events with EventBridge Scheduler in AWS SAM](using-eventbridge-scheduler.md)
+ [Orchestrating AWS SAM resources with AWS Step Functions](serverless-step-functions-in-sam.md)
+ [Set up code signing for your AWS SAM application](authoring-codesigning.md)
+ [Validate AWS SAM template files](serverless-sam-cli-using-validate.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
