---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/personalization-embedded-analytics.html
---

# Personalization
<a name="personalization-embedded-analytics"></a>

Amazon Quick Sight enhances user experience with state persistence to ensure a seamless transition across sessions with the maintenance of the current dashboard state. This feature allows for uninterrupted workflows and a consistent analytics experience. Furthermore, users can optimize their productivity with bookmarks to save and revisit specific views of their dashboard.

Personalization features including state persistence and bookmarks are only available for registered users. To integrate these capabilities into embedded analytics, developers can leverage the Quick Sight APIs. This API-driven approach allows developers to customize personalization features within embedded analytics. The Quick Sight APIs provide developers with the tools they need to create a tailored and efficient user experience to meet their business needs.

## State Persistence
<a name="personalization-embedded-analytics-state-persistence"></a>

Use state persistence to ensure a continuous user experience that maintains the current state of a dashboard across different sessions. This means that Quick Sight retains information about filters, selected tabs, and other configurations When a user revisits a dashboard, they can pick up where they left off, which eliminates the need to recreate the view each time. State persistence can be utilized to improve user productivity, enhance collaboration, and promote efficient data exploration.

## Bookmarks
<a name="personalization-embedded-analytics-bookmarks"></a>

Users can utilize bookmarks to save and revisit specific views within Quick Sight dashboards to enhance the efficiency and flexibility of data exploration. Bookmarks can be used to improve user productivity, enmahce collaboration, and create user defined views of a Quick Sight dashboard.

To learn more about bookmarks, see [Bookmarking views of a dashboard](https://docs.aws.amazon.com/quicksight/latest/user/dashboard-bookmarks.html) and [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
