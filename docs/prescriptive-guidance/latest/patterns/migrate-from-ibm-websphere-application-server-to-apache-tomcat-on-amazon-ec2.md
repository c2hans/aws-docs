---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2.html
---

# Migrate from IBM WebSphere Application Server to Apache Tomcat on Amazon EC2
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2"></a>

*Neal Ardeljan and Afroz Khan, Amazon Web Services*

## Summary
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-summary"></a>

This pattern walks you through the steps for migrating from an on-premises Red Hat Enterprise Linux (RHEL) 6.9 or later system that’s running IBM WebSphere Application Server (WAS) to RHEL 8 running Apache Tomcat on an Amazon Elastic Compute Cloud (Amazon EC2) instance.

The pattern can be applied to the following source and target versions:
+ WebSphere Application Server 7.x to Apache Tomcat 8 (with Java 7 or later)
+ WebSphere Application Server 8.x to Apache Tomcat 8 (with Java 7 or later)
+ WebSphere Application Server 8.5.5.x to Apache Tomcat 9 (with Java 8 or later)
+ WebSphere Application Server 8.5.5.x to Apache Tomcat 10 (with Java 8 or later)

## Prerequisites and limitations
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-prereqs"></a>

**Prerequisites****  **
+ An active AWS account
+ Source Java code, with the following assumptions:
  + Uses the Java Development Kit (JDK) version of Java 7 or later
  + Uses the Spring or Apache Struts framework
  + Doesn't use the Enterprise Java Beans (EJB) framework or any other WebSphere server functionality that's not readily available for Tomcat
  + Primarily uses servlets or Java Server Pages (JSPs)
  + Uses Java Database Connectivity (JDBC) connectors to connect to databases
+ Source IBM WebSphere Application Server version 7.x or higher
+ Target Apache Tomcat version 8.5 or higher

## Architecture
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-architecture"></a>

** ****Source technology stack**
+ A web application built using the Apache Struts Model-View-Controller (MVC) framework
+ A web application running on IBM WebSphere Application Server version 7.x or 8.x
+ A web application that uses a Lightweight Directory Access Protocol (LDAP) connector to connect to an LDAP directory (iPlanet/eTrust)
+ An application that uses IBM Tivoli Access Manager (TAM) connectivity to update the TAM user password (in the present implementation, applications use PD.jar)

** ****On-premises databases**
+ Oracle Database 21c (21.0.0.0)
+ Oracle Database 19c (19.0.0.0)
+ Oracle Database 12c Release 2 (12.2.0.1)
+ Oracle Database 12c Release 1 (12.1.0.2)

**Target technology stack**
+ Apache Tomcat version 8 (or later) running on RHEL on an EC2 instance
+ Amazon Relational Database Service (Amazon RDS) for Oracle

For more information about the Oracle versions supported by Amazon RDS, see the [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/) website.

**Target architecture**

![Architecture for migrating from IBM WebSphere to Apache Tomcat on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/96f91201-e0a6-4d3f-a94e-7bd68a59cc4e/images/11afe7c0-b400-423b-9dfe-02a915fe47ff.png)

## Tools
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-tools"></a>
+ Application tier: Rebuilding Java application into a WAR file.
+ Database tier: Oracle native backup and restore.
+ Apache Tomcat migration tool for Jakarta EE. This tool takes a web application written for Java EE 8 that runs on Apache Tomcat 9 and converts it automatically to run on Apache Tomcat 10, which implements Jakarta EE 9.

## Epics
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Complete the application discovery, current state footprint, and performance baseline. |  | BA, Migration Lead |
| Validate the source and target database versions. |  | DBA |
| Identify the hardware requirements for the target server EC2 instance. |  | DBA, SysAdmin |
| Identify storage requirements (storage type and capacity). |  | DBA, SysAdmin |
| Choose the proper EC2 instance type based on capacity, storage features, and network features. |  | DBA, SysAdmin |
| Identify the network access security requirements for the source and target databases. |  | DBA, SysAdmin |
| Identify the application migration strategy and tooling. |  | DBA, Migration Lead |
| Complete the migration design and migration guide for the application. |  | Build Lead, Migration Lead |
| Complete the application migration runbook. |  | Build Lead, Cutover Lead, Testing Lead, Migration Lead |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). |  | SysAdmin |
| Create the security groups. |  | SysAdmin |
| Configure and start Amazon RDS for Oracle. |  | DBA, SysAdmin |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create or obtain access to the endpoints to fetch the database backup files. |  | DBA |
| Use the native database engine or a third-party tool to migrate database objects and data. | For details, see "Migrating database objects and data" in the *Additional information *section. | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Lodge the change request (CR) for migration. |  | Cutover Lead |
| Obtain the CR approval for migration. |  | Cutover Lead |
| Follow the application migration strategy per the application migration runbook. | For details, see "Setting up the application tier" in the *Additional information* section. | DBA, Migration Engineer, App owner |
| Upgrade the application (if necessary). |  | DBA, Migration Engineer, App owner |
| Complete the functional, non-functional, data validation, SLA, and performance tests. |  | Testing Lead, App Owner, App Users |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Obtain signoff from the application owner or business owner. |  | Cutover Lead |
| Switch the application clients to the new infrastructure. |  | DBA, Migration Engineer, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down temporary AWS resources. |  | DBA, Migration Engineer, SysAdmin |
| Review and validate the project documents. |  | Migration Lead |
| Gather metrics such as time to migrate, percentage of manual versus automated tasks, and cost savings. |  | Migration Lead |
| Close out the project and provide feedback. |  | Migration Lead, App Owner |

## Related resources
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-resources"></a>

**References**
+ [Apache Tomcat 10.0 documentation](https://tomcat.apache.org/tomcat-10.0-doc/index.html)
+ [Apache Tomcat 9.0 documentation](https://tomcat.apache.org/tomcat-9.0-doc/index.html)
+ [Apache Tomcat 8.0 documentation](https://tomcat.apache.org/tomcat-8.0-doc)
+ [Apache Tomcat 8.0 installation guide](https://tomcat.apache.org/tomcat-8.0-doc/setup.html)
+ [Apache Tomcat JNDI documentation ](https://tomcat.apache.org/tomcat-8.0-doc/jndi-datasource-examples-howto.html)
+ [Amazon RDS for Oracle website](https://aws.amazon.com/rds/oracle/)
+ [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/)
+ [Oracle and Amazon Web Services](https://aws.amazon.com/oracle/)
+ [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)
+ [Amazon RDS Multi-AZ Deployments](https://aws.amazon.com/rds/details/multi-az/)

**Tutorials and videos**
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)

## Additional information
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-additional"></a>

**Migrating database objects and data**

For example, if you're using native Oracle backup/restore utilities:

1. Create the Amazon Simple Storage Service (Amazon S3) backup for database backup files (optional).

1. Back up the Oracle DB data to the network shared folder.

1. Log in to the migration staging server to map the network share folder.

1. Copy data from the network share folder to the S3 bucket.

1. Request an Amazon RDS Multi-AZ deployment for Oracle.

1. Restore the on-premises database backup to Amazon RDS for Oracle.

**Setting up the application tier**

1. Install Tomcat 8 (or 9/10) from the Apache Tomcat website.

1. Package the application and shared libraries into a WAR file.

1. Deploy the WAR file in Tomcat.

1. Monitor the start log to `Linux cat` any missing shared libraries from WebSphere.

1. Watch the start record to `Linux cat` any WebSphere-specific deployment descriptor extensions.

1. Collect any missing dependent Java libraries from the WebSphere server.

1. Amend WebSphere-specific deployment descriptor elements with Tomcat-compatible equivalents.

1. Rebuild the WAR file with the dependent Java libraries and updated deployment descriptors.

1. Update the LDAP configuration, database configuration, and test connections (see [Realm Configuration HOW-TO](https://tomcat.apache.org/tomcat-8.0-doc/realm-howto.html) and [JNDI Datasource HOW-TO](https://tomcat.apache.org/tomcat-8.0-doc/jndi-datasource-examples-howto.html) in the Apache Tomcat documentation).

1. Test the installed application against the restored Amazon RDS for Oracle database.

1. Create an Amazon Machine Image (AMI) for Linux from the EC2 instance.

1. Launch the completed architecture with the Application Load Balancer and Auto Scaling group.

1. Update the URLs (by using the WebSEAL junction) to point to the Application Load Balancer.

1. Update the configuration management database (CMDB).
