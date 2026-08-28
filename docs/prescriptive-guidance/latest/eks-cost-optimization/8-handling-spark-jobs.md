---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/8-handling-spark-jobs.html
---

# Spark jobs optimization
<a name="8-handling-spark-jobs"></a>

Apache Spark jobs on EKS have unique characteristics, they require large burst capacity, run for variable durations, and can waste resources if drivers outlive executors or if executor pools are over-provisioned.

## Actions
<a name="strategy"></a>

Implement Spark-specific node management and scheduling optimizations. Refer to [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/09-spark-jobs-optimization/spark-nodepool.yaml) for sample commands to create dedicated nodepool for Spark workloads.

### Spark configuration for cost optimization
<a name="spark-configuration-for-cost-optimization.78a0705c-a2af-5234-9c39-a8ba95997e81"></a>

For sample commands to create dynamic allocation scales executors based on pending tasks,see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/09-spark-jobs-optimization/spark-cost-optimized-config.yaml)

### Spark job lifecycle optimization
<a name="spark-job-lifecycle-optimization.0ce341f5-d3ea-5553-ace0-6379dc3a1cb1"></a>

|
|
| OptimizationFor the complete scripts and manifests, see the [09-spark-jobs-optimization](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/09-spark-jobs-optimization) folder in the code repository. | Configuration | Savings |
| --- |--- |--- |
| Dynamic allocation | `spark.dynamicAllocation.enabled=true` | 30–50% fewer executor-hours |
| Executor idle timeout | `spark.dynamicAllocation.executorIdleTimeout=60s` | Rapid scale-down |
| Spot instances for executors | Node selector for spot capacity type | 60–90% off on-demand pricing |
| On-demand for driver | Prevent job failure from Spot interruption | N/A (reliability) |
| Node decommissioning | `spark.decommission.enabled=true` | Graceful Spot handling |

**Recommendations**:
+ Use Spot instances for Spark executors (they are fault-tolerant by design)
+ Keep Spark drivers on On-Demand instances to prevent job failures
+ Enable dynamic allocation to scale executors based on pending tasks
+ Set aggressive `executorIdleTimeout` (30–60s) to release resources quickly
+ Use Karpenter's `consolidationPolicy: WhenEmpty` for Spark NodePools to avoid disrupting running executors
+ Schedule large batch Spark jobs during off-peak hours for better Spot availability and lower contention

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
