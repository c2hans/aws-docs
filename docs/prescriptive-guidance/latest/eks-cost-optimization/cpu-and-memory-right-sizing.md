---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/cpu-and-memory-right-sizing.html
---

# CPU and memory right-sizing
<a name="cpu-and-memory-right-sizing"></a>

Over-provisioned requests are the \#1 hidden cost in Kubernetes. Pods requesting more than they use prevent bin-packing and force unnecessary nodes.

## Identify Over-Provisioned Workloads
<a name="identify-over-provisioned-workloads.9d454aa4-b549-5466-b262-d145ca08d0c8"></a>

Compare resource requests against actual usage to find pods consuming significantly less than they reserve. Pods using less than 30% of their CPU request are candidates for right-sizing.

For kubectl-based commands to compare requests vs usage and identify waste, see the [identify-over-provisioned.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/identify-over-provisioned.sh)

**CloudWatch: Container Insights for Right-Sizing**

For a more accurate 7-day view (vs point-in-time `kubectl top`), use CloudWatch Container Insights metrics to measure average and peak CPU/memory utilization per namespace.

For sample commands, see the [cloudwatch-right-sizing-metrics.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/04-karpenter-cost-optimization/cloudwatch-right-sizing-metrics.sh)

### Actions
<a name="actions"></a>

**Implement Vertical Pod Autoscaler (VPA) for Recommendations, **Refer to [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/06-cpu-memory-right-sizing/vpa-recommendation-mode.yaml) for sample commands. For sample commands, to right-size pod resource requests, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/06-cpu-memory-right-sizing/get-vpa-recommendations.sh)

**Horizontal Pod Autoscaler (HPA) for Efficient Scaling, **For sample commands to configured HPA for cost-efficient scaling, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/06-cpu-memory-right-sizing/hpa-efficient-scaling.yaml)

Deploy VPA in `"Off"` mode first to collect recommendations for 7 days, then right-size requests to p95 usage \+ 20% buffer. Combine with HPA to scale horizontally at 70% utilization, this keeps pods lean while handling traffic spikes.

**Key takeaway:** Over-provisioned requests are invisible waste, they don't show up as errors or alerts, but they force extra nodes to exist. Right-sizing is often the single biggest cost win within an active cluster.
