---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer.html
---

# Create detailed cost and usage reports for AWS Glue jobs by using AWS Cost Explorer
<a name="create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer"></a>

*Parijat Bhide and Aromal Raj Jayarajan, Amazon Web Services*

## Summary
<a name="create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer-summary"></a>

This pattern shows how to track the usage costs of AWS Glue data integration jobs by configuring [user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html). You can use these tags to create detailed cost and usage reports in AWS Cost Explorer for jobs across multiple dimensions. For example, you can track usage costs at the team, project, or cost center level.

## Prerequisites and limitations
<a name="create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ One or more [AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/how-it-works.html) that have user-defined tags activated

## Architecture
<a name="create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer-architecture"></a>

**Target technology stack**
+ AWS Glue
+ AWS Cost Explorer

The following diagram shows how you can apply tags to track usage costs for AWS Glue jobs.

![Creating and applying tags in AWS Glue jobs to track usage costs in AWS Cost Explorer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e0ae6643-713d-423a-9013-b41b30638053/images/f2b74ef1-494d-439b-9aec-5a9d601126a6.png)

The diagram shows the following workflow:

1. A data engineer or AWS administrator creates user-defined cost allocation tags for the AWS Glue jobs.

1. An AWS administrator activates the tags.

1. The tags report metadata to AWS Cost Explorer.

## Tools
<a name="create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer-tools"></a>
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html) helps you view and analyze your AWS costs and usage.

## Epics
<a name="create-detailed-cost-and-usage-reports-for-aws-glue-jobs-by-using-aws-cost-explorer-epics"></a>

### Create and activate tags for your AWS Glue jobs
<a name="create-and-activate-tags-for-your-aws-glue-jobs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create user-defined cost allocation tags for your AWS Glue jobs. | **To add tags to an existing AWS Glue job**1. Sign in to the AWS Management console, and then open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the left navigation pane, under **ETL**, choose **Jobs**.<br />3. In the **Your jobs** section, choose the name of the job that you’re tagging.<br />4. Choose the **Job details** tab. Then, expand the **Advanced properties** section.<br />5. For **Tags**, choose **Add new tag**.<br />6. For **Key**, enter a name for your tag.<br />7. (Optional) For **Value**, enter a value that you want associated with the key.<br />8. (Optional) Repeat steps 5-7 for each tag that you want to create for the job.<br />9. Choose **Save**.<br />**To add tags to a new AWS Glue job**1. Create a new AWS Glue job based on your use case requirements. For instructions, see [Working with jobs on the AWS Glue Console](https://docs.aws.amazon.com/glue/latest/dg/console-jobs.html) in the *AWS Glue Developer Guide*.<br />2. When you configure the **Job details** settings, follow steps 4-9 of the **To add tags to an existing AWS Glue job** section of this task.For more information, see [AWS tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the *AWS Glue Developer Guide.* | Data engineer |
| Activate the user-defined cost allocation tags. | Follow the instructions in [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the *AWS Billing User Guide*. | AWS administrator |

### Create cost and usage reports for your AWS Glue jobs
<a name="create-cost-and-usage-reports-for-your-aws-glue-jobs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create cost and usage reports for your AWS Glue jobs by using tag filters in AWS Cost Explorer. | 1. Sign in to the AWS Management Console and open the [AWS Cost Management console](https://console.aws.amazon.com/cost-management/home).<br />2. In the left navigation pane, choose **Reports**.<br />3. Choose **Create new report**.<br />4. For **Select a report type**, choose **Cost and usage (recommended)**. Then, choose **Create Report**.<br />5. For **Filters**, choose **Service**. The **Service** dropdown appears.<br />6. Select the check boxes next to **Glue**. Then, choose **Apply filters**.<br />7. For **Filters**, choose **Tag**. The **Tag** dropdown appears.<br />8. Choose **Team**. Then, select the check boxes next to the teams that you’ve assigned tags to. Exclude any teams that you haven’t assigned tags to. Then, choose **Apply filters**.<br />9. At the top of the chart, choose **Tag**. Then, choose the tags for the AWS Glue jobs that you want to create a report for.<br />10. At the top of the chart, choose the **Last 3 Months** dropdown and choose the timeframe that you want the report to cover. Then, choose the **Monthly** dropdown and choose how you want the line items in the report to be aggregated based on timeframe.<br />11. Choose **Save as**. Then, enter a title for your report.<br />12. Choose **Save Report**.For more information, see [Exploring your data using Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) in the *AWS Cost Management User Guide*. | General AWS, AWS administrator |
