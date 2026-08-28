---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-inspection-third-party.html
---

# Centralized inbound inspection with third-party appliances
<a name="centralized-inspection-third-party"></a>

In this architectural design pattern, you deploy third-party firewall appliances on Amazon EC2 across multiple availability zones behind an Elastic Load Balancer (ELB) such as an Application/Network Load Balancer in a separate Inspection VPC.

The Inspection VPC along with other Spoke VPCs are connected together through a Transit Gateway as VPC attachments. The applications in Spoke VPCs are frontend by an internal ELB which can be either ALB or NLB depending on the application type. The clients over the internet connect to the DNS of the external ELB in the inspection VPC which routes the traffic to one of the Firewall appliances. The Firewall inspects the traffic and then routes the traffic to the Spoke VPC through Transit Gateway using the DNS of the internal ELB as shown in the following figure. For more information regarding inbound security inspection with third-party appliances, refer to the [How to integrate third-party firewall appliances into an AWS environment](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-integrate-third-party-firewall-appliances-into-an-aws-environment/) blog post.

![A diagram depicting centralized ingress traffic inspection using third-party appliances and ELB](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/ingress-inspection-third-party.png)

## Advantages
<a name="advantages-22"></a>
+ This architecture can support any application type for inspection and advanced inspection capabilities offered through third-party firewall appliances.
+ This pattern supports DNS based routing from firewall appliances to spoke VPCs, which allows the applications in Spoke VPCs to scale independently behind an ELB.
+ You can use Auto Scaling with the ELB to scale the firewall appliances in the Inspection VPC.

## Key considerations
<a name="key-considerations-52"></a>
+ You need to deploy multiple firewall appliances across Availability Zones for high availability.
+ The firewall needs to be configured with and perform Source NAT in order to maintain flow symmetry, which means the client IP address won’t be visible to the application.
+ Consider deploying Transit Gateway and Inspection VPC in the Network Services account.
+ Additional third-party vendor firewall licensing/support cost. Amazon EC2 charges are dependent on instance type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
