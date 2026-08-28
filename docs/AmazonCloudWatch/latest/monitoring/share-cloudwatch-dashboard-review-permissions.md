---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/share-cloudwatch-dashboard-review-permissions.html
---

# Reviewing shared CloudWatch dashboard permissions and changing permission scope
<a name="share-cloudwatch-dashboard-review-permissions"></a>

Use the steps in this section if you want to review the permissions of the users of your shared dashboards, or change the scope of shared dashboard permissions.

**To review shared dashboard permissions**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Dashboards**.

1. Choose the name of the shared dashboard.

1. Choose **Actions**, **Share dashboard**.

1. Under **Resources**, choose **IAM Role**.

1. In the IAM console, choose the displayed policy.

1. (Optional) To limit which alarms that shared dashboard users can see, choose **Edit policy** and move the `cloudwatch:DescribeAlarms` permission from its current position to a new `Allow` statement that lists the ARNs of only the alarms that you want to be seen by shared dashboard users. See the following example.

   ```
   {
      "Effect": "Allow",
       "Action": "cloudwatch:DescribeAlarms",
       "Resource": [
           "AlarmARN1",
           "AlarmARN2"
       ]
   }
   ```

   If you do this, be sure to remove the `cloudwatch:DescribeAlarms` permission from a section of the current policy that looks like this:

   ```
   {
      "Effect": "Allow",
       "Action": [
           "cloudwatch:GetInsightRuleReport",
           "cloudwatch:GetMetricData",
           "cloudwatch:DescribeAlarms",
           "ec2:DescribeTags"
       ],
       "Resource": "*"
   }
   ```

1. (Optional) To limit the scope of what Contributor Insights rules that shared dashboard users can see, choose **Edit policy** and move the `cloudwatch:GetInsightRuleReport` from its current position to a new `Allow` statement that lists the ARNs of only the Contributor Insights rules that you want to be seen by shared dashboard users. See the following example.

   ```
   {
      "Effect": "Allow",
       "Action": "cloudwatch:GetInsightRuleReport",
       "Resource": [
           "PublicContributorInsightsRuleARN1",
           "PublicContributorInsightsRuleARN2"
       ]
   }
   ```

   If you do this, be sure to remove `cloudwatch:GetInsightRuleReport` from a section of the current policy that looks like this:

   ```
   {
               "Effect": "Allow",
               "Action": [
                   "cloudwatch:GetInsightRuleReport",
                   "cloudwatch:GetMetricData",
                   "cloudwatch:DescribeAlarms",
                   "ec2:DescribeTags"
               ],
               "Resource": "*"
           }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
