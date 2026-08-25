---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/prerequisites-and-limitations.html
---

# Prerequisites and limitations
<a name="prerequisites-and-limitations"></a>

## Prerequisites
<a name="prerequisites.4df689e4-d458-5a8a-a2a5-cdb183ed309d"></a>

Before implementing the strategies in this guide, ensure you have:

**Technical requirements**:
+ An active AWS account with Amazon EKS clusters running
+ Familiarity with Kubernetes concepts (Pods, Nodes, Deployments, DaemonSets)
+ Karpenter v0.33\+ or Cluster Autoscaler installed on EKS clusters
+ Access to Amazon CloudWatch for metrics and monitoring
+ kubectl configured for EKS cluster access

**Organizational requirements**:
+ Executive sponsorship for cost optimization initiatives
+ Defined process for testing changes in non-production environments
+ Communication plan for workload migrations and disruptions
+ Cost allocation and chargeback model (recommended)

**Tools and utilities**:
+ Helm 3.x for installing Kubernetes applications
+ AWS CLI version 2.x
+ Monitoring tools (CloudWatch Container Insights, Prometheus, or similar)
+ Cost visibility tools ([AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), Kubecost, or similar)

### Limitations
<a name="limitations"></a>

Be aware of the following limitations:

**Technical limitations**:
+ Karpenter requires Amazon EKS version 1.23 or later
+ Graviton migration requires multi-architecture container images
+ Some third-party software may not support ARM64 architecture
+ Spot instances may be interrupted with 2-minute notice
+ VPA and HPA cannot target the same metrics simultaneously

**Operational considerations**:
+ Node consolidation may cause temporary pod disruptions
+ Cluster upgrades require careful planning and testing
+ Some optimizations may require application code changes
+ Initial implementation requires time investment from engineering teams

**Service quotas**:
+ Amazon EC2 instance limits per region
+ Amazon EKS cluster limits (100 clusters per region by default)
+ Auto Scaling group limits
+ Spot instance capacity availability varies by region and instance type
