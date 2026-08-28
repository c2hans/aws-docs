---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-dashboard.html
---

# Use the Apache Flink Dashboard with Managed Service for Apache Flink
<a name="how-dashboard"></a>

You can use your application's Apache Flink Dashboard to monitor your Managed Service for Apache Flink application's health. Your application's dashboard shows the following information:
+ Resources in use, including Task Managers and Task Slots.
+ Information about Jobs, including those that are running, completed, canceled, and failed.

For information about Apache Flink Task Managers, Task Slots, and Jobs, see [Apache Flink Architecture](https://flink.apache.org/what-is-flink/flink-architecture/) on the Apache Flink website.

Note the following about using the Apache Flink Dashboard with Managed Service for Apache Flink applications:
+ The Apache Flink Dashboard for Managed Service for Apache Flink applications is read-only. You can't make changes to your Managed Service for Apache Flink application using the Apache Flink Dashboard.
+ The Apache Flink Dashboard is not compatible with Microsoft Internet Explorer.

## Access your application's Apache Flink Dashboard
<a name="how-dashboard-accessing"></a>

You can access your application's Apache Flink Dashboard either through the Managed Service for Apache Flink console, or by requesting a secure URL endpoint using the CLI.

### Access your application's Apache Flink Dashboard using the Managed Service for Apache Flink console
<a name="how-dashboard-accessing-console"></a>

To access your application's Apache Flink Dashboard from the console, choose **Apache Flink Dashboard** on your application's page.

**Note**
When you open the dashboard from the Managed Service for Apache Flink console, the URL that the console generates will be valid for 12 hours.

### Access your application's Apache Flink Dashboard using the Managed Service for Apache Flink CLI
<a name="how-dashboard-accessing-cli"></a>

You can use the Managed Service for Apache Flink CLI to generate a URL to access your application dashboard. The URL that you generate is valid for a specified amount of time.

**Note**
If you don't access the generated URL within three minutes, it will no longer be valid.

You generate your dashboard URL using the [ CreateApplicationPresignedUrl](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplicationPresignedUrl.html) action. You specify the following parameters for the action:
+ The application name
+ The time in seconds that the URL will be valid
+ You specify `FLINK_DASHBOARD_URL` as the URL type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
