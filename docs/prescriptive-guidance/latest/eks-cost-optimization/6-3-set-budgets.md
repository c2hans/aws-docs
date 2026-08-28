---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/6-3-set-budgets.html
---

# Disruption budgets
<a name="6-3-set-budgets"></a>

Disruption budgets control how many nodes Karpenter can disrupt simultaneously — this prevents aggressive consolidation from causing availability issues while still allowing cost optimization to proceed.

For sample NodePool configuration with schedule-aware disruption budgets, see the [disruption-budgets.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/disruption-budgets.yaml) that:
+ Limits disruption to 10% of nodes during normal operations
+ Blocks all disruptions during peak traffic hours (Mon–Fri 9–11am UTC)
+ Allows aggressive 40% consolidation on weekends

**Why this matters for cost**
+ **Too restrictive (e.g., **`nodes: "1"`**): **consolidation happens so slowly that underutilized nodes linger for hours, wasting money.
+ **Too aggressive (e.g., **`nodes: "50%"`**):** mass disruption can trigger unnecessary scale-ups as pods reschedule, temporarily increasing cost.
+ **Scheduled budgets** let you consolidate aggressively during off-hours when traffic is low and risk is minimal.

## Identify nodeclaims blocking consolidation
<a name="identity-nodeclaims-blocking-for-consolidation"></a>

Verify that disruption budgets are being respected and identify any NodeClaims preventing consolidation from proceeding. For sample commands , see the [verify-disruption-budgets.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-disruption-budgets.sh)

For the complete scripts and manifests, see the [04-karpenter-cost-optimization](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/04-karpenter-cost-optimization) folder in the code repository.

## Actions
<a name="actions"></a>

Start with `nodes: "10%"` as your default budget, add a scheduled `nodes: "30%"` window during off-hours for aggressive consolidation, and set `nodes: "0"` during known peak events. Review disruption-blocked events weekly — if you see frequent blocks, your budget may be too restrictive and costing you money.

**Key takeaway: **Disruption budgets are the throttle on your cost savings. Too tight and consolidation stalls, leaving you paying for underutilized nodes. Too loose and you risk availability incidents that cost more than the compute you saved. Schedule-based budgets give you the best of both worlds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
