---
source_url: https://docs.aws.amazon.com/solutions/network-security-on-aws/index.html
---

---
title: 'Guidance for Network Security on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/network-security-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Network Security on AWS

Protect your workloads by using cloud security services for VPC isolation and firewall rules

## Overview

This Guidance helps you design and implement security policies and controls across different levels of the networking stack to protect your resources from external or internal threats. Protecting your resources in this way helps you ensure their confidentiality, availability, integrity, and usability. This Guidance also demonstrates how to prevent, detect, and block anomalous network traffic based on monitoring of ingress or egress and lateral data movement.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/network-security-on-aws.pdf)

![Architecture diagram](/images/solutions/network-security-on-aws/images/network-security-on-aws-1.png)

1. **Step 1**: Expand your networks across AWS Regions and accounts that can be divided into isolated networks with segments. Each network segment will represent a routing domain, where you can provide additional security layers at the perimeter of each segment. External calls to the application destined for the web layer would come through the perimeter and must pass through a security device and access control list (ACL).
1. **Step 2**: Enforce strong security policies to encrypt data and preserve its integrity, accountability, and authenticity across your entire network.
1. **Step 3**: Inspect north (ingress)-south (egress) traffic, such as internet connectivity. You may also require inspection of east-west traffic, such as internal cross application or location. Visualize and analyze traffic with Amazon QuickSight dashboards.
1. **Step 4**: Set up AWS Firewall Manager rules for different environments to filter traffic at the perimeter using a Layer 3/4 firewall appliance.
1. **Step 5**: Protect access to your Amazon Virtual Private Clouds (Amazon VPCs) by creating VPC endpoints. These endpoints allow you to apply identity-based controls to your network resources and allow connectivity between workloads and networks. You can send your request and data through the internet without leaving the AWS network.
1. **Step 6**: Amazon GuardDuty analyzes your network logs through intelligent threat detection.
## Related content

- **Networking**

[Networking](https://aws.amazon.com/solutions/cloud-foundations/glossary/#Networking)

[Read usage guidelines](/solutions/guidance-disclaimers/)
