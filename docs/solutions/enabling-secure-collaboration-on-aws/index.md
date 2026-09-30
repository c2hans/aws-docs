---
source_url: https://docs.aws.amazon.com/solutions/enabling-secure-collaboration-on-aws/index.html
---

---
title: 'Guidance for Enabling Secure Collaboration on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/enabling-secure-collaboration-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Enabling Secure Collaboration on AWS

## Overview

This Guidance helps you enable trusted communication for intellectual property (IP) design and data exchange in a secure environment. It includes a high-level architecture for well-optimized design environments to facilitate collaboration with third-party companies. Third-party companies may include foundries, independent software vendors (ISVs), and outsourced design services.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/enabling-secure-collaboration-on-aws.pdf)

![Architecture diagram](/images/solutions/enabling-secure-collaboration-on-aws/images/enabling-secure-collaboration-on-aws-1.png)

1. **Step 1**: The basis of a secure collaboration chamber is a primary design chamber built in an Amazon Virtual Private Cloud (Amazon VPC).
1. **Step 2**: Trusted users connect to their remote desktops over AWS Virtual Private Network (AWS VPN) or AWS Direct Connect.
1. **Step 3**: Third-party companies develop and test their IP in their own design chambers.
1. **Step 4**: To collaborate with third-party companies, create an Amazon VPC that will only be used for collaboration with infrastructure based on the primary design chamber. Create accounts, permissions, and remote desktop service endpoints for third-party remote desktops using AWS PrivateLink.
1. **Step 5**: Third-party companies connect to remote desktops in the collaboration chamber using the service endpoint in their design chamber.
1. **Step 6**: Curate data by using Amazon Simple Storage Service (Amazon S3) to transfer data in and out of the collaboration chamber. All Amazon S3 data transfers are logged in AWS CloudTrail for auditing. Third-party companies do not have access rights to transfer data out.
1. **Step 7**: Third-party users can access on-premises hardware, such as emulators, using routes to an isolated virtual local area network (VLAN) through AWS Transit Gateway and Direct Connect.
1. **Step 8**: When the collaboration is complete, you can delete the collaboration chamber.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Secure collaboration chambers allow the first-party company to work with numerous third-party companies so work can be done in parallel to achieve a faster time to market. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Collaboration on AWS allows customers to isolate design environments and separate third-party users. For example, if there is problem with an Electronic Design Automation (EDA) tool, a separate collaboration chamber is used to isolate access to only the data that is required to troubleshoot the problem with the EDA tool. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Customers can launch multiple design environments for reliability and scalability. You can provide multiple teams with secure access to the data required for the entire design workflow, and resources in the environment will scale accordingly. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Many hi-tech, electronics, and semiconductor customers have close relationships with third-party design companies and IP providers. The services in this architecture were selected to ensure collaboration across the entire workflow. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

As you collaborate across multiple IP providers and third-party designers, you only have to launch the VPCs (or collaboration chambers) that are required to complete the design of the integrated circuit. Launching the minimum resources required can help you save on costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture is scalable, allowing you to launch the exact number of collaboration chambers required to collaborate with third-party companies. This helps you avoid unused infrastructure and unnecessary resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
