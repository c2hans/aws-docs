---
source_url: https://docs.aws.amazon.com/solutions/hosting-aveva-pi-system-on-aws/index.html
---

---
title: 'Guidance for Hosting AVEVA PI System on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/hosting-aveva-pi-system-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Hosting AVEVA PI System on AWS

## Overview

This Guidance demonstrates how to host AVEVA PI components in a resilient and highly available architecture on AWS, enabling advanced analytics. It utilizes Amazon Elastic Compute Cloud (Amazon EC2) to provision AVEVA PI components across multiple Availability Zones, helping to ensure fault tolerance and optimal performance. The Guidance showcases the migration of AVEVA PI systems to AWS and the configuration of PI components for resiliency and performance optimization. By implementing this Guidance, you can improve the resiliency, performance, and integration of your AVEVA PI implementation with modern analytic tooling on AWS.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/hosting-aveva-pi-system-on-aws.pdf)

![Architecture diagram](/images/solutions/hosting-aveva-pi-system-on-aws/images/hosting-aveva-pi-system-on-aws-1.png)

1. **Step 1**: PI Interfaces collect data from sensors, programmable logic controllers (PLCs), Supervisory Control And Data Acquisition (SCADA), and human machine interfaces (HMIs) and send this data into PI System components running on Amazon Elastic Compute Cloud (Amazon EC2) in AWS Outposts.
1. **Step 2**: PI Vision is a visualization tool to access, organize, and visualize PI System data and share data visualizations.
1. **Step 3**: PI Asset Framework (AF) and PI Data Archive store PI System data.
1. **Step 4**: Amazon EC2 hosts SQL Server on Outposts to store the metadata used by PI Vision and PI AF.
1. **Step 5**: Outposts connects to an Amazon Virtual Private Cloud (Amazon VPC) through a private, secure, and encrypted tunnel using AWS Direct Connect and AWS Site-to-Site VPN.
1. **Step 6**: AWS Network Firewall provides fine-grained control over network traffic entering the VPC.
1. **Step 7**: Host PI Vision in an Amazon EC2 Auto Scaling group to unify access across plants with visualizations and asset data. Scale the number of PI Vision nodes based on user demand.
1. **Step 8**: Serve PI components with high availability by distributing nodes and Amazon Elastic Block Store (Amazon EBS) volumes across Availability Zones. Stream data from Outposts into all nodes in the PI Collective.
1. **Step 9**: Test system resiliency using AWS Fault Injection Service.
1. **Step 10**: Centrally manage and automate data protection by storing PI Vision, PI AF, PI Data Archives and OS level backups on AWS Backup from the AWS Cloud and Outposts.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The PI Data Archive node stores critical business data on an EBS volume, enabling dynamic capacity scaling. Amazon CloudWatch monitors the unallocated space on the EBS volume, allowing administrators to proactively manage storage requirements. When low disk space is detected, data can be offloaded from the archive, or the EBS volume size can be increased on-demand. CloudWatch agent uploads message logs to CloudWatch, facilitating centralized logging and monitoring. CloudWatch metric filters and alerts seamlessly integrate with other AWS service notifications, streamlining operational visibility and incident response across the underlying infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Direct Connect provides private networking between edge locations and the AWS Cloud over a standard Ethernet fiber-optic cable. Site-to-Site VPN encrypts traffic traversing the Direct Connect link, adding an extra layer of protection. Network Firewall provides granular control over network traffic entering the VPC, employing deep packet inspection, stateful protocol detection, source IP address filtering, and target domain name restrictions. This multi-layered approach, combining private networking, encryption, and advanced traffic inspection, enables a robust defense-in-depth strategy for securing critical Operational Technology (OT) workloads in the cloud. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Fault Injection Service enables proactive testing of a system’s resilience by simulating various failure scenarios, such as node failures and network disruptions. This managed chaos engineering service facilitates regular fault injection experiments in non-production environments, helping identify and address potential configuration issues before they impact the business-critical production environment. Regular chaos testing with Fault Injection Service enhances the reliability of system deployment by helping ensure it can withstand and recover from various failure modes, minimizing the risk of unplanned outages and data loss incidents. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EBS provides a range of configurable storage options, allowing you to select the appropriate volume type based on their workload's performance requirements, usage patterns, and cost considerations. For high-performance, large-scale deployments, the io2 Block Express volume type offers up to 256,000 IOPS and a maximum volume size of 64 TiB, catering to the most demanding workloads. By matching the EBS volume type to your specific needs, you can optimize performance and efficiency while minimizing unnecessary costs associated with over-provisioning or under-provisioning storage resources. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS Backup provides a centralized and automated backup offering, eliminating the need for multiple backup tools and reducing operational overhead. By using automated backup scheduling, retention policies, and incremental backups, AWS Backup optimizes resource utilization and minimizes storage costs associated with backup and recovery operations. This streamlined approach to data protection not only simplifies backup management but also helps reduce the overall cost of maintaining a robust backup and recovery strategy, contributing to overall cost optimization efforts. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The PI Vision workload exhibits significant variability, with usage patterns fluctuating throughout the day, week, and based on the number of concurrent users. EC2 Auto Scaling dynamically adjusts the number of PI Vision nodes based on demand for optimal resource utilization. By automatically scaling the PI Vision node group up or down in response to these usage patterns, EC2 Auto Scaling minimizes energy consumption from idle or over-provisioned compute resources. This aligns your resource footprint with actual requirements, contributing to improved energy efficiency and reduced environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
