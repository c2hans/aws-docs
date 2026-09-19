---
source_url: https://docs.aws.amazon.com/solutions/disaster-recovery-with-vmware-on-aws/index.html
---

---
title: 'Guidance for Disaster Recovery with VMware on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/disaster-recovery-with-vmware-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Disaster Recovery with VMware on AWS

Attain recovery point objectives with rapid failover and failback for VMware workloads

## Overview

This Guidance illustrates a disaster recovery approach for using VMware Cloud Disaster Recovery (VCDR) on AWS. A virtual appliance protects machines using a combination of VMware snapshot technology, including an orchestrator that manages the disaster recovery plan within AWS and a VMware Scale-Out File System that stores replicas of the virtual machines. In a disaster event, VCDR can recover protected virtual machines, especially if a Pilot Light mode is pre-established. The Pilot Light mode maintains a scaled-down warm standby environment, enabling faster recovery of critical applications. When the primary site is restored, VCDR orchestrates efficient failback, minimizing replication time.

## How it works

This architecture diagram shows how you can build a disaster recovery environment on AWS using VMware Cloud Disaster Recovery, a VMware-delivered disaster recovery as a service (DRaaS) offering that protects on-premises vSphere and VMware Cloud on AWS workloads.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/disaster-recovery-with-vmware-on-aws.pdf)

![Architecture diagram](/images/solutions/disaster-recovery-with-vmware-on-aws/images/disaster-recovery-with-vmware-on-aws-1.png)

1. **Step 1**: The disaster recovery as a service (DRaaS) Connector is a virtual appliance that helps you to protect VMware virtual machines through VMware APIs for Data Protection (VADP) snapshots. VADP uses the snapshot capabilities of VMware vSphere to enable backup without requiring downtime for virtual machines.
1. **Step 2**: The software as a service (SaaS) Orchestrator provides a disaster recovery orchestration service that operates within the AWS environment. This SaaS Orchestrator periodically evaluates the health and compliance of your disaster recovery plan so that your plan will function as intended when required.
1. **Step 3**: The VMware virtual machines are replicated using hypervisor snapshots and stored within the VMware Cloud Disaster Recovery (VCDR) Scale Out File System.
1. **Step 4**: In the event of a disaster, the protected VMware virtual machines will be recovered using the out-of-the-box orchestration capabilities of VCDR. If a VMware Cloud (VMC) on AWS Pilot Light environment is already established, the anticipated Recovery Time Objective (RTO) will be approximately minutes. Alternatively, the following tasks are required:
1. **Step 4a**: Deploy a VMC Software-Defined Data Center (SDDC) to be used as the recovery site.
1. **Step 4b**: Configure the minimal necessary user access and networking permissions.
1. **Step 5**: The Pilot Light mode enables the deployment of a smaller subset of SDDC hosts (minimum of 2 nodes) ahead of time, facilitating the recovery of critical applications with lower RTO requirements. The Pilot Light option allows you to reduce the total cost of the cloud infrastructure by maintaining a scaled-down version of a fully functional environment. This is done in a warm-standby state for core applications to remain readily available when a disaster event is triggered.
1. **Step 6**: When the original protected site is restored to an operational state, VCDR orchestrates the failback process, enabling the replication of only the delta changes to reduce the failback time. The VMC on AWS cluster can be scaled down to a 2-node Pilot Light configuration or even eliminated entirely, depending on the RTO requirements.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance combines compute, network, and storage capabilities to reduce the operational overhead associated with maintaining on-premises VMware clusters. It replaces the undifferentiated heavy lifting of manually configuring, managing, and maintaining clusters with a packaged approach that includes support and maintenance from both VMware and AWS. VMware delivers scheduled Software-Defined Data Center (SDDC) updates and emergency software patches with notifications, as well as auto-remediation of hardware failures. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance lets you deploy a Recovery SDDC in the VMware cloud (or add an existing SDDC for recovery) to use for recovery and testing of your recovery plans and for ransomware recovery. You can add hosts, clusters, new networks, request public IP addresses, configure NAT rules, and also delete the recovery SDDC. In the event of a disaster or ransomware attack, you can recover virtual machines from your protected site to your recovery SDDC. You can recover from the disaster when your production site is ready. For ransomware, you can repair the infected virtual machines in the isolated recovery SDDC environment and restore clean and validated virtual machines back to a production site. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance outlines the use of a dedicated, single-tenant cloud infrastructure supporting multiple VMware SDDCs. In this configuration, computing resources are exclusively allocated to a single customer or tenant, with up to 16 hosts for each cluster. These SDDCs are delivered using the latest high-performance computing and storage resources, optimized for high I/O workloads and featuring low-latency Non-Volatile Memory Express (NVMe)-based Solid-State Drives (SSDs). [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

With this Guidance, you have the ability to democratize advanced technologies through the management of the SDDC. This includes patch management and secure operations of the software stack, helping you and your team focus on your application layer rather than the software and underlying infrastructure. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance includes flexible storage options, such as a VMware Virtual SAN (vSAN) storage approach built on Non-Volatile Memory Express (NVMe) instance storage, allowing you to manage storage costs for your application. It also provides advanced data services like quality of service, snapshots, and third-party data protection, optimizing storage utilization and costs. Additionally, it supports custom-sized virtual machines and VMware-compatible operating systems. Lastly, the single-tenant bare metal AWS infrastructure can provide cost advantages over shared virtual resources by delivering dedicated computing and storage. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The AWS data centers that host the services in this Guidance are designed to offer a lower carbon footprint compared to traditional, on-premises data centers. In addition, this Guidance allows you to deploy a fully configured VMware SDDC cluster in under a few hours. Lastly, you can scale host capacity up and down in minutes, effectively minimizing the environmental impact of your workloads by dynamically adapting capacity based on demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
