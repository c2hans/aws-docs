---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling.html
---

# Migrate from IBM WebSphere Application Server to Apache Tomcat on Amazon EC2 with Auto Scaling
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling"></a>

*Kevin Yung and Afroz Khan, Amazon Web Services*

## Summary
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling-summary"></a>

This pattern provides guidance for migrating a Java application from IBM WebSphere Application Server to Apache Tomcat on an Amazon Elastic Compute Cloud (Amazon EC2) instance with Amazon EC2 Auto Scaling enabled.

By using this pattern, you can achieve:
+ A reduction in IBM licensing costs
+ High availability using Multi-AZ deployment
+ Improved application resiliency with Amazon EC2 Auto Scaling

## Prerequisites and limitations
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling-prerequisites-and-limitations"></a>

**Prerequisites**
+ Java applications (version 7.*x* or 8.*x*) should be developed in LAMP stacks.
+ The target state is to host Java applications on Linux hosts. This pattern has been successfully implemented in a Red Hat Enterprise Linux (RHEL) 7 environment. Other Linux distributions can follow this pattern, but the configuration of the Apache Tomcat distribution should be referenced.
+ You should understand the Java application's dependencies.
+ You must have access to the Java application source code to make changes.

**Limitations and replatforming changes**
+ You should understand the enterprise archive (EAR) components and verify that all libraries are packaged in the web component WAR files. You need to configure the [Apache Maven WAR Plugin](https://maven.apache.org/plugins/maven-war-plugin/) and produce WAR file artifacts.
+ When using Apache Tomcat 8, there is a known conflict between servlet-api.jar and the application package built-in jar files. To resolve this issue, delete servlet-api.jar from the application package.
+ You must configure WEB-INF/resources located in the *classpath* of the [Apache Tomcat configuration](https://tomcat.apache.org/tomcat-8.0-doc/class-loader-howto.html). By default, the JAR libraries are not loaded in the directory. Alternatively, you can deploy all the resources under src/main/resources*.*
+ Check for any hard-coded context roots within the Java application, and update the new [context root of Apache Tomcat.](https://tomcat.apache.org/tomcat-8.0-doc/config/context.html#Defining_a_context)
+ To set JVM runtime options, you can create the configuration file setenv.sh in the Apache Tomcat bin folder; for example, JAVA\_OPTS, JAVA\_HOME**,** etc.
+ Authentication is configured at the container level and is set up as a realm in Apache Tomcat configurations. Authentication is established for any of the following three realms:
  + [JDBC Database Realm](https://tomcat.apache.org/tomcat-8.0-doc/config/realm.html#JDBC_Database_Realm_-_org.apache.catalina.realm.JDBCRealm) looks up users in a relational database accessed by the JDBC driver.
  + [DataSource Database Realm](https://tomcat.apache.org/tomcat-8.0-doc/config/realm.html#DataSource_Database_Realm_-_org.apache.catalina.realm.DataSourceRealm) looks up users in a database that is accessed by JNDI.
  + [JNDI Directory Realm](https://tomcat.apache.org/tomcat-8.0-doc/config/realm.html#JNDI_Directory_Realm_-_org.apache.catalina.realm.JNDIRealm) looks up users in the Lightweight Directory Access Protocol (LDAP) directory that is accessed by the JNDI provider. The look-ups require:
    + LDAP connection details: user search base, search filter, role base, role filter
    + The key JNDI Directory Realm: Connects to LDAP, authenticates users, and retrieves all groups in which a user is a member
+ Authorization: In the case of a container with a role-based authorization that checks the authorization constraints in web.xml, web resources must be defined and compared to the roles defined in the constraints. If LDAP doesn't have group-role mapping, you must set the attribute <security-role-ref> in web.xml to achieve group-role mapping. To see an example of a configuration document, see the [Oracle documentation](https://docs.oracle.com/cd/E19226-01/820-7627/bncav/index.html).
+ Database connection: Create a resource definition in Apache Tomcat with an Amazon Relational Database Service (Amazon RDS) endpoint URL and connection details. Update the application code to reference a DataSource by using JNDI lookup. An existing DB connection defined in WebSphere would not work, as it uses WebSphere’s JNDI names. You can add a <resource-ref> entry in web.xml with the JNDI name and DataSource type definition. To see a sample configuration document, see the [Apache Tomcat documentation](https://tomcat.apache.org/tomcat-8.0-doc/jndi-resources-howto.html#JDBC_Data_Sources).
+ Logging: By default, Apache Tomcat logs to the console or to a log file. You can enable realm-level tracing by updating *logging.properties* (see [Logging in Tomcat](https://tomcat.apache.org/tomcat-8.0-doc/logging.html)). If you are using Apache Log4j to append logs to a file, you must download tomcat-juli and add it to the *classpath*.
+ Session management: If you are retaining IBM WebSEAL for application load balancing and session management, no change is required. If you are using an Application Load Balancer or Network Load Balancer on AWS to replace the IBM WebSEAL component, you must set up session management by using an Amazon ElastiCache instance with a Memcached cluster and set up Apache Tomcat to use [open-source session management](https://github.com/magro/memcached-session-manager).
+ If you are using the IBM WebSEAL forward proxy, you must set up a new Network Load Balancer on AWS. Use the IPs provided by the Network Load Balancer for WebSEAL junction configurations.
+ SSL configuration: We recommend that you use Secure Sockets Layer (SSL) for end-to-end communications. To set up an SSL server configuration in Apache Tomcat, follow the instructions in the [Apache Tomcat documentation](https://tomcat.apache.org/tomcat-8.0-doc/ssl-howto.html).

## Architecture
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling-architecture"></a>

**Source technology stack**
+ IBM WebSphere Application Server

**Target technology stack**
+ The architecture uses [Elastic Load Balancing (version 2](https://docs.aws.amazon.com/elasticloadbalancing/)). If you are using IBM WebSEAL for Identify management and load balancing, you can select a Network Load Balancer on AWS to integrate with the IBM WebSEAL reverse proxy.
+ Java applications are deployed to an Apache Tomcat application server, which runs on an EC2 instance in an [Amazon EC2 Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html). You can set up a [scaling policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling_plan.html) based on Amazon CloudWatch metrics such as CPU utilization.
+ If you're retiring the use of IBM WebSEAL for load balancing, you can use [Amazon ElastiCache for Memcached ](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/WhatIs.html) for session management.
+ For the back-end database, you can deploy [High Availability (Multi-AZ) for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) and select a database engine type.

**Target architecture**

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/52b91dab-7b3b-4751-abe2-25e7c7cd8d89/images/25125023-9a81-452a-9ada-184e2416cc02.png)

## Tools
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
+ Apache Tomcat (version 7.*x* or 8.*x*)
+ RHEL 7 or Centos 7
+ [Amazon RDS Multi-AZ deployment](https://aws.amazon.com/rds/details/multi-az/)
+ [Amazon ElastiCache for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/WhatIs.html) (optional)

## Epics
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling-epics"></a>

### Set up the VPC
<a name="set-up-the-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). |  |  |
| Create subnets. |  |  |
| Create routing tables if necessary. |  |  |
| Create network access control lists (ACLs). |  |  |
| Set up AWS Direct Connect or a corporate VPN connection. |  |  |

### Replatform the application
<a name="replatform-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Refactor the application build Maven configuration to generate the WAR artifacts. |  |  |
| Refactor the application dependency data sources in Apache Tomcat. |  |  |
| Refactor the application source codes to use JNDI names in Apache Tomcat. |  |  |
| Deploy the WAR artifacts into Apache Tomcat. |  |  |
| Complete application validations and tests. |  |  |

### Configure the network
<a name="configure-the-network"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the corporate firewall to allow the connection to dependency services. |  |  |
| Configure the corporate firewall to allow end-user access to Elastic Load Balancing on AWS. |  |  |

### Create the application infrastructure
<a name="create-the-application-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and deploy the application on an EC2 instance. |  |  |
| Create an Amazon ElastiCache for Memcached cluster for session management. |  |  |
| Create an Amazon RDS Multi-AZ instance for the backend database. |  |  |
| Create SSL certificates and import them into AWS Certificate Manager (ACM). |  |  |
| Install SSL certificates on load balancers. |  |  |
| Install SSL certificates for Apache Tomcat servers. |  |  |
| Complete application validations and tests. |  |  |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down the existing infrastructure. |  |  |
| Restore the database from production to Amazon RDS. |  |  |
| Cut over the application by making DNS changes. |  |  |

## Related resources
<a name="migrate-from-ibm-websphere-application-server-to-apache-tomcat-on-amazon-ec2-with-auto-scaling-related-resources"></a>

**References**
+ [Apache Tomcat 7.0 documentation](https://tomcat.apache.org/tomcat-7.0-doc/realm-howto.html)
+ [Apache Tomcat 7.0 installation guide](https://tomcat.apache.org/tomcat-7.0-doc/appdev/installation.html)
+ [Apache Tomcat JNDI documentation](https://tomcat.apache.org/tomcat-7.0-doc/jndi-datasource-examples-howto.html)
+ [Amazon RDS Multi-AZ Deployments](https://aws.amazon.com/rds/details/multi-az/)
+ [Amazon ElastiCache for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/WhatIs.html)

**Tutorials and videos**
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)
