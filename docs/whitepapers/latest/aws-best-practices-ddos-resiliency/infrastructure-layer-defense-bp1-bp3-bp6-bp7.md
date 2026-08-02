---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/infrastructure-layer-defense-bp1-bp3-bp6-bp7.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Infrastructure layer defense (BP1, BP3, BP6, BP7)
<a name="infrastructure-layer-defense-bp1-bp3-bp6-bp7"></a>

 In a traditional datacenter environment, you can mitigate infrastructure layer DDoS attacks by using techniques like overprovisioning capacity, deploying DDoS mitigation systems, or scrubbing traffic with the help of DDoS mitigation services. On AWS, DDoS mitigation capabilities are automatically provided; but you can optimize your application’s DDoS resilience by making architecture choices that best leverage those capabilities and also allow you to scale for excess traffic.

 Key considerations to help mitigate volumetric DDoS attacks include ensuring that enough transit capacity and diversity are available and protecting AWS resources, like Amazon EC2 instances, against attack traffic.

 Some Amazon EC2 instance types support features that can more easily handle large volumes of traffic, for example, up to 100 Gbps network bandwidth interfaces and enhanced networking. This helps prevent interface congestion for traffic that has reached the Amazon EC2 instance. Instances that support enhanced networking provide higher input/output (I/O) performance, higher bandwidth, and lower CPU utilization compared to traditional implementations. This improves the ability of the instance to handle large volumes of traffic and ultimately makes them highly resilient against packets per second (pps) load.

 To allow this high level of resilience, AWS recommends using [Amazon EC2 Dedicated Instances](https://aws.amazon.com/ec2/pricing/dedicated-instances/), or Amazon EC2 instances with higher networking throughput that have an "`N`" suffix and support for Enhanced Networking with up to 100 Gbps of Network bandwidth, for example, `c6gn.16xlarge` and `c5n.18xlarge` or metal instances (such as `c5n.metal`).

 For more information about Amazon EC2 instances that support 100 Gigabit network interfaces and enhanced networking, refer to [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/).

 The module required for enhanced networking and the required `enaSupport` attribute set are included with Amazon Linux 2 and the latest versions of the Amazon Linux AMI. Therefore, if you launch an instance with a hardware virtual machine (HVM) version of Amazon Linux on a supported instance type, enhanced networking is already enabled for your instance. For more information, refer to [Test whether enhanced networking is enabled](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html#test-enhanced-networking-ena) and [Enhanced networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html).
