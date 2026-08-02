---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AccessPlans.html
---

# Analyzing Oracle execution plans using the Performance Insights dashboard for Amazon RDS
<a name="USER_PerfInsights.UsingDashboard.AccessPlans"></a>

When analyzing DB load on an Oracle Database, you might want to know which plans are contributing the most to DB load. You can determine which plans are contributing the most to DB load by using the plan capture feature of Performance Insights.

**To analyze Oracle execution plans using the console**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Performance Insights**.

1. Choose an Oracle DB instance. The Performance Insights dashboard is displayed for that DB instance.

1. In the **Database load (DB load)** section, choose **Plans** next to **Slice by**.

   The Average active sessions chart shows the plans used by your top SQL statements. The plan hash values appear to the right of the color-coded squares. Each hash value uniquely identifies a plan.
![Slice by plans.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/pi-slice-by-plans.png)

1. Scroll down to the **Top SQL** tab.

   In the following example, the top SQL digest has two plans. You can tell that it's a digest by the question mark in the statement.
![The digest plan selection.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/top-sql-plans-unselected.png)

1. Choose the digest to expand it into its component statements.

   In the following example, the `SELECT` statement is a digest query. The component queries in the digest use two different plans. The colors of the plans correspond to the database load chart. The total number of plans in the digest is shown in the second column.
![The digest plan selection.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/pi-digest-plan.png)

1. Scroll down and choose two **Plans** to compare from **Plans for digest query** list.

   You can view either one or two plans for a query at a time. The following screenshot compares the two plans in the digest, with hash 2032253151 and hash 1117438016. In the following example, 62% of the average active sessions running this digest query are using the plan on the left, whereas 38% are using the plan on the right.
![Compare the plans side by side.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/pi-compare-plan.png)

   In this example, the plans differ in an important way. Step 2 in plan 2032253151 uses an index scan, whereas plan 1117438016 uses a full table scan. For a table with a large number of rows, a query of a single row is almost always faster with an index scan.
![Compare the plans side by side.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/pi-table-access.png)

1. (Optional) Choose **Copy** to copy the plan to the clipboard, or **Download** to save the plan to your hard drive.
