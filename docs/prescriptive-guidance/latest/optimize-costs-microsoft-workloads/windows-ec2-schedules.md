---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/windows-ec2-schedules.html
---

# Automate stop and start schedules
<a name="windows-ec2-schedules"></a>

## Overview
<a name="windows-ec2-schedules-overview"></a>

The [Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/) can help you reduce operational costs by automating the starting and stopping of [Amazon EC2](https://aws.amazon.com/ec2/) and [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) instances. If you leave all your instances running at full utilization continuously, you could end up paying for resources that aren't being used. The Instance Scheduler on AWS enables you to turn off instances during times when they're not needed, such as during non-business hours, weekends, or other periods when usage is low. This can lead to significant cost savings over time.

The Instance Scheduler on AWS also offers cross-account instance scheduling, automated tagging, and the ability to configure schedules or periods by using a command-line interface or the [AWS Systems Manager](https://aws.amazon.com/systems-manager/) maintenance window. These features can help you manage your instances more effectively and accurately track and allocate costs across different projects or teams.

## Case studies
<a name="windows-ec2-schedules-studies"></a>

Consider the example of a company that uses Instance Scheduler on AWS in a production environment to automatically stop instances outside of business hours every day. If this company leaves all of its instances running at full utilization, they can achieve up to 70 percent cost savings for those instances that are only necessary during regular business hours. The following chart shows how the weekly utilization is reduced from 168 hours to 50 hours.

![Weekly utilization reduction chart](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/13cae0e2-2a45-4e2a-a1aa-97362d3e9b69.png)

Consider another example. The electric utility company Jamaica Public Service Company Limited (JPS) migrated its database to Amazon RDS. Now, JPS uses Amazon EC2 to host API services and run other applications. For JPS, Instance Scheduler on AWS became the key tool for managing non-production environments. JPS used the Instance Scheduler on AWS to reduce development costs and manage EC2 instances based on team needs and work schedules. This helped JPS reduce costs by 40 percent. For more information, see the AWS case study [Jamaica Public Service Migrates Efficiently to the Cloud, Reduces Costs by 40% Using AWS Instance Scheduler](https://aws.amazon.com/solutions/case-studies/jamaica-public-service-case-study/#:~:text=%E2%80%9CMigrating%20to%20AWS%20has%20minimized,EC2%20and%20Amazon%20RDS%20instances.).

## Cost optimization scenario
<a name="windows-ec2-schedules-costopt"></a>

The following example scenario helps illustrate the cost advantages of using Instance Scheduler on AWS. In this scenario, a major retail company in Singapore deploys two Windows environments on Amazon EC2. The first environment, known as workload A, is utilized by the marketing team to analyze real-time in-store transactions while the stores are open. The second environment, known as workload B, is reserved for the accounting team, which works only during regular business hours. The current operating schedule of both environments (24/7) is not ideal given current usage patterns and requires optimization to reduce the company's operating costs.

The following diagram shows the monthly cost before optimization.

![Monthly cost before optimization](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/1f652105-698c-4a6f-aaf5-52f6d4b8c10e.png)

For example, there are 31 days in the month of March, out of which 23 are weekdays. If the marketing team uses Instance Scheduler on AWS and operates their instances only when needed (that is, for 321 hours per month instead of 730 hours per month), they could potentially save $932.52 each month. This amounts to a 56 percent reduction in operating costs. The accounting team can experience significant advantages as well, with their instance usage time dropping from 730 hours per month to 230 hours. This results in a reduction of $1,140, or 68.5 percent. The company could save a combined total of $2,072.52 per month (equal to a 62 percent reduction), or $24,870.24 annually.

The following diagram shows the monthly cost after optimization.

![Monthly cost after optimization](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/7b79d7ed-dba7-47fa-a7dd-e2fae4ba37d9.png)

**Note**
The pricing for this example was determined by using the [AWS Pricing Calculator](https://calculator.aws/) in March 2023.

## Cost optimization recommendations
<a name="windows-ec2-schedules-costopt-rec"></a>

This section explains how to deploy and configure the Instance Scheduler on AWS based on the example scenario covered in the previous *Cost optimization scenario* section. We recommend that you take the following next steps to optimize your costs by using the Instance Scheduler on AWS:

1. Launch the Instance Scheduler stack

1. Configure periods

1. Configure schedules

1. Tag instances

The following architecture diagram shows what's created in the AWS Cloud by the Instance Scheduler stack.

![Instance Scheduler stack architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/90b87bc8-8ad9-4be5-9982-cbbb6b158585.png)

The diagram shows the following workflow steps:

1. An AWS CloudFormation template sets up an Amazon CloudWatch event at an interval that you define. This event invokes an AWS Lambda function. During configuration, you define the AWS Regions and accounts. You also define a custom tag that Instance Scheduler on AWS uses to associate schedules with applicable Amazon EC2 instances, Amazon RDS instances, and clusters.

1. The schedule configuration values are stored in Amazon DynamoDB, and the Lambda function retrieves them each time it runs. You can then apply the custom tag to applicable instances.

1. During initial configuration of the Instance Scheduler, you define a tag key for identifying applicable Amazon EC2 and Amazon RDS instances. When you create a schedule, the name you specify is used as the tag value that identifies the schedule that you want to apply to the tagged resource.

### Launch the Instance Scheduler stack
<a name="launch-the-instance-scheduler-stack.be057144-f922-57cf-9f66-18bc40e7b8fe"></a>

This section shows you how to launch the CloudFormation stack for the Instance Scheduler on AWS.

**Note**
You're responsible for the cost of the AWS services used while running Instance Scheduler on AWS. As of January 2023, the cost for running this solution with default settings in the `us-east-1` Region is approximately $9.90 per month for Lambda charges, or less if you have a Lambda free tier monthly usage credit. For more information, see the *Cost* section of the [Instance Scheduler on AWS Implementation Guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/cost.html) in the AWS Solutions Library.

To launch the instance scheduler stack, complete the following steps.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and choose [Launch solution](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template) (downloadable template) to launch `instance-scheduler-on-aws.template` CloudFormation template.
**Note**
You can also [download the template](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template) as a starting point for your own implementation.

1. The template launches in the US East (N. Virginia) Region by default. To launch Instance Scheduler in a different Region, use the Region selector in the console navigation bar.
**Note**
This example uses the Asia Pacific (Singapore) Region.

1. On the **Create Stack **page, in the **Prerequisite - Prepare template** section, verify that the **Template is ready **option is selected. In the **Template source section**, verify that the **Amazon S3 URL** option is selected.

1. Verify that the correct template URL is in the **Amazon S3 URL **text box, and then choose **Next**.

1. On the **Specify stack details **page, assign a name to your solution stack. For information about naming character limitations, see [IAM and STS Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the AWS Identity and Access Management (IAM) documentation. The stack name for the example in this guide is called `MyInstanceScheduler`.
**Note**
The stack name can't contain more than 28 characters.

1. Under **Parameters**, review the parameters for the template and modify them as necessary.

1. Choose **Next**. On the **Configure stack options **page, choose **Next**.

1. On the **Review **page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create **to deploy the stack.

### Configure periods
<a name="configure-periods.7c336b09-fcc0-56d1-96b8-90be25f53489"></a>

After you deploy the CloudFormation template, the solution creates a DynamoDB table that contains sample period rules and schedules that you can use as a reference to create your own custom period rules and schedules. For an example period configuration, see [Sample schedules](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/sample-schedules.html) in the Instance Scheduler on AWS documentation.

To complete the step for this scenario, you must generate periods that correspond to each workload and meet their specific needs. For example:

```
Period 1 (Workload A):
    Name: retail-hours
    Days: Monday to Sunday
    Hours: 1100 - 2300
Period 2 (Workload B):
    Name: office-hours
    Days: Monday to Friday
    Hours: 0800 - 1800
```

To configure periods, complete the following steps:

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home) and make sure you're in the same Region where you launched the CloudFormation template for the Instance Scheduler on AWS.

1. In the navigation pane, choose **Tables**, and then select the table named **ConfigTable**.

1. Choose **Explore table** **items**.

1. To create a period for office hours, select **period** for the **office-hours **item.

1. On the **Edit item** page, change the value of **begintime** to **0800** and **endtime** to **1800**. Leave the default value in place for weekdays.
**Note**
The **begintime** and **endtime** values determine when the instances should be started and stopped, while the **weekdays** value determines which days of the week this schedule applies to (Monday to Friday for this example).

1. Choose **Save changes**.

1. To duplicate the **office-hours** period and use it to create a new period for retail hours, select **period** for the **office-hours** item. Then, from the **Actions** menu, choose **Duplicate item**.

1. Modify the attributes to match your needs. The following attributes are used to meet the requirements of the example scenario:

   ```
   type: period
   name: retail-hours
   begintime: 11:00
   description: Retail hours
   endtime: 23:00
   weekdays: mon-sun
   ```

1. Choose **Create item**.

1. In the DynamoDB **ConfigTable**, identify the two periods that you just created listed in the item lists.

### Configure schedules
<a name="configure-schedules.b72fa8d4-721f-565f-914d-36a920f5c6cd"></a>

In the context of Instance Scheduler on AWS, schedules refer to the application of one or more periods and the relevant time zone. These schedules are then assigned to your instances as tags. This section shows you how to create two schedules (shown below) to accommodate the varying time patterns of the two example workloads, and then associate the schedules with the periods that you created in the previous section.

```
Schedule 1:
    Name: singapore-office-hours
    Period: office-hours
    Timezone: Asia/Singapore
Schedule 2:
    Name: singapore-retail-hours
    Period: retail-hours
    Timezone: Asia/Singapore
```

To create and configure schedules, complete the following steps:

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home) and make sure you're in the same Region where you launched the CloudFormation template for the Instance Scheduler on AWS.

1. In the navigation pane, choose **Tables**, and then select the table named **ConfigTable**.

1. Choose **Explore table** **items**.

1. To duplicate the UK office hours schedule and use it to create a new schedule for your office hours (Singapore office hours, for this example), select **schedule** for the **uk-office-hours **item. Then, from the **Actions** menu, choose **Duplicate item**.

1. Modify the attributes to match your needs. The following attributes are used to meet the requirements of the example scenario:

   ```
   type: schedule
   name: singapore-office-hours
   description: Office hours in Singapore
   periods: office-hours
   timezone: Asia/Singapore
   ```

1. Choose **Create item**.

1. Repeat steps 4–6 to create a schedule for Singapore retail hours using the following attribute values:

   ```
   type: schedule
   name: singapore-retail-hours
   description: Retail hours in Singapore
   periods: retail-hours
   timezone: Asia/Singapore
   ```

1. In the DynamoDB **ConfigTable**, identify the two schedules and two periods that you created.

### Tag instances
<a name="tag-instances.776f8be9-7d1f-5e04-ab59-346dc38e4bf5"></a>

After you establish your schedules, you must uses tags to allocate the schedules to the specific instances that you want to use. You can use the tag editor within [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) to generate and assign tags to your Amazon EC2 instances.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and make sure you're in the same Region where you previously launched the CloudFormation template.

1. Open the [Resource Groups console](https://console.aws.amazon.com/resource-groups). In the navigation pane, expand **Tagging**, and then choose **Tag Editor**.

1. In the **Find resources to tag** section, for **Regions**, choose your Regions. For **Resource types**, choose Amazon EC2 or Amazon RDS. This scenario focuses on the Amazon EC2 instances in workload A. The marketing team is using workload A in the Singapore Region. The resources for this workload are already tagged with a **Department** key and a **Marketing** value. You can use this tag to search for the instances.

1. Choose **Search resources**.

1. Select the instances that you want to include in the schedule from the list of search results, and then choose **Manage tags of selected resources**.

1. In the **Edit tags of all selected resources **section, choose **Add tag **to add the Instance Scheduler schedule tags to your EC2 instances. You can use the tag keys and values that match **schedulea** (previously created in DynamoDB).

1. For **Tag key**, add **Schedule**. For **Tag value**,** **enter **singapore-retail-hours**.

1. Choose **Review and apply tag changes**.

1. To apply the tag to all the EC2 instances that you selected, choose **Apply changes to all selected**.

1. Repeat steps 3–9 for any additional schedules you wish to apply.

### Validate results
<a name="validate-results.e36b51f5-caed-5983-a5b1-141b295711a7"></a>

We recommend that you use [AWS Cost Explorer](https://www.youtube.com/watch?v=UfPqrkoUFiQ) to measure the cost benefits of using Instance Scheduler on AWS. You can use Cost Explorer to do the following:
+ View and analyze the costs associated with your EC2 instances, including instances managed by Instance Scheduler.
+ Filter your Cost Explorer view by tags so that you can focus on specific workloads and get a granular view of the cost savings achieved by using Instance Scheduler.
+ Gain insights into the financial impact of using Instance Scheduler.
+ Identify opportunities for further cost optimization and make data-driven decisions to optimize your AWS spending.

The following charts illustrate the cost of operating workload A and workload B during a seven day period (Monday–Sunday) before optimization by using Instance Scheduler.

**Combined total expenses of workloads A and B**

![Combined total expenses of workloads A and B](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/b53344b0-7ec0-415b-9386-dafe7967f13b.png)

**Workload A expenses**

![Expenses for Workload A](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/53ef8187-0bfd-4bd4-a007-d244aaec6c25.png)

**Workload B expenses**

![Expenses for Workload B](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/c7215478-1610-490c-b6c4-f1181c4aa222.png)

In this scenario, Cost Explorer shows the cost reductions that result from implementing Instance Scheduler on AWS. The following charts depict the operational costs of workload A and workload B for a period of seven days (Monday–Sunday) post-optimization.

**Combined total expenses of workload A and B**

![Combined total expenses of workload A and B](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/44c5a962-c7c0-4b46-890d-1a89757f3c69.png)

**Workload A expenses**

![Expenses for Workload A](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/c08bc7ce-1c55-4448-8250-8046dfd03615.png)

**Workload B expenses**

![Expenses for Workload B](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/03a8b43a-78a7-4236-bfaf-2f73b7cada3f.png)

## Additional resources
<a name="windows-ec2-schedules-resources"></a>
+ [Automate starting and stopping AWS instances](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html) (Instance Scheduler on AWS documentation)
+ [Back to Basics: Using an Instance Scheduler to Control Amazon EC2 and Amazon RDS Resource Costs](https://www.youtube.com/watch?v=UsC5ZNcZl9k) (YouTube)
+ [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) (Tagging AWS Resources User Guide)
+ [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) (AWS Billing and Cost Management documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
