---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/5-2-set-min-node-count-appropriately.html
---

# Set min-node-count appropriately
<a name="5-2-set-min-node-count-appropriately"></a>

The minimum node count per node group determines your cost floor — set it too high and you pay for idle nodes 24/7, set it too low and you risk cold-start delays during traffic spikes.

**Assessment criteria for min-node-count:**
+ Calculate total resource requests for always-on workloads (monitoring, logging, mesh)
+ Add headroom for DaemonSets (each node runs kube-proxy, VPC CNI, monitoring agent)
+ Factor in PDB requirements — if a deployment requires 2 replicas across 2 AZs, minimum is 2 nodes

**min\_nodes = ceil(total\_pod\_requests\_at\_lowest\_traffic / allocatable\_per\_node)**

For the commands to assess your current min-node-count, check off-peak utilization, and calculate the optimal minimum based on DaemonSet overhead and PDB requirements [verify-min-node-count.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-min-node-count.sh) .

## Actions
<a name="actions"></a>

Audit your node group minimums against actual off-peak utilization. If nodes at minimum count run below 40% CPU/memory, reduce the minimum. For non-production clusters, set `minSize=0` with Karpenter or `minSize=1` with Cluster Autoscaler to allow full scale-down outside business hours.

```
# Update min size for a managed node group
aws eks update-nodegroup-config --cluster-name my-cluster \
  --nodegroup-name my-nodegroup \
  --scaling-config minSize=2,maxSize=20,desiredSize=3
```

**Key takeaway: **Every node in your minimum count runs 24/7/365 regardless of demand. An over-provisioned minimum of just 2 extra nodes costs you the equivalent of those instances running all year — often thousands of dollars per node group.
