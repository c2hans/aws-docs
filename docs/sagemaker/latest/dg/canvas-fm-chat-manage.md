---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-manage.html
---

# Start up models
<a name="canvas-fm-chat-manage"></a>

**Note**
The following section describe starting up models, which only applies to the JumpStart foundation models, such as Falcon-40B-Instruct. You can access Amazon Bedrock models, such as Amazon Titan, instantly at any time.

You can start up as many JumpStart models as you like. Each active JumpStart model incurs charges on your account, so we recommend that you don’t start up more models than you are currently using.

To start up another model, you can do the following:

1. On the **Generate, extract and summarize content** page, choose **New chat**.

1. Choose the model from the dropdown menu. If you want to choose a model not displayed in the dropdown, choose **Start up another model**, and then select the model that you want to start up.

1. Choose **Start up model**.

The model should begin starting up, and within a few minutes you can chat with the model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
