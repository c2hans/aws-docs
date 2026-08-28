---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers.html
---

# Migrate Oracle Business Intelligence 12c to the AWS Cloud from on-premises servers
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers"></a>

*Lanre (Lan-Ray) showunmi and Patrick Huang, Amazon Web Services*

## Summary
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-summary"></a>

This pattern shows how to migrate [Oracle Business Intelligence Enterprise Edition 12c](https://www.oracle.com/business-analytics/business-intelligence/technologies/bi-enterprise-edition.html) from on-premises servers to the AWS Cloud by using AWS CloudFormation. It also describes how you can use other AWS services to implement Oracle BI 12c components that deliver high availability, security, flexibility, and the ability to dynamically scale.

For a list of best practices related to migrating Oracle BI 12c to the AWS Cloud, see the **Additional information** section of this pattern.

**Note**
It’s a best practice to run multiple test migrations before transferring your existing Oracle BI 12c data to the cloud. These tests help you fine tune your migration approach, identify and fix potential issues, and estimate downtime requirements more accurately.

## Prerequisites and limitations
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Secure network connectivity between your on-premises servers and AWS through either [AWS Virtual Private Network (AWS VPN)](https://aws.amazon.com/vpn/) services or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+ Software licenses for your Oracle operating system, Oracle BI 12c, Oracle Database, Oracle WebLogic Server, and Oracle HTTP Server

**Limitations **

For information about storage size limits, see the [Amazon Relational Database Service (Amazon RDS) for Oracle](https://aws.amazon.com/rds/oracle/features/) documentation.

**Product versions**
+ Oracle Business Intelligence Enterprise Edition 12c
+ Oracle WebLogic Server 12c
+ Oracle HTTP Server 12c
+ Oracle Database 12c (or newer)
+ Oracle Java SE 8

## Architecture
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-architecture"></a>

The following diagram shows an example architecture for running Oracle BI 12c components in the AWS Cloud:

![Example architecture for running Oracle BI 12c components in the AWS Cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8bb72df1-7546-4208-bc70-5789767e3600/images/aae8f8f3-8125-4868-a8e5-eac1cc42812f.png)

This diagram shows the following architecture:

1. Amazon Route 53 provides domain name service (DNS) configuration.

1. Elastic Load Balancing (ELB) distributes network traffic to improve the scalability and availability of the Oracle BI 12c components across multiple Availability Zones.

1. Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling groups host the Oracle HTTP Servers, Weblogic Admin server, and managed BI servers across multiple Availability Zones.

1. Amazon Relational Database Service (Amazon RDS) for Oracle database store BI Server metadata across multiple Availability Zones.

1. Amazon Elastic File System (Amazon EFS) is mounted to every Oracle BI 12c component for shared file storage.

**Technology stack**
+ Amazon Elastic Block Store (Amazon EBS)
+ Amazon Elastic Compute Cloud (Amazon EC2)
+ Amazon Elastic File System (Amazon EFS)
+ Amazon RDS for Oracle
+ AWS Certificate Manager (ACM)
+ Elastic Load Balancing (ELB)
+ Oracle BI 12c
+ Oracle WebLogic Server 12c
+ Oracle HTTP Server (OHS)

## Tools
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/?id=docs_gateway) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need, and quickly scale them up or down.
+ [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) helps you maintain application availability and allows you to automatically add or remove Amazon EC2 instances according to conditions you define.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
+ [Oracle Data Pump](https://docs.oracle.com/cd/B19306_01/server.102/b14215/dp_overview.htm) helps you move data and metadata from one database to another at high speeds.
+ [Oracle Fusion Middleware](https://www.oracle.com/middleware/technologies/business-intelligence-v12214-downloads.html) is a suite of application development tools and integration solutions to identity management, collaboration, and business intelligence reporting.
+ [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/#:~:text=OCI%20GoldenGate%20is%20a%20real,in%20the%20Oracle%20Cloud%20Infrastructure.) helps you design, run, orchestrate, and monitor your data replication and stream data processing solutions in the Oracle Cloud Infrastructure.
+ [Oracle WebLogic Scripting Tool (WLST)](https://docs.oracle.com/middleware/12213/cross/wlsttasks.htm) provides a command line interface that helps you horizontally scale out your WebLogic clusters.

## Epics
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-epics"></a>

### Assess the source environment
<a name="assess-the-source-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Gather software inventory information. | Identify versions and patch levels for each of your source technology stack’s software components, including the following:+ Oracle operating system<br />+ Oracle Database<br />+ Oracle BI 12c<br />+ Oracle WebLogic Server<br />+ Oracle HTTP Server<br />+ Java | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |
| Gather compute and storage inventory information. | In your source environment, review current and historical utilization metrics for the following:+ CPU usage<br />+ Memory usage<br />+ Storage usageMake sure that you account for historical spikes in usage. | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator, System Administrator |
| Gather information about the source environment’s architecture and its requirements. | Obtain a full understanding of your source environment’s architecture and its requirements, including knowledge of the following:+ Oracle WebLogic Server domain configuration<br />+ Clustering<br />+ Load balancing<br />+ Connectivity<br />+ Availability<br />+ Disaster recovery requirements | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |
| Identify Java Database Connectivity (JDBC) data sources. | Gather information about your source environment’s JDBC data sources and drivers for each database engine that it uses. | Migration Architect, Application Owner, Oracle BI Administrator, Database Engineer or Administrator |
| Gather information about environment-specific settings. | Collect information about settings and configurations that are specific to your source environment, including the following:+ Custom startup and shutdown scripts<br />+ Java and other environment variables<br />+ Certificates | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |
| Identify any dependencies on other applications. | Collect information about integrations in your source environment that create dependencies with other applications.Make sure that you identify any Lightweight Directory Access Protocol (LDAP) integrations and other networking requirements. | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |

### Design your target environment
<a name="design-your-target-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a high-level design document. | Create a target architecture design document. Make sure that you use the information that you collected when assessing your source environment to inform the design document. | Solutions Architect, Application Architect, Database Engineer, Migration Architect |
| Obtain approval for the design document. | Review the design document with stakeholders and obtain the required approvals. | Application or Service Owner, Solutions Architect, Application Architect |

### Deploy the infrastructure
<a name="deploy-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the infrastructure code in CloudFormation. | Create CloudFormation templates to provision your Oracle BI 12c infrastructure in the AWS Cloud.<br />For more information, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*.It’s a best practice to create modular CloudFormation templates for each Oracle BI 12c tier, rather than one large template for all of your resources. For more  information about CloudFormation best practices, see [8 best practices when automating your deployments with AWS CloudFormation](https://aws.amazon.com/blogs/infrastructure-and-automation/best-practices-automating-deployments-with-aws-cloudformation/) on the AWS Blog. | Cloud Infrastructure Achitect, Solutions Architect, Application Architect |
| Download the required software. | DDownload the following software along with the required versions and patches from the [Oracle website](https://www.oracle.com/):+ Java JDK8<br />+ Oracle WebLogic Server 12c<br />+ Oracle BI 12c | Migration Architect, Database Engineer, Application Architect |
| Prepare the installation scripts. | Create software installation scripts that run a silent install. These scripts simplify the deployment automation.<br />For more information, see [OBIEE 12c: How to Perform Silent Installation?](https://support.oracle.com/knowledge/Enterprise%20Performance%20Management%20and%20Business%20Intelligence/2267490_1.html) on the Oracle Support site. You need an Oracle Support account to view the documentation. | Migration Architect, Database Engineer, Application Architect |
| Create an Amazon EBS-backed Linux AMI for your web and application tiers. | 1. [Deploy and configure Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) for your web and application tiers. Make sure that the instances meet the prerequisites for running the following:Oracle operating system environment setupOracle operating system user account set upJava software installation<br />2. Create Amazon Machine Images (AMIs) of the instances and save copies for future use. For instructions, see [Create an Amazon EBS-backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) in the *Amazon EC2 User Guide for Linux Instances*. | Migration Architect, Database Engineer, Application Architect |
| Launch your AWS infrastructure by using CloudFormation. | Deploy your Oracle BI 12c web and application tiers in modules by using the CloudFormation templates that you created.<br />For instructions, see [Getting started with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html) in the *AWS CloudFormation User Guide*. | Cloud Infrastructure Architect, Solutions Architect, Application Architect |

### Migrate Oracle BI 12c to AWS by using a fresh installation
<a name="migrate-oracle-bi-12c-to-aws-by-using-a-fresh-installation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stage the required software. | Stage the required software in a location that is accessible to the Amazon EC2 instances. For example, you could stage the software in Amazon S3 or another Amazon EC2 instance that would be accessible to your web and application servers. | Migration Architect, Oracle BI Architect, Cloud Infrastructure Achitect, Solutions Architect, Application Architect |
| Prepare your repository database for Oracle BI 12c installation. | Create Oracle BI 12c schemas by running the [Oracle Repository Creation Utility (RCU)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Resources.RCU.html#Oracle.Resources.RCU.Installing) against a new [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) database instance. | Cloud Infrastructure Achitect, Solutions Architect, Application Architect, Migration Architect, Oracle BI Architect |
| Install Oracle Fusion Middleware 12c and Oracle BI 12c. | 1. Starting with one Amazon EC2 instance, install Oracle Fusion Middleware 12c infrastructure and OBIEE 12c. For more information, see the following sections of the *Oracle Fusion Middleware Enterprise Deployment Guide for Oracle Business Intelligence*:[Starting the infrastructure installer on BIHOST1](https://docs.oracle.com/middleware/bi12214/lcm/BIEDG/GUID-FD80C4C4-A2E9-4190-8B6A-7AD659D8FBE2.htm#SOEDG2197)[Installing Oracle Business Intelligence in preparation for an enterprise deployment](https://docs.oracle.com/middleware/bi12214/lcm/BIEDG/GUID-FD80C4C4-A2E9-4190-8B6A-7AD659D8FBE2.htm#BIEDG-GUID-19FB37DF-6ECD-4C0D-BC99-7997C8E670A3)Use Amazon EFS to host directories that will be shared among Oracle BI 12c cluster nodes.<br />2. Apply any required patches to the installation.<br />3. Create AMIs of the instances and save copies for future use. | Migration Architect, Oracle BI Architect |
| Configure your Oracle WebLogic Server domain for Oracle BI 12c. | Configure your Oracle BI 12c domain as a non-clustered deployment. <br />For more information, see [Configuring the BI Domain](https://docs.oracle.com/middleware/bi12214/lcm/BIEDG/GUID-FD80C4C4-A2E9-4190-8B6A-7AD659D8FBE2.htm#BIEDG-GUID-D4FC2F0A-88B0-453C-BF14-17D365018252) in the *Oracle Fusion Middleware Enterprise Deployment Guide for Oracle Business Intelligence*. | Migration Architect, Oracle BI Architect |
| Perform horizontal scale out of the Oracle BI 12c. | Horizontally scale out the single node to the desired number of nodes. <br />For more information, see [Scaling out Oracle Business Intelligence](https://docs.oracle.com/middleware/bi12214/lcm/BIEDG/GUID-B7BEA45C-A8C0-4591-B748-FC35C587DAE0.htm#BIEDG-GUID-B7BEA45C-A8C0-4591-B748-FC35C587DAE0) in the *Oracle Fusion Middleware Enterprise Deployment Guide for Oracle Business Intelligence*. | Migration Architect, Oracle BI Architect |
| Install Oracle HTTP Server 12c. | 1. Install Oracle HTTP Server 12c on the Oracle web tier Amazon EC2 instances. For instructions see [Install Oracle HTTP Server 12c](https://docs.oracle.com/en/middleware/idm/access-manager/12.2.1.4/tutorial-oam-install-ohswebgate/#install-oracle-http-server-12c) in *Install and configure Oracle HTTP Server for Oracle Access Management 12c*.<br />2. Apply any required patches to the installation.<br />3. Create AMIs of the instances and save copies for future use. | Migration Architect, Oracle BI Architect |
| Configure load balancers for SSL termination. | 1. Create or [import SSL certificates in ACM](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html).<br />2. [Associate the SSL certificates with ELB](https://aws.amazon.com/premiumsupport/knowledge-center/associate-acm-certificate-alb-nlb/). | Cloud Infrastructure Architect, Migration Architect |
| Migrate business intelligence metadata artifacts to AWS. | 1. Export Oracle Business Intelligence Application Archive (BAR) files from the on-premises Oracle BI 12c installation. To export the BAR files, use the [WebLogic Scripting Tool (WLST)](https://docs.oracle.com/middleware/bi12214/biee/BIESG/GUID-2989F6FC-5656-491C-A645-E7E5DB6C76DE.htm#BIESG933) to run the [exportServiceInstance](https://docs.oracle.com/middleware/bi12214/biee/BIESG/GUID-82E6AE36-7EC7-457A-A905-408C5751AF7D.htm#BIESG9372) command.<br />2. Import the on-premises BAR files into the AWS Oracle BI 12c installation. To import the BAR files, run the **importServiceInstance** WLST command.  | Migration Architect, Oracle BI Architect |
| Perform post-migration tasks. | After importing the BAR files, do the following:+ Configure any additional [JDBC data sources](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/wls/12c/04-ConfigDataSource/configds.htm).<br />+ Install drivers for other data sources like PostgreSQL, or Amazon Redshift.<br />+ Configure Oracle [LDAP](https://docs.oracle.com/middleware/12212/biee/BIESC/GUID-30F09EE4-A2DE-443D-BF24-CC401B6E13FD.htm#BIESC6128), [SSL](https://docs.oracle.com/middleware/1221/biee/BIESC/ssl.htm#BIESC374), [single sign-on (SSO)](https://docs.oracle.com/middleware/1221/biee/BIESC/sso.htm),  and [WebLogic security store](https://docs.oracle.com/middleware/12213/opss/JISEC/cfgauthr.htm#JISEC2291).<br />+ Configure AWS Identity and Access Management (IAM) policies.<br />+ Activate usage tracking.<br />+ Set up integrations to other systems.<br />+ Migrate any custom scripts. | Migration Architect, Oracle BI Architect |

### Test the new environment
<a name="test-the-new-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the new Oracle BI 12c environment. | Conduct end-to-end testing on the new Oracle BI 12c environment. Use automation as much as possible.<br />Example of testing activities include the following:+ Validating dashboards, reports, and URLs<br />+ User acceptance testing (UAT)<br />+ Operational acceptance testing (OAT)Conduct additional testing and validation as required. | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |

### Cut over to the new environment
<a name="cut-over-to-the-new-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Disconnect traffic to the on-premises Oracle BI 12c environment. | At the appointed cutover window, stop all traffic to the on-premises Oracle BI 12c environment. | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |
| Resynchronize the new Oracle BI 12c repository database with the source database. | Resynchronize the Amazon RDS Oracle Oracle BI 12c repository database with the on-premises database.<br />To synchronize the databases, you can either use an [Oracle Data Pump refresh](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.DataPump.html) or an [AWS DMS change data capture (CDC)](https://aws.amazon.com/blogs/database/migrating-oracle-databases-with-near-zero-downtime-using-aws-dms/). | Oracle BI Administrator, Database Engineer/Administrator |
| Switch your Oracle BI 12c URLs to point to the new AWS environment. | Update the Oracle BI 12c URLs on your internal DNS servers so that they point to the new AWS installation. | Migration Architect, Solutions Architect, Application Owner, Oracle BI Administrator |
| Monitor the new environment. | Monitor the new Oracle BI 12c environment by using any of the following tools:+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />+ [Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/)<br />+ [Oracle Enterprise Manager](https://www.oracle.com/enterprise-manager/) | Oracle BI Administrator, Database Engineer/Administrator, Application Administrator |
| Get sign-off on the project. | Review the testing results with stakeholders and obtain the required approvals to wrap up the migration. | Application Owner, Service Owner, Cloud Infrastructure Architect, Migration Architect, Oracle BI Architect |

## Related resources
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-resources"></a>
+ [Using the Oracle Repository Creation Utility on RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Resources.RCU.html) (*Amazon RDS User Guide*)
+ [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) (*Amazon RDS User Guide*)
+ [Oracle WebLogic Server 12c on AWS](https://d1.awsstatic.com/whitepapers/Oracle-WebLogic-12c-on-AWS.pdf) (AWS whitepaper)
+ [Deploying Oracle Business Intelligence for high availability](https://docs.oracle.com/middleware/1221/biee/BIESG/highavail.htm#BIESG1584) (Oracle Help Center)
+ [Oracle Business Intelligence Application Archive (BAR) Files](https://docs.oracle.com/middleware/bi12214/biee/BIESG/GUID-7FCD90A3-E005-49BF-902F-30FBF9B41B07.htm#BIESG2889) (Oracle Help Center)
+ [How to migrate OBI 12c between environments](https://support.oracle.com/knowledge/Enterprise%20Performance%20Management%20and%20Business%20Intelligence/2203360_1.html) (Oracle Support)

## Additional information
<a name="migrate-oracle-business-intelligence-12c-to-the-aws-cloud-from-on-premises-servers-additional"></a>

The following is a list of best practices related to migrating Oracle BI 12c to the AWS Cloud.

**Repository databases**

It’s a best practice to host Oracle BI 12c database schemas on an Amazon RDS for Oracle instance. This instance type provides cost-efficient and resizable capacity while automating administration tasks, such as hardware provisioning, database setup, patching, and backups.

For more information, see [Using the Oracle Repository Creation Utility on RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Resources.RCU.html) in the *Amazon RDS User Guide*.

**Web and application tiers**

[Memory optimized Amazon EC2 instances](https://aws.amazon.com/ec2/instance-types/) are often well suited for Oracle BI 12c servers. Whatever instance type you choose, make sure that the instances that you provision meet your system’s memory usage requirements. Also, make sure that you [configure a sufficient WebLogic Java Virtual Machine (JVM) heap size](https://docs.oracle.com/cd/E49933_01/server.770/es_install/src/tins_postinstall_jvm_heap.html#:~:text=The%20default%20JVM%20heap%20size%20for%20WebLogic%20is%203GB.,file%20for%20Linux%20or%20setDomainEnv.) based on your Amazon EC2 instance’s available memory.

**Local storage**

I/O plays an important part in the overall performance of your Oracle BI 12c application. Amazon Elastic Block Store (Amazon EBS) offers different storage classes that are optimized for different workload patterns. Make sure that you choose an Amazon EBS volume type that fits your use case.

For more information about EBS volume types, see [Amazon EBS features](https://aws.amazon.com/ebs/features/) in the Amazon EBS documentation.

**Shared storage**

A clustered Oracle BI 12c domain requires shared storage for the following resources:
+ Configuration files
+ Oracle BI 12c singleton data directory (SDD)
+ Oracle global cache
+ Oracle BI Scheduler scripts
+ Oracle WebLogic Server binaries

You can meet this shared storage requirement by using [Amazon EFS](https://aws.amazon.com/efs/), which provides a scalable, fully managed elastic Network File System (NFS) file system.

*Fine tuning shared storage performance*

Amazon EFS has two [throughput modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes): **Provisioned** and **Bursting**. The service also has two [performance modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes): **General Purpose** and **Max I/O**.

To fine tune performance, start by testing your workloads in the **General Purpose** performance mode and **Provisioned** throughput mode. Doing these tests will help you determine if those baseline modes are sufficient to meet your desired service levels.

For more information, see [Amazon EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html) in the *Amazon EFS User Guide*.

**Availability and disaster recovery**

It’s a best practice to deploy Oracle BI 12c components across multiple Availability Zones to protect those resources in the event of an Availability Zone failure. The following is a list of availability and disaster recovery best practices for specific Oracle BI 12c resources hosted in the AWS Cloud:
+ **Oracle BI 12c repository databases**: Deploy a multi-AZ Amazon RDS database instance to your Oracle BI 12crepository database. In a multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different AZ. Running an Oracle BI 12c repository database instance across Availability Zones can enhance availability during planned system maintenance and help protect your databases against instance and Availability Zone failures.
+ **Oracle BI 12c Managed Servers**: To achieve fault tolerance, it’s a best practice to deploy Oracle BI 12c system components on Managed Servers in an Amazon EC2 Auto Scaling Group configured to span multiple Availability Zones. Auto Scaling replaces faulty instances based on [Amazon EC2 health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html). In the event of an Availability Zone failure, Oracle HTTP Servers continue to direct traffic to Managed Servers in the functioning Availability Zone. Then, Auto Scaling launches instances to keep up with your host count requirements. Activating HTTP session state replication is recommended to help make sure that there’s a smooth failover of the existing sessions to the functioning Managed Servers.
+ **Oracle BI 12c Administration Servers:** To make sure that your Administration Server has high availability, host it in an Amazon EC2 Auto Scaling group configured to span multiple Availability Zones. Then, set the minimum and maximum size of the group set to **1**. If an Availability Zone failure occurs, Amazon EC2 Auto Scaling starts up a replacement Administration Server in an alternate Availability Zone. To recover any failed underlying hosts within the same Availability Zone, you can activate [Amazon EC2 Auto Recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html).
+ **Oracle Web Tier servers:** It’s a best practice to associate your Oracle HTTP Server with your Oracle WebLogic Server domain. For high availability, deploy your Oracle HTTP Server in an Amazon EC2 Auto Scaling group configured to aspen multiple Availability Zoness. Then, place the server behind an ELB elastic load balancer. To provide additional protection against host failure, you can activate Amazon EC2 Auto Recovery.

**Scalability**

The elasticity of the AWS Cloud helps you scale applications either horizontally or vertically in response to workload requirements.

*Vertical scaling*

To vertically scale your application, you can change the size and type of the Amazon EC2 instances that are running your Oracle BI 12c components. You don’t need to over-provision instances at the start of your deployment and incur unnecessary cost.

*Horizontal scaling*

Amazon EC2 Auto Scaling helps you horizontally scale your application by automatically adding or removing Managed Servers based on workload requirements.

**Note**
Horizontal scaling with Amazon EC2 Auto Scaling requires scripting skills and thorough testing to implement.

**Backup and recovery**

The following is a list of backup and recovery best practices for specific Oracle BI 12c resources hosted in the AWS Cloud:
+ **Oracle Business Intelligence metadata repositories:** Amazon RDS automatically creates and saves backups of your database instances. These backups are retained for a period of time that you specify. Make sure that you configure your Amazon RDS backup duration and retention settings based on your data protection requirements. For more information, see [Amazon RDS backup and restore](https://aws.amazon.com/rds/features/backup/).
+ **Managed Servers, Administration Servers, and Web Tier servers:** Make sure that you configure [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) based on your data protection and retention requirements.
+ **Shared storage:** You can manage backup and recovery for files stored in Amazon EFS by using [AWS Backup](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html). The AWS Backup service can also be deployed to centrally manage backup and recovery of other services, including Amazon EC2, Amazon EBS, and Amazon RDS. For more information, see [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) In the *AWS Backup Developer Guide*.

**Security and compliance**

The following is a list of security best practices and AWS services that can help you protect your Oracle BI 12c applications in the AWS Cloud:
+ **Encryption at rest:** Amazon RDS, Amazon EFS, and Amazon EBS all support industry standard encryption algorithms. You can use [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) to create and manage cryptographic keys and control their use across AWS services and in your applications. You can also configure [Oracle Transparent Data Encryption (TDE)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.AdvSecurity.html) on the Amazon RDS for Oracle database instance that’s hosting your Oracle BI 12c repository database.
+ **Encryption in transit:** It’s a best practice to activate either SSL or TLS protocols to protect data in transit between the various layers of your Oracle BI 12c installation. You can use [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/) to provision, manage, and deploy public and private SSL and TLS certificates for your Oracle BI 12c resources.
+ **Network security**: Make sure that you deploy your Oracle BI 12c resources in an Amazon VPC that has the appropriate access controls configured for your use case. Configure your security groups to filter inbound and outbound traffic from the Amazon EC2 instances that are running your installation. Also, make sure that you configure [Network Access Control Lists (NACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) that allow or deny traffic based on defined rules.
+ **Monitoring and logging**: You can use [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to track API calls to your AWS infrastructure, including your Oracle BI 12c resources. This functionality is useful when tracking changes to infrastructure or when conducting a security analysis. You can also use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to view operational data that can provide you with actionable insight into the performance and health of your Oracle BI 12c application. You can configure alarms and take automated actions based on those alarms, too. Amazon RDS provides additional monitoring tools, including [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) and [Performance Insights](https://aws.amazon.com/rds/performance-insights/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
