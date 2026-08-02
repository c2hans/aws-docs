---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/monitor-costs.html
---

# Monitor costs using AWS tools
<a name="monitor-costs"></a>

## Overview
<a name="monitor-costs-overview"></a>

Cost visibility is a key factor in optimizing costs on AWS. AWS has a number of tools you can use to visualize costs and create alerts in reaction to those costs. These include tools, like AWS Budgets, that help you track and report your spending. This section covers specific ways to monitor your Windows on AWS spending, so you can track and react accordingly to your budget requirements. This includes adding necessary tags to your Windows EC2 resources. These tags enable you to properly monitor Windows EC2 and other Microsoft services by using AWS Budgets.

By monitoring spending and creating alerts with AWS tools, you can be more informed about current spending, projected spending, and spending anomalies. If you use [Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) to help reduce your hourly EC2 instance pricing, we recommend that you view the overall utilization and coverage of the Savings Plans. This can help you ensure that you're continually realizing savings. You can use AWS Cost Explorer to view Savings Plans inventory and get recommendations for additional Savings Plans based on previous usage. You can also track specific spending by using [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) and setting up [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/).

## Cost optimization recommendations
<a name="monitor-costs-rec"></a>

We recommend that you take the following next steps to optimize your costs by using AWS Budgets, Cost Explorer, and anomaly detection:
+ Tag Windows EC2 resources
+ Set up alerts by using AWS Budgets
+ Enable Cost Anomaly Detection
+ Get a real-time spending analysis
+ View license-included spending for Windows by using Cost Explorer

### Tag Windows EC2 resources
<a name="tag-windows-ec2-resources.a1a76cd8-6acf-548f-982d-61fdd2ede17d"></a>

To effectively monitor your AWS spending, you must establish a [tagging strategy](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) for the workloads that you want to monitor. This is important so that you can categorically group resources and get notified on specific spending, as opposed to general usage spending. You can use tagging resources that not only help with cost but can also be used for other purposes such as [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/tagging-resources.html). Additionally, we recommend that you implement some management for [required tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html).

To track your spending in AWS Budgets, Cost Explorer, and Cost Anomaly Detection, you must ensure that proper tags are in place. You can use tags to set up a specific budget for items matching those tags so that you are alerted when spending increases.

For example, you can use a simple tag like **Key=OS Value=Windows**. This puts all of your Windows instances together into one group that you can track spending for. You can also use tags for other items, such as Systems Manager. After you create a tag, you must activate the tag for cost tracking. Consider adding an [AWS Config rule that monitors for tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) that are attached to certain resources. AWS Config can alert you if there are resources running that don't contain the appropriate tags, which provide you with an accurate representation of your Windows EC2 spending.

After you have your tags in place, you can create a custom budget in AWS Billing. This provides visibility into your Windows EC2 spending. You can set a daily budget or a monthly budget.

### Set up alerts using AWS Budgets
<a name="set-up-alerts-using-9999999999999999budgetslong-.06d539e5-c54f-5006-8557-6553949dc29b"></a>

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

1. Choose the **OS** tag, and then choose the Windows value for this to create a budget for the tag.

1. Choose **Next**.

1. On the **Configure alerts** page, choose **Add an alert threshold**. Here you set up two alerts: one for a 50 percent threshold and one for a 100 percent threshold. If the 50 percent threshold alert is breached before the halfway point in the month, it will provide a warning. That way, you can check if your spending is more than expected and react before reaching the end of the month.

1. For **Threshold**, enter **50** and select **% of budgeted amount**.

1. For **Trigger**, choose **Actual**.

1. For **email recipients**, enter an email address. Add another alert for a threshold of **100**.
**Note**
This example uses an email notification for the alert, but you can also use other approaches, such as [Slack](https://docs.aws.amazon.com/cost-management/latest/userguide/sns-alert-chime.html).

### Enable Cost Anomaly Detection
<a name="enable-9999999999999999cadet-.c2e3aed5-a04b-550c-a759-1a5ce2e9dcc9"></a>

You can use your cost tags to set up spending alerts that are an anomaly. For example, you can use [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/faqs/) to create monitors for your spending and get alerted when the system detects abnormal spending in your account.

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

1. Choose **Add threshold**. For **Threshold**, enter **10** and then select **percent above expected speed**.

1. Choose **Create monitor**.

### Get a real-time view into spending
<a name="get-a-real-time-view-into-spending.b5e9a491-329e-50a1-8369-d05fa584e79f"></a>

An alert is a useful tool for monitoring your Windows EC2 spending, but you must use Cost Explorer if you want a real-time view into spending. Watch this video to learn how Cost Explorer enables you to analyze and reduce your EC2 costs. For more information, watch the [AWS Supports You \| Understanding and Reducing Your EC2 Costs](https://www.youtube.com/watch?v=flEnJ44N-J8) video on YouTube.

### View license-included spending for Windows
<a name="view-license-included-spending-for-windows.4a463f04-1a47-55f0-8765-9dc6aa368b8e"></a>

You can view the EC2 Windows spending in your account by using Cost Explorer. To see license-included spending for Windows, you must set the following correct [filters](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html) in Cost Explorer:
+ For **Platform**, choose **Windows (Amazon VPC)**. For **API operation**, choose **RunInstance:0002**. This is the AWS Billing code for license-included Windows EC2 instances.
+ If you want to view your BYOL instance spending, change **RunInstance:0002** to **RunInstance:0800**. This is the billing code for Windows EC2 BYOL.

With this visibility in Cost Explorer, you can quickly filter down your costs to exactly what you're spending on Windows EC2. If you want to dive even deeper into your AWS spending, you can use AWS Cost and Usage Report to filter down to spending at the individual instance level. You can also generate reports that can be visualized in Amazon Quick and build customized dashboards.

For more information, watch the [AWS Supports You - Visualizing Your Cost and Usage Reports video](https://www.youtube.com/watch?v=Gq15yuPJ2Kc) on YouTube.

## Additional resources
<a name="monitor-costs-resources"></a>
+ [Setting up required tags with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) (AWS Config documentation)
+ [AWS Budgets Tutorial - Setup Alerts for AWS Billing \| Amazon Web Services](https://www.youtube.com/watch?app=desktop&v=O0sofGVT7uw) (YouTube)
+ [AWS Cost and Usage Report Query Library](https://wellarchitectedlabs.com/cost-optimization/cur_queries/) (AWS Well-Architected Labs)
