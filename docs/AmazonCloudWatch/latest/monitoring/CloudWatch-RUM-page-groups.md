---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-page-groups.html
---

# Use page groups
<a name="CloudWatch-RUM-page-groups"></a>

Use page groups to associate different pages in your application with each other so that you can see aggregated analytics for groups of pages. For example, you might want to see the aggregated page load times of all of your landing pages.

You put pages into page groups by adding one or more tags to page view events in the CloudWatch RUM web client. The following examples put the `/home` page into the page group named `en` and the page group named `landing`.

**Embedded script example**

```
cwr('recordPageView', { pageId: '/home', pageTags: ['en', 'landing']});
```

**JavaScript module example**

```
awsRum.recordPageView({ pageId: '/home', pageTags: ['en', 'landing']});
```

**Note**
Page groups are intended to facilitate aggregating analytics across different pages. For information about how to define and manipulate `pageIds` for your application, see the **Manually recording page views** section in [Modifying the code snippet to configure the CloudWatch RUM web client (optional)](CloudWatch-RUM-modify-snippet.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
