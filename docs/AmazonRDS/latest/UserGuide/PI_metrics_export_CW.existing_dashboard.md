---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.existing_dashboard.html
---

# Adding Performance Insights metrics to an existing CloudWatch dashboard
<a name="PI_metrics_export_CW.existing_dashboard"></a>

Add a preconfigured or custom metrics dashboard to an existing CloudWatch dashboard. You can add a label to the metrics dashboard to appear in a separate section in the CloudWatch dashboard.

**To export the metrics to an existing CloudWatch dashboard**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the left navigation pane, choose **Performance Insights**.

1. Choose a DB instance.

   The Performance Insights dashboard appears for the DB instance.

1. Scroll down and choose **Metrics**.

   By default, the preconfigured dashboard with Performance Insights metrics appears.

1. Choose the preconfigured or custom dashboard and then choose **Export to CloudWatch**.

   The **Export to CloudWatch** window appears.

1. Choose **Add to existing dashboard**.
![Export to CloudWatch window with add to existing dashboard option selected.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Pi-ExprtToCW-AddToExistingBoard.png)

1. Specify the dashboard destination and label, and then choose **Confirm**.
   + **CloudWatch dashboard destination** - Choose an existing CloudWatch dashboard.
   + **CloudWatch dashboard section label - optional** - Enter a name for the Performance Insights metrics to appear in this section in the CloudWatch dashboard.

   A banner displays a message after the dashboard export is successful.

1. Choose the link or **View in CloudWatch** in the banner to view the metrics dashboard in the CloudWatch console.
