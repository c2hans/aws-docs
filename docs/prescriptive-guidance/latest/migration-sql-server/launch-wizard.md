---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/launch-wizard.html
---

# AWS Launch Wizard for SQL Server
<a name="launch-wizard"></a>

[AWS Launch Wizard](https://aws.amazon.com/launchwizard/) is a service that guides you through the sizing, configuration, and deployment of Microsoft SQL Server on Amazon EC2. It supports both SQL Server single instance and high availability (HA) deployments on Amazon EC2.

Launch Wizard is a free service. You pay for only the AWS resources provisioned to run your application such as Amazon EC2, Amazon EBS, and Amazon VPC resources.

You input your application requirements, including performance, number of nodes, and connectivity, on the Launch Wizard console. Launch Wizard identifies the right AWS resources to deploy and run your SQL Server application. It also provides an estimated cost of deployment, and you can modify your resources and instantly view the updated cost assessment. When you confirm your selections and initiate deployment, Launch Wizard provisions and configures the selected resources in a few hours to create a fully functioning, production-ready SQL Server application. You can access your deployed SQL Server application from the Amazon EC2 console.

 Here are some of benefits of using Launch Wizard for SQL Server:
+ **Simple deployment **─ You can simplify the provisioning of your SQL Server resources on AWS by answering questions based on your requirements. A Launch Wizard deployment is faster than a manual deployment, so it eliminates the time to provision and configure your application on AWS.
+ **Automated sizing and cost estimation** – Launch Wizard provides built-in instance selection based on your requirements. It selects the instance type, Amazon EBS volumes, and other resources that best suit your SQL Server requirements. Launch Wizard also provides you with a cost estimate before it provisions the AWS resources.
+ **Time savings with repeatable automation templates** ─ You can redeploy SQL Server with reusable CloudFormation templates that are created by Launch Wizard. These templates serve as a baseline and save you time.

Launch Wizard supports the following operating systems, SQL Server versions, and features. For the latest information, see the [Launch Wizard documentation](https://docs.aws.amazon.com/launchwizard/latest/userguide/what-is-launch-wizard.html#launch-wizard-os).

The following table shows information about deployment on Windows.

|
|
| **Use case or feature** | **Launch Wizard support** | [https://aws.amazon.com/quickstart/](https://aws.amazon.com/quickstart/)** support** | **Amazon EC2 Console support** |
| --- |--- |--- |--- |
| Single SQL node deployment | Yes | No | Yes |
| HA deployment: Always On availability groups | Yes | Yes | No |
| HA deployment: Always On Failover Cluster Instances (FCIs) with Amazon FSx for Windows File Server | Yes | Yes | No |
| HA deployment: Dedicated Hosts | Yes | Yes | No |
| Reusable code templates | Yes | Yes | No |

The following table shows information about deployment on Linux.

|
|
| **Use case or feature** | **Launch Wizard support** | [https://aws.amazon.com/quickstart/](https://aws.amazon.com/quickstart/)** support** | **Amazon EC2 Console support** |
| --- |--- |--- |--- |
| Single SQL node deployment | Yes | No | Yes |
| HA deployment on Ubuntu | Yes | No | No |
| Reusable code templates | Yes | No | No |

The following table shows information about sizing.

|
|
| **Use case or feature** | **Launch Wizard support** | [https://aws.amazon.com/quickstart/](https://aws.amazon.com/quickstart/)** support** | **Amazon EC2 Console support** |
| --- |--- |--- |--- |
| Instance type recommendation | Yes | No | No |
| Cost estimation | Yes | No | No |

The following table shows information about configuration.

|
|
| **Use case or feature** | **Launch Wizard support** | [https://aws.amazon.com/quickstart/](https://aws.amazon.com/quickstart/)** support** | **Amazon EC2 Console support** |
| --- |--- |--- |--- |
| Automatically created AWS Systems Manager resource group | Yes | No | No |
| One-click Amazon SNSnotification | Yes | No | No |
| One-click Amazon CloudWatch monitoring | Yes | No | No |
| Connecting to existing Active Directory (both on-premises and managed) | Yes | No | No |
| Early input validation | Yes | No | No |
| Managed IAM policy | Yes | No | No |

For more information about Launch Wizard for SQL Server, see the following:
+ [AWS Launch Wizard for SQL Server documentation](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql.html)
+ [Simplify SQL Server Always On deployments with AWS Launch Wizard and Amazon FSx](https://aws.amazon.com/blogs/storage/simplify-sql-server-always-on-deployments-with-the-aws-launch-wizard-and-amazon-fsx/) blog post
+ [Accelerate SQL Server Always On Deployments with AWS Launch Wizard](https://aws.amazon.com/blogs/aws/accelerate-sql-server-always-on-deployments-with-aws-launch-wizard/) blog post
