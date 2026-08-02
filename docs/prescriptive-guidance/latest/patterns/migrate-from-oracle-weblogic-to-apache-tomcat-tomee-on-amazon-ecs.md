---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs.html
---

# Migrate from Oracle WebLogic to Apache Tomcat (TomEE) on Amazon ECS
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs"></a>

*Anya Epishcheva and Harshad Gohil, Amazon Web Services*

## Summary
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs-summary"></a>

This pattern discusses the steps for migrating an on-premises Oracle Solaris SPARC system running Oracle WebLogic to a Docker container-based installation running [Apache TomEE](http://tomee.apache.org/) (Apache Tomcat with added container support) with Amazon Elastic Container Service (Amazon ECS).

For information about migrating databases that are associated with the applications you are migrating from Oracle WebLogic to Tomcat, see the database migration patterns in this catalog.

**Best practices**

Steps for migrating Java and Java Enterprise Edition (Java EE) web applications vary, depending on the number of container-specific resources used by the application. Spring-based applications are typically easier to migrate, because they have a small number of dependencies on the deployment container. In contrast, Java EE applications that use Enterprise JavaBeans (EJBs) and managed container resources such as thread pools, Java Authentication and Authorization Service (JAAS), and Container-Managed Persistence (CMP) require more effort.

Applications developed for Oracle Application Server frequently use the Oracle Identity Management suite. Customers migrating to open-source application servers frequently choose to re-implement identity and access management using SAML-based federation. Others use Oracle HTTP Server Webgate for cases when migrating from the Oracle Identity Management suite isn't an option.

Java and Java EE web applications are great candidates for deployment on AWS services that are Docker-based, such as AWS Fargate and Amazon ECS. Customers frequently choose a Docker image with the latest version of the target application server (such as TomEE) and the Java Development Kit (JDK) pre-installed. They install their applications on top of the base Docker image, publish it in their Amazon Elastic Container Registry (Amazon ECR) registry, and use it for scalable deployment of their applications on AWS Fargate or Amazon ECS.

Ideally, application deployment is elastic; that is, the number of application instances scales in or out, depending on traffic or workload. This means that application instances need to come online or be terminated to adjust capacity for demand.

When moving a Java application to AWS, consider making it stateless. This is a key architectural principle of the AWS Well-Architected Framework that will enable horizontal scaling using containerization. For example, most Java-based web applications store user-session information locally. To survive application instance termination due to automatic scaling in Amazon Elastic Compute Cloud (Amazon EC2) or for other reasons, user-session information should be stored globally so that web application users can continue to work seamlessly and transparently without reconnecting or relogging into a web application. There are several architectural options for this approach, including Amazon ElastiCache for Redis, or storing session state in a global database. Application servers such as TomEE have plugins, which enable session storage and management via Redis, databases, and other global data stores.

Use a common, centralized logging and debugging tool that is easily integrated with Amazon CloudWatch and AWS X-Ray. Migration provides an opportunity to improve application lifecycle capabilities. For example, you might want to automate the build process so that changes are easily made using a continuous integration and continuous delivery (CI/CD) pipeline. This may require changes to the application so that it can be deployed without any downtime.

## Prerequisites and limitations
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs-prerequisites-and-limitations"></a>

**Prerequisites**
+ An active AWS account
+ Source Java code and JDK
+ Source application built with Oracle WebLogic
+ Defined solution for identity and access management (SAML or Oracle Webgate)
+ Defined solution for application session management (moving like-for-like or with Amazon ElastiCache, or making the application stateless if needed)
+ Understanding if the team needs to refactor J2EE-specific libraries for portability to Apache TomEE (see [Java EE 7 Implementation Status](http://tomee.apache.org/javaee7-status.html) on the Apache website)
+ Hardened TomEE image based on your security requirements
+ Container image with pre-installed target TomEE
+ Application remediation agreed and implemented if needed (for example, logging debug build, authentication)

**Product versions**
+ Oracle WebLogic OC4J, 9i, 10g
+ Tomcat 7 (with Java 1.6 or later)

## Architecture
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs-architecture"></a>

 **Source technology stack **
+ Web application built using Oracle WebLogic
+ Web application using Oracle Webgate or SAML authentication
+ Web applications connected to Oracle Database version 10g and later

**Target technology stack **
+ TomEE (Apache Tomcat with added container support) running on Amazon ECS (see also [Deploying Java Web Applications](https://aws.amazon.com/answers/web-applications/aws-web-app-deployment-java/) and [Java Microservices on Amazon ECS](https://aws.amazon.com/blogs/compute/deploying-java-microservices-on-amazon-ec2-container-service/))
+ Amazon Relational Database Service (Amazon RDS) for Oracle; for Oracle versions supported by Amazon RDS, see [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/)** **

** Target architecture **

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d5e7b3fa-062f-4559-af56-aa6058f96755/images/762193cf-aa68-4195-b3c7-6541caee61c9.png)

## Tools
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs-tools"></a>

To operate on TomEE, a Java application must be rebuilt into a .war file. In some cases, application changes may be required to operate the application on TomEE; you should check to make sure that the necessary configuration options and environment properties are defined correctly.

Also, Java Naming and Directory Interface (JNDI) lookups and JavaServer Pages (JSP) namespaces should be defined correctly. Consider checking file names used by the application to avoid naming collisions with built-in T libraries. For example, persistence.xml is a file name used by the Apache OpenJPA framework (which is bundled with OpenEJB in TomEE) for configuration purposes. The persistence.xml file in PUI contains Spring framework bean declarations.

TomEE version 7.0.3 and later (Tomcat 8.5.7 and later) returns an HTTP 400 response (bad request) for raw (unencoded) URLs with special characters. The server response appears as a blank page to the end-user. Earlier versions of TomEE and Tomcat allowed the use of certain unencoded special characters in URLs; however, it’s considered unsafe, as stated on the [CVE-2016-6816 website](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-6816). To resolve the URL encoding issue, the URLs passed to the browser directly via JavaScript must be encoded with the **encodeURI()** method instead of being used as raw strings.

After you deploy the .war file in TomEE, monitor *start log* to *Linux cat* for any missing shared libraries and Oracle-specific extensions to add missing components from Tomcat libraries.

**General procedure**
+ Configure the application on TomEE.
+ Identify and reconfigure application server-specific configuration files and resources from source to target format.
+ Identify and reconfigure JNDI resources.
+ Adjust EJB namespace and lookups to the format required by the target application server (if applicable).
+ Reconfigure JAAS application container-specific security roles and principle mappings (if applicable).
+ Package the application and shared libraries into a .war file.
+ Deploy the .war file in TomEE by using the Docker container provided.
+ Monitor *start log* to identify any missing shared library and deployment descriptor extensions. If any are found, go back to the first task.
+ Test the installed application against the restored Amazon RDS database.
+ Launch the complete architecture with a load balancer and Amazon ECS cluster by following the instructions in [Deploy Docker Containers](https://aws.amazon.com/getting-started/tutorials/deploy-docker-containers/).
+ Update the URLs to point to the load balancer.
+ Update the configuration management database (CMDB).

## Epics
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform application discovery (current state footprint and performance baseline). |  | BA, Migration Lead |
| Validate source and target database versions and engines. |  | DBA |
| Validate the source and target application design (identity and session management). |  | DBA, Migration Engineer, App owner |
| Identify hardware and storage requirements for the target server instance. |  | DBA, SysAdmin |
| Choose the proper instance type based on capacity, storage features, and network features. |  | DBA, SysAdmin |
| Identify network access security requirements for the source and target databases. |  | DBA, SysAdmin |
| Identify application migration strategy and tooling. |  | DBA, Migration Lead |
| Complete the migration design and migration guide for the application. |  | Build Lead, Migration Lead |
| Complete the application migration runbook. |  | Build Lead, Cutover Lead, Testing Lead, Migration Lead |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). |  | SysAdmin |
| Create security groups. |  | SysAdmin |
| Configure and start the Amazon RDS DB instance. |  | DBA, SysAdmin |
| Configure Amazon ECS deployment. |  | SysAdmin |
| Package your application as a Docker image. |  | SysAdmin |
| Push the image to the Amazon ECR registry (or skip this step and push it to the Amazon ECS cluster). |  | SysAdmin |
| Configure the task definition for the application and Amazon ECS service options. |  | SysAdmin |
| Configure your cluster, review security settings, and set AWS Identity and Access Management (IAM) roles. |  | SysAdmin |
| Launch your setup and run tests according to your application migration runbook. |  | SysAdmin |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get your security assurance team's permission to move production data to AWS. |  | DBA, Migration Engineer, App owner |
| Create and obtain access to endpoints to fetch database backup files. |  | DBA |
| Use the native database engine or third-party tools to migrate database objects and data. |  | DBA |
| Run necessary tests from the application migration runbook to confirm successful data migration. |  | DBA, Migration Engineer, App owner |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a change request (CR) for migration. |  | Cutover Lead |
| Obtain CR approval for migration. |  | Cutover Lead |
| Follow the application migration strategy from the application migration runbook. |  | DBA, Migration Engineer, App owner |
| Upgrade the application (if required). |  | DBA, Migration Engineer, App owner |
| Complete functional, non-functional, data validation, SLA, and performance tests. |  | Testing Lead, App Owner, App Users |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Obtain signoff from the application or business owner. |  | Cutover Lead |
| Run a table topic exercise to walk through all the steps of the cutover runbook. |  | DBA, Migration Engineer, App owner |
| Switch application clients to the new infrastructure. |  | DBA, Migration Engineer, App owner |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down temporary AWS resources. |  | DBA, Migration Engineer, SysAdmin |
| Review and validate the project documents. |  | Migration Lead |
| Gather metrics around time to migrate, % of manual vs. tool, cost savings, etc. |  | Migration Lead |
| Close out the project and provide feedback. |  | Migration Lead, App Owner |

## Related resources
<a name="migrate-from-oracle-weblogic-to-apache-tomcat-tomee-on-amazon-ecs-related-resources"></a>

**References**
+ [Apache Tomcat 7.0 documentation](https://tomcat.apache.org/tomcat-7.0-doc/realm-howto.html)
+ [Apache Tomcat 7.0 installation guide](https://tomcat.apache.org/tomcat-7.0-doc/appdev/installation.html)
+ [Apache Tomcat JNDI documentation](https://tomcat.apache.org/tomcat-7.0-doc/jndi-datasource-examples-howto.html)
+ [Apache TomEE documentation](http://tomee.apache.org/)
+ [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/)
+ [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/)
+ [Oracle and AWS](https://aws.amazon.com/oracle/)
+ [Oracle on Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)
+ [Amazon RDS Multi-AZ deployments](https://aws.amazon.com/rds/details/multi-az/)
+ [Getting started with Amazon ECS](https://aws.amazon.com/ecs/getting-started/)
+ [Getting started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)

**Tutorials and videos**
+ [Best Practices for Running Oracle Databases on Amazon RDS](https://www.youtube.com/watch?v=j2wqT0EPDbw) (re:Invent 2018 presentation)
