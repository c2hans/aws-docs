---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/eks-control-plane-upgrade-cost-savings.html
---

# EKS control plane upgrade cost savings
<a name="eks-control-plane-upgrade-cost-savings"></a>

Why upgrades save money

AWS charges a flat rate for the EKS control plane, but the rate increases significantly once your cluster version moves from **standard support** into **extended support**. For current pricing details, see the [Amazon EKS pricing page.](https://aws.amazon.com/eks/pricing/)

Beyond the direct control plane charge, outdated versions also lead to:
+ **Incompatibility with newer, cheaper instance types: **newer Kubernetes versions support the latest EC2 families (M7g, C7g, R7g) that offer better price-performance
+ **Missing performance improvements: **scheduler enhancements, memory management fixes, and networking optimizations in newer versions can reduce the number of nodes required
+ **Security patching overhead: **backporting fixes to older versions increases operational cost
+ **Addon drift: **older versions lock you into older addon versions that may lack cost-relevant features (e.g., Karpenter improvements, EBS CSI (Container Storage Interface) gp3 defaults)
+ **Extended support exit pressure: **once extended support ends, the cluster is auto-upgraded, potentially causing unplanned disruption if not proactively managed

Amazon EKS version lifecycle reference

For the current Kubernetes version calendar including standard support end dates and extended support windows, refer to the official [Amazon EKS Kubernetes release calendar](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#kubernetes-release-calendar).

## Identify clusters at risk
<a name="action"></a>

Scan all your clusters across regions to flag which ones are running on extended support and costing you extra. For sample commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/03-eks-control-plane-upgrade/audit-cluster-versions.sh) to identify clusters at risk.

**Estimate your extended support waste**

Quantify how much you're overpaying so you can prioritize upgrades with a clear dollar figure for leadership. For sample commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/03-eks-control-plane-upgrade/estimate-extended-support-waste.sh)

**CloudWatch: Monitor Control Plane Health Pre-Upgrade**

The health check validates: API server availability (no 5xx spikes), zero failed nodes, no deprecated API usage that would break post-upgrade, and addon compatibility with the target version. Confirm your cluster is healthy before upgrading, resolving existing issues first prevents failed upgrades and unplanned downtime. For sample commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/03-eks-control-plane-upgrade/pre-upgrade-health-check.sh)

## Actions
<a name="key-takeaway"></a>

⚠️ Always perform upgrades in non-production environments first. Ensure you have tested addon compatibility and verified no deprecated API usage before upgrading production clusters.

 Pre-upgrade compatibility check

Verify that your addons, APIs, and workloads are compatible with the target version to avoid breaking changes during the upgrade. The script checks addon version compatibility, deprecated API usage, PodSecurityPolicy presence, and workload-level feature dependencies.

For pre-upgrade compatibility check script, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/03-eks-control-plane-upgrade/pre-upgrade-compatibility-check.sh)

Upgrade procedure (cost-aware, zero-downtime)

Execute the upgrade in the correct order: control plane first, then addons, then nodes, to maintain availability while moving to a cheaper support tier. The script handles:
+ Control plane version upgrade (15–30 minutes, no workload impact)
+ EKS-managed addon upgrades (vpc-cni, kube-proxy, coredns) to compatible versions
+ Node rotation via managed node group rolling update or Karpenter drift annotation
+ Post-upgrade health verification

For upgrade procedure script, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/03-eks-control-plane-upgrade/upgrade-cluster.sh)

**Key takeaway: **Upgrading clusters out of extended support is often the single highest-ROI cost action, it requires no application changes and delivers immediate savings. Use the estimation script above with [current EKS pricing](https://aws.amazon.com/eks/pricing/) to quantify your specific savings.

For the complete scripts and manifests, see the [03-eks-control-plane-upgrade](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/03-eks-control-plane-upgrade) folder in the code repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
