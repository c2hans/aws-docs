---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-from-vmware-to-the-aws-cloud/on-premises-operational-analysis.html
---

# On-premises operational analysis
<a name="on-premises-operational-analysis"></a>

On-premises VMware environments encompass multiple components and can be broadly classified as virtualization, storage, networking, security, and operations. VMware environments require management of several key functions including:
+ Provisioning and managing virtual machines (VMs)
+ Implementing data protection strategies
+ Configuring virtual networks
+ Automating operational tasks
+ Ensuring compliance with organizational policies and industry regulations

This management approach helps organizations maintain control over their virtualized infrastructure while meeting security and operational requirements.

The following diagram shows a typical on-premises VMware environment and operational activities:
+ Customer applications can encompass VMs, datastores, port groups, and databases.
+ The self-managed VMware infrastructure supports bare metal compute, SAN and NFS storage, and network devices, all part of the data center hardware infrastructures.
+ During a migration to AWS, organizations need to establish new or modify existing operational functions. The AWS operations modernization framework encompasses 21 operational domains. These domains are grouped into four main functions: Core operations, security and control functions, business management functions, and supporting functions. For more information about these functions, see [Modernizing operations in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/guidelines-steps.html).
+ VCenter provides VMware platform management of multiple activities including:
  + VM management
  + Resource allocation and optimization
  + High availability and failover
  + Networking management
  + Storage management
  + Automation and orchestration
  + Monitoring and logging
  + Security and compliance

![Typical on-premises VMware environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-from-vmware-to-the-aws-cloud/images/guide-img/fa2c0c2d-160c-453b-9ba1-4a8c54d378c9/images/cccd8eeb-40c7-4ce5-b899-ca0d7a6c936a.png)

These functions can be categorized into multiple workstreams and tasks, each designed to support business operations within on-premises VMware infrastructures. Following are the common VMware operational workstreams and related tasks:
+ **Backup management** – Implement comprehensive backup and recovery operations. Tasks include daily virtual machine (VM) backups for critical systems, backup monitoring and troubleshooting, and retention policy management. Also includes the establishment of restore procedures with defined recovery point objectives (RPOs) for different workloads.
+ **Storage management** – Oversee storage infrastructure management. Tasks include vSAN datastore provisioning and administration for VM workloads, while maintaining robust data protection and disaster recovery measures to ensure business continuity.
+ **Network management** – Manage comprehensive network operations. Tasks include vSwitch configuration (standard and distributed), traffic management (vMotion, VM, and management), and virtual network administration.
+ **Virtualization and compute** – Oversee comprehensive VMware operations, such as VM provisioning, ESXi, and vCenter management. Also included are tasks such as performance monitoring, resource optimization, and capacity planning to maintain optimal infrastructure efficiency.
+ **Automation and management** – Streamline infrastructure operations through automated provisioning and lifecycle management processes, incorporating self-service capabilities to empower users.
+ **Monitoring** – Oversee centralized monitoring system for events and logs throughout the VMware environment. Tasks include implementing proactive troubleshooting measures across the infrastructure stack to ensure continuous operational efficiency.
+ **Security and compliance** – Oversee the security posture of the on-premises VMware infrastructure. Tasks are achieved through comprehensive identity and access management, while ensuring compliance with industry regulations and organizational security policies for the virtualized environment.
+ **Data center infrastructure** – Oversee the data center infrastructure that hosts the VMware environment through comprehensive management of physical components, ensuring optimal functioning and regular maintenance of critical systems. Examples of components include blade chassis systems, power supply units, and rack enclosures.
+ **Application support** – Maintain and support the full stack of virtualized workloads, while optimizing their performance and ensuring continuous availability. Examples of virtualized workloads are applications, operating systems, and databases operating within the VMware environment.
+ **Capacity planning** – Oversee hardware capacity management by monitoring and optimizing critical resources such as storage, CPU, RAM, and network infrastructure. Ensure efficient resource allocation while maintaining sufficient capacity for both planned operations and emergency requirements.
+ **Asset/vendor and license management** – Oversee hardware refreshment initiatives, maintain comprehensive inventory management, and track licensing requirements for the VMware infrastructure and related components. The purpose is to help ensure operational continuity and that compliance standards are met.
+ **Hardware management** – Manage and maintain the physical infrastructure that supports the VMware environment. Tasks include comprehensive hardware support, regular maintenance, and prompt issue resolution to support continuous optimal performance of the underlying systems.
+ **IT operations** – Function as the primary support interface for the VMware environment. Tasks include addressing business IT requirements and resolving technical queries while ensuring operational continuity and maintaining alignment between IT services and business needs.
+ **Account management** – Oversee financial management of the VMware infrastructure. Tasks include billing administration, cost allocation, and expenditure tracking, while providing accurate reporting and transparency of IT costs to respective business units and stakeholders.

Although specific workstream activities may differ across organizations, the fundamental objectives remain consistent. By transitioning from on-premises VMware to the AWS Cloud, organizations can capitalize on cloud advantages, achieving enhanced agility, improved scalability, and optimized cost management.

This guide discusses AWS services that align with your VMware workstreams. With this background, you can make informed decisions and develop comprehensive migration plans for a confident transition to the AWS Cloud.
