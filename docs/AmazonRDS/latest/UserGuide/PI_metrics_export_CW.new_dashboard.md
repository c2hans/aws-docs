---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.new_dashboard.html
---

# Exporting Performance Insights metrics as a new dashboard to CloudWatch
<a name="PI_metrics_export_CW.new_dashboard"></a>

Choose a preconfigured or custom metrics dashboard from the Performance Insights dashboard and export it as a new dashboard to CloudWatch. You can view the exported dashboard in the CloudWatch console.

**To export a Performance Insights metric dashboard as a new dashboard to CloudWatch**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the left navigation pane, choose **Performance Insights**.

1. Choose a DB instance.

   The Performance Insights dashboard appears for the DB instance.

1. Scroll down and choose **Metrics**.

   By default, the preconfigured dashboard with Performance Insights metrics appears.

1. Choose a preconfigured or custom dashboard and then choose **Export to CloudWatch**.

   The **Export to CloudWatch** window appears.
![Performance Insights dashboard with export to CloudWatch button.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/PI-ExprtToCW.png)

1. Choose **Export as new dashboard**.
![Export to CloudWatch window with export as new dashboard option selected.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/PI-ExprtToCW-NewDashboard.png)

1. Enter a name for the new dashboard in the **Dashboard name** field and choose **Confirm**.

   A banner displays a message after the dashboard export is successful.
![Banner with successful message.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/PI-ExprtToCW-SuccessBanner.png)

1. Choose the link or **View in CloudWatch** in the banner to view the metrics dashboard in the CloudWatch console.
