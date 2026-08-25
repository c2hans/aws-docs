---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/6-2-set-expiry-period-and-termination-grace-period.html
---

# Node expiry and termination grace period
<a name="6-2-set-expiry-period-and-termination-grace-period"></a>

Force periodic node replacement to pick up cheaper instance types, newer AMIs, and prevent long-running nodes from accumulating drift. Control how gracefully pods are evicted to balance cost reclaim speed with application stability.

**Why this matters for cost**
+ **expireAfter**: Nodes running for weeks may be on older, more expensive instance types. Periodic rotation lets Karpenter re-evaluate and pick the cheapest option available now.
+ **terminationGracePeriod":** Without this, pods with long shutdown hooks can keep a node alive (and billing) for hours. Setting a cap ensures nodes are reclaimed within a predictable window.

For sample NodePool configuration with expiry and termination grace period settings, see the [node-expiry-termination.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/node-expiry-termination.yaml) , and [verify-node-expiry.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-node-expiry.sh) to check node ages and monitor expiry-driven replacements.

## Actions
<a name="actions"></a>

Both *expireAfter* and *terminationGracePeriod* directly affect running workloads — set them too aggressively and you risk disrupting active traffic; set them too conservatively and you pay for idle compute. Tune these values based on your workload's tolerance for restarts.

**TerminationGracePeriod Recommendation**

|
|
| Workload Type | TerminationGracePeriod | Rationale |
| --- |--- |--- |
| Stateless web services | 2–6 hours | Quick drain, pods reschedule fast |
| Stateful applications | 24–48 hours | Time for graceful shutdown and data sync |
| Spark/batch jobs | 72\+ hours | Allow in-progress jobs to complete |
| GPU training | Match job duration | Avoid wasting GPU hours |

**Key takeaway: **Without expiry, nodes can run for weeks on instance types that are no longer the cheapest option. Periodic rotation lets Karpenter continuously re-optimize your fleet, and capping termination grace prevents dying pods from holding nodes hostage.
