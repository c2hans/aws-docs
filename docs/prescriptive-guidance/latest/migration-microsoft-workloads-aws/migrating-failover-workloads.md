---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/migrating-failover-workloads.html
---

# Migrating Windows failover clusters
<a name="migrating-failover-workloads"></a>

A [Microsoft failover cluster](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview) is a group of servers with mostly shared storage between them. You can use failover clusters to facilitate high availability for your applications and services. You can also migrate your failover clusters to the AWS Cloud to benefit from its reliability, performance, and lower TCO.

Windows failover clusters work differently in the cloud than in on-premises environments. It's important to note that only multi-subnet clusters can be deployed in the cloud. Unlike in on-premises environments, the IP address in a Windows failover cluster is assigned to an Elastic Network Adapter (ENA) rather than at the operating system level. In an on-premises environment, the operating system handles IP address assignment, but a cloud provider (AWS) handles the IP address assignment in the cloud. Because failover clustering is an operating system level feature it can't take control of the IP failover. Therefore, the same IP can't fail over between nodes. To work around that, you can use multi-subnet clusters where clusters fail over to a secondary IP. The secondary IP is assigned to ENA in another subnet and can come online. For more information, see [Failover Clustering Networking Basics and Fundamentals](https://techcommunity.microsoft.com/blog/failoverclustering/failover-clustering-networking-basics-and-fundamentals/1706005) in the Microsoft documentation.

Migrating a Windows failover cluster to AWS can be a complex process, but with careful planning and implementation it can be done with minimal disruption to your business operations. For example, every application is configured differently on a failover cluster, so it's imperative to understand its needs and then find out how they can be met in the cloud beforehand. The process involves the following steps:
+ Ensuring that all cluster nodes are running the same version of Windows and all necessary updates
+ Configuring the cluster quorum
+ Ensuring that all applications and data are backed up and can be restored during the migration

## Assess
<a name="migrating-failover-workloads-assess"></a>

The assess phase is a critical step in the process of migrating a failover cluster to AWS. During this phase, you gather information about your current environment, determine the feasibility of migrating to AWS, and identify any potential challenges or risks. We recommend that you follow these steps during the assess phase:
+ **Assess the readiness of your applications** – Determine whether your applications can be migrated to AWS without modifications or if they need to be updated or rewritten to take advantage of cloud-native services.
+ **Evaluate your networking and security requirements** – Determine your network and security requirements, including the configuration of firewalls, load balancers, and VPNs.
+ **Assess your data migration requirements** – Determine how your data gets migrated to AWS, including the size and location of your data, the time required for the migration, and any data transfer costs. In an on-premises environment, you might be using diverse storage technologies like JBOD, NAS, and SAN. Each one can present data to your application through different access methods, such as SAN Fiber Channel, iSCSI, SAS, or SMB/NFS shares.
+ **Identify potential risks and challenges** – Identify any potential risks or challenges that could impact the migration process, such as downtime, compatibility issues, or data loss.
+ **Estimate costs** – Estimate the cost of migrating to AWS, including the cost of Amazon EC2 instances, storage, data transfer, and any other AWS services required.
+ **Create a migration plan** – Based on the information gathered during the assess phase, create a detailed migration plan that includes timelines, required resources, and the steps involved in migrating to AWS.

### Evaluate your current environment
<a name="evaluate-your-current-environment.b6f99999-bf92-540e-8052-22716c1b66b8"></a>

Assess your current environment, including the hardware and software configurations, to determine what needs to be migrated to AWS. Identify any dependencies between applications, servers, and databases.

### Determine your migration strategy
<a name="determine-your-migration-strategy.cda8e403-7ba7-5bac-9c0c-0d3e40a00514"></a>

Consider your options for migrating to AWS, including a lift-and-shift approach or re-architecting your environment to take advantage of cloud-native services.
+ **Traditional failover cluster migration** – If you're manually configuring a Microsoft failover cluster from scratch, you can follow the instructions in [Deploy SQL Server on Amazon EC2](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/create-sql-server-on-ec2-instance.html). Shared storage is one of the most important considerations for a failover cluster migration. Amazon EBS multi-attach doesn't support SCSI-3 Persistent Reservation, but [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) and [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html) both work well as shared storage options. One of the most common use cases is using an Always On Failover Cluster Instance for a SQL Server cluster with Amazon FSx for Windows File Server. For more information, see the [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server/) post in the AWS Storage Blog. The next step is bringing the nodes to the cloud. This can be achieved by using AWS Transform MGN. For more information, see the [Migrating your Microsoft Windows clusters to AWS using CloudEndure Migration](https://aws.amazon.com/blogs/storage/migrating-your-microsoft-windows-clusters-to-aws-using-cloudendure-migration/#:~:text=Register%20for%20a%20CloudEndure%20account,for%20the%20replication%20to%20complete) post in the AWS Storage Blog. Then, you can configure a clustered role for your application to provide high availability.
+ **Migrating with virtually no downtime using a stretch cluster** – A stretch cluster could be a good fit** **if you have a business-critical application to migrate to the cloud and can't afford downtime. With a [Microsoft stretch cluster](https://learn.microsoft.com/en-us/windows-server/storage/storage-replica/stretch-cluster-replication-using-shared-storage), Site A and Site B must communicate with each other over a network but they can have their own individual shared storage. You can use this to your advantage in a migration scenario. For example, your source (whether it's on-premises or in another provider's cloud) can be Site A, which has network connectivity with an Amazon VPC where you deploy site B. After Site B is up and running, you can cut over to site B. The data replication mechanism is critical in this approach because your source storage technology might have limiting factors in terms of what replication method could work.
+ **Migrating a failover cluster deployed on VMware on-premises to VMware Cloud on AWS** – VMware Cloud on AWS has native support for SCSI-3 Persistent Reservation. This makes it possible to host a failover cluster on a virtual machine disk (VMDK) on VMware Cloud on AWS. For more information, see [Migrating SQL Server FCI cluster with shared disks to VMware Cloud on AWS](https://docs.vmware.com/en/VMware-Cloud-on-AWS/solutions/VMware-Cloud-on-AWS.919a954a9b6ca17cdc719ec42cda1401/GUID-E1F09B84241F7DD1DC702613CB717B2C.html) in the VMware documentation.
**Note**
As of April 30, 2024, VMware Cloud on AWS is no longer resold by AWS or its channel partners. The service will continue to be available through Broadcom. We encourage you to reach out to your AWS representative for details.
+ **Migrating a SQL Server FCI by using Amazon EBS Multi-Attach volume** – You can use Amazon EBS Multi-Attach and NVMe reservations to create SQL Server Failover Cluster Instances (FCIs) with Amazon EBS `io2` volumes as the shared storage on Windows Server failover clusters. These volumes can be attached only to instances that are in the same Availability Zone. Deploying Windows Server failover clusters by using Amazon EBS `io2` volumes requires the latest Windows drivers that translate SCSI reservation commands to NVMe reservation commands.  For more information about migrating your on-premises SQL Server FCI to AWS in a single Availability Zone by using this approach, see the AWS blog post [How to deploy a SQL Server failover cluster with Amazon EBS Multi-Attach on Windows Server](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-deploy-a-sql-server-failover-cluster-with-amazon-ebs-multi-attach-on-windows-server/).

The assess phase is critical for ensuring a successful migration of your failover cluster to AWS. If you take the time to gather information and identify potential challenges, you can develop a comprehensive migration plan that minimizes downtime, reduces risk, and ensures a smooth transition to AWS.

## Mobilize
<a name="migrating-failover-workloads-mobilize"></a>

During the migration of a failover cluster to AWS, the mobilize phase involves preparing the cluster for migration to AWS and testing it to ensure its functioning properly. The mobilize phase includes the following steps:

1. **Prepare the target environment** – In this step, you create the AWS resources needed to host the failover cluster. This involves setting up a VPC, subnets, security groups, and other necessary resources.

1. **Prepare the source environment** – In this step, you prepare the existing failover cluster for migration. This can involve making changes to the network configuration, configuring replication, or installing necessary software.

1. **Validate the cluster** – After both the source and target environments are prepared, you can perform a validation test to ensure that the cluster is functioning properly. This involves running a series of tests to ensure that the cluster can fail over to the target environment successfully.

1. **Create a replication link** – After the validation test, you can create a replication link between the source and target environments. This ensures that any changes made to the source environment are replicated to the target environment.

1. **Monitor replication** – After the replication link is established, monitor the replication process to ensure that all changes are being replicated properly.

1. **Fail over the cluster** – After verifying that replication is working correctly, perform the final failover to the target environment. This involves stopping the cluster services on the source environment and starting them on the target environment.

1. **Test the failover** – After the failover is complete, perform a test to ensure that the applications and services running on the cluster are functioning properly in the new environment

## Migrate
<a name="migrating-failover-workloads-migrate"></a>

Migrating a Microsoft failover cluster can be a complex process that requires careful planning and implementation to ensure a successful outcome. It's essential to thoroughly assess the existing environment, identify potential issues, and develop a comprehensive migration plan that includes testing and validation before making any changes to the production environment. During the migration phase, it's important to closely monitor the process and address any issues or unexpected behavior promptly. Communication and collaboration between all stakeholders— including IT teams, business users, and vendors—are crucial for a smooth migration process.

Additionally, it's important to consider the impact of the migration on any third-party applications or services that are running on the failover cluster. Identify any dependencies and test those applications thoroughly to ensure that they continue to function as expected after the migration. Another key aspect of the migration phase is to establish a rollback plan in case of any unforeseen issues or failures during the migration process. This plan ideally includes steps to revert the migration and restore the original environment, while minimizing any impact on the production environment.

Finally, after the migration is complete and the failover cluster is successfully running on the new environment, it's important to perform post-migration validation and testing to confirm that everything is working as intended. This includes monitoring performance, validating failover capabilities, and ensuring that all applications and services are functioning properly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
