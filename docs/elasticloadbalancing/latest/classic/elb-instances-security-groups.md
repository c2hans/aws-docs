---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-instances-security-groups.html
---

# Security groups for the instances for your Classic Load Balancer
<a name="elb-instances-security-groups"></a>

A *security group* acts as a firewall that controls the traffic allowed to and from one or more instances. When you launch an EC2 instance, you can associate one or more security groups with the instance. For each security group, you add one or more rules to allow traffic. You can modify the rules for a security group at any time; the new rules are automatically applied to all instances associated with the security group. For more information, see [Amazon EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

The security groups for your instances must allow them to communicate with the load balancer. The following table shows the recommended inbound rules.

| Source | Protocol | Port Range | Comment |
| --- | --- | --- | --- |
| {{load balancer security group}} | TCP | {{instance listener}} | Allow traffic from the load balancer on the instance listener port |
| {{load balancer security group}} | TCP | {{health check}} | Allow traffic from the load balancer on the health check port |

We also recommend that you allow inbound ICMP traffic to support Path MTU Discovery. For more information, see [Path MTU Discovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html#path_mtu_discovery) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
