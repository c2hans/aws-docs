---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/architecting-for-high-availability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecting for high availability
<a name="architecting-for-high-availability"></a>

 The following options have different approaches to high availability of Oracle databases.

## Amazon RDS
<a name="amazon-rds"></a>

 The Multi-AZ feature of Amazon RDS operates two databases in multiple Availability Zones with synchronous replication, thus creating a highly available environment with automatic failover. Amazon RDS has failover event detection, and initiates automated failover when failover events occur. You can also initiate manual failover through Amazon RDS API. Amazon RDS provides [SLA](https://aws.amazon.com/rds/sla/) with monthly uptime of 99.95%. A detailed under-the-hood blog post on Amazon RDS Multi-AZ capability is available [here](https://aws.amazon.com/blogs/database/amazon-rds-under-the-hood-multi-az/). Another option for Amazon RDS for Oracle is to use Oracle Active Data Guard. Customers should have their own license for the Oracle Active Data Guard option.

Amazon RDS for Oracle supports read replicas using Oracle Active Data Guard. Both Multi-AZ and Oracle Active Data Guard options are within the same AWS Region. [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/) supports Cross-Region Read Replicas with Oracle Active Data Guard. Amazon RDS for Oracle makes it easy to create physical standby DB instances in different AWS Regions from the primary DB instance. It fully manages the configuration of Active Data Guard, and replicates data over secure network connections between a primary DB instance and its replicas running across AWS Regions.

Amazon RDS for Oracle is also compatible with Oracle GoldenGate. You can choose to replicate the entire database or few tables and schemas with Oracle GoldenGate. Oracle GoldenGate is installed in a hub architecture in an EC2 instance and accesses the Amazon RDS for Oracle instance remotely. Oracle GoldenGate hub can replicate the data to another Amazon RDS for Oracle instance or Oracle database in Amazon EC2 or VMware Cloud on AWS within the same AWS Region. For cross-region instances, the recommended approach is to first replicate to an Oracle GoldenGate hub in another AWS Region.

## Amazon EC2
<a name="amazon-ec2"></a>

 Oracle databases on Amazon EC2 support Oracle Data Guard, Oracle Active DataGuard, and Oracle GoldenGate options as well. Third-party solutions available in AWS Marketplace also support replication for Oracle databases. Both Oracle and third-party solutions can be used to replicate databases within AWS Region and across AWS Regions as well. Oracle databases can be replicated from and to the customer’s on-premises data centers as well. AWS Database Migration Service can also be used to replicate all or a subset of tables.

## VMware Cloud on AWS
<a name="vmware-cloud-on-aws"></a>

 Since Oracle database is self-managed within VMware Cloud on AWS, all options including third-party agent-based replication are available. To replicate databases across AWS Regions or to the customer’s on-premises data center, Oracle Data Guard or Oracle GoldenGate can be used. VMware native technologies such as vMotion or Hybrid Cloud Extension (HCX) can be used to migrate databases between on-premises data centers and VMware Cloud on AWS. For large deployments involving multiple layers of application and database VMs, VMware Site Recovery Manager (SRM) can be considered to orchestrate replication and migration at site level.

## Oracle Real Application Cluster (RAC)
<a name="oracle-real-application-cluster-rac"></a>

 VMware Cloud on AWS has capability for multicast support and shared storage. Oracle RAC can be installed on VMware Cloud on AWS. Each Software-Defined Data Center (SDDC) in VMware Cloud on AWS can run at the minimum 3 AWS bare metal hosts and maximum of 16 AWS bare metal hosts. VMware Cloud on AWS can run SDDC in stretched cluster fashion across 2 different AWS AZ. This will also allow Oracle RAC to run in extended cluster mode, avoiding the need for a separate Oracle Data Guard setup.

VMware Cloud on AWS vSAN supports Oracle ASM. Oracle ASM disk group files are created out of VMDKs. The recommended allocation unit for Oracle ASM disk group for datafiles and log files should be 4 MB. This option is allowed during the creation of ASM disk group and cannot be modified later. For best performance, VMDK should have multi-writer flag enabled, and be provisioned for Eager Zero Thick. For more information on the Oracle RAC, refer to the [reference architecture diagram for Oracle RAC on VMware Cloud on AWS](https://d1.awsstatic.com/VMwareCloudonAWS/aws_reference_architecture_oracle_rac_on_vmware_cloud.pdf).

## FlashGrid Cluster
<a name="flashgrid-cluster"></a>

 FlashGrid Cluster is a virtual cloud appliance that provides all infrastructure capabilities required for running Oracle RAC on Amazon EC2. This includes multicast support and shared storage. For maximizing database uptime SLA, FlashGrid Cluster allows spreading Oracle RAC nodes across different availability zones. FlashGrid Cluster is delivered as an AWS CloudFormation template with fully automated deployment of all infrastructure components and Oracle software. FlashGrid software and support fees are billed through AWS Marketplace. FlashGrid architecture details are available in the [whitepaper](https://www.flashgrid.io/docs/FlashGrid_Oracle_RAC_on_AWS.pdf). To launch a FlashGrid Cluster with Oracle RAC visit the [product page](https://www.flashgrid.io/products/flashgrid-for-oracle-rac-on-aws/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
