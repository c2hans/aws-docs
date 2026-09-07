---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer.html
---

# Create detailed cost and usage reports for Amazon EMR clusters by using AWS Cost Explorer
<a name="create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer"></a>

*Parijat Bhide and Aromal Raj Jayarajan, Amazon Web Services*

## Summary
<a name="create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer-summary"></a>

This pattern shows how to track the usage costs of Amazon EMR clusters by configuring [user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html). You can use these tags to create detailed cost and usage reports in AWS Cost Explorer for clusters across multiple dimensions. For example, you can track usage costs at the team, project, or cost center level.

## Prerequisites and limitations
<a name="create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ One or more [EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html) that have user-defined tags activated

## Architecture
<a name="create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer-architecture"></a>

**Target technology stack**
+ Amazon EMR
+ AWS Cost Explorer

**Target architecture**

The following diagram shows how you can apply tags to track usage costs for specific Amazon EMR clusters.

![Using cost allocation tags for Amazon EMR clusters.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3e470077-e3b1-43cf-8cb9-0895fe39e664/images/fb6b78cb-47bb-4ba1-848a-98dba02bdbb2.png)

The diagram shows the following workflow:

1. A data engineer or AWS administrator creates user-defined cost allocation tags for the Amazon EMR clusters.

1. An AWS administrator activates the tags.

1. The tags report metadata to AWS Cost Explorer.

## Tools
<a name="create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer-tools"></a>

**Tools**
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) is a managed cluster platform that simplifies running big data frameworks on AWS to process and analyze large amounts of data.
+ [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html) helps you view and analyze your AWS costs and usage.

## Epics
<a name="create-detailed-cost-and-usage-reports-for-amazon-emr-clusters-by-using-aws-cost-explorer-epics"></a>

### Create and activate tags for your Amazon EMR clusters
<a name="create-and-activate-tags-for-your-amazon-emr-clusters"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create user-defined cost allocation tags for your Amazon EMR clusters. | **To add tags to an existing Amazon EMR cluster**<br />Follow the instructions in [Adding tags to an existing cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-add.html) in the *Amazon EMR Management Guide*.<br />**To add tags to a new Amazon EMR cluster**<br />Follow the instructions in [Add tags to a new cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-add-new.html) in the *Amazon EMR Management Guide*.<br />For more information about how to set up an Amazon EMR cluster, see [Plan and configure clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan.html) in the *Amazon EMR Management Guide*. | Data engineer |
| Activate the user-defined cost allocation tags. | Follow the instructions in [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the *AWS Billing User Guide*. | AWS administrator |

### Create cost and usage reports for your Amazon EMR clusters
<a name="create-cost-and-usage-reports-for-your-amazon-emr-clusters"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create cost and usage reports for your Amazon EMR clusters by using tag filters in AWS Cost Explorer. | 1. Sign in to the AWS Management Console and open the [AWS Cost Management console](https://console.aws.amazon.com/cost-management/home).<br />2. In the left navigation pane, choose **Reports**.<br />3. Choose **Create new report**.<br />4. For **Select a report type**, choose **Cost and usage (recommended)**. Then, choose **Create Report**.<br />5. For **Filters**, choose **Service**. The **Service** dropdown appears.<br />6. Select the check boxes next to **EMR (Elastic MapReduce)** and **EC2-Instances (Elastic Compute Cloud – Compute)**. Then, choose **Apply filters**.<br />7. For **Filters**, choose **Tag**. The **Tag** dropdown appears.<br />8. Choose **Team**. Then, select the check boxes next to the teams that you’ve assigned tags to. Exclude any teams that you haven’t assigned tags to. Then, choose **Apply filters**.<br />9. At the top of the chart, choose **Tag**. Then, choose the tags for the Amazon EMR clusters that you want to create a report for.<br />10. At the top of the chart, choose the **Last 3 Months** dropdown and choose the timeframe that you want the report to cover. Then, choose the **Monthly** dropdown and choose how you want the line items in the report to be aggregated based on timeframe.<br />11. Choose **Save as**. Then, enter a title for your report.<br />12. Choose **Save Report**.For more information, see [Exploring your data using Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) in the *AWS Cost Management User Guide*. | General AWS, AWS administrator |
