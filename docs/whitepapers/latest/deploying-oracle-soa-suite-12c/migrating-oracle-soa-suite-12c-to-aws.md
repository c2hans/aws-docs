---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/migrating-oracle-soa-suite-12c-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating Oracle SOA Suite 12c to AWS
<a name="migrating-oracle-soa-suite-12c-to-aws"></a>

 When migrating Oracle SOA Suite 12c to AWS, consider the architecture described in this whitepaper, perform a trial migration and validate it, then iterate one or two times before migrating to production. Review the migration approach to ensure the least amount of downtime for the business during the production cutover. Before starting the migration, you must create an [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) with the required subnets on AWS. You must also set up network connectivity from on-premises to AWS using a VPN connection or [AWS Direct Connect](https://aws.amazon.com/directconnect/).

 The following sections describe the process to migrate the various Oracle SOA Suite 12c components to AWS.

## Migrating the web and application tier
<a name="migrating-the-web-and-application-tier"></a>

 You can migrate the Oracle SOA Suite 12c Web and Application tier components to AWS using the following approaches.

### VM or server level migration
<a name="vm-or-server-level-migration"></a>

 You can migrate or clone the entire virtual machine (VM) or server hosting the Oracle SOA Suite 12c components using tools such as [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) (AWS MGN), the next generation of CloudEndure Migration. The following steps provide an overview of the migration process:

1.  Use AWS MGN (or a similar tool) to migrate the servers or VMs from the on-premises deployment. AWS MGN ensures the data is synchronized in real time and minimizes the cutover window.

1.  Use Amazon EFS as the shared storage mounted on the application tier nodes. Reconfigure Oracle WebLogic Server to use Amazon EFS for shared data such as the artifacts for Oracle Fusion Middleware, including Oracle home, Domain Home, Application Home, JTA Transaction Logs, and JMS Store for persisting the JMS messages.

1.  Migrate the [Oracle Metadata Services (MDS) Repository](https://docs.oracle.com/middleware/1213/core/ASADM/repos.htm#ASADM11533) as described in the *Migrating the Oracle MDS repository* section of this document.

1.  Update the metadata data source in WebLogic with the new database connection information of the Oracle Metadata Services (MDS) Repository.

1.  Open the WebLogic Administration Console to verify that the Domain, cluster, and managed servers are configured correctly.

1.  Configure the Web servers and ELB (Network Load Balancer and Application Load Balancer).

1.  Start the servers and test.

### Migration using Oracle Fusion Middleware utilities
<a name="migration-using-oracle-fusion-middleware-utilities"></a>

 The second option is to migrate the Oracle SOA Suite 12c components using the built-in Oracle Fusion Middleware utilities such as [copy binary](https://docs.oracle.com/en/middleware/fusion-middleware/12.2.1.3/asadm/copy-and-paste-binary-files-scripts1.html#GUID-97CFD814-A56C-447B-938E-B8CF9CDB04EF)/copy config, and paste binary/paste config. The following steps provide a high-level overview of migration. For more details, refer to [Overview of Procedures for Moving from a Source to a Target Environment](https://docs.oracle.com/middleware/1221/core/ASADM/testprod.htm#ASADM649) on the [Oracle Help Center](https://docs.oracle.com/en/).

1.  Launch the EC2 instances with Oracle Linux or a certified operating system for hosting the Oracle SOA Suite 12c components.

   1.  Apply the required prerequisite patches for Oracle SOA Suite 12c, including the security patches.

   1.  [Create an Amazon EBS-backed Linux Amazon Machine Image (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) and preserve the copy for future use.

1.  Install a new Oracle Home. You can also copy the Oracle Home binaries from the existing on-premises instance.

1.  Use [Copy binary](https://docs.oracle.com/en/middleware/fusion-middleware/12.2.1.3/asadm/copy-and-paste-binary-files-scripts1.html#GUID-97CFD814-A56C-447B-938E-B8CF9CDB04EF) and Copy Config commands on each application node to back up Oracle SOA Suite.

1.  Back up the web servers on each node.

1.  Back up the files on the on-premises NFS drive shared between the application tier nodes.

1.  Copy the backup of the Oracle SOA Suite files and the Web Servers to the respective instances on AWS.

1.  Restore the Oracle SOA Suite components using the paste library and paste config commands on the application tier nodes on AWS.

1.  Complete the Fusion Middleware steps for [Moving from a Test to a Production Environment](https://docs.oracle.com/middleware/1221/core/ASADM/testprod.htm#ASADM339). The RCU step is not required if you have already migrated the Oracle MDS Repository (refer to the [*Migrating the Oracle MDS Repository*](#migrating-the-oracle-mds-repository) section later in this document).

1.  Restore the Web Server backup on AWS.

1.  Mount the Amazon EFS share on the application tier nodes and copy the shared data from on-premises.

1.  Migrate the [Oracle MDS Repository](https://docs.oracle.com/middleware/1213/core/ASADM/repos.htm#ASADM11533). (Refer to the *Migrating the Oracle MDS repository* section of this document.)

1.  Update the metadata data source in WebLogic with the new database connection information of the MDS Repository.

1.  Open the WebLogic Administration Console to verify that the domain, cluster, and managed servers are configured correctly.

1.  Configure the Web servers and ELB (Network Load Balancer and Application Load Balancer).

1.  Start the servers and test.

### Migration using new installation and configuration
<a name="migration-using-new-installation-and-configuration"></a>

1.  Launch the EC2 instances with Oracle Linux or a certified operating system for hosting the Oracle SOA Suite 12c components.

   1.  Apply the required prerequisite patches for Oracle SOA Suite 12c, including the security patches.

   1.  [Create an Amazon EBS-backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) and preserve the copy for future use.

1.  Migrate the [Oracle MDS Repository](https://docs.oracle.com/middleware/1213/core/ASADM/repos.htm#ASADM11533). (Refer to the *Migrating the Oracle MDS repository* section of this document.)

1.  Install the Oracle Home.

1.  Mount the Amazon EFS share on the application tier nodes.

1.  Install Oracle SOA Suite 12c software on a single node.

1.  Configure an Oracle SOA Suite domain for each component (Oracle SOA, OSB, Oracle BPM, Oracle BAM, and Oracle ADF).

1.  Horizontally scale out to multiple nodes as per the requirements and complete the domain configuration.

1.  Configure data sources and JMS connection pools in WebLogic Server.

1.  Install the Web server and configure it (you can copy the configuration files from on-premises).

1.  Configure the Web servers and ELB (Network Load Balancer and Application Load Balancer).

1.  Start the servers and test.

## Migrating the Oracle MDS repository
<a name="migrating-the-oracle-mds-repository"></a>

 The steps for MDS Repository migration differ depending upon your database configuration.

### For databases on Amazon EC2
<a name="for-databases-on-amazon-ec2"></a>

 For initial data migration, copy the regular Oracle Recovery Manager (Oracle RMAN) backup files along with archive log files for recovery. Then, use [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) to synchronize the databases using change data capture (CDC). Refer to [Migrate an on-premises Oracle database to Oracle on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-oracle-on-amazon-ec2.html) for prescriptive guidance.

### For databases on Amazon RDS
<a name="for-databases-on-amazon-rds"></a>

 For initial migration, copy the export dump files taken from the on-premises database to restore on Amazon RDS using the import tools. Then, use AWS DMS to synchronize the databases using change data capture (CDC). Refer to [Migrate an on-premises Oracle database to Amazon RDS for Oracle](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html) for prescriptive guidance.
