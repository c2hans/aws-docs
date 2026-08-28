---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/creating-a-database-on-amazon-rds-amazon-ec2-or-vmware-cloud-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Creating a database on Amazon RDS, Amazon EC2, or VMware Cloud on AWS
<a name="creating-a-database-on-amazon-rds-amazon-ec2-or-vmware-cloud-on-aws"></a>

 To migrate your data to AWS, you need a source database (either on-premises or in a data center) and a destination database in AWS. Based on your business needs, you can choose between using Amazon RDS for Oracle, or installing and managing the database on your own in Amazon EC2 instance. To help you choose the service that’s best for your business, see the following sections.

## Amazon RDS
<a name="amazon-rds"></a>

 Many customers prefer Amazon RDS for Oracle because it frees them to focus on application development. Amazon RDS automates time-consuming database administration tasks, including provisioning, backups, software patching, monitoring, and hardware scaling. Amazon RDS simplifies the task of running a database by eliminating the need to plan and provision the infrastructure, as well as install, configure, and maintain the database software.

 Amazon RDS for Oracle makes it easy to use replication to enhance availability and reliability for production workloads. By using the Multi-Availability Zone (AZ) deployment option, you can run mission-critical workloads with high availability and built-in automated failover from your primary database to a synchronously replicated secondary database. As with all AWS services, no upfront investments are required, and you pay only for the resources you use. For more information, see [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/).

 To use Amazon RDS, log in to your AWS account and start an Amazon RDS Oracle instance from the [AWS Management Console](https://aws.amazon.com/console/). A good strategy is to treat this as an interim migration database from which the final database will be created. Do not enable the Multi-AZ feature until the data migration is completely done, because replication for Multi-AZ will hinder data migration performance. Be sure to give the instance enough space to store the import data files. Typically, this requires you to provision twice as much capacity as the size of the database.

## Amazon EC2
<a name="amazon-ec2"></a>

 Alternatively, you can run an Oracle database directly on Amazon EC2, which gives you full control over setup of the entire infrastructure and database environment. This option provides a familiar approach, but also requires you to set up, configure, manage, and tune all the components, such as Amazon EC2 instances, networking, storage volumes, scalability, and security, as needed (based on AWS architecture best practices). For more information, see the [Advanced Architectures for Oracle Database on Amazon EC2](https://d1.awsstatic.com/whitepapers/aws-advanced-architectures-for-oracle-db-on-ec2.pdf) whitepaper for guidance about the appropriate architecture to choose, and for installation and configuration instructions.

### VMware Cloud on AWS
<a name="vmware-cloud-on-aws"></a>

 [VMware Cloud on AWS](https://www.vmware.com/products/vmc-on-aws.html) is the preferred service for AWS for all vSphere-based workloads. VMware Cloud on AWS brings the VMware software designed data center (SDDC) software to the AWS Cloud with optimized access to native AWS services. If your Oracle workload runs on VMware on-premises, you can easily migrate the Oracle workloads to the AWS Cloud using VMware Cloud on AWS.

 VMware Cloud on AWS has the capability to run [Oracle Real Application Clusters](https://www.oracle.com/database/real-application-clusters/) (RAC) workloads. It allows multi-cast protocols, and provides shared storage capability across VMs running in VMware Cloud on AWS SDDC. VMware provides native migration capabilities such as VMware VMotion and [VMware HCX](https://www.vmware.com/products/hcx.html) to move virtual machines (VMs) from on-premises to the VMware Cloud on AWS. Depending on Oracle workload performance patterns, service-level agreement (SLA), and the bandwidth availability, you can choose to migrate the VM either live or using cold migration methods.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
