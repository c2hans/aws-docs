---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/monitoring-your-savings.html
---

# Monitoring your savings
<a name="monitoring-your-savings"></a>

## Monitoring Your Savings
<a name="monitoring-your-savings.8598d3c7-0f26-5eae-bac3-efcf84bac9ca"></a>

Optimization without measurement is guesswork — track utilization and node count trends over time to confirm your changes are delivering real cost reduction and to catch regressions early.

**Create a Cost Dashboard**

To set up a CloudWatch dashboard to track cluster efficiency (node utilization and node count over time), see this [create-cost-dashboard.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/create-cost-dashboard.sh).

**Weekly Cost Review Script**

Run a weekly report covering cluster version, node utilization, Spot/Graviton distribution, top consumers, pending pods, and orphaned volumes. Refer to [weekly-cost-review.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/weekly-cost-review.sh).

**CloudWatch: Monitor Karpenter Savings**

Use CloudWatch and Cost Explorer to validate that Karpenter's decisions translate into actual spend reduction — Spot adoption, instance right-selection, and consolidation should all be visible in your billing data. Refer to [monitor-karpenter-savings.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/monitor-karpenter-savings.sh).
