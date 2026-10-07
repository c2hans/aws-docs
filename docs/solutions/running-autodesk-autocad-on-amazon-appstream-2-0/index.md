---
source_url: https://docs.aws.amazon.com/solutions/running-autodesk-autocad-on-amazon-appstream-2-0/index.html
---

---
title: 'Guidance for Running Autodesk AutoCAD on Amazon AppStream 2.0'
canonical_url: https://docs.aws.amazon.com/solutions/running-autodesk-autocad-on-amazon-appstream-2-0/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Running Autodesk AutoCAD on Amazon AppStream 2.0

## Overview

This Guidance helps customers build an Amazon AppStream 2.0 environment to deploy and stream [Autodesk AutoCAD](https://www.autodesk.com/products/autocad/overview) . Amazon AppStream 2.0 is a fully managed AWS end user computing (EUC) service that provides secure access to applications and virtual desktops to users. AutoCAD is a leading 2D and 3D computer aided design (CAD) drafting software created by Autodesk. By leveraging this Guidance, customers can accelerate the deployment of a high-performance and on-demand virtual desktop while spending less on expensive high-performance workstations and standardizing software and collaboration efforts.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/running-autodesk-autoCAD-on-amazon-appstream-2-0.pdf)

![Architecture diagram](/images/solutions/running-autodesk-autocad-on-amazon-appstream-2-0/images/running-autodesk-autocad-on-amazon-appstream-2-0-1.png)

1. **Step 1**: Users that need AutoCAD connect to the Amazon AppStream 2.0 fleet instances using a web browser or Amazon AppStream 2.0 Client Application for Windows.
1. **Step 2**: The AutoCAD application streams from the AppStream 2.0 fleet to the user.
1. **Step 3**: Generated AppStream 2.0 fleet instances use AutoCAD License Manger running on Amazon Elastic Compute Cloud (Amazon EC2) instances. When AppStream 2.0 instances are created, they consume licenses. When AppStream 2.0 instances are deprecated, they release the licenses.
1. **Step 4**: Each user has a private folder hosted on Amazon Simple Storage Service (Amazon S3) to persist application settings, user data, and files.
1. **Step 5**: Administrators use a public Windows Bastion Host running on Amazon EC2 to log on to instances in the private subnet.
1. **Step 6**: The AppStream 2.0 fleet is created in private subnets in two different Availability Zones to which users connect, either on an On-Demand or Always-On basis.
1. **Step 7**: Machine images created by AppStream 2.0 are provisioned in the private subnet that will be used in the generation of the AppStream 2.0 fleet.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch captures metrics for the managed services in this architecture. You can monitor these metrics for errors. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance provides a way to secure Amazon EC2 resources using public and private subnets and security groups to restrict traffic to the Bastion host. AppStream 2.0 provides built-in authentication capabilities. Review Amazon AppStream 2.0Integration with SAML 2.0 and Using Active Directory with AppStream 2.0 for information on setting up authentication with AppStream 2.0. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AppStream 2.0 offers two available fleet types. Always-On or On-Demand fleets automatically match the supply of available instances to user demand. Because one user requires one fleet instance, the size of your fleet determines the number of users who can stream concurrently. You can define scaling policies that adjust the size of your fleet automatically based on a variety of utilization metrics, and you can optimize the number of available instances to match user demand. This will need to be done in conjunction with the AutoCAD network license manager (NLM) license maximum allowed. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AppStream 2.0 is built to support desktop software application workloads. Based on the application, AutoCAD user persona, and rendered file sizes, you can experiment with larger or smaller instance sizes to match the best performance and price for your workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses AWS managed services that scale to match demand. Most of the services are also serverless, which reduces infrastructure management and idle resources so you don’t end up paying for resource you don’t use. The AutoCAD NLM does not provide a way to scale out on Amazon EC2 and will need to be manually handled using the Guidance’s recommendation of setting up an NLM and configuring the host file. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AppStream 2.0 is designed for on-demand usage of the application and is graphics hardware-dependent. Because the service can be provisioned on demand, resources are consumed only when needed, minimizing hardware usage. The Guidance uses only the minimal Amazon EC2 resources required for operations and to support AppStream 2.0 application license usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
