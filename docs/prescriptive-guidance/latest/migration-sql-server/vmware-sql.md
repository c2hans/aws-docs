---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/vmware-sql.html
---

# VMware Cloud on AWS for SQL Server
<a name="vmware-sql"></a>

**Note**
As of April 30, 2024, VMware Cloud on AWS is no longer resold by AWS or its channel partners. The service will continue to be available through Broadcom. We encourage you to reach out to your AWS representative for details.

[VMware Cloud on AWS](https://aws.amazon.com/vmware/) is an integrated cloud offering jointly developed by AWS and VMware. SQL Server easily integrates with VMware Cloud on AWS. This migration option makes it possible for you to build on your existing investment in virtualization.

You can access VMware Cloud on AWS on an hourly, on-demand basis or in subscription form. It includes the same core VMware technologies that you run in your data centers, including [vSphere Hypervisor](https://www.vmware.com/products/esxi-and-esx.html) (ESXi), [Virtual SAN](https://www.vmware.com/products/virtual-san.html) (vSAN), and the [NSX network virtualization platform](https://www.vmware.com/products/nsx.html), and is designed to provide an efficient, seamless experience for managing your SQL Server databases. You can scale the storage, compute, and memory of your SQL Server databases on VMware Cloud on AWS within minutes.

VMware Cloud on AWS runs directly on the physical hardware, but takes advantage of network and hardware features that were designed to support the AWS security-first infrastructure model. This means that the VMware virtualization stack runs on AWS infrastructure without having to use nested virtualization.

VMware Cloud on AWS makes it is easy to set up, scale, and operate your SQL Server databases workloads on AWS. It provides high availability solutions, integrates with on-premises Active Directory, and provides access to AWS services like AWS Directory Service for Microsoft Active Directory and AD Connector, Amazon Route 53, Amazon CloudWatch, and Amazon S3. You can store your backups in Amazon S3, and modernize and simplify your disaster recovery process.

## When to choose VMware Cloud on AWS
<a name="vmware-sql-choosing"></a>

VMware Cloud on AWS is an option for your SQL Server database when:
+ Your SQL Server databases are already running in an on-premises data center in a vSphere virtualized environment.
+ You have a large number of databases and you need fast migration (for example, only a few hours) to the cloud for one of the following reasons, without requiring any additional work from the migration team:
+ Data center extension. You need on-demand capacity to run virtualized desktops, to publish applications, or to provide a development or testing environment.
+ Disaster recovery. You want to set up a new disaster recovery system or replace your existing system.
+ Cloud migration. You want to migrate your entire data center to the cloud, or refresh your infrastructure.

If your SQL Server database requires more than 80K IOPS, you can use vSAN.

For more information, see [In the Works – VMware Cloud on AWS](https://aws.amazon.com/blogs/aws/in-the-works-vmware-cloud-on-aws/) on the AWS News blog, and [Deploy Microsoft SQL Server on VMware Cloud on AWS](https://aws.amazon.com/solutionspace/solutions/sql-server-vmware-cloud-on-aws/) on the AWS website.
