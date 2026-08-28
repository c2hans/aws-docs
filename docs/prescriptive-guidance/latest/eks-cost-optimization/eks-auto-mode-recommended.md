---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/eks-auto-mode-recommended.html
---

# Amazon EKS Auto Mode (managed option)
<a name="eks-auto-mode-recommended"></a>

[Amazon EKS Auto Mode](https://aws.amazon.com/eks/auto-mode/) (launched December 2024) automates compute management entirely — no Karpenter installation, no NodePool configuration, no autoscaler upgrades. AWS handles instance selection, Spot/On-Demand mixing, consolidation, and node patching automatically. EKS Auto Mode is best suited for teams without dedicated platform engineering capacity, or for dev/test environments where operational simplicity outweighs fine-grained cost control. It does not support separate NodePool configurations, custom disruption budgets, workload-specific taints, or explicit Spot/On-Demand ratio control.

## When to use Amazon EKS Auto Mode
<a name="when-to-use-eks-auto-mode-recommended-path"></a>
+ **Greenfield clusters: **Get cost-optimal node provisioning out of the box without upfront tuning effort.
+ **Lean teams**: Reduce the platform engineering burden by letting AWS manage node lifecycle, instance selection, and patching decisions.
+ **Homogeneous workloads:** Standard web services and APIs that don't need dedicated GPU, Spark, or high-isolation node pools.
+ **Simplicity-first environments**: Accept slightly less granular control in exchange for zero operational overhead on node management.

For sample commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/enabled-auto-mode.sh) to create a new cluster with Auto Mode or enable it on an existing cluster.

## When to use self-managed Karpenter
<a name="when-to-use-self-managed-karpenter"></a>
+ You need **separate NodePools **per workload type (PDB-protected, non-PDB, GPU, Spark) with distinct cost strategies for each.
+ You require **explicit control over disruption budgets**, expiry periods, and termination grace periods.
+ Your **Spot/On-Demand ratio** must be governed by specific policies (for example, minimum 20% On-Demand for production, 100% Spot for batch).
+ You run **Spark or batch workloads** needing consolidationPolicy: WhenEmpty to avoid disrupting in-progress jobs.
+ **Regulatory or compliance requirements** mandate explicit instance family selection and audit trails for node provisioning decisions.

## Migrating an existing cluster to Amazon EKS Auto Mode
<a name="migrating-an-existing-cluster-to-eks-auto-mode"></a>

For clusters currently using self-managed Karpenter or Cluster Autoscaler, migration to Auto Mode is a phased process — enable Auto Mode first, let it provision new nodes, then drain the old ones. The migration script handles:
+ Enabling Auto Mode and waiting for new nodes to provision
+ Cordoning and draining old self-managed nodes gracefully
+ Verifying all pods are running on Auto Mode nodes
+ Removing old node groups, Karpenter, or Cluster Autoscaler

For complete migration script, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/migrate-to-auto-mode.sh)

## Validation after migration
<a name="validation-after-migration"></a>

**Migration considerations:**
+ PodDisruptionBudgets — Auto Mode respects PDBs during node rotation. Ensure PDBs are configured before draining.
+ DaemonSets — Auto Mode nodes run standard EKS-managed DaemonSets. Custom DaemonSets will be scheduled automatically.
+ Taints and tolerations — Review any custom taints on existing nodes. Auto Mode uses its own scheduling logic; workloads relying on custom taints may need toleration updates.
+ Spot interruption handling — Auto Mode manages Spot lifecycle internally. Remove any custom Spot interruption handlers (AWS Node Termination Handler) as they're no longer needed.

For the complete migration and validation scripts, see the [04-karpenter-cost-optimization](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/04-karpenter-cost-optimization) folder in the code repository.

**Key takeaway:** EKS Auto Mode is ideal for teams that want zero operational overhead on node management. For clusters requiring workload-specific NodePools, custom disruption budgets, or explicit Spot/On-Demand control, continue with self-managed Karpenter as described in the sections below.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
