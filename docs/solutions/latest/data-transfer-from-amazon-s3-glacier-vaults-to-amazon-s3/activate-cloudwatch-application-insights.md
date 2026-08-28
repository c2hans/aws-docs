---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/activate-cloudwatch-application-insights.html
---

# Activate CloudWatch Application Insights
<a name="activate-cloudwatch-application-insights"></a>

1.  Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1.  In the navigation pane, choose **Application Manager**.

1. In **Applications**, search for the application name for this Guidance and select it.

   The application name will have App Registry in the **Application Source** column, and will have a combination of the Guidance name, Region, account ID, or stack name.

1. In the **Components** tree, choose the application stack you want to activate.

1. In the **Monitoring** tab, in **Application Insights**, select **Auto-configure Application Insights**.

![Application Insights monitoring page showing advanced monitoring is not enabled message.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/appregistry2.png)

 Monitoring for your applications is now activated and the following status box appears:

![Success message confirming application monitoring is enabled and results will display shortly.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/appregistry3.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
