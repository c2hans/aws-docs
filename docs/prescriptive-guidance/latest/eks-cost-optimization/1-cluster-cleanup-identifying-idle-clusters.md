---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/1-cluster-cleanup-identifying-idle-clusters.html
---

# Idle cluster cleanup: Decommission or consolidation
<a name="1-cluster-cleanup-identifying-idle-clusters"></a>

Before optimizing how your clusters run, eliminate what shouldn't be running at all. Idle clusters and abandoned workloads are pure waste as they consume resources 24/7 while delivering no business value. A cluster is considered idle when it has fewer than 5 application pods running (excluding kube-system, karpenter, monitoring namespaces) and node CPU utilization remains below 10% for 7\+ consecutive days.

## Identify idle clusters
<a name="strategy"></a>

Find clusters with little to no application workload running, these are candidates for decommissioning or consolidation. For sample commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/01-idle-cluster-cleanup/detect-idle-clusters.sh) to identify idle clusters.

**CloudWatch: Detect Idle Clusters via Metrics**

For organizations managing multiple clusters across regions, CloudWatch metrics provide a centralized, automated way to flag idle clusters without requiring kubectl access to each one. Refer to [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/01-idle-cluster-cleanup/detect-idle-clusters-cloudwatch.sh) for sample commands to identify idle clusters.

## Action
<a name="recommendations"></a>

If a cluster shows <10% CPU utilization, zero application pods, or no deployments outside kube-system for 7\+ days, escalate for decommissioning or consolidate workloads into another cluster. Every idle cluster costs you the full control plane fee plus node compute.

Before deleting an idle cluster, verify these items:
+ No application pods running outside kube-system
+ No active CronJobs with future schedules
+ No external services pointing to this cluster's load balancers
+ DNS records updated or removed
+ Persistent data backed up or migrated
+ IAM roles and policies cleaned up
+ CloudWatch log groups archived or deleted

For the complete scripts and manifests, see the [01-idle-cluster-cleanup](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/01-idle-cluster-cleanup) folder in the code repository.

The cheapest resource is the one you don't run. Eliminating idle clusters delivers immediate savings with zero risk to active applications.
