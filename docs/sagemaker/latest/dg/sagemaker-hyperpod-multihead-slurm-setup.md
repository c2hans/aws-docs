---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-multihead-slurm-setup.html
---

# Setting up multiple controller nodes for a SageMaker HyperPod Slurm cluster
<a name="sagemaker-hyperpod-multihead-slurm-setup"></a>

This topic explains how to configure multiple controller (head) nodes in a SageMaker HyperPod Slurm cluster using lifecycle scripts. Before you start, review the prerequisites listed in [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md) and familiarize yourself with the lifecycle scripts in [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md). The instructions in this topic use AWS CLI commands in Amazon Linux environment. Note that the environment variables used in these commands are available in the current session unless explicitly preserved.

**Topics**
+ [Provisioning resources using CloudFormation stacks](sagemaker-hyperpod-multihead-slurm-cfn.md)
+ [Creating and attaching an IAM policy](sagemaker-hyperpod-multihead-slurm-iam.md)
+ [Preparing and uploading lifecycle scripts](sagemaker-hyperpod-multihead-slurm-scripts.md)
+ [Creating a SageMaker HyperPod cluster](sagemaker-hyperpod-multihead-slurm-create.md)
+ [Considering important notes](sagemaker-hyperpod-multihead-slurm-notes.md)
+ [Reviewing environment variables reference](sagemaker-hyperpod-multihead-slurm-variables-reference.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
