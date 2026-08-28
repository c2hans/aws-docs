---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/sas-infrastructure.html
---

# SAS infrastructure
<a name="sas-infrastructure"></a>

The following diagram shows the infrastructure components of SAS Grid Manager. The illustration is simplified to highlight major components that provide end-user functionality or that must be considered when planning resource allocations for processing, memory, network, and I/O.

![SAS Grid infrastructure components (simplified)](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/images/guide-img/305d2670-30eb-46db-a41c-bed418267f47/images/3c331566-cf27-4714-9f70-69703f954a67.png)

+ **SAS Metadata Server** is the central hub of SAS Grid that client, server, and intermediate software components rely on. It provides information regarding software processes, manages user authentication and authorization to resources, and maintains user content.
+ **SAS Web Server** hosts static collateral and also acts as a reverse proxy, providing a single point of contact to the web apps in their Java Virtual Machines (JVMs).
+ **SAS Web Application Servers** host the various web apps for end-user access and operation, including SAS Studio, SAS Environment Manager, and others.
+ SAS offers compute server processes that are specialized for their respective clients:
  + **SAS Object Spawner** initiates new SAS Integrated Object Model (IOM) processes.
  + **SAS Workspace Server** provides each user with a dedicated analytics environment for clients like SAS Enterprise Guide and SAS Studio.
  + **SAS Stored Process Server** acts a persistent analytics engine for predefined tasks (stored processes).
  + **SAS Grid Control Server** distributes jobs to one or more compute nodes on the grid. A grid control server can also do work allocated to the grid.
  + **SAS Grid nodes** run a portion of the work allocated to the grid.

The following architecture diagram shows how the tiers or infrastructure components interact.

![SAS Grid infrastructure components (with tiers)](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/images/guide-img/305d2670-30eb-46db-a41c-bed418267f47/images/74d5de12-b402-494c-a7c5-3f375af1fcb3.png)

**Note**
The five tiers represent categories of software that perform similar types of computing tasks and require similar types of resources. The tiers **do not necessarily** represent separate computers or groups of computers. For more information about each tier, use the links to the SAS documentation in the following list.
+ [Data tier](https://documentation.sas.com/doc/en/bicdc/9.4/biov/n1grfcwipq5x7gn1g65yxgbdm30t.htm) – Stores your enterprise data. You can use all your existing data assets, including data stored in third-party database management systems, SAS tables, enterprise resource planning (ERP) system tables, and AWS-specific storage services such as FSx for Lustre or Amazon S3.
+ [Server tier](https://documentation.sas.com/doc/en/bicdc/9.4/biov/n1rseywcpikiutn1tpfrd371s775.htm) – Performs SAS processing on your enterprise data. Several types of SAS servers are available to handle different workload types and processing intensities. The software distributes processing loads among server resources so that multiple client requests for information can be met without delay.
+ [Metadata tier](https://documentation.sas.com/doc/en/bicdc/9.4/biov/p0wsyb97ii3u1wn11uphl9uvxzvz.htm) – Client, server, and intermediate software components rely on SAS Metadata Server, which is the central hub of SAS Grid. It provides information regarding software processes, manages user authentication and authorization to access resources, and maintains user content.
+ [Web tier](https://documentation.sas.com/doc/en/bicdc/9.4/biov/p091iagmsk7kmen0zeg409unmpkb.htm) – Enables users to access intelligence data and functionality by using a web browser. This tier provides web-based interfaces for report creation and information distribution, and passes analysis and processing requests to the SAS servers.
+ [Client tier](https://documentation.sas.com/doc/en/bicdc/9.4/biov/n0g5u60z2ifbahn13prv5aqhxu51.htm) – Provides users with desktop access to intelligence data and functionality through easy-to-use interfaces. For most information consumers, reporting and analysis tasks can be performed with just a web browser. For more advanced design and analysis tasks, SAS client software is installed on users' desktops. Some support for mobile devices is also provided.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
