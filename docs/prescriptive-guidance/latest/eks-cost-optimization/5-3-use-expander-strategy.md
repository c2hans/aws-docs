---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/5-3-use-expander-strategy.html
---

# Use expander strategy
<a name="5-3-use-expander-strategy"></a>

The expander determines how Cluster Autoscaler chooses which node group to scale up when multiple options can fit pending pods — the wrong strategy leads to consistently picking expensive or oversized instances.

|
|
| Expander | Behavior | Best For |
| --- |--- |--- |
| `least-waste` | Chooses group that will have least idle CPU/memory after scheduling | **Cost optimization** (recommended) |
| `most-pods` | Chooses group that can schedule the most pending pods | Batch processing |
| `priority` | Uses user-defined priority list | Graviton-first, then x86 fallback |
| `random` | Random selection (default in some versions) | Not recommended for cost optimization |

For the deployment manifest with `least-waste` expander and a priority-based ConfigMap for Graviton-first strategy [expander-strategy.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/expander-strategy.yaml)

## Check expander
<a name="check-expander"></a>

Verify which expander is active and confirm scale-up decisions match your priority configuration. For the verification commands, see the [verify-expander-strategy.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-expander-strategy.sh)

For the complete scripts and manifests, see the [4-karpenter-cost-optimization](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/04-karpenter-cost-optimization) folder in the code repository.

## Actions
<a name="actions"></a>

Switch from the default `random` expander to `least-waste` for general cost optimization, or `priority` if you have mixed Spot/On-Demand/Graviton node groups and want explicit control over which scales first. Never use `random` in production — it ignores cost entirely.

**Key takeaway: **The expander strategy is a one-line change that determines whether every scale-up event picks the cheapest option or an arbitrary one. `least-waste` alone can reduce per-scale-up cost by 20–30% by avoiding oversized instances.
