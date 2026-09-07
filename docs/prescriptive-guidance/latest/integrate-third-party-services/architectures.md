---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architectures.html
---

# Integration architectures
<a name="architectures"></a>

This section discusses individual architectures that you can use to integrate third-party services in the AWS Cloud.

To choose an architecture, these are the most important characteristics to consider:

1. **Direction of traffic** – Unidirectional or bidirectional

1. **Network protocol** – TCP or UDP

1. **Scalability** – Number of virtual private clouds (VPCs) that the third-party service must support

The following figure is a decision chart to help you select an architecture for integrating third-party services in the AWS Cloud.

![Decision tree to select implementation architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/2a55c7fd-6818-4ddd-8af6-47608573b103.png)

The following table compares the integration architectures discussed in this guide.

|
|
|   | Architecture 1: AWS PrivateLink | Architecture 2: VPC peering | Architecture 3.1: Transit Gateway with AWS RAM | Architecture 3.2: Transit Gateway peering |
| --- |--- |--- |--- |--- |
| **Routing type** | Direct peering | Direct peering | Central hubs with direct peering connections | Central hubs with direct peering connections |
| **Traffic is not exposed to the public internet** | Yes | Yes | Yes | Yes |
| **Typical implementation complexity** | Low | Low | High | High |
| **Typical architecture complexity** | Low | High | Medium | Medium |
| **Support for bidirectional traffic** | No | Yes | Yes | Yes |
| **Support for overlapping Classless Inter-Domain Routing (CIDR) blocks** | Yes | No | No | No |
| **Support for transitive routing** | No | No | Yes | Yes |
| **Support for inter-Region connections** | No | Yes | Yes | Yes |
| **Supported traffic types** | TCP | TCP and UDP | TCP and UDP | TCP and UDP |
| **Highly scalable** | Yes | No | Yes | Yes |
