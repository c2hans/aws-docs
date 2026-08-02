---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/instance-types.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Instance types
<a name="instance-types"></a>

## Physical core requirements
<a name="physical-core-requirements"></a>

 SAS 9 and SAS Viya infrastructures require several SAS server types, depending on usage patterns. Each infrastructure has different and specific CPU, I/O throughput, and memory provisioning. Each instance contains a default number of virtual CUPs (vCPUs) that include CPU core and hyper threads for each core, which allows for multiple- threads to run concurrently on a single CPU core. The number of vCPUs helps determine the total number of physical cores required for SAS.

## Additional configurations
<a name="additional-configurations"></a>

 SAS servers require high I/O and sufficient bandwidth is required. You can obtain bandwidth through a dedicated network interface card (NIC) — additional CPUs and RAM may also be required.

### Multi-tenancy
<a name="multi-tenancy"></a>

 With a dedicated NIC, sharing the same with multi-tenant applications residing the same physical server can result in inferior performance for virtualized EC2 instances.

## Placement groups
<a name="placement-groups"></a>

 Ensure that all the instances and components of SAS are placed on the target infrastructure within the same Availability Zone (AZ) in an EC2 placement group. This is particularly useful for SAS workloads that require low-latency performance for node-to- node communication.

## SAS 9 systems
<a name="sas-9-systems"></a>

### SAS compute tiers \+ SAS grid node
<a name="sas-compute-tiers-sas-grid-node"></a>

 SAS compute and SAS grid nodes require a minimum of 8GM of physical RAM per core and robust I/O throughput.

 SAS WORK is a temporary library that is automatically defined by SAS at the beginning of each SAS session or job. The WORK library stores temporary SAS files that are created by users and is internally used by SAS. SAS UTILLOC is a temporary location for operations such as sorting, stats, multi-threaded processes which could have the same location as the WORK folder, but may be different.

 The following servers are recommended:
+  **I3 family** – EC2 I3 instances are the next generation of storage optimized instances for high transaction, low latency workloads. These instances include Non-Volatile Memory Express (NVMe) SSD-based instances storage optimized for high random I/O performance, high sequential read throughput, and high IOPS. Because of the high internal I/O bandwidth from striped NVMe SSD drives for SAS WORK and SAS UTILLOC, users should configure their environment to explicitly use the NVMe SSD local drives (not EBS volumes).
+  **I3en family** – This family provides Non-Volatile Memory Express (NVMe) SSD instance storage optimized on Amazon EC2 with enhanced networking via ENA to achieve up to 100 Gbps of network bandwidth.
+  **M5n family** – The M5 family provides a balance of compute, memory and networking. M5n instance variation are ideal for applications requiring improved network throughput and packet rate performance.

### Shared file system storage required for SAS grid
<a name="shared-file-system-storage-required-for-sas-grid"></a>

 These servers need robust I/O throughput to the permanent storage that supports the shared file system. They need 8 GM of RAM per physical core.
+  **M5 or M5dn family** — With M5dn instances that support 8 GB of RAM per physical core, local NVMe-based SSDs are physically connected to the host server and provide block-level storage for lifetime of the instance.

 Both instances types are suitable for workloads requiring a balance of compute, memory and networking resources.

### SAS mid-tier and metadata servers
<a name="sas-mid-tier-and-metadata-servers"></a>

 These servers do not require compute-intensive resources or robust I/O bandwidth, but they do require more memory than the SAS computing tiers. The recommendation is 24 GB of physical RAM, or 8 GB of physical Ram per physical core (whichever is larger).
+  **R5 or R5d family** – R5/R5d instances are suitable for memory intensive applications such as in-memory caches, mid-size in-memory databases and real- time big data analytics.

### SAS Viya node groups
<a name="sas-viya-node-groups"></a>

 Typically, SAS Viya deployments contain the following resource or node groups:
+  Cloud Analytics Services(CAS) node group
+  Stateless node group
+  Stateful node group
+  Compute node group
+  Default node group

 SAS Viya node groups are identified by the work the associated pods in the application perform. To manage the workload, node taints and labels are assigned to control scheduling.

In previous SAS Viya deployments (for example, 3.5 prior) SAS CAS nodes, SPRE, and microservices nodes were required and pricing was based on the number of processing cores. With the SAS Viya Kubernetes option, customers have the flexibility of cloud-native models, where they have to decide their solutions based on the number of users, types of users, and total revenue.

### Baseline resource recommendations
<a name="baseline-resource-recommendations"></a>

 As mentioned previously, SAS Viya pricing is based on the user profile, including the number and types of users. For example, the data scientist role might need SAS Visual Data Science, a different compute family of instances and their corresponding node groups, whereas a business analyst role might need SAS Visual Analytics and Data Preparation.

 For details on base line recommendations, refer to the [Costs and Licenses section in the Migrating SAS Viya to the AWS Cloud guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-viya/licensing.html).
