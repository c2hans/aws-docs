---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/overview.html
---

# Storage
<a name="overview"></a>

**Note**
Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

Traditional on-premises VMware vSphere–based environments rely on various storage options to meet workload requirements. Storage types range from block-and-file storage to specialized solutions like VMware vSAN. The following is a list of common storage types:
+ **Block storage –** Often used for Virtual Machine Disks (VMDKs) and Raw Device Mappings (RDMs). This type of storage provides fixed-sized blocks of data and is typically accessed through protocols like iSCSI or Fibre Channel.
+ **File storage –** Used for shared file systems and often implemented using Network File System (NFS) or Server Message Block (SMB) protocols. This storage type is used for virtual machine (VM) templates, ISO images, and data sharing between VMs.
+ **Object storage –** Often used for backups, archives, web content storage, and data lakes. Object storage for a VM isn't required in traditional on-premises VMware setups, but organizations may use this type for unstructured data backups.
+ **Local storage –** Used for high-performance workloads or cache tiers. This hypervisor storage type is physically attached to individual ESXi hosts.
+ **Virtual SAN (vSAN) –** Used for hyper-converged infrastructures, VM storage, and storage consolidation. This is a VMware software-defined storage pool that's physically attached to multiple ESXi hosts to create a distributed, shared datastore.

These on-premises storage types are often managed within the VMware vSphere environment and require capacity planning, performance tuning, and ongoing maintenance. Migrating to AWS helps to simplify these requirements by using cloud-native functionality. The following table maps traditional on-premises VMware storage types to their AWS equivalents.

|
|
| On-premises storage type | AWS storage service equivalent | Description |
| --- |--- |--- |
| Block storage (for example, SAN) | [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) | On-premises storage area network (SAN) maps to EBS, which provides persistent block-level storage volumes for use with EC2 instances. EBS offers multiple volume types for different performance needs, allowing organizations to match their on-premises SAN performance requirements. |
| File storage (for example, NAS, NFS) | [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) | NAS and NFS are equivalent to EFS, which provides scalable, elastic file storage that can be simultaneously accessed by multiple EC2 instances, mirroring the shared file system functionality of on-premises NAS. |
| Object storage | [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/pm/serv-s3/) | While less common in traditional VMware setups, object storage maps to S3, which offers scalable, durable storage that's suitable for unstructured data, backups, and archives. It provides features like versioning and lifecycle policies that may be unavailable in on-premises storage. |
| Local storage | [Amazon Elastic Compute Cloud (Amazon EC2) instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) | Physically attached storage in VMware environments maps to EC2 instance store. This provides temporary block-level storage and high I/O performance for specific use cases. |
| Virtual SAN (vSAN) | [Amazon EBS](https://aws.amazon.com/ebs/) or [Amazon S3](https://aws.amazon.com/pm/serv-s3), depending on use case | VMware's software-defined storage solution can be replaced by a combination of EBS or S3, depending on the use case. EBS provides block storage while S3 handles object storage. When combined, these AWS services offer a scalable alternative to vSAN. |
| Backup storage | [Amazon S3](https://aws.amazon.com/pm/serv-s3/) and [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/) | On-premises backup storage maps to S3 and Amazon Glacier. These services provide durable, cost-effective storage for backups and long-term archives. Amazon Glacier offers lower storage costs for infrequently accessed data. |

## Comparing VMware with AWS storage
<a name="comparing-vmware-with-9999999999999999aws--storage.79c1a8e5-8b7f-5825-abbf-6c4c9713d3e5"></a>

The following table highlights some of the storage differences between VMware's traditional on-premises approach and the AWS Cloud integrated approach.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Provisioning | Static provisioning of storage datastores or volumes based on capacity requirements, such as VMFS and vSAN | Dynamic provisioning with auto-scaling capabilities (S3 and EFS) and resizing (EBS) |
| Storage type | Uses underlying block storage through VMFS or vSAN | Object storage (S3), block storage (EBS), and file storage (EFS) |
| Cost Structure | On-premises VMware requires upfront costs for hardware and long-term management | Pay-as-you-go model with costs tied to usage, data transfer, and storage class |
| Scaling | Requires careful planning and manual scaling of storage | S3 and EFS scale automatically as data grows, with minimal intervention |
| Elasticity | Fixed physical storage allocations | Elastic storage that can automatically scale with demand |
| Global reach | Deployments typically restricted to on-premises data centers in specific geographical regions or data center locations | Global infrastructure allowing data storage and access from various AWS Regions worldwide |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
