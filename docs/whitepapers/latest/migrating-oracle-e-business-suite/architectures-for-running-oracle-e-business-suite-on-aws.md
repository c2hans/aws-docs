---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/architectures-for-running-oracle-e-business-suite-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architectures for running Oracle E-Business Suite on AWS
<a name="architectures-for-running-oracle-e-business-suite-on-aws"></a>

## High level architecture for running Oracle E-Business Suite on AWS
<a name="high-level-architecture-for-running-oracle-e-business-suite-on-aws"></a>

 The [Overview of Oracle E-Business Suite on AWS whitepaper](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/overview-oracle-e-business-suite.html) discusses various components of the Oracle E-Business Suite application tier, its interactions with AWS, and how the requests flow through those components. It also covers how to optimize HA for the Oracle database underlying the Oracle E-Business Suite.

 In addition, it discusses how to scale the Oracle E-Business Suite application tier by adding multiple application tier nodes and database replication using Oracle Data Guard.

 This whitepaper extends the same architecture and discusses a few other components that may require attention as part of your migration scenario.

![Reference architecture diagram showing running Oracle E-Business Suite on Amazon RDS Custom for Oracle, HA](https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/ref-arch-oracle-rds.png)

 In the preceding architecture, we have shown multiple application servers deployed across Availability Zones for high availability. Some application tier nodes may reside in a subnet acting as a perimeter network (external applications) as part of customer-facing applications, such as Oracle Internet Expenses module within E-Business Suite.

 You can enable [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (ALB) for both internal and external business users, and terminate SSL/TLS traffic at the ALB level. You can also incorporate an [AWS Web Application Firewall](https://aws.amazon.com/waf/) (AWS WAF) for another layer of security to protect against common web exploits and bots that can effect availability, compromise security, or consume excessive resources.

 You can use a [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS), or [Amazon FSx NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/), which are highly redundant and fully managed filesystems for the application filesystem, shared across Availability Zones.

 Lastly, to improve availability and achieve DR, you can provision a standby database instance in a different Region and use [AWS Backup](https://aws.amazon.com/backup/) service to configure backup policies, and monitor backup or restore activity for AWS services like Amazon EC2, Amazon RDS Custom for Oracle, Amazon EBS, Amazon FSx and Amazon S3 all in one place. With a few clicks in the AWS Backup console, you can automate your data protection policies and schedules.

 This paper now dives deeper into various database architectures for running Oracle E-Business Suite. You may choose different architectures for running Oracle Database, depending on the RTO, RPO, performance, and throughput requirements.

## Oracle E-Business Suite database tier on Amazon RDS Custom for Oracle or Amazon EC2
<a name="oracle-e-business-suite-database-tier-on-amazon-rds-custom-for-oracle-or-ec2"></a>

 Following is the deployment architecture for running Oracle database underlying Oracle E-Business Suite in an HA mode on [Amazon EC2](https://aws.amazon.com/ec2/), or [Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html) (RDS Custom). In this setup, there is a primary database instance running on Amazon EC2 or RDS Custom (Private subnet1/AZ1). You can select the compute or memory-optimized Amazon EC2/RDS Custom instance, depending on CPU and memory utilization metrics available as part of the migration assessment phase.

This instance may use [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) `io1` volumes to provide the Provisioned IOPS (PIOPS). Amazon EBS volumes can be provisioned from 4GiB up to 16TiB. Each volume provides up to 64K I/O operations per second (IOPS). On the other side of the spectrum, AWS has `io2` Block express volumes which can be from 4GiB to 64TiB per volume, with a maximum of 256K IOPS per volume. You can optionally use Oracle Automatic Storage Management (ASM) for striping and mirroring to achieve more IOPS and throughput than supported by a single EBS volume and for the HA at the database storage layer. Amazon RDS Custom manages the striping automatically using Logical Volume Management (LVM) across four underlying Amazon EBS volumes.

![Reference architecture diagram showing running Oracle on Amazon EC2/Amazon RDS Custom HA architecture](https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/ref-arch-oracle-ec2-rds.jpg)

 For additional availability and reporting offloading capability within the same Region, you can deploy another read-only standby database instance running on an Amazon EC2 instance in a different Availability Zone (private subnet2/Region1) using Oracle Active Data Guard. You can configure Parallel Concurrent Processing (PCP) for the Oracle E-Business Suite environment, and offload specific read-only reporting jobs to active standby database instances.

 This can reduce the load on the primary instance, and make the resources available for transactions and other read/write jobs. Refer to [Oracle Support Note \#2608030.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140550913995261&id=2608030.1&_adf.ctrl-state=ss7c2i22z_534) (sign-in required) for more details. While improving HA architecture within an AWS Region, you can extend a read-only standby database to another Region for DR purposes.

 Cross-Region replication for database can be configured using Oracle Data Guard Physical Standby. Refer to [Oracle Support Note \#1963472.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140532520639758&id=1963472.1&_adf.ctrl-state=ss7c2i22z_477) - Business Continuity for Oracle E-Business Suite Release 12.2 Using Oracle 12c (12.1.0.2) Physical Standby Database for more details (sign-in required). For 19c databases, refer to [Oracle Support Note \#2617788.1](https://support.oracle.com/epmos/faces/DocumentDisplay?id=2617788.1) - Business Continuity for Oracle E-Business Suite Release 12.2 on Oracle Database 19c Using Logical Host Names
