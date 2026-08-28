---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/customize-and-personalize-embedded-analytics.html
---

# Embedding custom Amazon Quick Sight assets into your application
<a name="customize-and-personalize-embedded-analytics"></a>

You can use Amazon Quick Sight embedded analytics to embed custom Amazon Quick Sight assets into your application that are tailored to meet your business needs. For embedded dashboards and visuals, Amazon Quick Sight authors can add filters and drill downs that readers can access as they navigate the dashboard or visual. Amazon Quick Sight developers can also use the Amazon Quick Sight SDKs to build tighter integrations between their SaaS applications and their Amazon Quick Sight embedded assets to add datapoint callback actions to visuals on a dashboard at runtime.

For more information about the Amazon Quick Sight SDKs, see the `amazon-quicksight-embedding-sdk` on [GitHub](https://github.com/awslabs/amazon-quicksight-embedding-sdk) or [NPM](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).

Following, you can find descriptions of how to use the Amazon Quick Sight SDKs to customize your Amazon Quick Sight embedded analytics.

**Topics**
+ [Adding embedded callback actions at runtime in Amazon Quick Sight](embedding-custom-actions-callback.md)
+ [Filtering data at runtime for Amazon Quick Sight embedded dashboards and visuals](embedding-runtime-filtering.md)
+ [Customize the look and feel of Amazon Quick Sight embedded dashboards and visuals](embedding-runtime-theming.md)
+ [Using the Amazon Quick Sight Embedding SDK to enable shareable links to embedded dashboard views](embedded-view-sharing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
