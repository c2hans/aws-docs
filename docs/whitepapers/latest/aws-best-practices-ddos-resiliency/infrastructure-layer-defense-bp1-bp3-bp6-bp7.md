---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/infrastructure-layer-defense-bp1-bp3-bp6-bp7.html
---

# Infrastructure layer defense (BP1, BP3, BP6, BP7)
<a name="infrastructure-layer-defense-bp1-bp3-bp6-bp7"></a>

 In a traditional datacenter environment, you can mitigate infrastructure layer DDoS attacks by using techniques like overprovisioning capacity, deploying DDoS mitigation systems, or scrubbing traffic with the help of DDoS mitigation services. On AWS, baseline DDoS mitigation capabilities are automatically provided by AWS Shield Standard at no additional cost; however, additional protections—such as AWS Shield Advanced, AWS WAF, and application-layer mitigations—require configuration and can incur additional charges. You can further optimize your application's DDoS resilience by making architecture choices that best use these capabilities and allow you to scale for excess traffic.

 Key considerations to help mitigate volumetric DDoS attacks include ensuring that enough transit capacity and diversity are available and protecting AWS resources, like Amazon EC2 instances, against attack traffic.

 To allow this high level of resilience, AWS recommends using [Amazon EC2 instances](https://aws.amazon.com/ec2/instance-types/) with higher networking throughput that have an N suffix and support for [Enhanced Networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) with up to 200 Gbps of network bandwidth, for example, `c7gn.16xlarge` (Graviton3E, network-optimized) and `c6in.32xlarge` (Intel, network-optimized).
