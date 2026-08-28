---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx.html
---

# Set up Multi-AZ infrastructure for a SQL Server Always On FCI by using Amazon FSx
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx"></a>

*Manish Garg, T.V.R.L.Phani Kumar Dadi, Nishad Mankar, and RAJNEESH TYAGI, Amazon Web Services*

## Summary
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-summary"></a>

If you need to migrate a large number of Microsoft SQL Server Always On Failover Cluster Instances (FCIs) quickly, this pattern can help you minimize provisioning time. By using automation and Amazon FSx for Windows File Server, it reduces manual efforts, human-made errors, and the time required to deploy  a large number of clusters.

This pattern sets up the infrastructure for SQL Server FCIs in a Multi-Availability Zone (Multi-AZ) deployment on Amazon Web Services (AWS). The provisioning of the AWS services required for this infrastructure is automated by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates. SQL Server installation and cluster node creation on an [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance is performed by using PowerShell commands.

This solution uses a highly available Multi-AZ [Amazon FSx for Windows](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) file system as the shared witness for storing the SQL Server database files. The Amazon FSx file system and EC2 Windows instances that host SQL Server are joined to the same AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) domain.

## Prerequisites and limitations
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS user with sufficient permissions to provision resources using AWS CloudFormation templates
+ AWS Directory Service for Microsoft Active Directory
+ Credentials in AWS Secrets Manager to authenticate to AWS Managed Microsoft AD in a key-value pair:
  + `ADDomainName`: <Domain Name>
  + `ADDomainJoinUserName`: <Domain Username>
  + `ADDomainJoinPassword`:<Domain User Password>
  + `TargetOU`: <Target OU Value>
**Note**
You will use the same key name in AWS Systems Manager automation for the AWS Managed Microsoft AD join activity.
+ SQL Server media files for SQL Server installation and Windows service or domain accounts created, which will be used during cluster creation
+ A virtual private cloud (VPC), with two public subnets in separate Availability Zones, two private subnets in the Availability Zones, an internet gateway, NAT gateways, route table associations, and a jump server

**Product versions**
+ Windows Server 2012 R2 and Microsoft SQL Server 2016

## Architecture
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-architecture"></a>

**Source technology stack**
+ On-premises SQL Server with FCIs using a shared drive

**Target technology stack**
+ AWS EC2 instances
+ Amazon FSx for Windows File Server
+ AWS Systems Manager Automation runbook
+ Network configurations (VPC, subnets, internet gateway, NAT gateways, jump server, security groups)
+ AWS Secrets Manager
+ AWS Managed Microsoft AD
+ Amazon EventBridge
+ AWS Identity and Access Management (IAM)

**Target architecture**

The following diagram shows an AWS account in a single AWS Region, with a VPC that includes two Availability Zones, two public subnets with NAT gateways, a jump server in the first public subnet, two private subnets, each with an EC2 instance for a SQL Server node in a node security group, and an Amazon FSx file system connecting to each of the SQL Server nodes. AWS Directory Service, Amazon EventBridge, AWS Secrets Manager, and AWS Systems Manager are also included.

![Multi-AZ architecture with resources in public and private subnets, with node security groups.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f09c0164-be2d-4665-a574-7ec29fd25082/images/543829a9-e130-4542-9c4e-7518c6cbe967.png)

**Automation and scale**
+ You can use AWS Systems Manager to join AWS Managed Microsoft AD and perform the SQL Server installation.

## Tools
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) provides multiple ways to use Microsoft Active Directory (AD) with other AWS services such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS) for SQL Server, and Amazon FSx for Windows File Server.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

**Other tools**
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS. This pattern uses PowerShell scripts.

**Code repository**

The code for this pattern is available in the GitHub [aws-windows-failover-cluster-automation](https://github.com/aws-samples/aws-windows-failover-cluster-automation) repository.

## Best practices
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-best-practices"></a>
+ The IAM roles that are used to deploy this solution should adhere to the principle of least privilege. For more information, see the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
+ Follow the [AWS CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html).

## Epics
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-epics"></a>

### Deploy the infrastructure
<a name="deploy-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Systems Manager CloudFormation stack. | 1. Sign in to your AWS account, and open the AWS Management Console.<br />2. Navigate to the CloudFormation console, and create the Systems Manager CloudFormation stack by uploading the `ssm.yaml` template. Provide values for the following parameters:**StateUnJoinAssociationLoggingBucketName** – Provide a name for the S3 bucket that the template will create for logging purposes.**SSMAssociationADUnjoinName** – Provide a name for the `AWS::SSM::Association` resource.**SSMAutomationDocumentName** – Provide a name for the Systems Manager Automation runbook.**EventBridgeName** – Provide a name for the EventBridge event bus.<br />3. Deploy the Systems Manager CloudFormation  stack by launching the `ssm.yaml` CloudFormation template. The template will create the Systems Manager Atomation runboook that is initiated when a new EC2 instance with the tag `ADJoined: FSXADD` launches. The Automation runbook will add the instance to AWS Managed Microsoft AD directory. | AWS DevOps, DevOps engineer |
| Deploy the infrastructure stack. | After successful deployment of the Systems Manager stack, create the `infra` stack, which includes EC2 instance nodes, security groups, the Amazon FSx for Windows File Server file system, and the IAM role.1. Navigate to the CloudFormation console and launch the `infra-cf.yaml` template. To deploy this stack, the following parameters are required:`ActiveDirectoryId` – ID for AWS Managed Microsoft AD`ADDnsIpAddresses1` – Primary DNS IP address of AWS Managed Microsoft AD`ADDnsIpAddresses2` – Secondary DNS IP address of AWS Managed Microsoft AD`FSxSecurityGroupName` – Name of the Amazon FSx security group`FSxWindowsFileSystemName` – Name of the Amazon FSx drive`ImageID` – ID of the base Windows 2012 R2 image or Amazon Machine Image (AMI) used to create the SQL Server instance node`KeyPairName` – Key-value pair to attach to the EC2 instance nodes for access`Node1SecurityGroupName` – Name of the first node security group`Node2SecurityGroupName` – Name of the second node security group`OUSecretName` – Name of the secret that contains the AWS Managed Microsoft AD information`PrivateSubnet1` – ID of the first private subnet`PrivateSubnet2` – ID of the second private subnet`SqlFSxFCIName` – Name of the tag applied to the primary and secondary nodes and to Amazon FSx.`SqlFSxServerNetBIOSName1` – Name of the primary EC2 instance node (maximum of 15 characters)`SqlFSxServerNetBIOSName2` – Name of the secondary EC2 instance node (maximum of 15 characters)`VPC` – VPC ID`WorkloadInstanceType` – Type of EC2 instance<br />Deploy the `infra` stack. The stack will create all the infrastructure components that are required to set up Windows SQL Server FCI.<br />2. After the EC2 instance nodes are launched, the Systems Manager Automation document will be invoked to join these instances to AWS Managed Microsoft AD. You can track the progress on the Systems Manager console **Automation** page. | AWS DevOps, DevOps engineer |

### Set up the Windows SQL Server Always On FCI
<a name="set-up-the-windows-sql-server-always-on-fci"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Windows tools. | 1. Log in to the primary EC2 instance, which is node 1. To install the Windows features (Active Directory and FCI Tools), run the following PowerShell script.<pre>Install-WindowsFeature -Name RSAT-AD-Powershell,Failover-Clustering -IncludeManagementTools<br />Install-WindowsFeature -Name RSAT-Clustering,RSAT-ADDS-Tools,RSAT-AD-Powershell,RSAT-DHCP,RSAT-DNS-Server</pre><br />2. Log in to the secondary EC2 instance, which is node 2, and run same script to enable features on node 2. | AWS DevOps, DevOps engineer, DBA |
| Prestage the cluster computer objects in Active Directory Domain Services. | To prestage the cluster name object (CNO) in Active Directory Domain Services (AD DS) and prestage a virtual computer object (VCO) for a clustered role, follow the instructions in the [Windows Server documentation](https://learn.microsoft.com/en-us/windows-server/failover-clustering/prestage-cluster-adds). | AWS DevOps, DBA, DevOps engineer |
| Create the WSFC. | To create the Windows Server Failover Clustering (WSFC) cluster, do the following:1. Log in to the primary EC2 instance, which is node 1. To create the Amazon FSx file share and grant full access to the listed AD service account, run the following code.<pre>Invoke-Command -ComputerName "<FSx Windows Remote PowerShell Endpoint>" -ConfigurationName FSxRemoteAdmin -scriptblock {<br />New-FSxSmbShare -Name "SQLDB" -Path "D:\share" -Description "SQL Databases Share" -ContinuouslyAvailable $true -FolderEnumerationMode AccessBased -EncryptData $true<br />grant-fsxsmbshareaccess -name SQLDB -AccountName "<domain\user>" -accessRight Full<br />}</pre><br />This command will also create the continuously available (CA) file share, which is optimized for use by Microsoft SQL Server.<br />2. To create the failover cluster on the primary instance (node 1), run the following command.<pre>New-Cluster -Name <CNO Name> -Node  <Node1 Name>, <Node2 Name> -StaticAddress <Node1 Secondary Private IP>, <Node2 Secondary Private IP></pre><br />The command requires the following parameters:`Name` – The name of the cluster (CNO)`Node` – The names of the primary and secondary nodes, respectively`StaticAddress` – The secondary IP addresses of the primary and secondary nodes, respectivelyA domain administrator or regular user must have administrator permission on both the nodes to create the Windows Server Failover Clustering (WSFC) cluster. Otherwise, the previous command will fail and return the message, `You do not have administrator privilege on servers`.<br />3. After the cluster is created, run the following command to attach the file share witness.<pre>Set-ClusterQuorum -FileShareWitness \\<FSx Windows Remote PowerShell Endpoint>\share\witness</pre> | AWS DevOps, DBA, DevOps engineer |
| Install the SQL Server failover cluster. | After the WSFC cluster is set up, install the SQL Server cluster on the primary instance (node1).1. In the T drive on both nodes, create `tempdb`** **and `log`** **folders. The folders are used in the PowerShell commands.<br />2. After you copy the SQL Server media files for SQL Server installation on both nodes, run the following PowerShell command on node 1 to install SQL Server on node 1.<pre>D:\setup.exe /Q  `<br />/ACTION=InstallFailoverCluster `<br />/IACCEPTSQLSERVERLICENSETERMS `<br />/FEATURES="SQL,IS,BC,Conn"  `<br />/INSTALLSHAREDDIR="C:\Program Files\Microsoft SQL Server"  `<br />/INSTALLSHAREDWOWDIR="C:\Program Files (x86)\Microsoft SQL Server"  `<br />/RSINSTALLMODE="FilesOnlyMode"  `<br />/INSTANCEID="MSSQLSERVER" `<br />/INSTANCENAME="MSSQLSERVER"  `<br />/FAILOVERCLUSTERGROUP="SQL Server (MSSQLSERVER)"  `<br />/FAILOVERCLUSTERIPADDRESSES="IPv4;<2nd Sec Private Ip node1>;Cluster Network 1;<subnet mask>"  `<br />/FAILOVERCLUSTERNETWORKNAME="<Fail over cluster Network Name>"  `<br />/INSTANCEDIR="C:\Program Files\Microsoft SQL Server"  `<br />/ENU="True"  `<br />/ERRORREPORTING=0  `<br />/SQMREPORTING=0  `<br />/SAPWD="<Domain User password>" `<br />/SQLCOLLATION="SQL_Latin1_General_CP1_CI_AS"  `<br />/SQLSYSADMINACCOUNTS="<domain\username>" `<br />/SQLSVCACCOUNT="<domain\username>"  /SQLSVCPASSWORD="<Domain User password>" `<br />/AGTSVCACCOUNT="<domain\username>"  /AGTSVCPASSWORD="<Domain User password>" `<br />/ISSVCACCOUNT="<domain\username>" /ISSVCPASSWORD="<Domain User password>"  `<br />/FTSVCACCOUNT="NT Service\MSSQLFDLauncher"  `<br />/INSTALLSQLDATADIR="\\<FSX DNS name>\share\Program Files\Microsoft SQL Server"  `<br />/SQLUSERDBDIR="\\<FSX DNS name>\share\data"  `<br />/SQLUSERDBLOGDIR="\\<FSX DNS name>\share\log" `<br />/SQLTEMPDBDIR="T:\tempdb"  `<br />/SQLTEMPDBLOGDIR="T:\log"  `<br />/SQLBACKUPDIR="\\<FSX DNS name>\share\SQLBackup" `<br />/SkipRules=Cluster_VerifyForErrors `<br />/INDICATEPROGRESS</pre> | AWS DevOps, DBA, DevOps engineer |
| Add a secondary node to the cluster. | To add SQL Server to the secondary node (node 2), run the following  PowerShell command.<pre>D:\setup.exe /Q  `<br />/ACTION=AddNode `<br />/IACCEPTSQLSERVERLICENSETERMS `<br />/INSTANCENAME="MSSQLSERVER"  `<br />/FAILOVERCLUSTERGROUP="SQL Server (MSSQLSERVER)" `<br />/FAILOVERCLUSTERIPADDRESSES="IPv4;<2nd Sec Private Ip node2>;Cluster Network 2;<subnet mask>" `<br />/FAILOVERCLUSTERNETWORKNAME="<Fail over cluster Network Name>" `<br />/CONFIRMIPDEPENDENCYCHANGE=1 `<br />/SQLSVCACCOUNT="<domain\username>"  /SQLSVCPASSWORD="<Domain User password>" `<br />/AGTSVCACCOUNT="domain\username>"  /AGTSVCPASSWORD="<Domain User password>" `<br />/FTSVCACCOUNT="NT Service\MSSQLFDLauncher" `<br />/SkipRules=Cluster_VerifyForErrors `<br />/INDICATEPROGRESS</pre> | AWS DevOps, DBA, DevOps engineer |
| Test the SQL Server FCI. | 1. On the Windows instance for one of the nodes, in **Administrative Tools**, launch the **Failover Cluster Manager**.<br />2. Navigate to **Nodes**, and confirm that the node status is **Status Running**.<br />3. Select **Roles**, open the context (right-click) menu for SQL Server (MSSQLSERVER), and select **Move and Select Node**.<br />4. After the node selection, SQL Server should be running on the other node. | DBA, DevOps engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | To clean up the resources, use the AWS CloudFormation stack deletion process:1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. On the **Stacks** page, select the `infra` stack. The stack must be currently running.<br />3. In the stack details pane, choose **Delete**.<br />4. Select **Delete stack** when prompted.<br />5. Repeat steps 2-4 for the `ssm` stack.<br />After the stack deletion is complete, the stacks will be in the `DELETE_COMPLETE` state. Stacks in the `DELETE_COMPLETE` state aren’t displayed in the CloudFormation console by default. To display deleted stacks, you must change the stack view filter as described in [Viewing deleted stacks on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-deleted-stacks.html).<br />If the deletion failed, a stack will be in the `DELETE_FAILED` state. For solutions, see [Delete stack fails](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-delete-stack-fails) in the CloudFormation documentation. | AWS DevOps, DBA, DevOps engineer |

## Troubleshooting
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS CloudFormation template failure | If the CloudFormation template fails during deployment, do the following:1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. On the **Stacks** page in the CloudFormation console, select the stack.<br />3. Choose **Events**, and check the [stack status](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html#cfn-console-view-stack-data-resources-status-codes). |
| AWS Managed Microsoft AD  join failure | To troubleshoot the join issues, follow these steps:1. Open the [Systems Manager](https://console.aws.amazon.com/systems-manager/home?region=us-east-1) console.<br />2. Select the deployment Region.<br />3. In the left pane, choose **Automation**, and locate the failed Automation runbook.<br />4. Open the Automation runbook, and check for the **Execution status and Execution steps**.<br />5. Investigate the details of the failed step to see the exact error or failure. |

## Related resources
<a name="set-up-multi-az-infrastructure-for-a-sql-server-always-on-fci-by-using-amazon-fsx-resources"></a>
+ [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server/)
+ [Using FSx for Windows File Server with Microsoft SQL Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/sql-server.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
