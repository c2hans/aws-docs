---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/customizing-models-training-types.html
---

# Training types
<a name="customizing-models-training-types"></a>

Training types determine how model weights are updated during customization. Every [customization technique](customizing-models-techniques.md) (SFT, DPO, RFT) can be combined with either training type. Choose based on your quality requirements, compute budget, and use case.

[LoRA](customizing-models-lora.md) — Low-Rank Adaptation
Trains a small set of adapter weights. Lower cost, faster training. Required for [continuous customization](customizing-models-continuous.md).

[FFT](customizing-models-fft.md) — Full Fine-Tuning
Updates all model weights. Higher compute, deeper customization. Best for large domain shifts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
