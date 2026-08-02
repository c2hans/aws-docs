---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/decentralized-conditional-forwarders.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Decentralized conditional forwarders
<a name="decentralized-conditional-forwarders"></a>

 While the Route 53 solution helps you avoid the complexities in running a hybrid DNS architecture, you might still prefer to configure your DNS infrastructure to use conditional forwarders within your VPCs. One reason to run your own forwarders is to log DNS queries. Refer to *[DNS logging](additional-considerations.md#dns-logging)* (under *Additional considerations*) to determine if this is right for you.

 There are two options under this solution. The first option, called *highly distributed forwarders,* discusses how to run forwarders on every instance of the environment trying to mimic the scale that the Route 53 solution provides. The second option, called *zonal forwarders using supersede,* presents a strategy of localizing forwarders to a specific Availability Zone and its instances.

 The following table highlights these two options followed by their detailed discussion:

 *Table 3– Solution highlights – decentralized conditional forwarders*

|  Option  |  Use case  |  Advantages  |  Limitations  |
| --- | --- | --- | --- |
| Highly distributed forwarders  | Workload generates high volumes of DNS queries <br /> Infrequently changing DNS environment  | Resilient DNS infrastructure <br />Low possibility for instances to breach the PPS per network interface limit  | Complex setup and management <br />Investment in relevant skill sets for configuration management  |
| Zonal forwarders using supersede  | Customers with existing set of conditional forwarders <br />Environment that doesn’t generate a high volume of DNS traffic  | Fewer forwarders to manage <br />Zonal isolation provides better overall resiliency  | Complex setup and management as the DNS environment grows <br />Possibility of breaching the PPS per network interfaces limit is higher than the highly distributed option  |

## Highly distributed forwarders
<a name="highly-distributed-forwarders"></a>

 This option decentralizes forwarders and runs a small lightweight DNS forwarder on every instance in the environment. The forwarder is configured to serve the DNS needs of only the instance it is running on, which reduces bottlenecks and dependency on a central set of instances.

 Given the implementation and management complexity of this solution, we recommend that you use a mature configuration management solution.

 The following diagram shows how this solution functions in a single VPC:

![A diagram depciting distributed forwarders in a single VPC.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/distributed-forwarders.jpeg)

1.  Each instance in the VPC runs its own conditional forwarder (unbound). The resolv.conf has a single DNS Server entry pointing to `127.0.0.1`. A straightforward approach for modifying resolv.conf would be creating a DHCP options set that has `127.0.0.1` as the `domain-name-server` value. You may alternatively choose to overwrite any existing DHCP options settings using the supersede option in the `dhclient.conf`.

1.  Records requested for on-premises hosted zones are forwarded to the on-premises DNS server by the forwarder running locally on the instance.

1.  Any requests that don’t match the on-premises forwarding filters are forwarded to Route 53 Resolver.

 Similar to the Route 53 solution, this solution allows every single instance to use the limit of 1024 PPS per network interfaces to Route 53 Resolver to its full potential. The solution also scales up as additional instances are added and works the same way regardless of whether you’re using a single or multi-VPC setup. The DNS infrastructure is low latency, and the failure of a DNS component such as an individual forwarder does not affect the entire fleet due to the decoupled nature of the design.

 This solution poses implementation and management complexities, especially as the environment grows. You can manage and modify configuration files at instance launch using Amazon EC2 [user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html). After instance launch, you can use the [Amazon EC2 Run command](https://aws.amazon.com/ec2/run-command/) or [AWS OpsWorks for Chef Automate](https://aws.amazon.com/opsworks/chefautomate/) to deploy and maintain your configuration files.

 The implementation of these solutions is outside the scope of this whitepaper, but it is important to know that they provide the flexibility and power to manage configuration files and their state at a large scale. Greater flexibility brings with it the challenge of greater complexity. Consider additional operational costs, including the need to have an in-house DevOps workforce.

## Zonal forwarders using supersede
<a name="zonal-forwarders-using-supersede"></a>

 If you don’t want to manage and implement a forwarder on each instance of your environment, and you want to have conditional forwarder instances as the center piece of your hybrid DNS architecture, you should consider this option.

 For this option, you localize instances in an Availability Zone (AZ) to forward queries to conditional forwarders only in the same Availability Zone of the Amazon VPC. For reasons discussed in the [*Linux Resolver*](key-concepts.md#linux-resolver) section, each instance can have up to three DNS servers in their `resolv.conf`, as shown in the following diagram:

![A diagram depicting zonal forwarders with supersede option.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/zonal-forwarders.png)

+  Instances in Availability Zone A are configured using the supersede option, which uses a list of DNS forwarders that are local to that Availability Zone. To avoid burdening any specific forwarder in the Availability Zone, randomize the order for the DNS forwarders across instances in the Availability Zone.

1.  Records requested for on-premises hosted zones are directly forwarded to the on- premises DNS server by the DNS forwarder.

1.  Any requests that don’t match the on-premises forwarding filters are forwarded to the Route 53 Resolver. This illustration doesn’t depict the actual flow of traffic. It’s presented for representation purposes

1.  Similarly, other Availability Zones in the VPC can be set up to use their own set of local conditional forwarders that serve the respective Availability Zone. You determine the number of conditional forwarders serving an Availability Zone based on your need and the importance of the environment.

 If one of the three instances in Availability Zone A fails, the other two instances continue serving DNS traffic. It is important to note that placement groups must be used in order to guarantee that the forwarders are not running on the same parent hardware, which is a single point of failure. To ensure separate parent hardware, you may set up and take advantage of [Amazon Elastic Compute Cloud Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) to avoid this type of failure domain.

 If all three DNS forwarders in Availability Zone A fail at the same time, the instances in Availability Zone A fails to resolve any DNS requests because they are unaware of the presence of forwarders in other Availability Zones. This prevents the impact from spreading to multiple Availability Zones and ensures that other Availability Zones continue to function normally.

 Currently, the DHCP options that you set apply to the VPC as a whole. Therefore, you must self-manage the list of DNS servers that are local to instances in each Availability Zone. In addition, we recommend that you don’t use the same order of DNS servers in your `resolv.conf` for all instances in the Availability Zone, because it would burden the first server in the list and push it closer to breaching the PPS per network interfaces limit. Although each Linux instance can only have three resolvers, if you’re managing the resolver list yourself, you can have as many resolvers as you want per Availability Zone. Each instance should be configured with three random resolvers from the resolver list.
