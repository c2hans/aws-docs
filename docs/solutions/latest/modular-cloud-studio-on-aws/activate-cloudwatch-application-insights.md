---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/activate-cloudwatch-application-insights.html
---

# Activate CloudWatch Application Insights
<a name="activate-cloudwatch-application-insights"></a>

1. Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. In the navigation pane, choose **Application Manager**.

1. In **Applications**, choose **AppRegistry applications**.

1. In **AppRegistry applications**, search for the application name for this solution and select it.

   The next time you open Application Manager, you can find the new application for your solution in the **AppRegistry application** category.

1. In the **Components** tree, choose the application stack you want to activate.

1. In the **Monitoring** tab, in **Application Insights**, select **Auto-configure Application Monitoring**.

![application insights](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/application-insights.png)

Monitoring for your applications is now activated and the following status box appears:

![application insights 2](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/application-insights-2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
