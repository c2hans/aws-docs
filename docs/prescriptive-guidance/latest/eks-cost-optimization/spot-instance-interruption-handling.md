---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/spot-instance-interruption-handling.html
---

# Spot instance interruption handling
<a name="spot-instance-interruption-handling"></a>

Make Spot instances viable for more workloads by handling interruptions gracefully — the more workloads you can safely run on Spot, the greater your savings.

For a sample pod configuration with a graceful termination grace period, see this [spot-interruption-handling.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/spot-interruption-handling.yaml) , a preStop hook to drain connections, and topology spread constraints for resilience across Spot pools.

For the complete scripts and manifests, see the [10-additional-cost-saving-strategies](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/10-additional-strategies) folder in the code repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
