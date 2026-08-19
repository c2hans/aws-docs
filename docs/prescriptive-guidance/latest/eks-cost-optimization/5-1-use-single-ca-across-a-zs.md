---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/5-1-use-single-ca-across-a-zs.html
---

# Use single Cluster Autoscaler across AZs
<a name="5-1-use-single-ca-across-a-zs"></a>

Run one Cluster Autoscaler deployment that manages node groups across all Availability Zones — this gives the autoscaler full visibility into cluster-wide capacity and prevents AZ-isolated scaling decisions that lead to imbalanced, over-provisioned clusters.

For the deployment manifest, see the [single-ca-multi-az.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/single-ca-multi-az.yaml) and [verify-ca-az-distribution.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/verify-ca-az-distribution.sh) to verify node distribution across AZs.

## Actions
<a name="solution"></a>

Consolidate multiple per-AZ Cluster Autoscaler deployments into a single instance with `--balance-similar-node-groups=true`. This prevents one AZ from scaling up while another has idle capacity, eliminating cross-AZ over-provisioning.

### Cost impact
<a name="cost-impact.a6c24389-3049-5674-b0e9-7db6f728f2e9"></a>

|
|
| Configuration | Min Nodes | Monthly Min Cost (m6g.large) |
| --- |--- |--- |
| 3 CAs × 1 min node | 3 | \~$210/month |
| 1 CA × 1 min node | 1 | \~$70/month |
| **Savings** | **2 nodes** | **\~$140/month per cluster** |

**Key takeaway: **Multiple autoscaler instances per AZ can't see each other's capacity. A single CA with cross-AZ visibility makes globally optimal scaling decisions and avoids redundant nodes sitting idle in one zone while another scales up.
