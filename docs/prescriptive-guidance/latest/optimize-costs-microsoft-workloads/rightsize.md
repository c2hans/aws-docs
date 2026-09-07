---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/rightsize.html
---

# Right size Windows workloads
<a name="rightsize"></a>

## Overview
<a name="rightsize-overview"></a>

Right sizing is one of the most potent cost-saving tools. AWS offers various methods to collect right sizing information, from reviewing potential workloads by using an [AWS Optimization and Licensing Assessment (AWS OLA)](https://aws.amazon.com/optimization-and-licensing-assessment/) to reviewing existing workloads by using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/).

This section shows you how to use [AWS Compute Optimizer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) to identify Amazon EC2 right sizing opportunities. Compute Optimizer helps prevent over-provisioning and under-provisioning for the following types of AWS resources:
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instance types
+ [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) volumes
+ [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) services on AWS Fargate
+ [AWS Lambda](https://aws.amazon.com/lambda/) functions based on utilization data provided by [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

## Cost optimization scenario
<a name="rightsize-costopt-scenario"></a>

Measuring the effectiveness of right sizing can be challenging, because right sizing efforts can be directed toward a specific app, team, or the entire organization. For example, consider an organization that migrates several thousand instances to AWS, with 90 percent of their fleet comprising Windows workloads. The organization can employ Compute Optimizer to analyze their fleet and discover significant over-provisioning across their accounts and AWS Regions. Then, they can use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to right size their fleet through multiple maintenance windows. As a result, the organization manages to adjust the right sized instance type for 70 percent of their fleet and achieves a cost savings of 35 percent.

The following dashboard illustrates the savings achieved over several months as this example organization strategically implemented the right sizing recommendations of Compute Optimizer. Their objective was to operate their existing workloads as efficiently as possible in order to resume a stalled migration from a colocation data center nearing the end of its contract.

![Savings from right sizing](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/2abddb5d-c36f-4688-ba02-54c42e6dd8fa.png)

## Cost optimization recommendations
<a name="rightsize-costopt-rec"></a>

We recommend that you take the following next steps to optimize your costs by using Compute Optimizer:
+ Enable Compute Optimizer
+ Enable Memory metrics collection for Windows nodes
+ Consume Compute Optimizer recommendations
+ Tag instances for right sizing
+ Enable the cost allocation tag to work with AWS billing tools
+ Implement right sizing recommendations with AWS Systems Manager Automation
+ Consider alternative resizing methods
+ Review before and after costs in Cost Explorer

### Enable Compute Optimizer
<a name="enable-9999999999999999co-.c7e0cb9a-bcb5-5a4d-a494-91b9c9a41c7b"></a>

You can enable [Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html#account-opt-in) at the organization or single account level in AWS Organizations. The organization-wide configuration provides ongoing reports for new and existing instances across your entire fleet for all member accounts. This enables right sizing to be a recurring activity instead of a point-in-time activity.

#### Organization level
<a name="organization-level.05114395-ca65-553e-a4a6-0f6845249c83"></a>

For most organizations, the most efficient way to use Compute Optimizer is at the organization level. This provides multi-account and multi-Region visibility into your organization and centralizes the data into one source for review. To enable this at the organization level, do the following:

1. Sign in to your [Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) with a role that has the [required permissions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) and choose to opt in for all accounts within this organization. Your organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).

1. After you enable the management account, you can sign in to the account, see all other member accounts, and browse their recommendations.

**Note**
It's a best practice to configure a [delegated administrator account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/delegate-administrator-account.html) for Compute Optimizer. This enables you to exercise the principle of least privilege. That way, you can minimize access to the organization's management account while still providing access to the organization-wide service.

#### Single account level
<a name="single-account-level.1c0ae85c-180f-585e-8cc7-2b1d11c418a1"></a>

If you're targeting an account with high costs but don't have access to AWS Organizations, you can still enable Compute Optimizer for that account and Region. To learn about the opt-in process, see [Getting started with AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html) in the Compute Optimizer documentation.

### Enable memory metrics collection for Windows nodes
<a name="enable-memory-metrics-collection-for-windows-nodes.70aa32d7-37c8-544a-978d-90dfe48c666d"></a>

Memory metrics supply Compute Optimizer with the essential metrics required to make well-informed right sizing recommendations in your organization. This is due to the analysis of CPU, memory, network, and storage being conducted before offering a recommendation.

To pass memory metrics from Windows EC2 instances to Compute Optimizer, you must enable the CloudWatch agent and configure memory metrics to be collected every 60 seconds. There is no additional cost for using memory metrics with CloudWatch.

#### Enable the CloudWatch agent and configure memory metrics
<a name="enable-the-9999999999999999cw--agent-and-configure-memory-metrics.eb6cd8a8-7234-55c3-8138-6be75ae4f72f"></a>

Download the [ComputeOptimize.yml](https://static.us-east-1.prod.workshops.aws/public/93110159-2ede-4c0c-9767-877c96d68a7e/static/code/wec2/ComputeOptimize.yml) file. You can use this file to enable memory collection for all instances in your account. The template file generates the following components:
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) – This stores the configuration for the CloudWatch agent that's required for collecting memory metrics.
+ AWS Identity and Access Management (IAM) role with [AWS managed policies for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html#managed-policies) attached – This is for the Systems Manager Automation document.
+ [AWS Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) – This installs and configures the CloudWatch agent (replacing any existing CloudWatch configuration).
+ [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) association – This enables Systems Manager documents to run on all instances in your account.

**Important**
Running this template overwrites any existing CloudWatch configuration on the instances.

Next, do the following:

1. Sign in to the AWS Management Console and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. In the navigation pane, choose **Stacks**.

1. Choose **Create stack**, and then choose **With existing resources (import resources)**.

1. Choose **Next**.

1. For **Template resource**, select **Upload a template file**.

1. Choose** file**, and then upload the `ComputeOptimize.yml` file.

1. Choose **Next**.

1. On the **Specify stack details** page, for **Stack name**, enter a name for your stack, and then choose **Next**.

1. On the **Identify resources** page, enter the identifier values for the resources you're importing.

1. Choose **Import resources**.

1. After the stack is deployed, choose the **Outputs** tab to find the key, value, and description for your association.

#### Monitor the progress of the association
<a name="monitor-the-progress-of-the-association.d339463e-24c7-56d6-ac20-adcffaa2ebf8"></a>

1. After the deployment of the CloudFormation stack is complete, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, in the **Node Management** section, choose **State Manager**.

1. On the **Associations** page, choose the association ID of your association.

1. Choose the **Execution history** tab.

1. In the **Execution id** column, choose your association's execution ID. The status should be **Success**.

#### View the metrics in CloudWatch
<a name="view-the-metrics-in-9999999999999999cw-.c944de56-a710-54e4-89db-ecac29e5a05e"></a>

We recommend that you wait for at least five minutes for the metrics to populate CloudWatch.

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, expand the **Metrics** section, and then choose **All metrics**.

1. Confirm that the metrics appear under the **CWAgent **namespace.

**Note**
To apply the settings to any new instances, rerun the association.

### Consume Compute Optimizer recommendations
<a name="consume-9999999999999999co--recommendations.baac70c3-8505-5d97-91ad-1141abe27700"></a>

Consider an example that focuses on making right sizing changes within a single account and single Region. In this example, Compute Optimizer is enabled at the organization level across all accounts. Keep in mind that right sizing is a disruptive process that in most cases is carried out with precision by the application owners during a scheduled maintenance window over several weeks.

If you navigate to Compute Optimizer from within an organization's management account (as shown in the following steps), you can choose the account that you want to investigate. In this example, there are six instances running in a single account in the `us-east-1` Region. All six instances are over-provisioned. The goal is to resize the instances based on the recommendations from Compute Optimizer.

#### Identify over-provisioned instances and export recommendation details
<a name="identify-over-provisioned-instances-and-export-recommendation-details.a2db2a0f-51e1-5152-a87a-cfeb7ec0f784"></a>

1. Sign in to the AWS Management Console and open the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Dashboard**.

1. In the search box on the **Dashboard** page, enter **Region=US East (N. Virginia)**. Then, enter **Findings=Over-provisioned**. These filters allow you to see all the over-provisioned instances in the `us-east-1` Region.

1. To review detailed recommendations for over-provisioned** **EC2 instances,** **scroll down to the **EC2 instances** card, and then choose **View recommendations**.

1. Choose **Export** and save the file for future use.

1. For **S3 bucket**, enter the name of the Amazon S3 bucket that you want to be the destination for the export file.
**Note**
To save recommendations for future review, you must have an S3 bucket available for Compute Optimizer to write to in each Region. For more information, see [Amazon S3 bucket policy for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html) in the Compute Optimizer documentation.

1. In the **Export filters** section, select the **Include recommendations for all member accounts in the organization **check box.

1. For **Resource type**, choose **EC2 instances**.

1. In the **Columns to include** section, select the **Select all** check box.

1. Choose **Export**.

#### Choose instances based on recommendations
<a name="choose-instances-based-on-recommendations.b09131ac-b5d6-52d7-ab92-3559dba3ca86"></a>

Instance recommendations are based on the performance metrics collected and analyzed by Compute Optimizer. It's essential to be aware of the workloads running on the instance to ensure that you choose the best instance. This example assumes that you can choose from the latest generation of Amazon EC2 [R6i](https://aws.amazon.com/ec2/instance-types/r6i/), [R5](https://aws.amazon.com/ec2/instance-types/r5/), and [T3](https://aws.amazon.com/ec2/instance-types/t3/) instances. T3 instances are burstable and have lower network bandwidth capabilities. R5 and R6 instances have the same cost per hour and are nearly identical. However, the R6 instance has a higher network bandwidth capacity, features the latest generation of Intel processors, and offers the same compute footprint as the R5. In this example, R6 is the best option to choose for resizing.

1. In the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/), choose **Recommendations for EC2 instances** from the navigation bar. This page shows you a comparison of the current instance type with recommended options to replace it.

1. To get the ID of the instance that you want to right size, open the [Amazon S3 console](https://console.aws.amazon.com/s3/) from the management account in AWS Organizations.

1. In the navigation pane, choose **Buckets**, and then choose the bucket that you're using to store your exported results.

1. On the **Objects** tab, select your export file from the objects list, and then choose **Download**.

1. To extract the instance information from the file, you can use the **Text to Columns** button on the **Data** tab in Microsoft Excel.
**Note**
Instance IDs are represented as Amazon Resource Names (ARNs). Be sure to set the delimiter to "/" and extract the instance ID. Alternatively, you can write a script or use an integrated development environment (IDE) to trim the ARN.

1. In Excel, filter the **finding** column to display only the **OVER\_PROVISIONED** instances. These are the instances that you're targeting for right sizing.

1. Save the instance IDs in a text editor for easy access later.

### Tag instances for right sizing
<a name="tag-instances-for-right-sizing.7f1b2983-371b-5fdd-a5a7-5bedb9c350c4"></a>

Tagging your workloads is a powerful tool for organizing your resources in AWS. Tags enable you to gain fine-grained visibility into costs and facilitate chargeback. For more information about strategies and methods for adding tags to AWS resources, see the AWS Whitepaper [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). For this example, you can use the [AWS Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) to make tagging adjustments across the over-provisioned instances that you wish to target for resizing during a maintenance window. You can also use this tag to view the costs before and after the change.

1. Sign in to the AWS Management Console and open the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups) for the account containing the instances targeted for resizing.

1. On the navigation bar, in the **Tagging** section, choose **Tag Editor**.

1. For **Regions**, select your target Region.

1. For **Resources types**, choose** AWS::EC2::Instance**.

1. Choose **Search resources**.

1. On the **Resource search results** page, select all the instances that you want to right size, and then choose **Manage tags of selected resources**.

1. Choose **Add tag**.

1. For **Tag key**, enter **Rightsizing**. For **Tag value**, enter **enabled**. Then, choose **Review and apply tag changes**.
**Note**
You can include additional metadata like Team or Business Unit to help with filtering later on in Cost Explorer.

After creating and applying user-defined tags to your resources, it may take up to 24 hours for the tags to appear on your cost allocation tags page for activation. After you select your tags for activation, it could take another 24 hours for the tags to become active.

For advanced users, you can use [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home) within the target account and Region to tag multiple instances. For example:

```
bash
#!/bin/bash
# Set variables
TAG_KEY="rightsizing"
TAG_VALUE="type-m5"
# Get a list of instance IDs
INSTANCE_IDS=$(aws ec2 describe-instances —query "Reservations[].Instances[].InstanceId" —output text)
# Loop through each instance ID and add the tag
for INSTANCE_ID in $INSTANCE_IDS; do
 aws ec2 create-tags —resources $INSTANCE_ID —tags Key=$TAG_KEY,Value=$TAG_VALUE
done
```

### Enable the cost allocation tag to work with AWS billing tools
<a name="enable-the-cost-allocation-tag-to-work-with-9999999999999999aws--billing-tools.a39f60b9-dc2a-57bd-b156-f1fdfe2f1e6e"></a>

We recommend activating the user-defined cost allocation tag. This enables the **Rightsizing **tag to be recognized and filterable in the AWS billing tools (for example, Cost Explorer and AWS Cost and Usage Report). If you don't enable this, the tag filtering option and data won't be available. For information about using cost allocation tags, see [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the AWS Billing and Cost Management documentation.

1. Sign in to the AWS Management Console and open the [AWS Billing console](https://console.aws.amazon.com/billing).

1. On the navigation pane, in the **Billing** section, choose **Cost allocation tags**.

1. On the **User-defined cost allocation tags** tab, enter **Rightsizing**.

1. Select the **Rightsizing** tag key, and then choose **Activate**.

After 24 hours, the tag should appear in Cost Explorer.

### Implement right sizing recommendations with Systems Manager Automation
<a name="implement-right-sizing-recommendations-with-9999999999999999sys--automation.40334752-63e7-5da3-a948-37d245cfae11"></a>

Resizing is a scenario that requires an instance to be stopped and started. In this scenario, you might need to handle this interruption in a maintenance window and need different teams to handle their own resizing. Before you change an instance type, review the [Considerations for compatible instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html#resize-ebs-backed-instance-considerations) in the Amazon EC2 documentation.

The example steps in this section implement right sizing recommendations per account and Region by using a Systems Manager Automation document called [AWS-ResizeInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-resizeinstance.html). This approach is typical for most organizations as most organizations require different instance types for different purposes. You can also use the same `AWS-ResizeInstance` automation document to target single and multi-account deployments.

1. Sign in to the AWS Management Console and open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. On the navigation pane, in the **Shared Resources** section, choose **Documents**.

1. In the search bar, enter **AWS-ResizeInstance**, and then choose the **AWS-ResizeInstance **from the search results.

1. Choose **Execute automation**.

1. On the **Execute automation runbook** page, choose **Simple execution**.

1. In the **Input parameters** section, enter **InstanceId** and **InstanceType**. Keep the rest of the default values.

1. Choose **Execute**,** **and then** **wait for the automation to go through the steps to change the instance type.

### Consider alternative resizing methods
<a name="consider-alternative-resizing-methods.163c873f-035c-5f4d-a208-6d8f7d41575d"></a>

If you're using a launch template to deploy your instances, you can update the launch template with the right sized instance type, and then perform an instance refresh to replace the instances with the right-sized version.

If you plan to use the right sizing process across multiple accounts and Regions, you must create a custom Systems Manager Automation document. This document enables you to feed in multiple instances as a parameter and target instances moving to the same destination instance type (for example, all instances transitioning to t3a.medium, irrespective of the source instance type).

### Review before and after costs in Cost Explorer
<a name="review-before-and-after-costs-in-9999999999999999ce-.fe86919e-cdae-5d63-959d-a1d5367cd06a"></a>

After you have right sized your resources, you can use Cost Explorer to show before and after costs by using the **Rightsizing** tag. Recall that you can use [resource tags](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) to track costs. By using several layers of tags, you can achieve granular visibility into your costs. In the example covered in this guide, the **Rightsizing** tag is used to apply a generic tag to all targeted instances. Then, a team tag is used to further organize resources. The next step is to introduce application tags to further show the cost impact for operating a specific application.

The following diagram shows the tag structure for an organization.

![Organization's tag structure](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/4d7b75ac-2923-48e5-8e4e-543f06bf9bd0.png)

Consider the example of a business that right sizes the production web servers owned by the Operations team. In Cost Explorer, the **Rightsizing** tag is set to **enabled**, and the **Team** tag is set to **operations**. In this example, the right sizing effort reduces operating costs from 0.89 cents to 0.28 cents an hour. Assuming 744 hours per month, the annual cost before right sizing is $7,945.92. After right sizing, the annual cost drops to $2,499.84. This translates to a 68.5 percent decrease in annual workload costs. Imagine the impact of this across a large organization. Keep in mind, this is done in a sample environment and the instances are mostly idle. In a production environment, you can see savings between 10–35 percent.

Now, consider the impact of right sizing the production bastion host owned by the Engineering team. In Cost Explorer, the **Rightsizing** tag is set to **enabled**, and the **Team** tag is set to **engineering**. In this example, the right sizing effort reduces costs from 0.75 cents to 0.44 cents an hour. Assuming 744 hours per month, the annual cost before right sizing is $6,696.00. After right sizing, the annual cost drops to $3,928.32.

If you use multiple tags, you can filter the data down to granular cost details. In this example, the **Team** tag reduces the noise so that you can view the impact at a team level. Because the **Rightsizing** tag is enabled, you can also filter for any instance that has that tag with the value of **enabled** or no value present. This can provide a global view of your right sizing efforts, particularly when viewed in the management account (payer) at the Cost Explorer level. This view enables you to see all accounts and instances.

Consider an example at the single account level where the **Rightsizing** tag is set to **enabled**.  The operating costs drop from $1.64 an hour to $.72 cents an hour. Assuming 744 hours per month, the annual cost before right sizing is $14,641.92. After right sizing, the annual cost drops to $6,428.16. This translates to a 56 percent decrease in compute costs for this account.

Before embarking on your right sizing journey, consider the following:
+ AWS offers many options for cost reduction. This includes [AWS OLA](https://aws.amazon.com/optimization-and-licensing-assessment/), where AWS reviews your on-premises instances prior to moving to AWS. The AWS OLA also provides you with right sizing recommendations and licensing guidance.
+ Complete all of your right sizing before purchasing [Savings Plans](https://aws.amazon.com/savingsplans/). This can help you avoid over purchases on your Savings Plans commitment.

## Recommendations
<a name="rightsize-recommendations"></a>

We recommend the following next steps:

1. Review your existing landscape and consider converting Amazon EBS gp2 volumes to gp3 volumes.

1. Review [Savings Plans](https://aws.amazon.com/savingsplans/).

## Additional resources
<a name="additional-resources"></a>
+ [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) (AWS documentation)
+ [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) (AWS Whitepapers)
+ [How to collect data from AWS Compute Optimizer and AWS Trusted Advisor across your AWS Organizations](https://www.youtube.com/watch?v=ekR6RSgqJ4Q) (YouTube)
+ [Optimizing performance and reducing licensing costs: Leveraging AWS Compute Optimizer for Amazon EC2 SQL Server instances](https://aws.amazon.com/blogs/modernizing-with-aws/optimizing-performance-and-reducing-licensing-costs-leveraging-aws-compute-optimizer-for-ec2-sql-server-instances/) (Microsoft Workloads on AWS blog)
