---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/monitor-costs.html
---

# Monitor costs using AWS tools
<a name="monitor-costs"></a>

## Overview
<a name="monitor-costs-overview"></a>

Cost visibility is a key factor in optimizing costs on AWS. AWS offers tools that you can use to visualize costs and create alerts based on those costs. These tools, such as AWS Budgets, help you track and report your spending. This section describes how to monitor your Windows on AWS spending so that you can meet your budget requirements. It includes adding tags to your Windows EC2 instances. These tags help you monitor Windows EC2 instances and other Microsoft products by using AWS Budgets.

By monitoring spending and creating alerts with AWS tools, you gain insight into current spending, projected spending, and spending anomalies. If you use [Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) to help reduce your hourly EC2 instance pricing, view the overall utilization and coverage of the Savings Plans. This helps you confirm that you're realizing savings. You can use AWS Cost Explorer to view Savings Plans inventory and get recommendations for additional Savings Plans based on past usage. You can also track specific spending by using [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) and setting up [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/).

## Cost optimization recommendations
<a name="monitor-costs-rec"></a>

We recommend that you take the following next steps to optimize your costs by using AWS Budgets, Cost Explorer, and anomaly detection:
+ Tag Windows EC2 resources
+ Set up alerts by using AWS Budgets
+ Enable Cost Anomaly Detection
+ Get a real-time spending analysis
+ View license-included spending for Windows by using Cost Explorer

### Tag Windows EC2 resources
<a name="tag-windows-ec2-resources.ba38165a-3deb-57dc-8f0d-85bc1a9935f9"></a>

To effectively monitor your AWS spending, you must establish a [tagging strategy](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) for the workloads that you want to monitor. A tagging strategy helps you group resources by category and get notified about specific spending instead of general usage spending. Tags help with cost tracking, and you can also use them for other purposes, such as [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/tagging-resources.html). Additionally, we recommend that you enforce [required tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) on your resources.

To track your spending in AWS Budgets, Cost Explorer, and Cost Anomaly Detection, you must ensure that proper tags are in place. You can use tags to set up a specific budget for items matching those tags so that you are alerted when spending increases.

For example, you can use a simple tag like **Key=OS Value=Windows**. This tag groups all of your Windows instances so that you can track spending for them. You can also use tags for other items, such as Systems Manager. After you create a tag, you must activate the tag for cost tracking. Consider adding an [AWS Config rule that monitors for tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) that are attached to certain resources. AWS Config can alert you if resources are running without the required tags. Required tags help provide an accurate representation of your Windows EC2 spending.

After you have your tags in place, you can create a custom budget in AWS Billing. This provides visibility into your Windows EC2 spending. You can set a daily budget or a monthly budget.

### Set up alerts using AWS Budgets
<a name="set-up-alerts-using-9999999999999999budgetslong-.475bea2c-a12a-5aa8-b732-2e5d623dd9c9"></a>

In this example scenario, you create a daily budget for Windows EC2. It's a recurring budget that uses the auto-adjusting option to track your spending and adjust the budget accordingly. If you have a static environment, you can use a fixed budget instead. Make sure to choose a baseline time-range (for example, 30 days).

1. Sign in to the AWS Management Console and open the [AWS Cost Management console](https://console.aws.amazon.com/cost-management/home).

1. In the navigation pane, choose **Budgets**.

1. At the top of the page, choose **Create budget**.

1. Under **Budget setup**, choose **Customize (advanced)**.

1. Under **Budget types**, choose **Cost budget**. Then, choose **Next**.

1. Under **Details**, for **Budget name**, enter the name of your budget. For example, **Windows EC2 spend**.

1. Under **Set budget amount**, for **Period**, choose **Daily**.

1. For **Budget renewal type**, choose **Recurring budget** for a budget that resets after the budget period.

1. For **Start date**, choose the start date or period to begin tracking against your budgeted amount.

1. For **Budgeting method**, choose **Auto-adjusting (New)**.

1. For **Baseline time range**, choose **Custom range**, and then enter 30 days.

1. Choose **Next**.

1. In the **Budget scope** section, select **Filter specific AWS cost dimensions**. This is where tags are used to create the proper dimensions. AWS Budgets doesn't support **Platform Type** as an option in its filters. For this reason, you must apply **OS** tags.

1. Choose **Add filter**, and then select the **Tag** option from **Dimensions**.

1. Choose the **OS** tag, and then choose the **Windows** value to create a budget for the tag.

1. Choose **Next**.

1. On the **Configure alerts** page, choose **Add an alert threshold**. Set up two alerts: one for a 50 percent threshold and one for a 100 percent threshold. If your spending reaches the 50 percent threshold before the halfway point in the month, the alert warns you. You can then check whether your spending is more than expected and react before the end of the month.

1. For **Threshold**, enter **50** and select **% of budgeted amount**.

1. For **Trigger**, choose **Actual**.

1. For **email recipients**, enter an email address. Add another alert for a threshold of **100**.
**Note**
This example uses an email notification for the alert, but you can also use other approaches, such as [Slack](https://docs.aws.amazon.com/cost-management/latest/userguide/sns-alert-chime.html).

### Enable Cost Anomaly Detection
<a name="enable-9999999999999999cadet-.5f3c1144-fcaf-5042-bb29-e6141b03c7d2"></a>

You can use your cost tags to set up alerts for anomalous spending. For example, you can use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/faqs/) to create monitors for your spending and receive alerts when it detects abnormal spending in your account.

To set up a monitor and alerts for the **Key=OS and Value=Windows** tag that you created previously, do the following:

1. Sign in to the AWS Management Console and open the [AWS Cost Management console](https://console.aws.amazon.com/cost-management/home).

1. In the navigation pane, choose **Cost Anomaly Detection**.

1. Choose the **Cost monitors** tab, and then choose **Create monitor**.

1. In Step 1, choose the **Cost Allocation Tag** as your monitor type.

1. For **Cost Allocation Tag key**, choose **Windows EC2 spend**.

1. For **Cost Allocation Tag value**, choose **Windows**.

1. For **Name your monitor**, enter **Windows EC2 spend**.

1. Choose **Next**.

1. To create a subscription for the alerts, select **Create a new subscription**. If you have existing subscriptions, select **Choose an existing subscription**.

1. For **Subscription name**, enter **Windows EC2 spend anomaly**.

1. For **Alerting frequency**, choose **Daily summaries**.

1. For **Alert recipients**, enter your email address.

1. Choose **Add threshold**. For **Threshold**, enter **10**, and then select **percent above expected spend**.

1. Choose **Create monitor**.

### Get a real-time view into spending
<a name="get-a-real-time-view-into-spending.6c697c2e-e128-5e17-adcc-64309c240866"></a>

Alerts help you monitor your Windows EC2 spending, but you must use Cost Explorer if you want a real-time view into spending. To learn how Cost Explorer helps you analyze and reduce your EC2 costs, watch the [AWS Supports You \| Understanding and Reducing Your EC2 Costs](https://www.youtube.com/watch?v=flEnJ44N-J8) video on YouTube.

### View license-included spending for Windows
<a name="view-license-included-spending-for-windows.6c967f03-829d-522d-8b6b-f933a1c88342"></a>

You can view the Windows EC2 spending in your account by using Cost Explorer. To see license-included spending for Windows, set the following [filters](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html) in Cost Explorer:
+ For **Platform**, choose **Windows (Amazon VPC)**. For **API operation**, choose **RunInstance:0002**. This is the AWS Billing code for license-included Windows EC2 instances.
+ If you want to view your BYOL instance spending, change **RunInstance:0002** to **RunInstance:0800**. This is the billing code for Windows EC2 BYOL.

With this visibility in Cost Explorer, you can filter your costs to view your Windows EC2 spending. To analyze your AWS spending in more detail, you can use AWS Cost and Usage Report to view spending at the individual instance level. You can also generate reports, visualize them in AWS Quick, and build customized dashboards.

For more information, watch the [AWS Supports You - Visualizing Your Cost and Usage Reports video](https://www.youtube.com/watch?v=Gq15yuPJ2Kc) on YouTube.

## Additional resources
<a name="monitor-costs-resources"></a>
+ [Setting up required tags with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) (AWS Config documentation)
+ [AWS Budgets Tutorial - Setup Alerts for AWS Billing \| Amazon Web Services](https://www.youtube.com/watch?app=desktop&v=O0sofGVT7uw) (YouTube)
+ [AWS Cost and Usage Report Query Library](https://wellarchitectedlabs.com/cost-optimization/cur_queries/) (AWS Well-Architected Labs)
