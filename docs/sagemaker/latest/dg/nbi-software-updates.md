---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-software-updates.html
---

# Notebook Instance Software Updates
<a name="nbi-software-updates"></a>

Amazon SageMaker AI periodically tests and releases software that is installed on notebook instances. This includes:
+ Kernel updates
+ Security patches
+ AWS SDK updates
+ [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable) updates
+ Open source software updates

To ensure that you have the most recent software updates, stop and restart your notebook instance, either in the SageMaker AI console or by calling [  `StopNotebookInstance`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopNotebookInstance.html).

You can also manually update software installed on your notebook instance while it is running by using update commands in a terminal or in a notebook.

**Note**
Updating kernels and some packages might depend on whether root access is enabled for the notebook instance. For more information, see [Control root access to a SageMaker notebook instance](nbi-root-access.md).

You can check the [Personal Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/) or the security bulletin at [Security Bulletins](https://aws.amazon.com/security/security-bulletins/) for updates.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
