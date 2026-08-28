---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets.html
---

# Preserve routable IP space in multi-account VPC designs for non-workload subnets
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets"></a>

*Adam Spicer, Amazon Web Services*

## Summary
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-summary"></a>

Amazon Web Services (AWS) has published best practices that recommend using dedicated subnets in a virtual private cloud (VPC) for both [transit gateway attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html) and [Gateway Load Balancer endpoints](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html) (to support [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-high-level-steps.html) or third-party appliances). These subnets are used to contain elastic network interfaces for these services. If you use both AWS Transit Gateway and a Gateway Load Balancer, two subnets are created in each Availability Zone for the VPC. Because of the way VPCs are designed, these extra subnets [can’t be smaller than a /28 mask](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-sizing) and can consume precious routable IP space that could otherwise be used for routable workloads. This pattern demonstrates how you can use a secondary, non-routable Classless Inter-Domain Routing (CIDR) range for these dedicated subnets to help preserve routable IP space.

## Prerequisites and limitations
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-prereqs"></a>

**Prerequisites **
+ [Multi-VPC strategy](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) for routable IP space
+ A non-routable CIDR range for the services you’re using ([transit gateway attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html) and [Gateway Load Balancer](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/) or [Network Firewall endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/))

## Architecture
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-architecture"></a>

**Target architecture **

This pattern includes two reference architectures: one architecture has subnets for transit gateway (TGW) attachments and a Gateway Load Balancer endpoint (GWLBe), and the second architecture has subnets for TGW attachments only.

**Architecture 1 ‒ TGW-attached VPC with ingress routing to an appliance**

The following diagram represents a reference architecture for a VPC that spans two Availability Zones. On ingress, the VPC uses an [ingress routing pattern](https://aws.amazon.com/blogs/aws/new-vpc-ingress-routing-simplifying-integration-of-third-party-appliances/) to direct traffic destined for the public subnet to a [bump-in-the-wire appliance](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-gateway-load-balancer-supported-architecture-patterns/) for firewall inspection. A TGW attachment supports egress from the private subnets to a separate VPC.

This pattern uses a non-routable CIDR range for the TGW attachment subnet and the GWLBe subnet. In the TGW routing table, this non-routable CIDR is configured with a blackhole (static) route by using a set of more specific routes. If the routes were to get propagated to the TGW routing table, these more specific blackhole routes would apply.

In this example, the /23 routable CIDR is divided up and fully allocated to routable subnets.

![TGW-attached VPC with ingress routing to an appliance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0171d91d-ab1e-41ca-a425-1e6e610080e1/images/adad1c83-cdc2-4c5e-aa35-f47fc31af384.png)

**Architecture 2 – TGW-attached VPC**

The following diagram represents another reference architecture for a VPC that spans two Availability Zones. A TGW attachment supports outbound traffic (egress) from the private subnets to a separate VPC. It uses a non-routable CIDR range only for the TGW attachments subnet. In the TGW routing table, this non-routable CIDR is configured with a blackhole route by using a set of more specific routes. If the routes were to get propagated to the TGW routing table, these more specific blackhole routes would apply.

In this example, the /23 routable CIDR is divided up and fully allocated to routable subnets.

![VPC spans 2 availability zones with TGW attachment for egress from private subnets to separate VPC.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0171d91d-ab1e-41ca-a425-1e6e610080e1/images/31a2a241-5be6-425e-93e9-5ff7ffeca3a9.png)

## Tools
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-tools"></a>

**AWS services and resources**
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. In this pattern, VPC secondary CIDRs are used to preserve routable IP space in workload CIDRs.
+ [Internet gateway ingress routing](https://aws.amazon.com/blogs/aws/new-vpc-ingress-routing-simplifying-integration-of-third-party-appliances/) (edge associations) can be used along with Gateway Load Balancer endpoints for dedicated non-routable subnets.
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a central hub that connects VPCs and on-premises networks. In this pattern, VPCs are centrally attached to a transit gateway, and the transit gateway attachments are in a dedicated non-routable subnet.
+ [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html) help you deploy, scale, and manage virtual appliances, such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems. The gateway serves as a single entry and exit point for all traffic. In this pattern, endpoints for a Gateway Load Balancer can be used in a dedicated non-routable subnet.
+ [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) is a stateful, managed, network firewall and intrusion detection and prevention service for VPCs in the AWS Cloud. In this pattern, endpoints for an firewall can be used in a dedicated non-routable subnet.

**Code repository**

A runbook and AWS CloudFormation templates for this pattern are available in the GitHub [Non-Routable Secondary CIDR Patterns](https://github.com/aws-samples/non-routable-secondary-vpc-cidr-patterns/) repository. You can use the sample files to set up a working lab in your environment.

## Best practices
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-best-practices"></a>

**AWS Transit Gateway**
+ Use a separate subnet for each transit gateway VPC attachment.
+ Allocate a /28 subnet from the secondary non-routable CIDR range for the transit gateway attachment subnets.
+ In each transit gateway routing table, add a static, more specific route for the non-routable CIDR range as a blackhole.

**Gateway Load Balancer and ingress routing**
+ Use ingress routing to direct traffic from the internet to the Gateway Load Balancer endpoints.
+ Use a separate subnet for each Gateway Load Balancer endpoint.
+ Allocate a /28 subnet from the secondary non-routable CIDR range for the Gateway Load Balancer endpoint subnets.

## Epics
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-epics"></a>

### Create VPCs
<a name="create-vpcs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine non-routable CIDR range. | Determine a non-routable CIDR range that will be used for the transit gateway attachment subnet and (optionally) for any Gateway Load Balancer or Network Firewall endpoint subnets. This CIDR range will be used as the secondary CIDR for the VPC. It must **not be routable** from the VPC’s primary CIDR range or the larger network. | Cloud architect |
| Determine routable CIDR ranges for VPCs. | Determine a set of routable CIDR ranges that will be used for your VPCs. This CIDR range will be used as the primary CIDR for your VPCs. | Cloud architect |
| Create VPCs. | Create your VPCs and attach them to the transit gateway. Each VPC should have a primary CIDR range that is routable and a secondary CIDR range that is non-routable, based on the ranges you determined in the previous two steps. | Cloud architect |

### Configure Transit Gateway blackhole routes
<a name="configure-transit-gateway-blackhole-routes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create more specific non-routable CIDRs as blackholes. | Each transit gateway routing table needs to have a set of blackhole routes created for the non-routable CIDRs. These are configured to ensure that any traffic from the secondary VPC CIDR remains non-routable and doesn't leak into the larger network. These routes should be more specific than the non-routable CIDR that is set as the secondary CIDR on the VPC. For example, if the secondary non-routable CIDR is 100.64.0.0/26, the blackhole routes in the transit gateway routing table should be 100.64.0.0/27 and 100.64.0.32/27. | Cloud architect |

## Related resources
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-resources"></a>
+ [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/)
+ [Distributed Inspection Architectures with Gateway Load Balancer](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/distributed-inspection-architectures-gwlb-ra.pdf?did=wp_card&trk=wp_card)
+ [Networking Immersion Day ](https://catalog.workshops.aws/networking/en-US/gwlb/lab2-internettovpc)‒ [Internet to VPC Firewall Lab](https://catalog.workshops.aws/networking/en-US/gwlb/lab2-internettovpc)
+ [Transit gateway design best practices](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html)

## Additional information
<a name="preserve-routable-ip-space-in-multi-account-vpc-designs-for-non-workload-subnets-additional"></a>

The non-routable secondary CIDR range can also be useful when working with larger scaled container deployments that require a large set of IP addresses. You can use this pattern with a private NAT Gateway to use a non-routable subnet to host your container deployments. For more information, see the blog post [How to solve Private IP exhaustion with Private NAT Solution](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-solve-private-ip-exhaustion-with-private-nat-solution/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
