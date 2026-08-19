---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/network-cost-reduction.html
---

# Network cost reduction
<a name="network-cost-reduction"></a>

Cross-AZ data transfer is a hidden cost that grows with traffic — keeping service-to-service communication within the same AZ eliminates per-GB transfer charges ($0.01/GB each way).

For commands to check pod distribution across AZs and identify services that would benefit from topology-aware routing, see [check-cross-az-traffic.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/check-cross-az-traffic.sh) , and [topology-aware-routing.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/topology-aware-service.yaml) for a sample Service configured to keep traffic in-zone.

For the complete scripts and manifests, see the [10-additional-cost-saving-strategies](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/10-additional-strategies) folder in the code repository.
