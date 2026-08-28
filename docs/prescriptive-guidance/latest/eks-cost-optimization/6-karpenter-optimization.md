---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/6-karpenter-optimization.html
---

# Karpenter cost optimization
<a name="6-karpenter-optimization"></a>

Karpenter is the most powerful tool for EKS compute cost optimization. It replaces Cluster Autoscaler with faster, smarter provisioning that directly reduces costs through better instance selection, better consolidation, and Spot-aware scheduling. The sections below cover how to configure Karpenter for maximum savings.

For teams that prefer a fully managed alternative with less control, [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) is also available. However **Karpenter is the recommended approach,** for organizations that want full control over cost optimization, workload isolation, and scaling behavior.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
