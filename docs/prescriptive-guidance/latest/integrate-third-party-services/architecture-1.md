---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architecture-1.html
---

# Architecture 1: AWS PrivateLink
<a name="architecture-1"></a>

[AWS PrivateLink](https://aws.amazon.com/privatelink/) is a feature of Amazon Virtual Private Cloud (Amazon VPC) that provides private connectivity between VPCs and AWS services. Network traffic that uses PrivateLink doesn't travel over the public internet, which reduces the risk of external threats, such as exposure to brute force and distributed denial-of-service (DDoS) attacks. It provides a way for two parties to establish private connectivity without requiring an internet gateway. Both parties can deploy private VPCs that are insulated from threats on the internet.

To connect interface endpoints to other services, PrivateLink uses [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html). Network Load Balancers provide scalability and can support millions of requests per second.

You can connect services across different accounts and VPCs, and you don't need firewall rules, path definitions, route tables, an internet gateway, VPC peering connections, or managed CIDR blocks. This simplification of the network architecture can make it easier to manage your global network.

The following architecture diagram shows how you can use PrivateLink and a Network Load Balancer to connect endpoints in your account to interface endpoints in a third-party account, such as the account of a software as a service (SaaS) provider. The third-party account hosts the Network Load Balancer.

![Using PrivateLink and a Network Load Balancer to connect EC2 instances in different accounts](http://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/d9332d6e-d661-4ffd-a474-0278653cc226.png)

This architecture is the most commonly selected approach for integrating third-party services because it provides strong segregation between the third-party account and your account, without shared components. It allows for overlapping CIDR blocks, which is one of the most prominent challenges when integrating with an external account. It also abstracts the network communication path. However, it is limited to only TCP traffic and unidirectional communication. The third-party workloads cannot initiate communication back to your account.

Not all AWS Partners can integrate by using PrivateLink. To determine whether your current or prospective Partner is capable, see [AWS PrivateLink Partners](https://aws.amazon.com/privatelink/partners/).

## Cost considerations
<a name="cost-considerations-1"></a>
+ There is an hourly charge for each VPC endpoint provisioned in each Availability Zone, regardless of the state of its association with the service. Even if the endpoint is in a pending state, you are charged hourly. For a list of all possible service states, see [AWS PrivateLink concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html).
+ Data processing charges apply for each GB processed through the VPC endpoint, regardless of the traffic's source or destination.

For more information, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
