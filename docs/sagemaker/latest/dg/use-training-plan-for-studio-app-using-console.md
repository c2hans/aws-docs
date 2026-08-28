---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-studio-app-using-console.html
---

# Create or update a Studio app with a training plan in the Studio UI
<a name="use-training-plan-for-studio-app-using-console"></a>

To create a Studio app using training plans from the Studio UI, follow these steps:

1. Open Studio. For information about opening Studio, see [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **JupyterLab** or **Code Editor**.

1. Create a new space or open an existing space. For more information, see [Create a space](studio-updated-jl-user-guide-create-space.md) for JupyterLab or [Launch a Code Editor application in Studio](code-editor-use-studio.md) for Code Editor application in Studio.

1. From the **Instance** dropdown list, navigate to **Available Training Plans** and choose a training plan that aligns with your compute capacity needs.

1. Choose **Run space** to launch the app on the training plan capacity.

![Studio UI showing the Instance dropdown list with Available Training Plans section for selecting a training plan when configuring a JupyterLab space.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/training-plans/tp-create-studio-app.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
