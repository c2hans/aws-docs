---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/6-1-separate-node-pools-by-application-usage.html
---

# Workload tiered Nodepools: Right capacity for the right workload
<a name="6-1-separate-node-pools-by-application-usage"></a>

Isolate workloads into dedicated NodePools based on their characteristics — this prevents low-priority batch jobs from blocking expensive on-demand capacity meant for production, and allows tailored cost strategies per workload type.

## Actions
<a name="actions"></a>

Create separate NodePools based on workload criticality to manage disruption and keep blocking nodes isolated from other workloads. The sample manifest provides three NodePool configurations:
+ **critical-workloads** — On-Demand, Graviton, with time-based disruption budgets (conservative during business hours, zero during peak, aggressive on weekends)
+ **non-pdb-workloads** — Spot-first for stateless workloads with 50% disruption tolerance
+ **gpu-workloads** — On-Demand GPU instances with `WhenEmpty` consolidation and `nvidia.com/gpu` taint

For complete NodePool manifests, see the [workload-tiered-nodepools.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/workload-tiered-nodepools.yaml) and to validate workloads are landing on the correct pool see this [verify-nodepool-placement.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-nodepool-placement.sh)

**Key takeaway: **Map your workloads into the correct nodepool based on workload requirements. You can also create nodepools based on tiers (production, staging, batch, dev). This will help to explore Spot savings options for non-production workload as well. For the complete scripts and manifests, see the [04-karpenter-cost-optimization](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/04-karpenter-cost-optimization) folder in the code repository.
