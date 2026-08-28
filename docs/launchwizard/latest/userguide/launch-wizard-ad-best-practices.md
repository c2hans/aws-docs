---
source_url: https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-ad-best-practices.html
---

# High availability and security best practices for AWS Launch Wizard for Active Directory
<a name="launch-wizard-ad-best-practices"></a>

The domain controller architecture created by AWS Launch Wizard supports AWS best practices for high availability and security as promoted by the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

**Topics**
+ [High availability](#launch-wizard-ad-ha)
+ [Security in Launch Wizard for Active Directory](#launch-wizard-ad-security)

## High availability
<a name="launch-wizard-ad-ha"></a>

With Amazon EC2, you can set the location of instances in multiple locations composed of AWS Regions and Availability Zones. Regions are dispersed and located in separate geographic areas. Availability Zones are distinct locations within a Region that are engineered to be isolated from failures in other Availability Zones. Availability Zones provide inexpensive, low-latency network connectivity to other Availability Zones in the same Region.

When you launch your instances in different Regions, you can set your domain controllers to be closer to specific customers, or to meet legal or other requirements. When you launch your instances in different Availability Zones, you can protect your domain controllers from the failure of a single location.

## Security in Launch Wizard for Active Directory
<a name="launch-wizard-ad-security"></a>

Launch Wizard creates a number of security groups and rules for you. When your directory resources are launched, they must be associated with a security group, which acts as a stateful firewall. You have complete control over the network traffic entering or leaving the security group. You can also build granular rules that are scoped by protocol, port number, and source or destination IP address or subnet. By default, all outbound traffic from a security group is permitted. Inbound traffic, on the other hand, permits traffic from the VPC used for the deployment and resources that Launch Wizard deploys. You might require additional configuration to allow appropriate traffic to reach your resources.

The [Securing the Microsoft Platform on Amazon Web Services](https://d1.awsstatic.com/whitepapers/aws-microsoft-platform-security.pdf) whitepaper discusses the different methods for securing your AWS infrastructure. Recommendations include providing isolation between application tiers using security groups. We recommend that you tightly control inbound traffic to reduce the attack surface of your EC2 instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
