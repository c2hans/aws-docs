---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/spot-instance-interruption-handling.html
---

# Spot instance interruption handling
<a name="spot-instance-interruption-handling"></a>

Make Spot instances viable for more workloads by handling interruptions gracefully — the more workloads you can safely run on Spot, the greater your savings.

For a sample pod configuration with a graceful termination grace period, see this [spot-interruption-handling.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/spot-interruption-handling.yaml) , a preStop hook to drain connections, and topology spread constraints for resilience across Spot pools.

For the complete scripts and manifests, see the [10-additional-cost-saving-strategies](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/10-additional-strategies) folder in the code repository.
