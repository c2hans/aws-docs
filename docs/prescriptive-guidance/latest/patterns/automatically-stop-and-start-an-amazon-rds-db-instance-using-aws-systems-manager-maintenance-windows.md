---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html
---

# Automatically stop and start an Amazon RDS DB instance using AWS Systems Manager Maintenance Windows
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows"></a>

*Ashita Dsilva, Amazon Web Services*

## Summary
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-summary"></a>

This pattern demonstrates how to automatically stop and start an Amazon Relational Database Service (Amazon RDS) DB instance on a specific schedule (for example, shutting down a DB instance outside of business hours to reduce costs) by using AWS Systems Manager Maintenance Windows. For this purpose, Systems Manager is cost-effective for typical use cases.

AWS Systems Manager Automation provides the  `AWS-StopRdsInstance` and `AWS-StartRdsInstance` runbooks to stop and start Amazon RDS DB instances. This means that you don’t need to write custom logic with AWS Lambda functions or create an Amazon CloudWatch Events rule.

Systems Manager provides two capabilities for scheduling tasks: [State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-about.html) and [Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html). State Manager sets and maintains the required state configuration for resources in your Amazon Web Services (AWS) account one time or on a specific schedule. Maintenance Windows runs tasks on the resources in your account during a specific time window. Although you can use this pattern’s approach with State Manager or Maintenance Windows, we recommend that you use Maintenance Windows because it can run one or more tasks based on assigned priority and can also run AWS Lambda functions and AWS Step Functions tasks. For more information about State Manager and Maintenance Windows, see [Choosing between State Manager and Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-vs-maintenance-windows.html) in the Systems Manager documentation.

This pattern provides detailed steps to configure two separate maintenance windows that use cron expressions to stop and then start an Amazon RDS DB instance.

## Prerequisites and limitations
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An existing Amazon RDS DB instance that you want to stop and start on a specific schedule.
+ Cron expressions for your required schedule. For example, the expression `cron(0 9 ? * MON-FRI *)` runs the task at 09:00 on every Monday, Tuesday, Wednesday, Thursday, and Friday. For more information, see [Cron and rate expressions for maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html#reference-cron-and-rate-expressions-maintenance-window) in the Systems Manager documentation.
+ Familiarity with Systems Manager.
+ Permissions to start and stop the RDS instance. For more information, see the [Epics](#automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-epics) section.

**Limitations**
+ An Amazon RDS DB instance can be stopped for up to seven days at one time. After seven days, the DB instance automatically restarts to ensure that it receives any required maintenance updates.
+ You can’t stop a DB instance that is a read replica or that has a read replica.
+ You can’t stop an Amazon RDS for SQL Server DB instance in a Multi-AZ configuration.
+ Service quotas apply to Maintenance Windows and Systems Manager Automation. For more information about service quotas, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html) in the AWS General Reference documentation.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-architecture"></a>

The following diagram shows the workflow to automatically stop and start an Amazon RDS DB instance.

![Workflow to automatically stop and start an Amazon RDS DB instance](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/45b81621-5674-4bcf-bf7c-75ae6f62524e/images/7d943830-716e-46a3-be44-7e668c3c01ff.png)

The workflow has the following steps:

1. Create a maintenance window and use cron expressions to define the stop and start schedule for your Amazon RDS DB instances.

2. Register a Systems Manager Automation task to the maintenance window by using the `AWS-StopRdsInstance` or `AWS-StartRdsInstance` runbook.

3. Register a target with the maintenance window by using a tag-based resource group for your Amazon RDS DB instances.

**Technology stack**
+ AWS CloudFormation
+ AWS Identity and Access Management (IAM)
+ Amazon RDS
+ Systems Manager

**Automation and scale**

You can stop and start multiple Amazon RDS DB instances at the same time by tagging the required Amazon RDS DB instances, creating a resource group that includes all the tagged DB instances, and registering this resource group as a target for the maintenance window.

## Tools
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) is a service that helps you model and set up your AWS resources.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) is a web service that helps you securely control access to AWS resources.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) helps you organize AWS resources into groups, tag resources, and manage, monitor, and automate tasks on grouped resources.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) is an AWS service that you can use to view and control your infrastructure on AWS. This pattern uses the following features of Systems Manager:
  + [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) simplifies common maintenance and deployment tasks of Amazon Elastic Compute Cloud (Amazon EC2) instances and other AWS resources.
  + [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) helps you define a schedule for when to perform potentially disruptive actions on your instances.

## Epics
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-epics"></a>

### Create and configure the IAM service role for Systems Manager Automation
<a name="create-and-configure-the-iam-service-role-for-sys-automation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the IAM service role for Systems Manager Automation. | Sign in to the AWS Management Console and create a service role for Systems Manager Automation. You can use one of the following two methods to create this service role:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html)<br />The Systems Manager Automation workflow invokes Amazon RDS by using a service role to perform start and stop actions on the Amazon RDS DB instance.<br />The service role must be configured with the following [inline policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) that has permissions to start and stop the Amazon RDS DB instance:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "RdsStartStop",<br />            "Effect": "Allow",<br />            "Action": [<br />                "rds:StopDBInstance",<br />                "rds:StartDBInstance"<br />            ],<br />            "Resource": "<RDS_Instance_ARN>"               <br />        },<br />        {<br />            "Sid": "RdsDescribe",<br />            "Effect": "Allow",<br />            "Action": "rds:DescribeDBInstances",<br />            "Resource": "*"<br />        }<br />    ]<br />}</pre><br />Make sure that you replace `<RDS_Instance_ARN>` with the Amazon Resource Name (ARN) of your Amazon RDS DB instance.<br />If you are unfamiliar with using IAM policies and roles, follow the instructions in the *Solution Overview* section of the [Schedule Amazon RDS stop and start using AWS Systems Manager](https://aws.amazon.com/blogs/database/schedule-amazon-rds-stop-and-start-using-aws-systems-manager/) blog post.Make sure that you record the ARN of the service role. | AWS administrator |

### Create a resource group
<a name="create-a-resource-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Tag the Amazon RDS DB instances. | Open the [Amazon RDS console](https://console.aws.amazon.com/rds/) and tag the Amazon RDS DB instances that you want to add to the resource group. A tag is metadata assigned to an AWS resource and consists of a key-value pair. We recommend that you use *Action *as the **Tag key** and *StartStop* as the **Value**.<br />For more information about this, see [Adding, listing, and removing tags](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#Tagging.HowTo) in the Amazon RDS documentation. | AWS administrator |
| Create a resource group for your tagged Amazon RDS DB instances. | Open the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups) and create a resource group based on the tag that you created for your Amazon RDS DB instances.<br />Under **Grouping Criteria**, make sure that you choose **AWS::RDS::DBInstance **for the resource type and then provide the tag's key-value pair (for example, "Action-StartStop"). This ensures that the service only checks for Amazon RDS DB instances and not other resources that have this tag.** **Make sure that you record the resource group’s name.<br />For more information and detailed steps, see [Build a tag-based query and create a group](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-tag-based) in the AWS Resource Groups documentation.  | AWS administrator |

### Configure a maintenance window to stop the Amazon RDS DB instances
<a name="configure-a-maintenance-window-to-stop-the-rds-db-instances"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a maintenance window. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html)The task to stop the DB instance runs almost instantly when initiated and doesn't span the entire duration of the maintenance window. This pattern provides the minimum values for **Duration** and **Stop initiating tasks** because they are the required parameters for a maintenance window.For more information and detailed steps, see [Create a maintenance window (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-create-mw.html) in the Systems Manager documentation. | AWS administrator |
| Assign a target to the maintenance window. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html)For more information and detailed steps, see [Assign targets to a maintenance window (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-targets.html) in the Systems Manager documentation. | AWS administrator |
| Assign a task to the maintenance window. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html)** **The **Service role** option defines the service role required for the maintenance window to run tasks. However, this role is not identical to the service role that you created earlier for Systems Manager Automation.For more information and detailed steps, see [Assign tasks to a maintenance window (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-tasks.html) in the Systems Manager documentation. | AWS administrator |

### Configure a maintenance window to start the Amazon RDS DB instances
<a name="configure-a-maintenance-window-to-start-the-rds-db-instances"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure a maintenance window to start the Amazon RDS DB instances. | Repeat the steps from the *Configure a maintenance window to stop the Amazon RDS DB instances* epic to configure another maintenance window to start the Amazon RDS DB instances at a scheduled time.You must make the following changes when you configure the maintenance window to start the DB instances:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html) | AWS administrator |

## Related resources
<a name="automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows-resources"></a>
+ [Use Systems Manager Automation documents to manage instances and cut costs off-hours](https://aws.amazon.com/blogs/mt/systems-manager-automation-documents-manage-instances-cut-costs-off-hours/) (AWS blog post)
