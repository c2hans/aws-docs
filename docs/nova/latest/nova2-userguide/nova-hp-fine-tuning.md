---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-fine-tuning.html
---

# Fine-tuning for Amazon Nova models
<a name="nova-hp-fine-tuning"></a>

Fine-tuning Amazon Nova models on SageMaker HyperPod supports Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT). Each technique serves different customization needs and can be applied to different Amazon Nova model versions. SageMaker HyperPod additionally supports [Pre-training for Amazon Nova models](nova-hp-training.md) for domain-specific knowledge acquisition.

**Topics**
+ [Supervised fine-tuning (SFT) on Nova 2.0 on SageMaker HyperPod](nova-sft-2-smhp.md)
+ [Reinforcement fine-tuning (RFT) on Nova 2.0 on SageMaker HyperPod](nova-hp-rft-nova2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
