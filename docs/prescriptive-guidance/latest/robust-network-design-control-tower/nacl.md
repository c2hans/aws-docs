---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/nacl.html
---

# Network ACL configurations
<a name="nacl"></a>

A network access control list (network ACL) is a stateless service that validates both inbound and outbound traffic in case any traffic reaching the Application Load Balancer attempts a distributed denial of service attack (DDoS) or any other malicious activities.

To prevent access to the IP address or CIDR block, add a deny rule in both the inbound and outbound sections of the network ACL. In the network ACL, the rule number plays a crucial role in the evaluation of traffic. Be sure to place the deny rules with the appropriate rule number. For more information about network ACLs, see the [AWS Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-rules).
