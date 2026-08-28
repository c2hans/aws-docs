---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk.html
---

# Migrate a .NET application from Microsoft Azure App Service to AWS Elastic Beanstalk
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk"></a>

*Raghavender Madamshitti, Amazon Web Services*

## Summary
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-summary"></a>

This pattern describes how to migrate a .NET web application hosted on Microsoft Azure App Service to AWS Elastic Beanstalk. There are two ways to migrate applications to Elastic Beanstalk:
+ Use AWS Toolkit for Visual Studio - This plugin for the Microsoft Visual Studio IDE provides the easiest and most straightforward way to deploy custom .NET applications to AWS. You can use this approach to deploy .NET code directly to AWS and to create supporting resources, such as Amazon Relational Database Service (Amazon RDS) for SQL Server databases, directly from Visual Studio.
+ Upload and deploy to Elastic Beanstalk - Each Azure App Service includes a background service called Kudu, which is useful for capturing memory dumps and deployment logs, viewing configuration parameters, and accessing deployment packages. You can use the Kudu console to access Azure App Service content, extract the deployment package, and then upload the package to Elastic Beanstalk by using the upload and deploy option in the Elastic Beanstalk console.

This pattern describes the second approach (uploading your application to Elastic Beanstalk through Kudu). The pattern also uses the following AWS services: AWS Elastic Beanstalk, Amazon Virtual Private Cloud (Amazon VPC), Amazon CloudWatch, Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling, Amazon Simple Storage Service (Amazon S3), and Amazon Route 53.

The .NET web application is deployed to AWS Elastic Beanstalk, which runs in an Amazon EC2 Auto Scaling Group. You can set up a scaling policy based on Amazon CloudWatch metrics such as CPU utilization. For a database, you can use Amazon RDS in a Multi-AZ environment, or Amazon DynamoDB, depending on your application and business requirements.

## Prerequisites and limitations
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A .NET web application running in Azure App Service
+ Permission to use the Azure App Service Kudu console

**Product versions**
+ .NET Core (x64) 1.0.1, 2.0.0, or later, or .NET Framework 4.x, 3.5 (see [.NET on Windows Server platform history](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-dotnet.html))
+ Internet Information Services (IIS) version 8.0 or later, running on Windows Server 2012 or later
+ .NET 2.0 or 4.0 Runtime.

## Architecture
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-architecture"></a>

**Source technology stack  **
+  Application developed using .NET Framework 3.5 or later, or .NET Core 1.0.1, 2.0.0, or later, and hosted on Azure App Service (web app or API app)

**Target technology stack**
+ AWS Elastic Beanstalk running in an Amazon EC2 Auto Scaling group

**Migration architecture**

![Kudu accesses Azure App Service content, gets deployment package, uploads it to Elastic Beanstalk.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/df606a2d-b0a8-4035-b377-0a760e7300c9/images/dd15f97b-9cf2-4bcc-af45-44df1c4ca4a5.png)

**Deployment workflow**

![Deployment workflow to create app, publish it to launch environment, and then manage environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/df606a2d-b0a8-4035-b377-0a760e7300c9/images/accec77d-c753-4166-8f27-bd4932b3d884.png)

## Tools
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-tools"></a>

**Tools**
+ .NET Core or .NET Framework
+ C\#
+ IIS
+ Kudu console

**AWS services and features**
+ [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) – Elastic Beanstalk is an easy-to-use service for deploying and scaling .NET web applications. Elastic Beanstalk automatically manages capacity provisioning, load balancing, and auto scaling.
+ [Amazon EC2 Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) – Elastic Beanstalk includes an Auto Scaling group that manages the Amazon EC2 instances in the environment. In a single-instance environment, the Auto Scaling group ensures that there is always one instance running. In a load-balanced environment, you can configure the group with a range of instances to run, and Amazon EC2 Auto Scaling adds or removes instances as needed, based on load.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) – When you enable load balancing in AWS Elastic Beanstalk, it creates a load balancer that distributes traffic among the EC2 instances in the environment.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) – Elastic Beanstalk automatically uses Amazon CloudWatch to provide information about your application and environment resources. Amazon CloudWatch supports standard metrics, custom metrics, and alarms.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) – Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. You can use Route 53 alias records to map custom domain names to AWS Elastic Beanstalk environments.

## Epics
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-epics"></a>

### Set up a VPC
<a name="set-up-a-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a virtual private cloud (VPC). | In your AWS account, create a VPC with the required information. | System administrator |
| Create subnets. | Create two or more subnets in your VPC. | System administrator |
| Create a route table. | Create a route table, based on your requirements. | System administrator |

### Set up Elastic Beanstalk
<a name="set-up-elastic-beanstalk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access the Azure App Service Kudu console. | Access Kudu through the Azure portal by navigating to the App Service dashboard, and then choosing **Advanced Tools**, **Go**. Or, you can modify the Azure App Service URL as follows: `https://<appservicename>.scm.azurewebsites.net`. | App developer, System administrator |
| Download the deployment package from Kudu. | Navigate to Windows PowerShell by choosing the **DebugConsole** option. This will open the Kudo console. Go to the `wwwroot` folder and download it. This will download the Azure App Service deployment package as a zip file. For an example, see the attachment. | App developer, System administrator |
| Create a package for Elastic Beanstalk. | Unzip the deployment package that you downloaded from Azure App Service. Create a JSON file called `aws-windows-deployment-manifest.json` (this file is required only for .NET Core applications). Create a zip file that includes `aws-windows-deployment-manifest.json` and the Azure App Service deployment package file. For an example, see the attachment. | App developer, System administrator |
| Create a new Elastic Beanstalk application. | Open the Elastic Beanstalk console. Choose an existing application or create a new application. | App developer, System administrator |
| Create the environment. | In the Elastic Beanstalk console **Actions** menu, choose **Create environment**. Select the web server environment and .NET/IIS platform. For application code, choose **Upload**. Upload the zip file that you prepared for Elastic Beanstalk, and then choose **Create Environment**. | App developer, System administrator |
| Configure Amazon CloudWatch. | By default, basic CloudWatch monitoring is enabled. If you want to change the configuration, in the Elastic Beanstalk wizard, choose the published application, and then choose **Monitoring**. | System administrator |
| Verify that the deployment package is in Amazon S3.  | When the application environment has been created, you can find the deployment package in the S3 bucket. | App developer, System administrator |
| Test the application. | When the environment has been created, use the URL provided in the Elastic Beanstalk console to test the application. | System administrator |

## Related resources
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-resources"></a>
+ [AWS Elastic Beanstack concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html) (Elastic Beanstalk documentation)
+ [Getting Started with .NET on Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-getstarted.html) (Elastic Beanstalk documentation)
+ [Kudu console](https://github.com/projectkudu/kudu/wiki/Kudu-console) (GitHub)
+ [Using "Kudu" to Manage Azure Web Apps](https://www.gslab.com/blogs/kudu-azure-web-app/) (GS Lab article)
+ [Custom ASP.NET Core Elastic Beanstalk Deployments](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/deployment-beanstalk-custom-netcore.html) (AWS Toolkit for Visual Studio user guide)
+ [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
+ [AWS Elastic Beanstalk Supported Platforms](https://docs.amazonaws.cn/en_us/elasticbeanstalk/latest/platforms/platforms-supported.html) (Elastic Beanstalk documentation)
+ [Deploy a Web Application to AWS](https://www.c-sharpcorner.com/article/deploying-a-web-application-to-aws/) (C\# Corner article)
+ [Scaling the Size of Your Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling_plan.html) (Amazon EC2 documentation)
+ [High Availability (Multi-AZ) for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) (Amazon RDS documentation)

## Additional information
<a name="migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk-additional"></a>

**Notes**
+ If you are migrating an on-premises or Azure SQL Server database to Amazon RDS, you must update the database connection details as well.
+ For testing purposes, a sample demo application is attached.

## Attachments
<a name="attachments-df606a2d-b0a8-4035-b377-0a760e7300c9"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/df606a2d-b0a8-4035-b377-0a760e7300c9/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
