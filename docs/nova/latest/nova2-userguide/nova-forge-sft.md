---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-sft.html
---

# Supervised Fine-Tuning
<a name="nova-forge-sft"></a>

Amazon Nova Forge data mixing allows you to combine your custom training data with Amazon Nova's proprietary training data during supervised fine-tuning (SFT). This helps preserve the model's general capabilities while specializing it for your target domain. Data mixing is available on two platforms:
+ **SageMaker HyperPod** – Use YAML recipe files to configure data mixing with both text and multimodal data. Supports LoRA and full-rank SFT.
+ **SageMaker Training Jobs** – Use the serverless `CreateTrainingJob` API with `ServerlessJobConfig` for text-only SFT with data mixing. Supports LoRA and full-rank.

**Topics**
+ [Data mixing on SageMaker HyperPod](nova-forge-sft-datamix-smhp.md)
+ [Data mixing on SageMaker Training Jobs](nova-forge-sft-datamix-smtj.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
