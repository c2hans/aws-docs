---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm-cluster-health-check.html
---

# Health monitoring agent
<a name="sagemaker-hyperpod-resiliency-slurm-cluster-health-check"></a>

This section describes the set of health checks that SageMaker HyperPod uses to regularly monitor cluster instance health for issues with devices such as accelerators (GPU and Trainium cores) and networking (EFA). SageMaker HyperPod health-monitoring agent (HMA) continuously monitors the health status of each GPU-based or Trainium-based instance. When it detects any instance or GPU failures, the agent marks the instance as unhealthy.

SageMaker HyperPod HMA performs the same health checks for both EKS and Slurm orchestrators. For more information about HMA, see [Health Monitoring System](sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
