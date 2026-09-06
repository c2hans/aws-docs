---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager.html
---

# Build a Micro Focus Enterprise Server PAC with Amazon EC2 Auto Scaling and Systems Manager
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager"></a>

*Kevin Yung and Krithika Palani Selvam, Amazon Web Services*

*Peter Woods, None*

*Abraham Rondon, Micro Focus*

## Summary
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-summary"></a>

This pattern introduces a scalable architecture for mainframe applications using [Micro Focus Enterprise Server in Scale-Out Performance and Availability Cluster (PAC)](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-F6E1BBB7-AEC2-45B1-9E36-1D86B84D2B85.html) and an Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling group on Amazon Web Services (AWS). The solution is fully automated with AWS Systems Manager and Amazon EC2 Auto Scaling lifecycle hooks. By using this pattern, you can set up your mainframe online and batch applications to achieve high resiliency by automatically scaling in and out based on your capacity demands.

**Note**
This pattern was tested with Micro Focus Enterprise Server version 6.0. For version 8, see [Set up Micro Focus Runtime (on Amazon EC2)](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup.html).

## Prerequisites and limitations
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Micro Focus Enterprise Server software and license. For details, contact [Micro Focus sales](https://www.microfocus.com/en-us/contact/contactme).
+ An understanding of the concept of rebuilding and delivering a mainframe application to run in Micro Focus Enterprise Server. For a high-level overview, see [Micro Focus Enterprise Server Data Sheet](https://www.microfocus.com/media/data-sheet/enterprise_server_ds.pdf).
+ An understanding of the concepts in Micro Focus Enterprise Server scale-out Performance and Availability Cluster. For more information, see the [Micro Focus Enterprise Server documentation](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-F6E1BBB7-AEC2-45B1-9E36-1D86B84D2B85.html).
+ An understanding of the overall concept of mainframe application DevOps with continuous integration (CI). For an AWS Prescriptive Guidance pattern that was developed by AWSand Micro Focus, see [Mainframe modernization: DevOps on AWS with Micro Focus](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/mainframe-modernization-devops-on-aws-with-micro-focus.html).

**Note**
This pattern was tested with Micro Focus Enterprise Server version 6. For version 8, see [Set up Micro Focus Runtime (on Amazon EC2)](https://docs.aws.amazon.com/m2/latest/userguide/mf-runtime-setup.html).

**Limitations **
+ For a list of platforms that are supported by Micro Focus Enterprise Server, see the [Micro Focus Enterprise Server Data Sheet](https://www.microfocus.com/media/data-sheet/enterprise_server_ds.pdf).
+ The scripts and tests used in this pattern are based on Amazon EC2 Windows Server 2019; other Windows Server versions and operating systems were not tested for this pattern.
+ The pattern is based on Micro Focus Enterprise Server 6.0 for Windows; earlier or later releases were not tested in the development of this pattern.

**Product versions**
+ Micro Focus Enterprise Server 6.0
+ Windows Server 2019

## Architecture
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-architecture"></a>

In the conventional mainframe environment, you must provision hardware to host your applications and corporate data. To cater for and meet the spikes in seasonal, monthly, quarterly, or even unprecedented or unexpected demands, mainframe users must *scale out* by purchasing additional storage and compute capacity. Increasing the number of storage and compute capacity resources improves overall performance, but the scaling is not linear.

This is not the case when you start adopting an on-demand consumption model on AWS by using Amazon EC2 Auto Scaling and Micro Focus Enterprise Servers. The following sections explain detail how to build a fully automated, scalable mainframe application architecture using Micro Focus Enterprise Server Scale-Out Performance and Availability Cluster (PAC) with an Amazon EC2 Auto Scaling group.

**Micro Focus Enterprise Server automatic scaling architecture**

First, it is important to understand the basic concepts of Micro Focus Enterprise Server. This environment provides a mainframe-compatible, x86 deployment environment for applications that have traditionally run on the IBM mainframe. It delivers both online and batch runs and a transaction environment that supports the following:
+ IBM COBOL
+ IBM PL/I
+ IBM JCL batch jobs
+ IBM CICS and IMS TM transactions
+ Web services
+ Common batch utilities, including SORT

Micro Focus Enterprise Server enables mainframe applications to run with minimal changes. Existing mainframe workloads can be moved to x86 platforms and modernized to take advantage of AWS Cloud native extensions for rapid expansion to new markets or geographies.

The AWS Prescriptive Guidance pattern [Mainframe modernization: DevOps on AWS with Micro Focus](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/mainframe-modernization-devops-on-aws-with-micro-focus.html) introduced the architecture to accelerate the development and testing of mainframe applications on AWS using Micro Focus Enterprise Developer and Enterprise Test Server with AWS CodePipeline and AWS CodeBuild. This pattern focuses on the deployment of mainframe applications to the AWS production environment to achieve high availability and resiliency.

In a mainframe production environment, you might have set up IBM Parallel Sysplex in the mainframe to achieve high performance and high availability. To create a scale-out architecture similar to Sysplex, Micro Focus introduced the Performance and Availability Cluster (PAC) to Enterprise Server. PACs support mainframe application deployment onto multiple Enterprise Server regions managed as a single image and scaled out in Amazon EC2 instances. PACs also support predictable application performance and system throughput on demand.

In a PAC, multiple Enterprise Server instances work together as a single logical entity. Failure of one Enterprise Server instance, therefore, will not interrupt business continuity because capacity is shared with other regions while new instances are automatically started using industry standard functionality such as an Amazon EC2 Auto Scaling group. This removes single points of failure, improving resilience to hardware, network, and application issues. Scaled-out Enterprise Server instances can be operated and managed by using the Enterprise Server Common Web Administration (ESCWA) APIs, simplifying the operational maintenance and serviceability of Enterprise Servers.

**Note**
Micro Focus recommends that the [Performance and Availability Cluster (PAC)](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-C06DC883-8A67-44DB-8553-8F0DD2062DAB.html) should consist of at least three Enterprise Server regions so that availability is not compromised in the event an Enterprise Server region fails or requires maintenance.

PAC configuration requires a supported relational database management service (RDBMS) to manage the region database, a cross-region database, and optional data store databases. A data store database should be used to managed Virtual Storage Access Method (VSAM) files using the Micro Focus Database File Handler support to improve availability and scalability. Supported RDBMSs include the following:
+ Microsoft SQL Server 2009 R2 and later
+ PostgreSQL 10.x, including Amazon Aurora PostgreSQL-Compatible Edition
+ DB2 10.4 and later

For details of supported RDBMS and PAC requirements, see [Micro Focus Enterprise Server - Prerequisites](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-486C5A4B-E3CD-4B17-81F3-32F9DE970EA5.html) and [Micro Focus Enterprise Server - Recommended PAC Configuration](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-7038DB6F-E89F-4B5F-BCAA-BD1456F6CCA3.html).

The following diagram shows a typical AWS architecture setup for a Micro Focus PAC.

![A three-Availability Zone architecture with five steps described in a table after the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/64e3c22b-1058-4ab8-855f-18bbbed5dc13/images/df291568-a442-454f-80bf-49e4ffff4f6d.png)

|
|
|  | ** Component** | **Description** |
| --- |--- |--- |
| 1 | Enterprise Server instances automatic scaling group | Set up an automatic scaling group deployed with Enterprise Server instances in a PAC. The number of instances can be scaled out or in initiated by Amazon CloudWatch alarms using CloudWatch metrics. |
| 2 | Enterprise Server ESCWA instances automatic scaling group  | Set up an automatic scaling group deployed with Enterprise Server Common Web Administration (ESCWA). ESCWA provides cluster management APIs.   The ESCWA servers act as a control plane to add or remove Enterprise Servers and start or stop Enterprise Server regions in the PAC during the Enterprise Server instance automatic scaling events.   Because the ESCWA instance is used only for the PAC management, its traffic pattern is predictable, and its automatic scaling desired capacity requirement can be set to 1.  |
| 3 | Amazon Aurora instance in a Multi-AZ setup | Set up a relational database management system (RDBMS) to host both user and system data files to be shared across the Enterprise Server instances. |
| 4 | Amazon ElastiCache (Redis OSS) instance and replica | Set up an ElastiCache (Redis OSS) primary instance and at least one replica to host user data and act as a scale-out repository (SOR) for the Enterprise Server instances. You can configure one or more [scale-out repository](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-3840E10F-80AA-4109-AF2C-894237D3AD00.html) to store specific types of user data.   Enterprise Server uses a Redis NoSQL database as an SOR, [a requirement to maintain PAC integrity](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-176B97CA-4F9F-4CE1-952F-C3F4FB0ADD25.html). |
| 5 | Network Load Balancer | Set up a load balancer, providing a hostname for applications to connect to the services provided by Enterprise Server instances (for example, accessing the application through a 3270 emulator). |

These components form the minimum requirement for a Micro Focus Enterprise Server PAC cluster. The next section covers cluster management automation.

**Using AWS Systems Manager Automation for scaling**

After the PAC cluster is deployed on AWS, the PAC is managed through the Enterprise Server Common Web Administration (ESCWA) APIs.

To automate the cluster management tasks during automatic scaling events, you can use Systems Manager Automation runbooks and Amazon EC2 Auto Scaling with Amazon EventBridge. The architecture of these automations is shown in the following diagram.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/64e3c22b-1058-4ab8-855f-18bbbed5dc13/images/6f9e4035-fafd-4aee-a6cc-d5e95d6514c2.png)

|
|
|  | **Component** | **Description** |
| --- |--- |--- |
| 1 | Automatic scaling lifecycle hook | Set up automatic scaling lifecycle hooks and send notifications to Amazon EventBridge when new instances are launched and existing instances are terminated in the automatic scaling group. |
| 2 | Amazon EventBridge | Set up an Amazon EventBridge rule to route automatic scaling events to Systems Manager Automation runbook targets. |
| 3 | Automation runbooks | Set up Systems Manager Automation runbooks to run Windows PowerShell scripts and invoke ESCWA APIs to manage the PAC. For examples, see the *Additional information* section. |
| 4 | Enterprise Server ESCWA instance in an automatic scaling group | Set up an Enterprise Server ESCWA instance in an automatic scaling group. The ESCWA instance provides APIs to manage the PAC.  |

## Tools
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-tools"></a>
+ [Micro Focus Enterprise Server](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-A2F23243-962B-440A-A071-480082DF47E7.html) – Micro Focus Enterprise Server provides the run environment for applications created with any integrated development environment (IDE) variant of Enterprise Developer.
+ [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) – Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Auto Scaling groups, and specify minimum and maximum numbers of instances.
+ [Amazon ElastiCache (Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) – Amazon ElastiCache is a web service for setting up, managing, and scaling a distributed in-memory data store or cache environment in the cloud. It provides a high-performance, scalable, and cost-effective caching solution.
+ [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) – Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for a relational database and manages common database administration tasks.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) – AWS Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Using the Systems Manager console, you can view operational data from multiple AWS services and automate operational tasks across your AWS resources. Systems Manager helps you maintain security and compliance by scanning your managed instances and reporting on (or taking corrective action on) any policy violations it detects.

## Epics
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-epics"></a>

### Create an Amazon Aurora instance
<a name="create-an-amazon-aurora-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS CloudFormation template for an Amazon Aurora instance. | Use the [AWS example code snippet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RDS.html) to make a CloudFormation template that will create an Amazon Aurora PostgreSQL-Compatible Edition instance. | Cloud architect |
| Deploy a CloudFormation stack to create the Amazon Aurora instance. | Use the CloudFormation template to create an Aurora PostgreSQL-Compatible instance that has Multi-AZ replication enabled for production workloads. | Cloud architect |
| Configure database connection settings for Enterprise Server. | Follow the instructions in the [Micro Focus documentation](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-40748F62-84B3-4B7B-8E96-5484ADEDFB5F.html) to prepare the connection strings and database configuration for Micro Focus Enterprise Server. | Data engineer, DevOps engineer |

### Create an Amazon ElastiCache cluster for the Redis instance
<a name="create-an-elclong-cluster-for-the-redis-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFormation template for the Amazon ElastiCache cluster for the Redis instance. | Use the [AWS example code snippet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.html) to make a CloudFormation template that will create an Amazon ElastiCache cluster for the Redis instance. | Cloud architect |
| Deploy the CloudFormation stack to create an Amazon ElastiCache cluster for the Redis instance. | Create the Amazon ElastiCache cluster for the Redis instance that has Multi-AZ replication enabled for production workloads. | Cloud architect |
| Configure Enterprise Server PSOR connection settings. | Follow the instructions in the [Micro Focus documentation](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-2A420ADD-4CA6-472D-819F-371C037C0653.html) to prepare the PAC Scale-Out Repository (PSOR) connection configuration for Micro Focus Enterprise Server PAC. | DevOps engineer |

### Create a Micro Focus Enterprise Server ESCWA automatic scaling group
<a name="create-a-micro-focus-enterprise-server-escwa-automatic-scaling-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Micro Focus Enterprise Server AMI. | Create an Amazon EC2 Windows Server instance and install the Micro Focus Enterprise Server binary in the EC2 instance. Create an Amazon Machine Image (AMI) of the EC2 instance. For more information, see the [Enterprise Server installation documentation](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-FACEF60F-BAE3-446C-B2B4-4379A5DF6D9F.html). | Cloud architect |
| Create a CloudFormation template for Enterprise Server ESCWA.  | Use the [AWS example code snippet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AutoScaling.html) to make a template for creating a custom stack of Enterprise Server ESCWA in an automatic scaling group. | Cloud architect |
| Deploy the CloudFormation stack to create an Amazon EC2 scaling group for Enterprise Server ESCWA. | Use the CloudFormation template to deploy the automatic scaling group with the Micro Focus Enterprise Server ESCWA AMI created in the previous story. | Cloud architect |

### Create an AWS Systems Manager Automation runbook
<a name="create-an-aws-systems-manager-automation-runbook"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFormation template for a Systems Manager Automation runbook. | Use the example code snippets in the *Additional information* section to make a CloudFormation template that will create a Systems Manager Automation runbook for automating PAC creation, Enterprise Server scale in, and Enterprise Server scale out. | Cloud architect |
| Deploy the CloudFormation stack that contains the Systems Manager Automation runbook. | Use the CloudFormation template to deploy a stack that contains the Automation runbook for PAC creation, Enterprise Server scale in, and Enterprise Server scale out. | Cloud architect |

### Create an automatic scaling group for Micro Focus Enterprise Server
<a name="create-an-automatic-scaling-group-for-micro-focus-enterprise-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFormation template for setting up an automatic scaling group for Micro Focus Enterprise Server. | Use the [AWS example code snippet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AutoScaling.html) to make a CloudFormation template that will create an automatic scaling group. This template will reuse the same AMI that was created for the Micro Focus Enterprise Server ESCWA instance. <br />Then use an [AWS example code snippet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html) to create the automatic scaling lifecycle event and set up Amazon EventBridge to filter for scale-out and scale-in events in the same CloudFormation template. | Cloud architect |
| Deploy the CloudFormation stack for the automatic scaling group for Micro Focus Enterprise Servers. | Deploy the CloudFormation stack that contains the automatic scaling group for Micro Focus Enterprise Servers. | Cloud architect |

## Related resources
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-resources"></a>
+ [Micro Focus Enterprise Server Performance and Availability Cluster (PAC)](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-613F5E2D-2FBC-47AE-9327-48CA4FF84C5B.html)
+ [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)
+ [Running automations with triggers using EventBridge](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-cwe-target.html)

## Additional information
<a name="build-a-micro-focus-enterprise-server-pac-with-amazon-ec2-auto-scaling-and-systems-manager-additional"></a>

The following scenarios must be automated for scaling in or scaling out the PAC clusters.

**Automation for starting or recreating a PAC**

At the start of a PAC cluster, Enterprise Server requires ESCWA to invoke APIs to create a PAC configuration. This starts and adds Enterprise Server regions into the PAC. To create or recreate a PAC, use the following steps:

1. Configure a [PAC Scale-Out Repository (PSOR)](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-2A420ADD-4CA6-472D-819F-371C037C0653.html) in ESCWA with a given name.

   ```
   POST /server/v1/config/groups/sors
   ```

1. Create a PAC with a given name and attach the PSOR to it.

   ```
   POST /server/v1/config/groups/pacs
   ```

1. Configure the region database and cross-region database if this is the first time you are setting up a PAC.
**Note**
This step uses SQL queries and the Micro Focus Enterprise Suite command line **dbhfhadmin** tool to create the database and import initial data.

1. Install the PAC definition into the Enterprise Server regions.

   ```
   POST /server/v1/config/mfds
   POST /native/v1/config/groups/pacs/${pac_uid}/install
   ```

1. Start Enterprise Server regions in the PAC.

   ```
   POST /native/v1/regions/${host_ip}/${port}/${region_name}/start
   ```

The previous steps can be implemented by using a Windows PowerShell script.

The following steps explain how to build an automation for creating a PAC by reusing the Windows PowerShell script.

1. Create an Amazon EC2 launch template that downloads or creates the Windows PowerShell script as part of the bootstrap process. For example, you can use EC2 user data to download the script from an Amazon Simple Storage Service (Amazon S3) bucket.

1. Create an AWS Systems Manager Automation runbook to invoke the Windows PowerShell script.

1. Associate the runbook to the ESCWA instance by using the instance tag.

1. Create an ESCWA automatic scaling group by using the launch template.

You can use the following example AWS CloudFormation snippet to create the Automation runbook.

*Example CloudFormation snippet for a Systems Manager Automation runbook used for PAC creation*

```
  PACInitDocument:
     Type: AWS::SSM::Document
     Properties:
       DocumentType: Command
       Content:
         schemaVersion: '2.2'
         description: Operation Runbook to create Enterprise Server PAC
         mainSteps:
         - action: aws:runPowerShellScript
           name: CreatePAC
           inputs:
             onFailure: Abort
             timeoutSeconds: "1200"
             runCommand:
             - |
               C:\Scripts\PAC-Init.ps1
  PacInitAutomation:
     Type: AWS::SSM::Document
     Properties:
       DocumentType: Automation
       Content:
         description: Prepare Micro Focus PAC Cluster via ESCWA Server
         schemaVersion: '0.3'
         assumeRole: !GetAtt SsmAssumeRole.Arn
         mainSteps:
           - name: RunPACInitDocument
             action: aws:runCommand
             timeoutSeconds: 300
             onFailure: Abort
             inputs:
               DocumentName: !Ref PACInitDocument
               Targets:
                 - Key: tag:Enterprise Server - ESCWA
                   Values:
                     - "true"
   PacInitDocumentAssociation:
     Type: AWS::SSM::Association
     Properties:
       DocumentVersion: "$LATEST"
       Name: !Ref PACInitDocument
       Targets:
         - Key: tag:Enterprise Server - ESCWA
           Values:
             - "true"
```

For more information, see [Micro Focus Enterprise Server - Configuring a PAC](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-2B15EBA5-84AF-47C3-9F8E-EE57EB17245F.html).

**Automation for scaling out with a new Enterprise Server instance**

When an Enterprise Server instance is scaled out, its Enterprise Server region must be added to the PAC. The following steps explain how to invoke ESCWA APIs and add the Enterprise Server region into the PAC.

1. Install the PAC definition into the Enterprise Server regions.

   ```
   POST '/server/v1/config/mfds'
   POST /native/v1/config/groups/pacs/${pac_uid}/install
   ```

1. Warm Start the region in the PAC.

   ```
   POST /native/v1/regions/${host_ip}/${port}/${region_name}/start
   ```

1. Add the Enterprise Server instance to the load balancer by associating the automatic scaling group to the load balancer.

The previous steps can be implemented by using a Windows PowerShell script. For more information, see [Micro Focus Enterprise Server - Configuring a PAC](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-2B15EBA5-84AF-47C3-9F8E-EE57EB17245F.html).

The following steps can be used to build an event driven automation to add a newly launched Enterprise Server instance into a PAC by reusing the Windows PowerShell script.

1. Create an Amazon EC2 launch template for Enterprise Server instance that provisions an Enterprise Server Region during its bootstrap. For example, you can use the Micro Focus Enterprise Server command mfds to import a region configuration. For further details and options available for this command, see the [Enterprise Server Reference](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/HRADRHCOMM06.html).

1. Create an Enterprise Server automatic scaling group that uses the launch template created in the previous step.

1. Create a Systems Manager Automation runbook to invoke the Windows PowerShell script.

1. Associate the runbook to the ESCWA instance by using the instance tag.

1. Create an Amazon EventBridge rule to filter for the EC2 Instance Launch Successful event for the Enterprise Server automatic scaling group, and create the target to use the Automation runbook.

You can use the following example CloudFormation snippet to create the Automation runbook and the EventBridge rule.

*Example CloudFormation snippet for Systems Manager used for scaling out Enterprise Server instances*

```
  ScaleOutDocument:
     Type: AWS::SSM::Document
     Properties:
       DocumentType: Command
       Content:
         schemaVersion: '2.2'
         description: Operation Runbook to Adding MFDS Server into an existing PAC
         parameters:
           MfdsPort:
             type: String
           InstanceIpAddress:
             type: String
             default: "Not-Available"
           InstanceId:
             type: String
             default: "Not-Available"
         mainSteps:
         - action: aws:runPowerShellScript
           name: Add_MFDS
           inputs:
             onFailure: Abort
             timeoutSeconds: "300"
             runCommand:
             - |
               $ip = "{{InstanceIpAddress}}"
               if ( ${ip} -eq "Not-Available" ) {
                 $ip = aws ec2 describe-instances --instance-id {{InstanceId}} --output text --query "Reservations[0].Instances[0].PrivateIpAddress"
               }
               C:\Scripts\Scale-Out.ps1 -host_ip ${ip} -port {{MfdsPort}}

   PacScaleOutAutomation:
     Type: AWS::SSM::Document
     Properties:
       DocumentType: Automation
       Content:
         parameters:
           MfdsPort:
             type: String
           InstanceIpAddress:
             type: String
             default: "Not-Available"
           InstanceId:
             type: String
             default: "Not-Available"
         description: Scale Out 1 New Server in Micro Focus PAC Cluster via ESCWA Server
         schemaVersion: '0.3'
         assumeRole: !GetAtt SsmAssumeRole.Arn
         mainSteps:
           - name: RunScaleOutCommand
             action: aws:runCommand
             timeoutSeconds: 300
             onFailure: Abort
             inputs:
               DocumentName: !Ref ScaleOutDocument
               Parameters:
                 InstanceIpAddress: "{{InstanceIpAddress}}"
                 InstanceId: "{{InstanceId}}"
                 MfdsPort: "{{MfdsPort}}"
               Targets:
                 - Key: tag:Enterprise Server - ESCWA
                   Values:
                     - "true"
```

**Automation for scaling in an Enterprise Server instance**

Similar to scaling out, when an Enterprise Server instance is *scaled in*, the event EC2 Instance-terminate Lifecycle Action is initiated, and the following process and API calls are needed to remove a Micro Focus Enterprise Server instance from the PAC.

1. Stop the region in the terminating Enterprise Server instance.

   ```
   POST "/native/v1/regions/${host_ip}/${port}/${region_name}/stop"
   ```

1. Remove the Enterprise Server Instance from the PAC.

   ```
   DELETE "/server/v1/config/mfds/${uid}"
   ```

1. Send signal to continue terminating the Enterprise Server instance.

The previous steps can be implemented in a Windows PowerShell script. For additional details of this process, see [Micro Focus Enterprise Server document - Administering a PAC](https://www.microfocus.com/documentation/enterprise-developer/ed60/ES-WIN/GUID-E864E2E9-EB49-43BF-9AAD-7FE334749441.html).

The following steps explain how to build an event-driven automation to terminate an Enterprise Server instance from a PAC by reusing the Windows PowerShell script.

1. Create a Systems Manager Automation runbook to invoke the Windows PowerShell script.

1. Associate the runbook to the ESCWA instance by using the instance tag.

1. Create an automatic scaling group lifecycle hook for EC2 instance termination.

1. Create an Amazon EventBridge rule to filter EC2 Instance-terminate Lifecycle Action event for the Enterprise Server automatic scaling group, and create the target to use the Automation runbook.

You can use the following example CloudFormation template for creating a Systems Manager Automation runbook, lifecycle hook, and EventBridge rule.

*Example CloudFormation snippet for a Systems Manager Automation runbook used for scaling in an Enterprise Server instance*

```
  ScaleInDocument:
     Type: AWS::SSM::Document
     Properties:
       DocumentType: Command
       Content:
         schemaVersion: '2.2'
         description: Operation Runbook to Remove MFDS Server from PAC
         parameters:
           MfdsPort:
             type: String
           InstanceIpAddress:
             type: String
             default: "Not-Available"
           InstanceId:
             type: String
             default: "Not-Available"
         mainSteps:
         - action: aws:runPowerShellScript
           name: Remove_MFDS
           inputs:
             onFailure: Abort
             runCommand:
             - |
               $ip = "{{InstanceIpAddress}}"
               if ( ${ip} -eq "Not-Available" ) {
                 $ip = aws ec2 describe-instances --instance-id {{InstanceId}} --output text --query "Reservations[0].Instances[0].PrivateIpAddress"
               }
               C:\Scripts\Scale-In.ps1 -host_ip ${ip} -port {{MfdsPort}}

   PacScaleInAutomation:
     Type: AWS::SSM::Document
     Properties:
       DocumentType: Automation
       Content:
         parameters:
           MfdsPort:
             type: String
           InstanceIpAddress:
             type: String
             default: "Not-Available"
           InstanceId:
             type: String
             default: "Not-Available"
         description: Scale In 1 New Server in Micro Focus PAC Cluster via ESCWA Server
         schemaVersion: '0.3'
         assumeRole: !GetAtt SsmAssumeRole.Arn
         mainSteps:
           - name: RunScaleInCommand
             action: aws:runCommand
             timeoutSeconds: "600"
             onFailure: Abort
             inputs:
               DocumentName: !Ref ScaleInDocument
               Parameters:
                 InstanceIpAddress: "{{InstanceIpAddress}}"
                 MfdsPort: "{{MfdsPort}}"
                 InstanceId: "{{InstanceId}}"
               Targets:
                 - Key: tag:Enterprise Server - ESCWA
                   Values:
                     - "true"
           - name: TerminateTheInstance
             action: aws:executeAwsApi
             inputs:
               Service: autoscaling
               Api: CompleteLifecycleAction
               AutoScalingGroupName: !Ref AutoScalingGroup
               InstanceId: "{{ InstanceId }}"
               LifecycleActionResult: CONTINUE
               LifecycleHookName: !Ref ScaleInLifeCycleHook
```

**Automation for an Amazon EC2 automatic scaling trigger**

The process of setting up a scaling policy for Enterprise Server instances requires an understanding of the application behavior. In most cases, you can set up target tracking scaling policies. For example, you can use the average CPU utilization as the Amazon CloudWatch metric to set for the automatic scaling policy. For more information, see [Target tracking scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html). For applications that have regular traffic patterns, consider using a predictive scaling policy. For more information, see [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html).
