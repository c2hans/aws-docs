---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi.html
---

# Modernize mainframe batch printing workloads on AWS by using Rocket Enterprise Server and LRS VPSX/MFI
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi"></a>

*Shubham Roy and Kevin Yung, Amazon Web Services*

*Abraham Rondon, Micro Focus*

*Guy Tucker, Levi, Ray and Shoup Inc*

## Summary
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-summary"></a>

This pattern shows you how to modernize your business-critical mainframe batch printing workloads on the Amazon Web Services (AWS) Cloud by using Rocket Enterprise Server as a runtime for a modernized mainframe application and LRS VPSX/MFI (Micro Focus Interface) as a print server. The pattern is based on the [replatform](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/) mainframe modernization approach. In this approach, you migrate your mainframe batch jobs to Amazon Elastic Compute Cloud (Amazon EC2) and migrate your mainframe database, such as IBM DB2 for z/OS, to Amazon Relational Database Service (Amazon RDS). The authentication and authorization for the modernized print workflow is performed by AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD. The LRS Directory Information Server (LRS/DIS) is integrated with AWS Managed Microsoft AD. By modernizing your batch printing workloads, you can reduce IT infrastructure costs, mitigate the technical debt of maintaining legacy systems, remove data silos, increase agility and efficiency with a DevOps model, and take advantage of on-demand resources and automation in the AWS Cloud.

## Prerequisites and limitations
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A mainframe printing or output management workload
+ Basic knowledge of how to rebuild and deliver a mainframe application that runs on Rocket Enterprise Server (For more information, see the [Rocket Enterprise Server](https://www.rocketsoftware.com/sites/default/files/resource_files/enterprise-server.pdf) data sheet in the Rocket documentation.)
+ Basic knowledge of [LRS cloud printing](https://www.lrsoutputmanagement.com/solutions/solutions-cloud-printing/) solutions and concepts
+ Rocket Enterprise Server software and license (For more information, contact [Rocket sales](https://www.rocketsoftware.com/en-us/products/enterprise-suite/request-contact).)
+ LRS VPSX/MFI, LRS/Queue, and LRS/DIS software and licenses (For more information, contact [LRS sales](https://www.lrsoutputmanagement.com/about-us/contact-us/).)

**Note**
For more information about configuration considerations for mainframe batch printing workloads, see *Considerations* in the [Additional information](#modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-additional) section of this pattern.

**Product versions**
+ [Rocket Enterprise Server](https://www.microfocus.com/en-us/products/enterprise-server/overview?utm_campaign=7018e000000PgfnAAC&utm_content=SCH-BR-AMC-AppM-AMS&gclid=EAIaIQobChMIoZCQ6fvS9wIVxQN9Ch2MzAOlEAAYASAAEgKx2fD_BwE) 6.0 (product update 7)
+ [LRS VPSX/MFI](https://www.lrsoutputmanagement.com/products/vpsx-enterprise/) V1R3 or higher

## Architecture
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-architecture"></a>

**Source technology stack**
+ Operating system – IBM z/OS
+ Programming language – Common Business-Oriented Language (COBOL), job control language (JCL), and Customer Information Control System (CICS)
+ Database – IBM DB2 for z/OS and Virtual Storage Access Method (VSAM)
+ Security – Resource Access Control Facility (RACF), CA Top Secret for z/OS, and Access Control Facility 2 (ACF2)
+ Printing and output management – IBM mainframe z/OS printing products (IBM Tivoli Output Manager for z/OS, LRS, and CA View)

**Target technology stack**
+ Operating system – Microsoft Windows Server running on Amazon EC2
+ Compute – Amazon EC2
+ Programming language – COBOL, JCL, and CICS
+ Database – Amazon RDS
+ Security – AWS Managed Microsoft AD
+ Printing and output management – LRS printing solution on AWS
+ Mainframe runtime environment – Rocket Enterprise Server

**Source architecture**

The following diagram shows a typical current state architecture for a mainframe batch printing workload:

![From user to mainframe service, Db2 for z/OS, job scheduler, batch job, and output in six steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/36de7312-4860-4702-a325-c01cf74c4f33/images/83d82435-0aa6-4eb8-a5c8-0920102afb09.png)

The diagram shows the following workflow:

1. Users perform business transactions on a system of engagement (SoE) that’s built on an IBM CICS application written in COBOL.

1. The SoE invokes the mainframe service, which records the business transaction data in a system-of-records (SoR) database such as IBM DB2 for z/OS.

1. The SoR persists the business data from the SoE.

1. The batch job scheduler initiates a batch job to generate print output.

1. The batch job extracts data from the database, formats the data according to business requirements, and then generates business output such as billing statements, ID cards,  or loan statements. Finally, the batch job routes the output to printing output management for processing and output delivery, based on the business requirements.

1. Printing output management receives print output from the batch job, and then delivers that output to a specified destination, such as email, a file share that uses secure FTP, a physical printer that uses LRS printing solutions (as demonstrated in this pattern), or IBM Tivoli.

**Target architecture**

The following diagram shows an architecture for a mainframe batch printing workload that’s deployed in the AWS Cloud:

![Batch application on AWS with scheduler, Rocket Enterprise Server, and database in four steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/36de7312-4860-4702-a325-c01cf74c4f33/images/8cdd4ef7-3cbd-476a-9aa4-c1c0924f17c6.png)

The diagram shows the following workflow:

1. The batch job scheduler initiates a batch job to create print output, such as billing statements, ID cards, or loan statements.

1. The mainframe batch job ([replatformed to Amazon EC2](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/)) uses the Rocket Enterprise Server runtime to extract data from the application database, apply business logic to the data, format the data, and then send the data to a print destination by using [Rocket Software Print Exit](https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/HCOMCMJCLOU020.html) (Micro Focus documentation).

1. The application database (an SoR that runs on Amazon RDS) persists data for print output.

1. The LRS VPSX/MFI printing solution is deployed on Amazon EC2 and its operational data is stored in Amazon Elastic Block Store (Amazon EBS). LRS VPSX/MFI uses the TCP/IP-based LRS/Queue transmission agent to collect print data through the Rocket Software JES Print Exit API and deliver the data to a specified printer destination.

**Note**
The target solution typically doesn’t require application changes to accommodate mainframe formatting languages, such as IBM Advanced Function Presentation (AFP) or Xerox Line Condition Data Stream (LCDS). For more information about using Rocket Software for mainframe application migration and modernization on AWS, see the [Empowering Enterprise Mainframe Workloads on AWS with Micro Focus](https://aws.amazon.com/blogs/apn/empowering-enterprise-grade-mainframe-workloads-on-aws-with-micro-focus/) blog post.

**AWS infrastructure architecture**

The following diagram shows a highly available and secure AWS infrastructure architecture for a mainframe batch printing workload:

![Multi-AZ deployment on AWS with Rocket Software and LRS components in seven steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/36de7312-4860-4702-a325-c01cf74c4f33/images/287dd143-338c-4d83-a9b2-8e39214a81b0.png)

The diagram shows the following workflow:

1. The batch scheduler initiates the batch process and is deployed on Amazon EC2 across multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) for high availability (HA).
**Note**
This pattern doesn’t cover the implementation of the batch scheduler. For more information about implementation, see the software vendor documentation for your scheduler.

1. The mainframe batch job (written on a programming language such as JCL or COBOL) uses core business logic to process and generate print output, such as billing statements, ID cards, and loan statements. The job is deployed on Amazon EC2 across two Availability Zones for HA and uses Rocket Software Print Exit to route print output to LRS VPSX/MFI for end-user printing.

1. LRS VPSX/MFI uses a TCP/IP-based LRS/Queue transmission agent to collect or capture print data from the Rocket Software JES Print Exit programming interface. Print Exit passes the necessary information to enable LRS VPSX/MFI to effectively process the spool file and dynamically build LRS/Queue commands. The commands are then run using a standard built-in function from Rocket Software.
**Note**
For more information on print data passed from Rocket Software Print Exit to LRS/Queue and LRS VPSX/MFI supported mainframe batch mechanisms, see *Print data capture* in the [Additional information](#modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-additional) section of this pattern.

1.
**Note**
A [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) provides a DNS name to integrate Rocket Enterprise Server with LRS VPSX/MFI. : LRS VPSX/MFI supports a Layer 4 load balancer. The Network Load Balancer also does a basic health check on LRS VPSX/MFI and routes traffic to the registered targets that are healthy.

1.
**Note**
The LRS VPSX/MFI print server is deployed on Amazon EC2 across two Availability Zones for HA and uses [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) as an operational data store. LRS VPSX/MFI supports both the active-active and active-passive service modes. This architecture uses multiple AZs in an active-passive pair as an active and hot standby. The Network Load Balancer performs a health check on LRS VPSX/MFI EC2 instances and routes traffic to hot standby instances in the other AZ if an active instance is in an unhealthy state. The print requests are persisted in the LRS Job Queue locally in each of the EC2 instances. In the event of recovery, a failed instance has to be restarted for the LRS services to resume processing the print request. : LRS VPSX/MFI can also perform health checks at the printer fleet level. For more information, see *Printer fleet health checks* in the [Additional information](#modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-additional) section of this pattern.

1. [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) integrates with LRS/DIS to perform print workflow authentication and authorization. For more information, see *Print authentication and authorization *in the [Additional information](#modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-additional) section of this pattern.

1. LRS VPSX/MFI uses Amazon EBS for block storage. You can back up Amazon EBS data from active EC2 instances to Amazon S3 as point-in-time snapshots and restore them to hot standby EBS volumes. To automate the creation, retention, and deletion of Amazon EBS volume snapshots, you can use [Amazon Data Lifecycle Manager](https://aws.amazon.com/blogs/aws/new-lifecycle-management-for-amazon-ebs-snapshots/) to set the frequency of automated snapshots and restore them based on your [RTO/RPO requirements](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Tools
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-tools"></a>

**AWS services**
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) provides block level storage volumes for use with EC2 instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can use Amazon EC2 to launch as many or as few virtual servers as you need, and you can scale out or scale in.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for a relational database and manages common database administration tasks.
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), also known as AWS Managed Microsoft AD, enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.

**Other tools**
+ [LRS VPSX/MFI (Micro Focus Interface)](https://www.lrsoutputmanagement.com/products/vpsx-enterprise/), co-developed by LRS and Rocket Software, captures output from a Rocket Enterprise Server JES spool and reliably delivers it to a specified print destination.
+ LRS Directory Information Server (LRS/DIS) is used for authentication and authorization during the print workflow.
+ TCP/IP-based LRS/Queue transmission agent is used by LRS VPSX/MFI to collect or capture print data through the Rocket Software JES Print Exit programming interface.
+ [Rocket Enterprise Server](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-A2F23243-962B-440A-A071-480082DF47E7.html) is an application deployment environment for mainframe applications. It provides the execution environment for mainframe applications that are migrated or created by using any version of Rocket Software Enterprise Developer.

## Epics
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-epics"></a>

### Set up Rocket Enterprise Server on Amazon EC2 and deploy a mainframe batch application
<a name="set-up-rocket-enterprise-server-on-amazon-ec2-and-deploy-a-mainframe-batch-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Rocket Enterprise Server and deploy a demo application. | Set up Rocket Enterprise Server on Amazon EC2, and then deploy the Rocket Software BankDemo demonstration application on Amazon EC2.<br />The BankDemo application is a mainframe batch application that creates and then initiates print output. | Cloud architect |

### Set up an LRS print server on Amazon EC2
<a name="set-up-an-lrs-print-server-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get an LRS product license for printing. | To get an LRS product license for LRS VPSX/MFI, LRS/Queue, and LRS/DIS, contact the [LRS Output Management team](https://www.lrsoutputmanagement.com/about-us/contact-us/). You must provide the host names of the EC2 instances where the LRS products will be installed. | Build lead |
| Create an Amazon EC2 Windows instance to install LRS VPSX/MFI. | Launch an Amazon EC2 Windows instance by following the instructions from [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) in the Amazon EC2 documentation. Your instance must meet the following hardware and software requirements for LRS VPSX/MFI:  + CPU – Dual Core<br />+ RAM – 16 GB<br />+ Drive – 500 GB<br />+ Minimum EC2 instance – m5.xlarge<br />+ OS – Windows/Linux<br />+ Software – Internet Information Service (IIS) or ApacheThe preceding hardware and software requirements are intended for a small printer fleet (around 500–1000). To get the full requirements, consult with your LRS and AWS contacts.<br />When you create your Windows instance, do the following:1. Confirm that the EC2 host name is the same host name used for the LRS product license.<br />2. Enable CGI in Amazon EC2 by completing the following:Connect to your EC2 instance by following the instructions from | Cloud architect |
| Install LRS VPSX/MFI on the EC2 instance. | 1. Connect to your EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation. <br />2. Open the link to the product download page from the LRS email that you should receive. : LRS products are distributed by electronic file transfer (EFT). <br />3. Download LRS VPSX/MFI and unzip the file (default folder: `c:\LRS`).<br />4. Launch the LRS Product Installer from the unzipped folder to install LRS VPSX/MFI. <br />5. In the **Select Features** menu, select **VPSX® Server (V1R3.022)**, and then choose **Next** to start the installation process. You will receive a success message when installation is complete. | Cloud architect |
| Install LRS/Queue. | 1. Connect to your Rocket Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the link to the LRS product download page from the LRS email that you should receive, download LRS/Queue, and then unzip the file.<br />3. Go to the location where you downloaded the files, and then launch the LRS product installer to install LRS/Queue. | Cloud architect |
| Install LRS/DIS. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the link to the LRS product download page from the LRS email that you should receive, download LRS/DIS, and then unzip the file.<br />3. Go to the location where you downloaded the files, and then launch the LRS Product Installer.<br />4. In the LRS Product Installer, expand **LRS Misc Tools**, select** LRS DIS**, and then choose **Next**.<br />5. Follow the rest of the instructions in the LRS Product Installer to complete the installation process. | Cloud architect |
| Create a target group and register LRS VPSX/MFI EC2 as the target. | Create a target group by following the instructions from [Create a target group for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html) in the Elastic Load Balancing documentation.<br />When you create the target group, do the following:1. On the **Specify group details **page, for **Choose a** **Target Type**, choose **Instances**.<br />2. For **Protocol**,** **choose **TCP**.<br />3. For **Port**, choose **5500**. <br />4. On the **Register targets** page, in the **Available instances** section, select the LRS VPSX/MFI EC2 instances. | Cloud architect |
| Create a Network Load Balancer. | Follow the instructions from [Create a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html) in the Elastic Load Balancing documentation. Your Network Load Balancer routes traffic from Rocket Enterprise Server to LRS VPSX/MFI EC2.<br />When you create the Network Load Balancer, do the following on the **Listeners and Routing** page:1. For **Protocol**, choose **TCP**. <br />2. For **Port**, choose **5500**.<br />3. For **Default action**, choose **Forward to** for the target group that you created earlier. | Cloud architect |

### Integrate Rocket Enterprise Server with LRS VPSX/MFI and LRS/Queue
<a name="integrate-rocket-enterprise-server-with-lrs-vpsx-mfi-and-lrs-queue"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Rocket Enterprise Server for LRS/Queue integration. | 1. Connect to your Rocket Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In the Windows Start menu, open the Rocket Enterprise Server Administration UI.<br />3. In the menu bar, choose **NATIVE**.<br />4. In the navigation pane, choose **Directory Server**, and then choose **BANKDEMO**.<br />5. From **General **in the left navigation pane, scroll down to the **Additional** section to configure the environment variables (LRSQ\_ADDRESS, LRSQ\_PORT, LRSQ\_COMMAND) to point to LRSQ.<br />6. For **LRSQ\_ADDRESS**, enter the IP address or DNS name of the Network Load Balancer that you created earlier.<br />7. For **LRSQ\_PORT**, enter **VPSX LRSQ Listener Port (5500)**.<br />8. For **LRSQ\_COMMAND**, enter the path location of the LRSQ executable.LRS currently supports a maximum character limit of 50 for DNS names, but this is subject to change in the future. If your DNS name is greater than 50, then you can use the IP address of the Network Load Balancer as an alternative. | Cloud architect |
| Configure Rocket Enterprise Server for LRS VPSX/MFI integration. | 1. Copy the `VPSX_MFI_R2` folder from the LRS VPSX/MFI installer to the Rocket Enterprise Server location at `C\BANKDEMO\print`.<br />2. Connect to your Rocket Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />3. In the Windows Start menu, open the Rocket Enterprise Server Administration UI.<br />4. In the menu bar, choose **NATIVE**.<br />5. In the navigation pane, choose **Directory Server**, and then choose **BANKDEMO**.<br />6. Under **BANKDEMO**, choose **JES**.<br />7. Under **JES Program Path**, add the `DLL(VPSX_MFI_R2)` path from the `C\BANKDEMO\print` location. | Cloud architect |

### Set up printers and print users in Rocket Enterprise Server and LRS VPSX/MFI
<a name="set-up-printers-and-print-users-in-rocket-enterprise-server-and-lrs-vpsx-mfi"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Associate the Rocket Software Print Exit module to the Rocket Enterprise Server batch printer Server Execution Process. | 1. Connect to your Rocket Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In the Windows Start menu, open the Rocket Enterprise Server Administration UI.<br />3. In the menu bar, choose **NATIVE**.<br />4. In the navigation pane, choose **Directory Server**, and then choose **BANKDEMO**.<br />5. Under **BANKDEMO**, choose **JES**, and scroll down to **Printers**.<br />6. In** Printers**,** **associate the Rocket Software Print Exit module (LRSPRTE6 for Batch) to the Rocket Enterprise Server batch printer Server Execution Process (SEP). This allows print output routing to LRS VPSX/MFI.<br />7. Sign in to the Enterprise Server Administration UI.For more information about configuration, see [Using the Exit](https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/HCOMCMJCLOS025.html) in the Micro Focus documentation. | Cloud architect |
| Add a printer in LRS VPSX/MFI. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the VPSX Web Interface from the Windows Start menu.<br />3. In the navigation pane, choose **Printers**.<br />4. Choose **Add**, and then choose **Add Printer**.<br />5. On the **Printer Configuration **page, for **Printer Name**, enter **Local**.<br />6. For **VPSX ID**, enter **VPS1**.<br />7. For **CommType**, select **TCPIP/LRSQ**.<br />8. For **Host/IP Address**, enter the IP address of the physical printer that you want to add.<br />9. For **Device**, enter the name of your device.<br />10. Choose either **Windows Driver** or **Linux/Mac Driver**.<br />11. Choose **Add**. | Cloud architect |
| Create a print user in LRS VPSX/MFI. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the VPSX Web Interface from the Windows Start menu.<br />3. In the navigation pane, choose **Security**, and then choose **Users**.<br />4. In the **User Name** column, choose **admin**, and then choose **Copy**.<br />5. In the **User Profile Maintenance** window, for **User Name**, enter a user name (for example, **PrintUser**).<br />6. For **Description**, enter a brief description (for example, **User for test print**).<br />7. Choose **Update**. This creates a print user (for example, **PrintUser**).<br />8. In the navigation pane, under **User**,** **choose the new user that you created.<br />9. From the **Command** menu, choose **Security**.<br />10. On the **Security Rules** page, choose all the applicable printer security and job security options, and then choose **Save**.<br />11. To add your new print user to the **Administrator** group, go to the navigation pane, choose **Security**, and then choose **Configure**.<br />12. In the **Security configuration** window, add your new print user to the **Administrator** column. | Cloud architect |

### Set up print authentication and authorization
<a name="set-up-print-authentication-and-authorization"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS Managed Microsoft AD domain with users and groups. | 1. Create an Active Directory on AWS Managed Microsoft AD by following the instructions from [Create your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html#ms_ad_getting_started_create_directory) in the AWS Directory Service documentation. <br />2. Deploy an EC2 instance (Active Directory manager) and install Active Directory tools to manage your AWS Managed Microsoft AD by following the instructions from [Step 3: Deploy an EC2 instance to manage your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbasestep3.html) in the AWS Directory Service documentation.<br />3. Connect to your EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation. : When you connect to the EC2 instance, enter your administrator credentials (for the directory that you created in step one) in the Windows Security window.<br />4. In the Windows Start menu, under **Windows Administrative Tools**, choose **Active Directory Users and Computers**.<br />5. Create a print user in the Active Directory domain by following the steps from [Create a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html) in the AWS Directory service documentation. | Cloud architect |
| Join LRS VPSX/MFI EC2 to an AWS Managed Microsoft AD domain. | Join LRS VPSX/MFI EC2 to your AWS Managed Microsoft AD domain [automatically](https://repost.aws/knowledge-center/ec2-systems-manager-dx-domain) (AWS Knowledge Center documentation) or [manually](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html) (AWS Directory Service documentation). | Cloud architect |
| Configure and integrate LRS/DIS with AWS Managed Microsoft AD. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In the Windows Start** **menu, open the VPSX Web Interface.<br />3. In the navigation pane, choose **Security**, and then choose **Configure**.<br />4. On the **Security Configuration** page, in the **Security Parameters** section, for **Security Type**, select **Internal**.<br />5. Enter your preferences for the rest of the options in the **Security Parameters** section.<br />6. Open the **LRS Output Management** folder from the Microsoft Windows Start menu, choose **Server Start**, and then choose **Server Stop**.<br />7. Log in to LRS VPSX/MFI with your Active Directory user name and password. | Cloud architect |

### Test a print workflow
<a name="test-a-print-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initiate a batch print request from the Rocket Software BankDemo app. | 1. Open the 3270 terminal emulator in your Rocket Enterprise Server EC2 instance.<br />2. Connect to the BankDemo app by running the following command: `connect 127.0.0.1:9278`<br />3. On the BankDemo command line interface, for **User id**, enter **B0001**. For **Password**, enter a non-blank key.<br />4. For the **Request printed statement(s)** option, enter **X** on the blank line.<br />5. In the **Send statement by** section, for **Mail**, enter **Y**, and then press F10. | Test engineer |
| Check the print output in LRS VPSX/MFI. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In Windows Start menu, open the VPSX Web Interface.<br />3. In the navigation pane, choose **Printers**, and then choose **Output Queue**.<br />4. In the **Spool ID** column, choose the spool ID for the request in the printer queue.<br />5. On the **Actions** tab, in the **COMMAND **column, choose **Browse**. You can now see the print output of an account statement with columns for **Account No.**, **Description**, **Date**, **Amount**, and **Balance**. For an example, see the **batch\_print\_output **attachment for this pattern. | Test engineer |

## Related resources
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-resources"></a>
+ [LRS Output Modernization](https://www.lrsoutputmanagement.com/) (LRS documentation)
+ [ANSI and machine carriage controls](https://www.ibm.com/docs/en/cmofz/9.5.0?topic=tips-ansi-machine-carriage-controls) (IBM documentation)
+ [Channel command words](https://www.ibm.com/docs/en/zos/2.3.0?topic=devices-channel-command-words) (IBM documentation)
+ [Empowering Enterprise Mainframe Workloads on AWS with Micro Focus](https://aws.amazon.com/blogs/apn/empowering-enterprise-grade-mainframe-workloads-on-aws-with-micro-focus/) (AWS Partner Network Blog)
+ [Build a Micro Focus Enterprise Server PAC with Amazon EC2 Auto Scaling and Systems Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager.html) (AWS Prescriptive Guidance documentation)
+ [Advanced Function Presentation (AFP) data stream](https://www.ibm.com/docs/en/i/7.4?topic=streams-advanced-function-presentation-data-stream) (IBM documentation)
+ [Line Conditioned Data Stream (LCDS)](https://www.compart.com/en/lcds) (Compart documentation)

## Additional information
<a name="modernize-mainframe-batch-printing-workloads-on-aws-by-using-rocket-enterprise-server-and-lrs-vpsx-mfi-additional"></a>

**Considerations**

During your modernization journey, you may consider a wide variety of configurations for both mainframe batch processes and the output they generate. The mainframe platform has been customized by every customer and vendor that uses it with particular requirements that directly affect print. For example, your current platform may incorporate the IBM Advanced Function Presentation (AFP) or the Xerox Line Condition Data Stream (LCDS) into the current workflow. Additionally, [mainframe carriage control characters](https://www.ibm.com/docs/en/cmofz/9.5.0?topic=tips-ansi-machine-carriage-controls) and [channel command words](https://www.ibm.com/docs/en/zos/2.3.0?topic=devices-channel-command-words) can affect the look of the printed page and may need special handling. As part of the modernization planning process, we recommend that you assess and understand the configurations in your specific print environment.

**Print data capture**

Rocket Software Print Exit passes the necessary information to enable LRS VPSX/MFI to effectively process the spool file. The information consists of fields passed in the relevant control blocks, such as:
+ JOBNAME
+ OWNER (USERID)
+ DESTINATION
+ FORM
+ FILENAME
+ WRITER

LRS VPSX/MFI supports the following mainframe batch mechanisms for capturing data from Rocket Enterprise Server.
+ BATCH COBOL print/spool processing using standard z/OS JCL SYSOUT DD/OUTPUT statements
+ BATCH COBOL print/spool processing using standard z/OS JCL CA-SPOOL SUBSYS DD statements
+ IMS/COBOL print/spool processing using the CBLTDLI interface (For a full list of supported methods and programming examples, see the LRS documentation that’s included with your product license.)

**Printer fleet health checks**

LRS VPSX/MFI (LRS LoadX) can perform deep dive health checks, including device management and operational optimization. Device management can detect failure in a printer device and route the print request to a healthy printer. For more information about deep dive health checks for printer fleets, see the LRS documentation that’s included with your product license.

**Print authentication and authorization **

LRS/DIS enables LRS applications to authenticate user IDs and passwords by using Microsoft Active Directory or an LDAP server. In addition to basic print authorization, LRS/DIS can also apply granular-level print security controls in the following use cases:
+ Manage who can browse the printer job.
+ Manage the browsing level of other user's jobs.
+ Manage operational tasks. For example, command-level security such as hold/release, purge, modify, copy, and reroute. Security can be set up by either the User-ID or Group (similar to AD group or LDAP group).** **

## Attachments
<a name="attachments-36de7312-4860-4702-a325-c01cf74c4f33"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/36de7312-4860-4702-a325-c01cf74c4f33/attachments/attachment.zip)
