---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-deprecated.html
---

# Embedding analytics using the GetDashboardEmbedURL and GetSessionEmbedURL API operations
<a name="embedded-analytics-deprecated"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  Amazon Quick developers  |

The following API operations for embedding Amazon Quick Sight dashboards and the Amazon Quick Sight console have been replaced by the GenerateEmbedUrlForAnonymousUser and GenerateEmbedUrlForRegisteredUser API operations. You can still use them to embed analytics in your application, but they are no longer maintained and do not contain the latest embedding features or functionality. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your applications](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html)
+ The [GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetDashboardEmbedUrl.html) API operation embeds interactive dashboards.
+ The [GetSessionEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetSessionEmbedUrl.html) API operation embeds the Amazon Quick Sight console.

**Topics**
+ [Embedding dashboards for everyone using GetDashboardEmbedURL (old API)](embedded-analytics-dashboards-with-anonymous-users-get.md)
+ [Embedding dashboards for registered users using GetDashboardEmbedUrl (old API)](embedded-analytics-dashboards-for-authenticated-users-get.md)
+ [Embedding the Amazon Quick Sight console using GetSessionEmbedUrl (old API)](embedded-analytics-full-console-for-authenticated-users-get.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
