---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/introduction.html
---

# Migrating perimeter zone applications to the AWS Cloud using AWS Network Firewall
<a name="introduction"></a>

*Sidharth Shah, Amazon Web Services*

A *perimeter zone* is a physical or logical subnetwork that contains and exposes applications and services to outside users (for example, untrusted users) and networks (for example, the internet). The purpose of a perimeter zone is to add an additional layer of security to your network. A perimeter zone can help you control the incoming and outgoing network traffic from your virtual private cloud (VPC).

This guide provides a network architecture and best practices to help you overcome the network security challenges of migrating applications that are hosted on an on-premises perimeter zone to the AWS Cloud. Organizations often divide a single application into frontend, backend, and database tiers, with the frontend tier placed in a perimeter zone and the other application components placed in a secured network. This guide presents a different approach to application architecture that's based on using AWS Network Firewall, AWS Transit Gateway, and Gateway Load Balancer.
