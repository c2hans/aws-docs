---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-notebook.html
---

# Create a Notebook Instance
<a name="automatic-model-tuning-ex-notebook"></a>

**Important**
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

Create a Jupyter notebook that contains a pre-installed environment with the default Anaconda installation and Python3.

**To create a Jupyter notebook**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Open a running notebook instance, by choosing **Open** next to its name. The Jupyter notebook server page appears:

![Example Jupyter notebook server page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/notebook-dashboard.png)

1. To create a notebook, choose **Files**, **New**, and **conda\_python3**. .

1. Name the notebook.

## Next Step
<a name="automatic-model-tuning-ex-next-client"></a>

[Get the Amazon SageMaker AI Boto 3 Client](automatic-model-tuning-ex-client.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
