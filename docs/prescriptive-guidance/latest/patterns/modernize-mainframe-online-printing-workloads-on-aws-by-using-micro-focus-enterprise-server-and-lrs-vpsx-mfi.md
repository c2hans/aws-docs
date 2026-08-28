---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi.html
---

# Modernize mainframe online printing workloads on AWS by using Micro Focus Enterprise Server and LRS VPSX/MFI
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi"></a>

*Shubham Roy and Kevin Yung, Amazon Web Services*

*Abraham Rondon, Micro Focus*

*Guy Tucker, Levi, Ray and Shoup Inc*

## Summary
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-summary"></a>

This pattern shows you how to modernize your business-critical mainframe online printing workloads on the Amazon Web Services (AWS) Cloud by using Micro Focus Enterprise Server as a runtime for a modernized mainframe application and LRS VPSX/MFI (Micro Focus Interface) as a print server. The pattern is based on the [replatform](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/) mainframe modernization approach. In this approach, you migrate your mainframe online application to Amazon Elastic Compute Cloud (Amazon EC2) and migrate your mainframe database, such as IBM DB2 for z/OS, to Amazon Relational Database Service (Amazon RDS). The authentication and authorization for the modernized print workflow is performed by AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD. The LRS Directory Information Server (LRS/DIS) is integrated with AWS Managed Microsoft AD for print workflow authentication and authorization. By modernizing your online printing workloads, you can reduce IT infrastructure costs, mitigate the technical debt of maintaining legacy systems, remove data silos, increase agility and efficiency with a DevOps model, and take advantage of on-demand resources and automation in the AWS Cloud.

## Prerequisites and limitations
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A mainframe online printing or output management workload
+ Basic knowledge of how to rebuild and deliver a mainframe application that runs on Micro Focus Enterprise Server (For more information, see the [Enterprise Server](https://www.microfocus.com/media/data-sheet/enterprise_server_ds.pdf) data sheet in the Micro Focus documentation.)
+ Basic knowledge of LRS cloud printing solutions and concepts (For more information, see [Output Modernization](https://www.lrsoutputmanagement.com/products/modernization-products) in the LRS documentation.)
+ Micro Focus Enterprise Server software and license (For more information, contact [Micro Focus sales](https://www.microfocus.com/en-us/contact/contactme).)
+ LRS VPSX/MFI, LRS/Queue, and LRS/DIS software and licenses (For more information, contact [LRS sales](https://www.lrsoutputmanagement.com/about-us/contact-us/).)

**Note**
For more information about configuration considerations for mainframe online printing workloads, see *Considerations* in the *Additional information* section of this pattern.

**Product versions**
+ [Micro Focus Enterprise Server](https://www.microfocus.com/en-us/products/enterprise-server/overview?utm_campaign=7018e000000PgfnAAC&utm_content=SCH-BR-AMC-AppM-AMS&gclid=EAIaIQobChMIoZCQ6fvS9wIVxQN9Ch2MzAOlEAAYASAAEgKx2fD_BwE) 8.0 or later
+ [LRS VPSX/MFI](https://www.lrsoutputmanagement.com/products/modernization-products/) V1R3 or later

## Architecture
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-architecture"></a>

**Source technology stack**
+ Operating system – IBM z/OS
+ Programming language – Common Business-Oriented Language (COBOL) and Customer Information Control System (CICS)
+ Database – IBM DB2 for z/OS IBM Information Management System (IMS) and Virtual Storage Access Method (VSAM)
+ Security – Resource Access Control Facility (RACF), CA Top Secret for z/OS, and Access Control Facility 2 (ACF2)
+ Printing and output management – IBM mainframe z/OS printing products (IBM Infoprint Server for z/OS, LRS, and CA View)

**Target technology stack**
+ Operating system – Microsoft Windows Server running on Amazon EC2
+ Compute – Amazon EC2
+ Programming language – COBOL and CICS
+ Database – Amazon RDS
+ Security – AWS Managed Microsoft AD
+ Printing and output management – LRS printing solution on AWS
+ Mainframe runtime environment – Micro Focus Enterprise Server

**Source architecture**

The following diagram shows a typical current state architecture for a mainframe online printing workload.

![Six-step process to produce viewable output.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/924cdae7-9265-4fc9-8e5e-bb2da5368e7e/images/293368f5-d102-4f4e-b290-71da4aeff347.png)

The diagram shows the following workflow:

1. Users perform business transactions on a system of engagement (SoE) that’s built on an IBM CICS application written in COBOL.

1. The SoE invokes the mainframe service, which records the business transaction data in a system-of-records (SoR) database such as IBM DB2 for z/OS.

1. The SoR persists the business data from the SoE.

1. A user initiates a request to generate print output from the CICS SoE, which initiates a print transaction application to process the print request.

1. The print transaction application (such as a CICS and COBOL program) extracts data from the database, formats the data according to business requirements, and generates business output (print data) such as billing statements, ID cards, or loan statements. Then, the application sends a print request by using Virtual Telecommunications Access Method (VTAM). A z/OS print server (such as IBM Infoprint Server) uses NetSpool or a similar VTAM component to intercept the print requests, and then creates print output datasets on the JES spool by using JES output parameters. The JES output parameters specify routing information that the print server uses to transmit the output to a particular network printer. The term *VTAM* refers to the z/OS Communications Server and the System Network Architecture (SNA) services element of z/OS.

1. The printing output transmission component transmits the output print datasets from the JES spool to remote printers or print servers, such as LRS (as demonstrated in this pattern), IBM Infoprint Server, or email destinations.

**Target architecture**

The following diagram shows an architecture for a mainframe online printing workload that’s deployed in the AWS Cloud:

![Four-step process from initiate print request to processing on AWS to LRS printing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/924cdae7-9265-4fc9-8e5e-bb2da5368e7e/images/07c97b6f-1a86-493d-a4e0-b8321b46f9b7.png)

The diagram shows the following workflow:

1. A user initiates a print request from an online (CICS) user-interface to create print output, such as billing statements, ID cards, or loan statements.

1. The mainframe online application ([replatformed to Amazon EC2](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/)) uses the Micro Focus Enterprise Server runtime to extract data from the application database, apply business logic to the data, format the data, and then send the data to a print destination by using [Micro Focus CICS Print Exit](https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/HCOMCMJCLOU020.html) (DFHUPRNT).

1. The application database (an SoR that runs on Amazon RDS) persists data for print output.

1. The LRS VPSX/MFI printing solution is deployed on Amazon EC2, and its operational data is stored in Amazon Elastic Block Store (Amazon EBS). LRS VPSX/MFI uses a TCP/IP-based LRS/Queue transmission agent to collect print data through the Micro Focus CICS Print Exit API (DFHUPRNT) and deliver the data to a specified printer destination. The original TERMID (TERM) that’s used in the modernized CICS application is used as the VPSX/MFI Queue name.

**Note**
The target solution typically doesn’t require application changes to accommodate mainframe formatting languages, such as IBM Advanced Function Presentation (AFP) or Xerox Line Condition Data Stream (LCDS). For more information about using Micro Focus for mainframe application migration and modernization on AWS, see [Empowering Enterprise Mainframe Workloads on AWS with Micro Focus](https://aws.amazon.com/blogs/apn/empowering-enterprise-grade-mainframe-workloads-on-aws-with-micro-focus/) in the AWS documentation.

**AWS infrastructure architecture**

The following diagram shows a highly available and secure AWS infrastructure architecture for a mainframe online printing workload:

![Two Availability Zones with Micro Focus Enterprise server on EC2, Amazon RDS, and LRS printing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/924cdae7-9265-4fc9-8e5e-bb2da5368e7e/images/093555a1-342c-420c-bb90-e9440d2e8650.png)

The diagram shows the following workflow:

1. The mainframe online application (written on a programming language such as CICS or COBOL) uses core business logic to process and generate print output, such as billing statements, ID cards, and loan statements. The online application is deployed on Amazon EC2 across two [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) (AZ) for high availability (HA) and uses Micro Focus CICS Print Exit to route print output to LRS VPSX/MFI for end-user printing.

1. LRS VPSX/MFI uses a TCP/IP-based LRS/Queue transmission agent to collect or capture print data from the Micro Focus online Print Exit programming interface. Online Print Exit passes the necessary information to enable LRS VPSX/MFI to effectively process the print file and dynamically build LRS/Queue commands.
**Note**
For more information on various CICS application programing methods for print and how they are supported in Micro Focus Enterprise server and LRS VPSX/MFI, see *Print data capture* in the *Additional information* section of this pattern.

1.
**Note**
A [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) provides a DNS name to integrate Micro Focus Enterprise Server with LRS VPSX/MFI. : LRS VPSX/MFI supports a Layer 4 load balancer. The Network Load Balancer also does a basic health check on LRS VPSX/MFI and routes traffic to the registered targets that are healthy.

1. The LRS VPSX/MFI print server is deployed on Amazon EC2 across two Availability Zones for HA and uses [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) as an operational data store. LRS VPSX/MFI supports both the active-active and active-passive service modes. This architecture uses multiple Availability Zones in an active-passive pair as an active and hot standby. The Network Load Balancer performs a health check on LRS VPSX/MFI EC2 instances and routes traffic to hot standby instances in another Availability Zone if an active instance is in an unhealthy state. The print requests are persisted in the LRS Job Queue locally in each of the EC2 instances. In the event of recovery, a failed instance has to be restarted for the LRS services to resume processing the print request.
**Note**
LRS VPSX/MFI can also perform health checks at the printer fleet level. For more information, see *Printer fleet health checks* in the *Additional information* section of this pattern.

1. [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) integrates with LRS/DIS to perform print workflow authentication and authorization. For more information, see *Print authentication and authorization* in the *Additional information* section of this pattern.

1. LRS VPSX/MFI uses Amazon EBS for block storage. You can back up Amazon EBS data from active EC2 instances to Amazon S3 as point-in-time snapshots and restore them to hot standby EBS volumes. To automate the creation, retention, and deletion of Amazon EBS volume snapshots, you can use [Amazon Data Lifecycle Manager](https://aws.amazon.com/blogs/aws/new-lifecycle-management-for-amazon-ebs-snapshots/) to set the frequency of automated snapshots and restore them based on your [RTO/RPO requirements](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Tools
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-tools"></a>

**AWS services**
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon EC2 instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS Directory Service for Microsoft Active Directory (AD)](https://aws.amazon.com/directoryservice/active-directory/), also known as AWS Managed Microsoft Active Directory, enables your directory-aware workloads and AWS resources to use managed Active Directory in AWS.

**Other tools**
+ [LRS VPSX/MFI (Micro Focus Interface)](https://www.lrsoutputmanagement.com/products/modernization-products/), co-developed by LRS and Micro Focus, captures output from a Micro Focus Enterprise Server JES spool and reliably delivers it to a specified print destination.
+ LRS Directory Information Server (LRS/DIS) is used for authentication and authorization during the print workflow.
+ LRS/Queue is a TCP/IP-based LRS/Queue transmission agent, used by LRS VPSX/MFI, to collect or capture print data through the Micro Focus online Print Exit programming interface.
+ [Micro Focus Enterprise Server](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-A2F23243-962B-440A-A071-480082DF47E7.html) is an application deployment environment for mainframe applications. It provides the execution environment for mainframe applications that are migrated or created by using any version of Micro Focus Enterprise Developer.

## Epics
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-epics"></a>

### Set up Micro Focus Enterprise Server on Amazon EC2 and deploy a mainframe online application
<a name="set-up-micro-focus-enterprise-server-on-amazon-ec2-and-deploy-a-mainframe-online-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Micro Focus Enterprise Server and deploy a demo online application. | Set up Micro Focus Enterprise Server on Amazon EC2, and then deploy the Micro Focus Account Demo application (ACCT Demo) on Amazon EC2 by following the instructions from [Tutorial: CICS Support](https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/GMWALK00.html) in the Micro Focus documentation.<br />The ACCT Demo application is a mainframe online (CICS) application that creates and then initiates print output. | Cloud architect |

### Set up an LRS print server on Amazon EC2
<a name="set-up-an-lrs-print-server-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get an LRS product license for printing. | To get an LRS product license for LRS VPSX/MFI, LRS/Queue, and LRS/DIS, contact the [LRS Output Management team](https://www.lrsoutputmanagement.com/about-us/contact-us/). You must provide the host names of the EC2 instances where the LRS products will be installed. | Build lead |
| Create an Amazon EC2 Windows instance to install LRS VPSX/MFI. | Launch an Amazon EC2 Windows instance by following the instructions from [Step 1: Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-launch-instance) in the Amazon EC2 documentation. Your instance must meet the following hardware and software requirements for LRS VPSX/MFI:  + CPU – Dual Core<br />+ RAM – 16 GB<br />+ Drive – 500 GB<br />+ Minimum EC2 instance – m5.xlarge<br />+ OS – Windows/Linux<br />+ Software – Internet Information Service (IIS) or ApacheThe preceding hardware and software requirements are intended for a small printer fleet (around 500–1000). To get the full requirements, consult with your LRS and AWS contacts.<br />When you create your Windows instance, do the following:1. Confirm that the EC2 host name is the same host name used for the LRS product license.<br />2. Enable CGI in Amazon EC2 by completing the following:Connect to your EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.In the Windows Start menu, find and open Server Manager.In Server Manager, choose **Dashboard**, **Quick Start**, **Add roles and features**. Then, choose **Server roles**.In **Server roles**, choose **WebServer (IIS)**, and then choose **Application Development**.In **Application Development**, select the **CGI** check box.Follow the instructions on the Windows Server Manager **Add roles and features** wizard to install CGI.Open port 5500 in the Windows firewall of the EC2 instance for LRS/Queue communication. | Cloud architect |
| Install LRS VPSX/MFI on the EC2 instance. | 1. Connect to your EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the link to the product download page from the LRS email that you should receive. : LRS products are distributed by electronic file transfer (EFT). <br />3. Download LRS VPSX/MFI and unzip the file (default folder: `c:\LRS`).<br />4. Launch the LRS Product Installer from the unzipped folder to install LRS VPSX/MFI. <br />5. In the **Select Features** menu, select **VPSX® Server (V1R3.022)**, and then choose **Next** to start the installation process. You will receive a success message when installation is complete. | Cloud architect |
| Install LRS/Queue. | 1. Connect to your Micro Focus Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the link to the LRS product download page from the LRS email that you should receive, download LRS/Queue, and then unzip the file.<br />3. Go to the location where you downloaded the files, and then launch the LRS product installer to install LRS/Queue. | Cloud architect |
| Install LRS/DIS. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the link to the LRS product download page from the LRS email that you should receive, download LRS/DIS, and then unzip the file.<br />3. Go to the location where you downloaded the files, and then launch the LRS Product Installer.<br />4. In the LRS Product Installer, expand **LRS Misc Tools**, select** LRS DIS**, and then choose **Next**.<br />5. Follow the rest of the instructions in the LRS Product Installer to complete the installation process. | Cloud architect |
| Create a target group and register LRS VPSX/MFI EC2 as the target. | Create a target group by following the instructions from [Create a target group for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html) in the Elastic Load Balancing documentation.<br />When you create the target group, do the following:1. On the **Specify group details **page, for **Choose a** **Target Type**, choose **Instances**.<br />2. For **Protocol**,** **choose **TCP**.<br />3. For **Port**, choose **5500**. <br />4. On the **Register targets** page, in the **Available instances** section, select the LRS VPSX/MFI EC2 instances. | Cloud architect |
| Create a Network Load Balancer. | Follow the instructions from [Create a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html) in the Elastic Load Balancing documentation. Your Network Load Balancer routes traffic from Micro Focus Enterprise Server to LRS VPSX/MFI EC2.<br />When you create the Network Load Balancer, do the following on the **Listeners and Routing** page:1. For **Protocol**, choose **TCP**. <br />2. For **Port**, choose **5500**.<br />3. For **Default action**, choose **Forward to** for the target group that you created earlier. | Cloud architect |

### Integrate Micro Focus Enterprise Server with LRS VPSX/MFI and LRS/Queue
<a name="integrate-micro-focus-enterprise-server-with-lrs-vpsx-mfi-and-lrs-queue"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Micro Focus Enterprise Server for LRS/Queue integration. | 1. Connect to your Micro Focus Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In the Windows Start menu, open the Micro Focus Enterprise Server Administration UI.<br />3. In the menu bar, choose **NATIVE**.<br />4. In the navigation pane, choose **Directory Server**, and then choose **BANKDEMO **or your Enterprise server region.<br />5. From **General **in the left navigation pane, scroll down to the **Additional** section to configure the environment variables (LRSQ\_ADDRESS, LRSQ\_PORT, LRSQ\_COMMAND) to point to LRSQ.<br />6. For **LRSQ\_ADDRESS**, enter the IP address or DNS name of the Network Load Balancer that you created earlier.<br />7. For **LRSQ\_PORT**, enter **VPSX LRSQ Listener Port (5500)**.<br />8. For **LRSQ\_COMMAND**, enter the path location of the LRSQ executable.<br />9. LRS currently supports a maximum character limit of 50 for DNS names, but this is subject to change in the future. If your DNS name is greater than 50, then you can use the IP address of the Network Load Balancer as an alternative. | Cloud architect |
| Make CICS Print Exit (DFHUPRNT) available to Micro Focus Enterprise Server initialization. | 1. Connect to your Micro Focus Enterprise Server EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Copy CICS Print Exit (DFHUPRNT) from the LRS VPSX/MFI executable folder (named `VPSX_MFI_R2`) to the Micro Focus Enterprise Server EC2 instance location. For 32 bit systems, the location is `C:\Program Files (x86) \Micro Focus\Enterprise Server\bin`. For 64 bit systems, the location is `C:\Program Files (x86) \Micro Focus\Enterprise Server\bin64`. : The `DFHUPRNT_64.dll` file must be renamed to `DFHUPRNT.dll` when copied.**Validate that Micro Focus Enterprise Server has detected CICS Print Exit (DFHUPRNT)**1. Stop and start Micro Focus Enterprise Server. <br />2. In the Administration panel of Micro Focus Enterprise Server, open **Monitor**, **Logs**, **Console logs**.<br />3. Check the console logs for the following message: "3270 printer user exit DFHUPRNT installed successfully." | Cloud architect |
| Define the CICS printer's terminal ID (TERMIDs) as Micro Focus Enterprise Server. | **Enable 3270 printing in Micro Focus Enterprise Server**1. In the Administration panel of Micro Focus Enterprise Server, open **CICS**, **Resources**, **By Group**.<br />2. From the left navigation panel, choose **SIT (System Initialization Table)**, and then choose **BNKCICV**.<br />3. In the **General** section, scroll down to **3270**, and then select the **3270 Print** check box.<br />**Define the CICS printer's terminal in Micro Focus Enterprise Server**1. In the Administration panel of Micro Focus Enterprise Server, open **CICS**, **Resources**, **By Type**.<br />2. From the left navigation panel, choose **Term**, and then choose **New**. The **Create Terminal Resource** form opens.<br />3. For **Name**, enter the name of the LRS Print Queue. (**Note**: This pattern uses **"P275"** as the CICS printer's terminal ID and LRS VPSX Print Queue.) <br />4. For **Group**, enter **BANKTERM**. <br />5. For **Auto Install – Model**, enter **NO**.<br />6. For **Terminal Identifiers - Terminal type**, enter **DFHPRT32**.<br />7. For **Net name**, enter **VTAMP275**.<br />8. For **Terminal Usage**, select the **In Service** check box.<br />9. Scroll at the top of the page, and then chose **Save**.<br />10. Choose **Install**. A pop-up message displays a successful installation message. | Cloud architect |

### Set up printers and print users in Micro Focus Enterprise Server and LRS VPSX/MFI
<a name="set-up-printers-and-print-users-in-micro-focus-enterprise-server-and-lrs-vpsx-mfi"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a print queue in the LRS VPSX. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the VPSX Web Interface from the Windows Start menu.<br />3. In the navigation pane, choose **Printers**.<br />4. Choose **Add**, and then choose **Add Printer**.<br />5. On the **Printer Configuration **page, for **Printer Name**, enter **P275**.<br />6. For **VPSX ID**, enter **VPS1**.<br />7. For **CommType**, select **TCPIP/LRSQ**.<br />8. For **Host/IP Address**, enter the IP address of the physical printer that you want to add.<br />9. For **Device**, enter the name of your device.<br />10. Choose either **Windows Driver** or **Linux/Mac Driver**.<br />11. Choose **Add**.The print queue must be equivalent to the Print TERMIDs created in Micro Focus Enterprise Server. | Cloud architect |
| Create a print user in LRS VPSX/MFI. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. Open the VPSX Web Interface from the Windows Start menu.<br />3. In the navigation pane, choose **Security**, and then choose **Users**.<br />4. In the **User Name** column, choose **admin**, and then choose **Copy**.<br />5. In the **User Profile Maintenance** window, for **User Name**, enter a user name (for example, **PrintUser**).<br />6. For **Description**, enter a brief description (for example, **User for test print**).<br />7. Choose **Update**. This creates a print user (for example, **PrintUser**).<br />8. In the navigation pane, under **User**,** **choose the new user that you created.<br />9. From the **Command** menu, choose **Security**.<br />10. On the **Security Rules** page, choose all the applicable printer security and job security options, and then choose **Save**.<br />11. To add your new print user to the **Administrator** group, go to the navigation pane, choose **Security**, and then choose **Configure**.<br />12. In the **Security configuration** window, add your new print user to the **Administrator** column. | Cloud architect |

### Set up print authentication and authorization
<a name="set-up-print-authentication-and-authorization"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS Managed Microsoft AD domain with users and groups. | 1. Create an Active Directory on AWS Managed Microsoft AD by following the instructions from [Create your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html) in the AWS Directory Service documentation. <br />2. Deploy an EC2 instance (Active Directory manager) and install Active Directory tools to manage your AWS Managed Microsoft AD by following the instructions from [Step 3: Deploy an EC2 instance to manage your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbasestep3.html) in the AWS Directory Service documentation.<br />3. Connect to your EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation. : When you connect to the EC2 instance, enter your administrator credentials (for the directory that you created in step one) in the Windows Security window.<br />4. In the Windows Start menu, under **Windows Administrative Tools**, choose **Active Directory Users and Computers**.<br />5. Create a print user in the Active Directory domain by following the steps from [Create a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html) in the AWS Directory service documentation. | Cloud architect |
| Join LRS VPSX/MFI EC2 to an AWS Managed Microsoft AD domain. | Join LRS VPSX/MFI EC2 to your AWS Managed Microsoft AD domain [automatically](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-dx-domain/) (AWS Knowledge Center documentation) or [manually](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_windows_instance.html) (AWS Directory Service documentation). | Cloud architect |
| Configure and integrate LRS/DIS with AWS Managed Microsoft AD. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In the Windows Start** **menu, open the **VPSX Web Interface**.<br />3. In the navigation pane, choose **Security**, and then choose **Configure**.<br />4. On the **Security Configuration** page, in the **Security Parameters** section, for **Security Type**, select **Internal**.<br />5. Enter your preferences for the rest of the options in the **Security Parameters** section.<br />6. Open the **LRS Output Management** folder from the Microsoft Windows Start menu, choose **Server Start**, and then choose **Server Stop**.<br />7. Log in to LRS VPSX/MFI with your Active Directory user name and password. | Cloud architect |

### Test an online print workflow
<a name="test-an-online-print-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initiate an online print request from the Micro Focus ACCT Demo app. | 1. Open the TN3270 terminal emulator in your Micro Focus Enterprise Server EC2 instance. (: This pattern uses 3270 terminal emulators.) <br />2. Connect to the TN3270 terminal emulator (Rumba). For **Host name address**, use **127.0.0.1**. For **Telnet Port**, use **9270**.<br />3. After connecting to the 3270 screen, press CTL\+SHIFT\+Z to clear the screen.<br />4. To start the ACCT Demo application, in clear screen, enter **ACCT**. This opens the ACCT Demo online (CICS) application main screen. **Note**: The main screen includes menu options such as **Account file**, **To search by name**,** enter**, **Request type**, **Account**, and **Printer**.<br />5. To submit a print request from the ACCT Demo online (CICS) application, enter **P** in the **request type** field, **11111** in the **account** field, and **P275** in the **printer** field*.* Be sure to set the value in the **printer** field to the value of the CICS printer's terminal ID.<br />6. Press **Enter**.The "Print Request Scheduled" message appears at the bottom of the screen. This confirms that an online print request was generated from the ACCT Demo application and sent to LRS VPS/MFI for print processing.  | Cloud architect |
| Check the print output in LRS VPSX/MFI. | 1. Connect to your LRS VPSX/MFI EC2 instance by following the instructions from [Step 2: Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the Amazon EC2 documentation.<br />2. In the Windows Start menu, open the **VPSX Web Interface**.<br />3. In the navigation pane, choose **Printers**, and then choose **Output Queue**. Find the **P275** print queue that you created for online printing earlier.<br />4. For the print queue (**P275**), in the **Spool ID** column, choose the spool ID for the request in the printer queue.<br />5. On the **Actions** tab, in the **COMMAND **column, choose **Browse**. You can now see the print output of an account statement with columns for Account No., SURNAME, FIRST, ADDRESS, TELEPHONE, No. Cards Issued, Date issued, Amount, and Balance.<br />For an example, see the **online\_print\_output** attachment for this pattern. | Test engineer |

## Related resources
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-resources"></a>
+ [LRS Output Modernization](https://www.lrsoutputmanagement.com/products/modernization-products) (LRS documentation)
+ [VTAM networking concepts](https://www.ibm.com/docs/en/zos/2.1.0?topic=guide-vtam-networking-concepts) (IBM documentation)
+ [Summary of logical unit (LU) types](https://www.ibm.com/docs/en/wsfz-and-o/1.1?topic=installation-summary-logical-unit-lu-types) (IBM documentation)
+ [ANSI and machine carriage controls](https://www.ibm.com/docs/en/cmofz/9.5.0?topic=tips-ansi-machine-carriage-controls) (IBM documentation)
+ [Empowering Enterprise Mainframe Workloads on AWS with Micro Focus](https://aws.amazon.com/blogs/apn/empowering-enterprise-grade-mainframe-workloads-on-aws-with-micro-focus/) (AWS Partner Network Blog)
+ [Build a Micro Focus Enterprise Server PAC with Amazon EC2 Auto Scaling and Systems Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager.html) (AWS Prescriptive Guidance documentation)
+ [Advanced Function Presentation (AFP) data stream](https://www.ibm.com/docs/en/i/7.4?topic=streams-advanced-function-presentation-data-stream) (IBM documentation)
+ [Line Conditioned Data Stream (LCDS)](https://www.compart.com/en/lcds) (Compart documentation)

## Additional information
<a name="modernize-mainframe-online-printing-workloads-on-aws-by-using-micro-focus-enterprise-server-and-lrs-vpsx-mfi-additional"></a>

**Considerations**

During your modernization journey, you may consider a wide variety of configurations for mainframe online processes and the output they generate. The mainframe platform has been customized by every customer and vendor that uses it with particular requirements that directly affect print. For example, your current platform may incorporate the IBM Advanced Function Presentation (AFP) or the Xerox Line Condition Data Stream (LCDS) into the current workflow. Additionally, [mainframe carriage control characters](https://www.ibm.com/docs/en/cmofz/9.5.0?topic=tips-ansi-machine-carriage-controls) and [channel command words](https://www.ibm.com/docs/en/zos/2.3.0?topic=devices-channel-command-words) can affect the look of the printed page and may need special handling. As part of the modernization planning process, we recommend that you assess and understand the configurations in your specific print environment.

**Print data capture**

This section summarizes the CICS application programming methods that you can use in an IBM mainframe environment for printing. LRS VPSX/MFI components provide techniques to allow the same application programs to create data in the same way. The following table describes how each application programming method is supported in a modernized CICS application running in AWS and Micro Focus Enterprise Server with an LRS VPSX/MFI print server.

|
|
| Method | Description | Support for the method in a modernized environment |
| --- |--- |--- |
| EXEC CICS SEND TEXT..    or EXEC CICS SEND MAP..  | These CICS and VTAM methods are responsible for creating and delivering 3270/SCS print data streams to LUTYPE0, LUTYPE1, and LUTYPE3 print devices.  | A Micro Focus online Print Exit (DFHUPRNT) application program interface (API) enables print data to be processed by VPSX/MFI when 3270/SCS print data streams are created by using either of these methods.  |
| EXEC CICS SEND TEXT..    or EXEC CICS SEND MAP.. (with third-party IBM mainframe software) | The CICS and VTAM methods are responsible for creating and delivering 3270/SCS print data streams to LUTYPE0, LUTYPE1, and LUTYPE3 print devices. Third-party software products intercept the print data, convert the data to standard print format data with an ASA/MCH control character, and place the data on the JES spool to be processed by mainframe-based printing systems that use JES.  | A Micro Focus online Print Exit (DFHUPRNT) API enables print data to be processed by VPSX/MFI when 3270/SCS print data streams are created by using either of these methods.  |
| EXEC CICS SPOOLOPEN  | This method is used by CICS application programs to write data directly to the JES spool. The data then becomes available to be processed by mainframe-based printing systems that use JES.  | Micro Focus Enterprise Server spools the data to the Enterprise Server spool where it can be processed by the VPSX/MFI Batch Print Exit (LRSPRTE6) that spools the data to VPSX.  |
| DRS/API | An LRS-supplied programmatic interface is used for writing print data to JES.  | VPSX/MFI supplies a replacement interface that spools the print data directly to VPSX.  |

**Printer fleet health checks**

LRS VPSX/MFI (LRS LoadX) can perform deep dive health checks, including device management and operational optimization. Device management can detect failure in a printer device and route the print request to a healthy printer. For more information about deep dive health checks for printer fleets, see the LRS documentation that’s included with your product license.

**Print authentication and authorization **

LRS/DIS enables LRS applications to authenticate user IDs and passwords by using Microsoft Active Directory or an LDAP server. In addition to basic print authorization, LRS/DIS can also apply granular-level print security controls in the following use cases:
+ Manage who can browse the printer job.
+ Manage the browsing level of other user's jobs.
+ Manage operational tasks. For example, command-level security such as hold/release, purge, modify, copy, and reroute. Security can be set up by either the User-ID or Group (similar to AD group or LDAP group).

## Attachments
<a name="attachments-924cdae7-9265-4fc9-8e5e-bb2da5368e7e"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/924cdae7-9265-4fc9-8e5e-bb2da5368e7e/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
