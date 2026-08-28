---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-shut-down.html
---

# Shut down models
<a name="canvas-fm-chat-shut-down"></a>

We highly recommend that you shut down models that you aren’t using. The models automatically shut down after 2 hours of inactivity. However, to manually shut down a model, you can do the following:

1. On the **Generate, extract and summarize content** page, open the chat for the model that you want to shut down.

1. On the chat page, choose the **More options** icon (![Vertical ellipsis icon representing a menu or more options.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)).

1. Choose **Shut down model**.

1. In the **Shut down model** confirmation box, choose **Shut down**.

The model begins shutting down. If your chat compares two or more models, you can shut down an individual model from the chat page by choosing the model’s **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)) and then choosing **Shut down model**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
