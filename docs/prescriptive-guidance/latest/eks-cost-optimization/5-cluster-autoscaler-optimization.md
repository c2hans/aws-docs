---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/5-cluster-autoscaler-optimization.html
---

# Cluster Autoscaler optimization
<a name="5-cluster-autoscaler-optimization"></a>

For clusters still running Cluster Autoscaler, the default configuration prioritizes safety over cost. Tuning these parameters controls how quickly underutilized nodes are reclaimed and how efficiently new capacity is provisioned.

**Cost-Optimized Cluster Autoscaler Configuration**

The key tuning changes vs defaults:
+ `scale-down-delay-after-add`: 5m (default 10m): faster reclaim after scale-up
+ `scale-down-unneeded-time`: 5m (default 10m): detect idle nodes sooner
+ `scale-down-utilization-threshold`: 0.5: scale down if node is <50% utilized
+ `expander`: least-waste: choose node group with best bin-packing fit
+ `balance-similar-node-groups`: true: spread across AZs for Spot availability

For the complete deployment manifest,see the [cluster-autoscaler-cost-optimized.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/cluster-autoscaler-cost-optimized.yaml)

## Verify autoscaler behavior
<a name="problem"></a>

Confirm that scale-down is actually happening, misconfigured flags or pod disruption budgets can silently block node removal. The verification script checks:
+ Autoscaler status ConfigMap for current decisions
+ Nodes with `scale-down-disabled` label (blocked from removal)
+ Pending pods that may be triggering unnecessary scale-up
+ Node utilization levels (nodes below 50% should be consolidated)
+ CloudWatch node count trend (flat count despite variable traffic = paying for unused capacity)

For the verification commands, see the [verify-autoscaler-behavior.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-autoscaler-behavior.sh)

For the complete scripts and manifests, see the [04-karpenter-cost-optimization](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/04-karpenter-cost-optimization) folder in the code repository.

## Actions
<a name="actions"></a>

Set `scale-down-utilization-threshold` to 0.5, `scale-down-unneeded-time` to 5m, and use the `least-waste` expander. Monitor node count trends weekly, if it's flat while pod count fluctuates, your scale-down settings are too conservative.

**Key takeaway: **The default Cluster Autoscaler settings are designed for safety, not cost. Tuning scale-down aggressiveness and using least-waste bin-packing can reduce node count by 20–40% without impacting workload availability.
