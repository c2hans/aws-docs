---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/6-4-use-preference-policy.html
---

# Disruption preference policy
<a name="6-4-use-preference-policy"></a>

Disruption Preference Policy tells Karpenter which nodes to disrupt first when consolidating — prioritize removing the most expensive or least utilized nodes to maximize savings per disruption event.

The configuration covers:
+ NodePool-level budget `reasons` (Underutilized, Empty, Drifted) to target on-demand nodes first for Spot replacement
+ Pod-level `karpenter.sh/do-not-disrupt` annotations to control which workloads move first during consolidation
+ Topology spread constraints to prevent consolidation from concentrating pods in a single zone

For the NodePool and Deployment configuration, see the [disruption-preference-policy.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/disruption-preference-policy.yaml) and [verify-disruption-preference.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-disruption-preference.sh) for verification commands.

## Actions
<a name="actions"></a>

Combine budgets with preference policies to create a disruption strategy that removes the most expensive nodes first, during the safest windows, at a rate that doesn't impact availability.

**Key takeaway: **Not all disruptions save the same amount. Prioritizing on-demand node removal over Spot, and empty nodes over underutilized ones, maximizes the dollar value of each disruption event.
