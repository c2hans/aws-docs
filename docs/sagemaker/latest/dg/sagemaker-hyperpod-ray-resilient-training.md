---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-resilient-training.html
---

# Resilient training
<a name="sagemaker-hyperpod-ray-resilient-training"></a>

HyperPod resiliency runs beneath your Ray workloads. Health checks detect faulty nodes and recover them, host-level detection catches silent stalls, and tiered checkpointing shortens recovery after a failure. These capabilities apply to Ray without changes to your Ray code.

**Topics**
+ [Automatic node recovery with Ray](sagemaker-hyperpod-ray-node-recovery.md)
+ [Tiered checkpointing](sagemaker-hyperpod-ray-tiered-storage.md)
+ [Hung job detection](sagemaker-hyperpod-ray-hung-job-detection.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
