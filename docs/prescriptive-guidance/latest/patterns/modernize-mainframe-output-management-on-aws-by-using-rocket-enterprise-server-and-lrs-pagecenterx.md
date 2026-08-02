---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html
---

# Modernize mainframe output management on AWS by using Rocket Enterprise Server and LRS PageCenterX
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx"></a>

*Shubham Roy, Amazon Web Services*

*Abraham Rondon, Micro Focus*

*Guy Tucker, Levi, Ray and Shoup Inc*

## Summary
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-summary"></a>

By modernizing your mainframe output management, you can achieve cost savings, mitigate the technical debt of maintaining legacy systems, and improve resiliency and agility through DevOps and Amazon Web Services (AWS) cloud-native technologies. This pattern shows you how to modernize your business-critical mainframe output-management workloads on the AWS Cloud. The pattern uses [Rocket Enterprise Server](https://www.rocketsoftware.com/en-us/products/enterprise-suite/enterprise-server) as a runtime for a modernized mainframe application, with Levi, Ray & Shoup, Inc. (LRS) VPSX/MFI (Micro Focus Interface) as a print server and LRS PageCenterX as an archive server. LRS PageCenterX provides output-management solutions for viewing, indexing, searching, archiving, and securing access to business outputs.

The pattern is based on the [replatform](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/) mainframe modernization approach. Mainframe applications are migrated by [AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) on Amazon Elastic Compute Cloud (Amazon EC2). Mainframe output-management workloads are migrated to Amazon EC2, and a mainframe database, such as IBM Db2 for z/OS, is migrated to Amazon Relational Database Service (Amazon RDS). The LRS Directory Integration Server (LRS/DIS) works with AWS Directory Service for Microsoft Active Directory for output-management workflow authentication and authorization.

## Prerequisites and limitations
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A mainframe output-management workload.
+ Basic knowledge of how to rebuild and deliver a mainframe application that runs on Rocket Enterprise Server. For more information, see the [Rocket Enterprise Server](https://www.rocketsoftware.com/sites/default/files/resource_files/enterprise-server.pdf) data sheet in the Rocket Software documentation.
+ Basic knowledge of LRS cloud printing solutions and concepts. For more information, see *Output Modernization* in the LRS documentation.
+ Rocket Enterprise Server software and license. For more information, contact [Rocket Software](https://www.rocketsoftware.com/products/enterprise-suite/request-contact).
+ LRS VPSX/MFI, LRS PageCenterX, LRS/Queue, and LRS/DIS software and licenses. For more information, [contact LRS](https://www.lrsoutputmanagement.com/about-us/contact-us/). You must provide the hostnames of the EC2 instances where the LRS products will be installed.

|
|
| Note: For more information about configuration considerations for mainframe output-management workloads, see *Considerations* in the [Additional information](#modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-additional) section of this pattern. |
| --- |

**Product versions**
+ [Rocket Enterprise Server 10.0](https://www.rocketsoftware.com/products/enterprise-suite/enterprise-test-server)
+ [LRS VPSX/MFI](https://www.lrsoutputmanagement.com/products/modernization-products/)
+ [LRS PageCenterX](https://www.lrsoutputmanagement.com/products/content-management/pagecenterx-for-open-systems/) V1R3 or later

## Architecture
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-architecture"></a>

**Source technology stack**
+ Operating system – IBM z/OS
+ Programming language – Common business-oriented language (COBOL), job control language (JCL), and Customer Information Control System (CICS)
+ Database – IBM Db2 for z/OS, IBM Information Management System (IMS) database, and Virtual Storage Access Method (VSAM)
+ Security – Resource Access Control Facility (RACF), CA Top Secret for z/OS, and Access Control Facility 2 (ACF2)
+ Print and archive solutions – IBM mainframe z/OS output and printing products (IBM Infoprint Server for z/OS, LRS, and CA Deliver) and archiving solutions (CA Deliver, ASG Mobius, or CA Bundle)

**Source architecture**

The following diagram shows a typical current state architecture for a mainframe output-management workload.

![Mainframe output process in seven steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f9ad041d-b9f0-4a9a-aba7-40fdc3088b27/images/d170394a-c9b2-43c0-a3d4-677b5f7c2473.png)

The diagram shows the following workflow:

1. Users perform business transactions on a system of engagement (SoE) that’s built on an IBM CICS application written in COBOL.

1. The SoE invokes the mainframe service, which records the business transaction data in a system-of-records (SoR) database such as IBM Db2 for z/OS.

1. The SoR persists the business data from the SoE.

1. The batch job scheduler initiates a batch job to generate print output.

1. The batch job extracts data from the database. It formats the data according to business requirements, and then it generates business output such as billing statements, ID cards, or loan statements. Finally, the batch job routes the output to output management for format, publish, and storage of the output based on the business requirements.

1. Output management receives output from the batch job. Output management indexes, arranges, and publishes the output to a specified destination in the output-management system, such as LRS PageCenterX solutions (as demonstrated in this pattern) or CA View.

1. Users can view, search, and retrieve the output.

**Target technology stack**
+ Operating system – Windows Server running on Amazon EC2
+ Compute – Amazon EC2
+ Storage – Amazon Elastic Block Store (Amazon EBS) and Amazon FSx for Windows File Server
+ Programming language – COBOL, JCL, and CICS
+ Database – Amazon RDS
+ Security – AWS Managed Microsoft AD
+ Printing and archiving – LRS printing (VPSX) and archiving (PageCenterX) solution on AWS
+ Mainframe runtime environment – Rocket Enterprise Server

**Target architecture**

The following diagram shows an architecture for a mainframe output-management workload that’s deployed in the AWS Cloud.

![Target architecture for batch app and output management in seven steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f9ad041d-b9f0-4a9a-aba7-40fdc3088b27/images/3e25ab03-bf3a-4fea-b5eb-38cea9e50138.png)

The diagram shows the following workflow:

1. The batch job scheduler initiates a batch job to create output, such as billing statements, ID cards, or loan statements.

1. The mainframe batch job ([replatformed to Amazon EC2](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/)) uses the Rocket Enterprise Server runtime to extract data from the application database, apply business logic to the data, and format the data. It then sends the data to an output destination by using the [Rocket Software printer exit module](https://www.microfocus.com/documentation/enterprise-developer/ed100/ED-Eclipse/HCOMCMJCLOU020.html) (OpenText Micro Focus documentation).

1. The application database (an SoR that runs on Amazon RDS) persists data for print output.

1. The LRS VPSX/MFI printing solution is deployed on Amazon EC2, and its operational data is stored in Amazon EBS. LRS VPSX/MFI uses the TCP/IP-based LRS/Queue transmission agent to collect output data through the Rocket Software JES Print Exit API.

   LRS VPSX/MFI does data preprocessing, such as EBCDIC to ASCII translation. It also does more complex tasks, including converting mainframe-exclusive data streams such as IBM Advanced Function Presentation (AFP) and Xerox Line Conditioned Data Stream (LCDS) into more common viewing and printing data streams such as Printer Command Language (PCL) and PDF.

   During the maintenance window of LRS PageCenterX, LRS VPSX/MFI persists the output queue and serves as backup for the output queue. LRS VPSX/MFI connects and sends output to LRS PageCenterX by using the LRS/Queue protocol. LRS/Queue performs an exchange of both readiness and completion for the jobs to help ensure that the data transfer occurs.

   **Notes:**

   For more information on print data passed from Rocket Software Print Exit to LRS/Queue and LRS VPSX/MFI supported mainframe batch mechanisms, see *Print data capture* in the [Additional information](#modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-additional) section.

   LRS VPSX/MFI can perform health checks at the printer-fleet level. For more information, see *Printer-fleet health checks* in the [Additional information](#modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-additional) section of this pattern.

1. The LRS PageCenterX output-management solution is deployed on Amazon EC2, and its operational data is stored in Amazon FSx for Windows File Server. LRS PageCenterX provides a central report management system of all files imported into LRS PageCenterX along with all users able to access the files. Users can view specific file content or perform searches across multiple files for matching criteria.

   The LRS/NetX component is a multi-threaded web application server that provides a common runtime environment for the LRS PageCenterX application and other LRS applications. The LRS/Web Connect component is installed on your web server and provides a connector from the web server to the LRS/NetX web application server.

1. LRS PageCenterX provides storage for file system objects. The operational data of LRS PageCenterX is stored in Amazon FSx for Windows File Server.

1. Output-management authentication and authorization are performed by AWS Managed Microsoft AD with LRS/DIS.

**Note**
The target solution typically doesn’t require application changes to accommodate mainframe formatting languages, such as IBM AFP or Xerox LCDS.

**AWS infrastructure architecture**

The following diagram shows a highly available and secure AWS infrastructure architecture for a mainframe output-management workload.

![Multi-AZ AWS infrastructure with a workflow in seven steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f9ad041d-b9f0-4a9a-aba7-40fdc3088b27/images/8d8aa995-b576-4ecd-8a7c-5f566740a515.png)

The diagram shows the following workflow:

1. The batch scheduler initiates the batch process and is deployed on Amazon EC2 across multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) for high availability (HA).
**Note**
This pattern doesn’t cover the implementation of the batch scheduler. For more information about implementation, see the software vendor documentation for your scheduler.

1. The mainframe batch job (written in a programming language such as JCL or COBOL) uses core business logic to process and generate print output, such as billing statements, ID cards, and loan statements. The batch job is deployed on Amazon EC2 across two Availability Zones for HA. It uses the Rocket Software Print Exit API to route print output to LRS VPSX/MFI for data preprocessing.

1. The LRS VPSX/MFI print server is deployed on Amazon EC2 across two Availability Zones for HA (active-standby redundant pair). It uses [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) as an operational data store. The Network Load Balancer performs a health check on the LRS VPSX/MFI EC2 instances. If an active instance is in an unhealthy state, the load balancer routes traffic to hot standby instances in the other Availability Zone. The print requests are persisted in the LRS Job Queue locally in each of the EC2 instances. In the event of a failure, a failed instance must be restarted before the LRS services can resume processing the print request.
**Note**
LRS VPSX/MFI can also perform health checks at the printer-fleet level. For more information, see *Printer-fleet health checks* in the [Additional information](#modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-additional) section of this pattern.

1. LRS PageCenterX output management is deployed on Amazon EC2 across two Availability Zones for HA (active-standby redundant pair). It uses [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) as an operational data store. If an active instance is in an unhealthy state, the load balancer performs a health check on the LRS PageCenterX EC2 instances and routes traffic to standby instances in the other Availability Zone.

1. A [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) provides a DNS name to integrate the LRS VPSX/MFI Server with LRS PageCenterX.
**Note**
LRS PageCenterX supports a Layer 4 load balancer.

1. LRS PageCenterX uses Amazon FSx for Windows File Server as an operational data store deployed across two Availability Zones for HA. LRS PageCenterX understands only files that are in the file share, not in an external database.

1. [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) is used with LRS/DIS to perform output-management workflow authentication and authorization. For more information, see *Print output authentication and authorization* in the [Additional information](#modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-additional) section.

## Tools
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-tools"></a>

**AWS services**
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon EC2 instances, containers, and IP addresses in one or more Availability Zones. This pattern uses a Network Load Balancer.
+ [Amazon FSx](https://docs.aws.amazon.com/fsx/?id=docs_gateway) provides file systems that support industry-standard connectivity protocols and offer high availability and replication across AWS Regions. This pattern uses Amazon FSx for Windows File Server.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.

**Other tools**
+ [LRS PageCenterX](https://www.lrsoutputmanagement.com/products/content-management/pagecenterx-for-open-systems/) software provides a scalable document and report content management solution that helps users obtain maximum value from information through automated indexing, encryption, and advanced search features.
+ [LRS VPSX/MFI (Micro Focus Interface)](https://www.lrsoutputmanagement.com/products/modernization-products/), codeveloped by LRS and Rocket Software, captures output from a Rocket Software JES spool and reliably delivers it to a specified print destination.
+ LRS/Queue is a transmission agent that’s TCP/IP based. LRS VPSX/MFI uses LRS/Queue to collect or capture print data through the Rocket Software JES Print Exit programming interface.
+ LRS Directory Integration Server (LRS/DIS) is used for authentication and authorization during the print workflow.
+ [Rocket Enterprise Server](https://www.microfocus.com/documentation/enterprise-developer/ed80/ES-WIN/GUID-F7D8FD6E-BDE0-4169-8D8C-96DDFFF6B495.html) is an application deployment environment for mainframe applications. It provides the runtime environment for mainframe applications that are migrated or created by using any version of Rocket Enterprise Developer.

## Epics
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-epics"></a>

### Set up the Rocket runtime and deploy a mainframe batch application
<a name="set-up-the-rocket-runtime-and-deploy-a-mainframe-batch-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the runtime and deploy a demo application. | To set up Rocket Enterprise Server on Amazon EC2 and deploy the Rocket Software BankDemo demonstration application, follow the instructions in AWS Mainframe Modernization [user-guide](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup.html).<br />The BankDemo application is a mainframe batch application that creates and then initiates print output. | Cloud architect |

### Set up an LRS print server on Amazon EC2
<a name="set-up-an-lrs-print-server-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EC2 Windows instance. | To launch an Amazon EC2 Windows instance, follow the instructions in [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) in the Amazon EC2 documentation. Use the same hostname that you used for your LRS product license.<br />Your instance must meet the following hardware and software requirements for LRS VPSX/MFI:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html)The preceding hardware and software requirements are intended for a small printer fleet (around 500-1000). To get the full requirements, consult with your LRS and AWS contacts.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Install LRS VPSX/MFI on the EC2 instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Install LRS/Queue. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Install LRS/DIS. | The LRS/DIS product often is included in LRS VPSX installation. However, if LRS/DIS wasn't installed along with LRS VPSX, use the following steps to install it:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a target group. | Create a target group by following the instructions in [Create a target group for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html). When you create the target group, register the LRS VPSX/MFI EC2 instance as the target:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a Network Load Balancer. | To create the Network Load Balancer, follow the instructions in the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html). Your Network Load Balancer routes traffic from Rocket Enterprise Server to the LRS VPSX/MFI EC2 instance.<br />When you create the Network Load Balancer, choose the following values on the **Listeners and Routing** page:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Integrate Rocket Enterprise Server with LRS/Queue and LRS VPSX/MFI
<a name="integrate-rocket-enterprise-server-with-lrs-queue-and-lrs-vpsx-mfi"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Rocket Enterprise Server for LRS/Queue integration. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Configure Rocket Enterprise Server for LRS VPSX/MFI integration. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Set up the print queue and the print users
<a name="set-up-the-print-queue-and-the-print-users"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Associate the Rocket Software Print Exit module with the Rocket Enterprise Server batch printer Server Execution Process. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a print output queue in LRS VPSX/MFI and integrate it with LRS PageCenterX. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a print user in LRS VPSX/MFI. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Set up an LRS PageCenterX server on Amazon EC2
<a name="set-up-an-lrs-pagecenterx-server-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EC2 Windows instance. | Launch an Amazon EC2 Windows instance by following the instructions from [Step 1: Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-launch-instance) in the Amazon EC2 documentation. Use the same hostname that you used for your LRS product license.<br />Your instance must meet the following hardware and software requirements for LRS PageCenterX:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html)The preceding hardware and software requirements are intended for a small printer fleet (around 500–1000). To get the full requirements, consult with your LRS and AWS contacts.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Install LRS PageCenterX on the EC2 instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Install LRS/DIS. | The LRS/DIS product often is included in LRS VPSX installation. However, if LRS/DIS wasn't installed along with LRS VPSX, use the following steps to install it:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a target group. | Create a target group by following the instructions in [Create a target group for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html). When you create the target group, register the LRS PageCenterX EC2 instance as the target:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a Network Load Balancer. | To create the Network Load Balancer, follow the instructions in the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html). Your Network Load Balancer routes traffic from LRS VPSX/MFI to the LRS PageCenterX EC2 instance.<br />When you create the Network Load Balancer, choose the following values on the **Listeners and Routing** page:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Set up output-management features in LRS PageCenterX
<a name="set-up-output-management-features-in-lrs-pagecenterx"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable the Import function in LRS PageCenterX. | You can use the LRS PageCenterX Import function to recognize the outputs landing on LRS PageCenterX by criteria such as Job name or Form ID. You can then route the outputs to specific folders in LRS PageCenterX.<br />To enable the Import function, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Configure the document retention policy. | LRS PageCenterX uses a document retention policy to decide how long to keep a document in LRS PageCenterX.<br />To configure the document retention policy, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a rule to route the output document to a specific folder in LRS PageCenterX. | In LRS PageCenterX, **Destination **determines the folder path where output will be sent when this destination is invoked by **Report Definition**. For this example, create a folder based on the **Form ID** folder in the report definition, and save the output to that folder.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a report definition. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Set up authentication and authorization for output management
<a name="set-up-authentication-and-authorization-for-output-management"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS Managed Microsoft AD domain with users and groups. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Join the EC2 instances to an AWS Managed Microsoft AD domain. | Join the LRS VPSX/MFI and LRS PageCenterX EC2 instances to your AWS Managed Microsoft AD domain [automatically](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-dx-domain/) (AWS Knowledge Center documentation) or [manually](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_windows_instance.html) (AWS Directory Service documentation). | Cloud architect |
| Configure and integrate LRS/DIS with AWS Managed Microsoft AD for the LRS PageCenterX EC2 instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Configure an Import group to import output from LRS VPSX to LRS PageCenterX. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Add a security rule to the Import group. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Create a user in LRS PageCenterX to perform output import from LRS VPSX/MFI.  | When you create a user in LRS PageCenterX to perform output import, the username should be the same as the **VPSX ID** of the print output queue in LRS VPSX/MFI. In this example, the VPSX ID is **VPS1**.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Add the LRS PageCenterX Import user to the Import only group. | To provide necessary permission for document import from LRS VPSX to LRS PageCenterX, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |
| Configure LRS/DIS with AWS Managed Microsoft AD for the LRS VPSX/MFI EC2 instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Configure Amazon FSx for Windows File Server as the operational data store for LRS PageCenterX
<a name="configure-amazon-fsx-for-windows-file-server-as-the-operational-data-store-for-lrs-pagecenterx"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a file system for LRS PageCenterX. | To use Amazon FSx for Windows File Server as an operational data store for LRS PageCenterX in a Multi-AZ environment, follow the instructions in [Step 1: Create your file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started-step1.html). | Cloud architect |
| Map the file share to the LRS PageCenterX EC2 instance. | To map the file share created in previous step to the LRS PageCenterX EC2 instance, follow the instructions in [Step 2: Map your file share to an EC2 instance running Windows Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started-step2.html). | Cloud architect |
| Map LRS PageCenterX Control Directory and Master Folder Directory to the Amazon FSx network share drive. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Cloud architect |

### Test an output-management workflow
<a name="test-an-output-management-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initiate a batch print request from the Rocket Software BankDemo app. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Test engineer |
| Check the print output in LRS PageCenterX. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx.html) | Test engineer |

## Related resources
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-resources"></a>
+ [LRS](https://www.lrsoutputmanagement.com/products/modernization-products)
+ [Advanced Function Presentation data stream](https://www.ibm.com/docs/en/i/7.4?topic=streams-advanced-function-presentation-data-stream) (IBM documentation)
+ [Line Conditioned Data Stream (LCDS)](https://www.compart.com/en/lcds) (Compart documentation)
+ [Empowering Enterprise Mainframe Workloads on AWS with Micro Focus](https://aws.amazon.com/blogs/apn/empowering-enterprise-grade-mainframe-workloads-on-aws-with-micro-focus/) (blog post)
+ [Modernize your mainframe online printing workloads on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi.html) (AWS Prescriptive Guidance)
+ [Modernize your mainframe batch printing workloads on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-batch-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi.html) (AWS Prescriptive Guidance)

## Additional information
<a name="modernize-mainframe-output-management-on-aws-by-using-rocket-enterprise-server-and-lrs-pagecenterx-additional"></a>

**Considerations**

During your modernization journey, you might consider a wide variety of configurations for mainframe batch and online processes and the output they generate. The mainframe platform has been customized by every customer and vendor that uses it with particular requirements that directly affect print. For example, your current platform might incorporate the IBM AFP data stream or Xerox LCDS into the current workflow. Additionally, [mainframe carriage control characters](https://www.ibm.com/docs/en/cmofz/10.5.0?topic=tips-ansi-machine-carriage-controls) and [channel command words](https://www.ibm.com/docs/en/zos/3.1.0?topic=devices-channel-command-words) can affect the look of the printed page and might need special handling. As part of the modernization planning process, we recommend that you assess and understand the configurations in your specific print environment.

**Print data capture**

Rocket Software Print Exit passes the necessary information for LRS VPSX/MFI to effectively process the spool file. The information consists of fields passed in the relevant control blocks, such as the following:
+ JOBNAME
+ OWNER (USERID)
+ DESTINATION
+ FORM
+ FILENAME
+ WRITER

LRS VPSX/MFI supports the following mainframe batch mechanisms for capturing data from Rocket Enterprise Server:
+ BATCH COBOL print/spool processing using standard z/OS JCL SYSOUT DD/OUTPUT statements.
+ BATCH COBOL print/spool processing using standard z/OS JCL CA-SPOOL SUBSYS DD statements.
+ IMS/COBOL print/spool processing using the CBLTDLI interface. For a full list of supported methods and programming examples, see the LRS documentation that’s included with your product license.

**Printer-fleet health checks**

LRS VPSX/MFI (LRS LoadX) can perform deep dive health checks, including device management and operational optimization. Device management can detect failure in a printer device and route the print request to a healthy printer. For more information about deep-dive health checks for printer fleets, see the LRS documentation that’s included with your product license.

**Print authentication and authorization**

LRS/DIS enables LRS applications to authenticate user IDs and passwords by using Microsoft Active Directory or a Lightweight Directory Access Protocol (LDAP) server. In addition to basic print authorization, LRS/DIS can also apply granular-level print security controls in the following use cases:
+ Manage who can browse the printer job.
+ Manage the browsing level of other user's jobs.
+ Manage operational tasks—for example, command-level security such as hold or release, purge, modify, copy, and reroute. Security can be set up by either the user-ID or the group, similar to an Active Directory security group or an LDAP group.

## Attachments
<a name="attachments-f9ad041d-b9f0-4a9a-aba7-40fdc3088b27"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/f9ad041d-b9f0-4a9a-aba7-40fdc3088b27/attachments/attachment.zip)
