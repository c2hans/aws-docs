---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/network-firewall-proxy-developer-guide.html
---

# AWS Network Firewall Proxy Developer Guide
<a name="network-firewall-proxy-developer-guide"></a>

## Overview of Network Firewall Proxy
<a name="overview-network-firewall-proxy"></a>

**Note**
Network Firewall Proxy is in public preview release and is subject to change.

AWS Network Firewall proxy is an AWS managed service that offers granular security controls to inspect and filter your AWS Virtual Private Cloud (VPC) outbound connections to prevent data exfiltration and malware intrusion. For more information on Virtual Private Clouds, see [here](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

The proxy acts as an intermediary between your workloads and the internet, inspecting and filtering traffic to comply with your security policies. You can configure your applications to route HTTP and HTTPS traffic via the Proxy. You can set appropriate security policies in your proxy to define the trust perimeter for your clients and describe what response is acceptable from the destinations. Your proxy filters both the outbound requests from your clients and the inbound response from the allowed destinations based on the security policies you set.

You can choose to configure your proxy to decrypt HTTPS traffic and filter it based on any of the header attributes including the URL path, header verb, and other attributes.

Network Firewall proxy is a fully managed system that is built with scale and resilience. You can use it to eliminate the operational overhead of maintaining custom DIY proxy solutions and complex logging systems. It provides centralized control and visibility into all outbound web and inter-network communication.

## Key benefits and Use Cases
<a name="proxy-key-benefits-use-cases"></a>

1. Security Compliance & Auditing - Addresses security and compliance requirements for outbound web and inter-network traffic. Provides comprehensive visibility into traffic VPC outbound traffic.

1. Provides tight access control by verifying source clients using VPC ID, VPC endpoint ID, account ID, and IP CIDR.

1. Manages which domains and subdomains applications can be accessed by workloads, including allowlisting and denylisting capabilities. Blocks unnecessary outbound traffic. Provides HTTP method restrictions.

1. Actively blocks DNS tunneling attempts to prevent unauthorized data exfiltration, while implementing robust domain validation to guard against SNI spoofing attacks.

1. Filters response traffic based on content type and length.

1. Provides TLS interception capabilities.

1. Reduces maintenance and scaling overheads of maintaining DIY proxy solutions.

## Glossary and key terms
<a name="proxy-glossary-key-terms"></a>

Understanding these key terms will help you work effectively with Network Firewall Proxy.

**AWS NAT Gateway**
AWS service that allows resources in your private subnets to securely communicate with external destinations, including the internet, while protecting them against any unsolicited traffic.

**Virtual private cloud (VPC)**
A logically isolated virtual network to host your resources.

**Proxy configuration**
A Proxy Configuration defines the monitoring and protection behavior for a Proxy. The details of the behavior are defined in the rule groups that you add to your configuration.

**Phases**
Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. They are:

1. Pre-DNS - before domain resolution.

1. Pre-request - after DNS, before request.

1. Post-response - after receiving response.

**Rule Groups**
Collections of related proxy filtering rules. Rule groups help you manage and reuse sets of rules across multiple proxy configurations.

**Rules**
Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). Evaluation of rules happens in this same order as phases.

**Proxy**
Attaches a Proxy configuration to a NAT Gateway.

**Conditions**
Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against.

**Insert Position**
The priority order of rules within each phase type. Lower numbers have higher priority and are evaluated first.

**Private Link endpoints**
AWS PrivateLink is a highly available, scalable technology that you can use to privately connect your VPC to services and resources, as if they were in your VPC. For more information, check [here](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html).

**DNS Exfiltration**
A technique used to transfer data out of a secured network by encoding that data into DNS queries.

**SNI (Server Name Indication)**
An extension of the TLS protocol that indicates the hostname being contacted by the client during the TLS handshake, allowing servers to present the appropriate SSL certificate when hosting multiple domains on a single IP address.

**TLS Intercept**
The process of decrypting and re-encrypting TLS traffic for inspection and filtering on HTTP headers.

**Trust Perimeter**
The boundary between trusted internal networks and untrusted external networks.

**URI Path**
The specific location of a resource within a domain.
