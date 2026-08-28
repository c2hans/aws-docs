---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/activate-cloudwatch-application-insights.html
---

# Activate CloudWatch Application Insights
<a name="activate-cloudwatch-application-insights"></a>

1. Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. In the navigation pane, choose **Application Manager**.

1. In **Applications**, search for the application name for this solution and select it.

   The application name will have **App Registry** in the **Application Source** column, and will have a combination of the solution name, Region, account ID, or stack name.

1. In the **Components** tree, choose the application stack you want to activate.

1. In the **Monitoring** tab, in **Application Insights**, select **Auto-configure Application Insights**.

 **Application Insights dashboard showing no detected problems and option to auto-configure.**

![appreg1](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/appreg1.png)

Monitoring for your applications is now activated and the following status box appears:

 **Application Insights dashboard showing successful monitoring activation message.**

![appreg2](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/appreg2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
