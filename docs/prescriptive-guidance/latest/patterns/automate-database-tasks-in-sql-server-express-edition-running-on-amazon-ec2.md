---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2.html
---

# Automate database tasks in SQL Server Express on Amazon EC2 by using AWS Lambda and Task Scheduler
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2"></a>

*Subhani Shaik, Amazon Web Services*

## Summary
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-summary"></a>

This pattern demonstrates how to schedule and manage database tasks in SQL Server Express edition, which is the free version of SQL Server. However, SQL Server Express edition lacks the SQL Server Agent service that typically handles automated database operations. This pattern explains how you can use Task Scheduler and AWS Lambda as an alternative for automating database tasks in SQL Server Express edition running on an Amazon Elastic Compute Cloud (Amazon EC2) instance.

[Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) is a built-in Windows system utility that facilitates the automatic execution of routine tasks. It provides a mechanism to schedule and manage automated operations, eliminating the need for manual intervention in recurring processes. [AWS Lambda](https://aws.amazon.com/lambda/) is a serverless computing service that automatically runs code in response to events, without requiring you to manage the underlying infrastructure.

## Prerequisites and limitations
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A virtual private cloud (VPC) created with Amazon Virtual Private Cloud (Amazon VPC)
+ An Amazon EC2 instance with Windows Server
+ Amazon Elastic Block Store (Amazon EBS) volumes that are attached to an Amazon EC2 instance with Windows Server
+ [SQL Server Express Edition](https://www.microsoft.com/en-us/download/details.aspx?id=101064) binaries

**Limitations**
+ For information about feature limitations of SQL Server Express edition, see the [Microsoft website](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver16).
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ SQL Server 2016 or later with SQL Server Express edition

## Architecture
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-architecture"></a>

The following diagram shows an Amazon EC2 instance running with SQL Server Express edition installed. The instance is accessible through Remote Desktop Protocol (RDP) client or from AWS Systems Manager Session Manager. AWS Key Management Service (AWS KMS) handles the data encryption for the Amazon EBS volumes to ensure data-at-rest security. The infrastructure also includes AWS Identity and Access Management (IAM), which provides access control and manages permissions for the execution of Lambda functions. Amazon Simple Storage Service (Amazon S3) stores Lambda functions.

![An Amazon EC2 instance running with SQL Server Express edition installed on a private subnet.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3af2174d-bf49-4e43-86f7-34759e5eea84/images/3a37dcb8-10af-42f2-8ff1-fab4f87eb646.png)

## Tools
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-tools"></a>

**AWS services**
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) provides block-level storage volumes for use with Amazon EC2 instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) is a fully managed AWS Systems Manager tool. With Session Manager, you can manage your Amazon EC2 instances, edge devices, on-premises servers, and virtual machines (VMs).
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [Microsoft SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/download-sql-server-management-studio-ssms) is a tool for managing SQL Server, including accessing, configuring, and administering SQL Server components.
+ [Python](https://www.python.org/) is a general-purpose computer programming language. You can use it to build applications, automate tasks, and develop services on the [AWS Cloud](https://aws.amazon.com/developer/language/python/).
+ [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) is a Microsoft tool that you can use to schedule routine tasks on your computer automatically.

## Best practices
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-best-practices"></a>
+ [Best practices for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html)
+ [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Epics
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-epics"></a>

### Create an Amazon EC2 instance and install SQL Server Express edition
<a name="create-an-amazon-ec2-instance-and-install-sql-server-express-edition"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy an Amazon EC2 instance. | To create an Amazon EC2 instance, open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/) and select an [Amazon Machine Image (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html) from the list of instances available for Windows Server.<br />For more information, see [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) in the AWS documentation. | DBA, AWS DevOps |
| Install SQL Server Express edition. | To install SQL Server Express edition, complete the following steps:1. To [connect to your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html), choose an option:**Option A **– Use Remote Desktop Protocol (RDP). For instructions, see [Connect to your Windows instance using an RDP client](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-rdp.html) in the AWS documentation.**Option B **– Use the Amazon EC2 console and AWS Systems Manager Session Manager. For instructions, see [Connect to your Amazon EC2 instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-systems-manager-session-manager.html) in the AWS documentation.<br />2. To download the required SQL Server Express edition, go to [SQL Server Downloads](https://www.microsoft.com/en-in/sql-server/sql-server-downloads) on the Microsoft website.<br />3. To install SQL Server Express edition, follow the instructions in [Plan a SQL Server installation](https://learn.microsoft.com/en-us/sql/sql-server/install/planning-a-sql-server-installation?view=sql-server-ver16) on the Microsoft website. | DBA, AWS DevOps |

### Create automated database maintenance tasks
<a name="create-automated-database-maintenance-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify routine tasks. | Identify the routine tasks that you want to automate. For example, the following tasks are eligible for automation:+ Database backups (Full, differential, and transaction log)<br />+ Index maintenance and reorganization<br />+ Statistics updates<br />+ Application-specific operations<br />+ Data cleanup or archiving | DBA |
| Prepare SQL scripts. | To prepare SQL scripts, do the following:1. Create SQL queries for each maintenance task. Following is an example [T-SQL](https://learn.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver16) query to perform a specific database backup: `Backup Database <Database_Name> To Disk='C:\Backups\Database_Name.bak'`<br />2. Save the script file as `<File Name>.sql`. Then, save the scripts to an accessible location on the server’s local drive on the Amazon EC2 instance or a network file share. | DBA |
| Configure access permissions. | To configure access permissions, do the following:1. Set appropriate file system permissions. For instructions, see [Configure file system permissions for Database Engine access](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-file-system-permissions-for-database-engine-access?view=sql-server-ver16) on the Microsoft website.<br />2. Check that the SQL Server service account has the necessary access. For instructions, see [Configure Windows service accounts and permissions](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-windows-service-accounts-and-permissions?view=sql-server-ver16) on the Microsoft website.<br />3. Verify network connectivity for remote shares. For more information, see [Accessing data using file shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html) in the AWS documentation. | DBA |

### Automate tasks with Task Scheduler
<a name="automate-tasks-with-task-scheduler"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create batch files. | + To create a batch file, use a text editor to type the following command. Replace the parameters `username` and `password` with your own values. Then save the file as `<Name>.bat`.<pre>sqlcmd -S servername -U username -P password -i <T-SQL query path.sql></pre>+ To create a batch file for SQL tasks, use a text editor and type the following commands. Replace the parameters `ServerName`, `DatabaseName`, `username`, and `password` with your own values. Then save the file as `<Name>.bat`.<pre><br />@echo off<br />sqlcmd -S [ServerName] -d [DatabaseName] -U username -P password -i "PathToSQLScript\Script.sql" -o "PathToOutput\Output.txt"</pre> | AWS DevOps, DBA |
| Create tasks in Task Scheduler. | To create a task in Task Scheduler, use the following steps:1. To open Task Scheduler, type **taskschd.msc** in Windows search.<br />2. Choose the **Action **menu, and then select **Create Basic Task**.<br />3. For **Name**, provide a name for the task, and then choose **Next**.<br />4. For **Trigger**, select the option for when you want the task to start and then choose **Next**.<br />5. Provide the **Start** and **Recur **information for the task, and then choose **Next**.<br />6. For the **Action **section, select **Start a program** and then choose **Next**.<br />7. For **Program/script**, specify the path for the batch file that you created in the previous task and then choose **Next**.<br />8. Choose **Finish**.<br />To run the task manually, right-click the newly created task and then select **Run**. | DBA |
| View task status. | To view the status of a task in Task Scheduler, use the following steps:1. In Task Scheduler, go to **Task Scheduler Library**, which displays all tasks.<br />2. To see the status of the task that you created earlier, select the task and then go to the **History **tab. | DBA, AWS DevOps |

### Automate tasks with AWS Lambda
<a name="automate-tasks-with-lamlong"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Implement the solution. | To implement this pattern’s solution, use the following steps:1. Create a Lambda function. For instructions, see [Create your first Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) in the AWS documentation. <br />2. Schedule the Lambda function. For instructions, see [Invoke a Lambda function on a schedule](https://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html) in the AWS documentation.<br />3. Run T-SQL queries. For more information, see [Tutorial: Using a Lambda function to access an Amazon RDS database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-lambda-tutorial.html) in the AWS documentation. The tutorial explains how to connect Amazon RDS databases from Lambda functions to run SQL queries | AWS DevOps, DevOps engineer |

## Troubleshooting
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Lambda issues | For help with errors and issues that you might encounter when using AWS Lambda, see [Troubleshooting issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html) in the AWS documentation. |

## Related resources
<a name="automate-database-tasks-in-sql-server-express-edition-running-on-amazon-ec2-resources"></a>
+ [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/)
+ [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html)
+ [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/)
+ [Task Scheduler for developers](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) (Microsoft website)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
