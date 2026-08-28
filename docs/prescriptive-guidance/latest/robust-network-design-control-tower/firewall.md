---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/firewall.html
---

# Centralized network firewall
<a name="firewall"></a>

Deploy AWS Network Firewall in the firewall VPC. This VPC plays a crucial role by hosting the firewall that inspects traffic moving from source to destination and traffic coming from the internet.

## Firewall rule group
<a name="firewall-rule-group"></a>

Define custom rules or use existing AWS Managed Rules for monitoring and managing traffic that flows from the firewall VPC to the internet, and from the internet to the VPC. Based on your requirements, create either stateful or stateless rules:
+ **Stateful rules** – Traffic flow direction and other traffic approvals related to the packet are considered when inspecting packets.

  This rule group adheres to Suricata compatible intrusion prevention system (IPS) requirements. For more information, see the [Network Firewall documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-ips.html).

  Network Firewall also supports domain-traffic filtering. Traffic to the specific domains listed will be monitored using rules that are defined based on standard network attributes to control traffic flow.
+ **Stateless rules** – The stateless rules engine of the Network Firewall analyzes each packet separately for stateless rule groups. Firewalls for networks don't account for context such as traffic direction or other relevant packets.
+ **AWS Managed Rules rule groups** – When you use Network Firewall, you get access to AWS Managed Rules rule groups. These collections of preset, usable rules maintain up-to-date security. AWS updates the rule groups based on any new vulnerabilities or threats that are discovered.

## Firewall policy
<a name="firewall-policy"></a>

Create the firewall policy, which defines the monitoring and protection behavior of firewall based on the rules that you attach to the firewall policy. These rules can be managed rules provided by AWS or custom stateful or stateless rules that you created.

## Firewall
<a name="firewall"></a>

In the firewall VPC, create the firewall by using the firewall policy that you defined. Select the three subnets that are dedicated to the firewall (not the transit gateway subnets). After the firewall is created, make a note of the VPC endpoints created by Network Firewall.

Configure the firewall VPC transit gateway subnet destination of `0.0.0.0/0` to route traffic to these endpoints. While configuring endpoints, make sure that each transit gateway subnet is matched with its corresponding firewall endpoint subnet. Appropriate subnet mapping helps to ensure high availability of traffic routing and inspection.

## Firewall logging
<a name="firewall-logging"></a>

To help analyze traffic that is blocked by the network firewall, enable firewall logging. In addition to identifying unauthorized activities, firewall logging can help you analyze other activities that are happening inside and outside the VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
