---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/smtj-iterative-training.html
---

# Iterative training
<a name="smtj-iterative-training"></a>

Iterative training is a systematic approach to fine-tuning models through multiple training cycles, where each round builds on the previous checkpoint by addressing specific weaknesses discovered through evaluation. This method enables targeted improvements to model performance by incorporating curated examples that address failure modes, adapting to changing requirements, and validating enhancements incrementally rather than committing to a single long training run. The process typically follows patterns like SFT (Supervised Fine-Tuning) followed by RFT (Reward-based Fine-Tuning), with checkpoints stored in AWS-managed escrow S3 buckets that can be referenced for subsequent training iterations while maintaining consistency in model type and training technique throughout the pipeline.

For more details, refer to [Iterative Training](nova-iterative-training.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
