---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-dashboards-for-authenticated-users-get.html
---

# Embedding dashboards for registered users using GetDashboardEmbedUrl (old API)
<a name="embedded-analytics-dashboards-for-authenticated-users-get"></a>

**Important**
Amazon Quick Sight has new APIs for embedding analytics: `GenerateEmbedUrlForAnonymousUser` and `GenerateEmbedUrlForRegisteredUser`.
You can still use the `GetDashboardEmbedUrl` and `GetSessionEmbedUrl` APIs to embed dashboards and the Amazon Quick Sight console, but they do not contain the latest embedding capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your applications](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html).

In the following sections, you can find detailed information on how to set up embedded Amazon Quick Sight dashboards for registered users using `GetDashboardEmbedUrl`.

**Topics**
+ [Step 1: Set up permissions](embedded-dashboards-for-authenticated-users-get-step-1.md)
+ [Step 2: Get the URL with the authentication code attached](embedded-dashboards-for-authenticated-users-get-step-2.md)
+ [Step 3: Embed the dashboard URL](embedded-dashboards-for-authenticated-users-get-step-3.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
