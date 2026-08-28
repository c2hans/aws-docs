---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-limitations.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Document enrichment limitations
<a name="cde-limitations"></a>

When you use document enrichment, be aware of the following limitations that affect how you can process different types of content.

## Multimedia content limitations
<a name="multimedia-limitations"></a>

Document enrichment doesn't support the following multimedia file types:
+ Audio files - You can't use document enrichment operations on audio content.
+ Video files - You can't use document enrichment operations on video content.

## Visual content in documents limitations
<a name="visual-content-limitations"></a>

When you work with visual content in documents, the following limitations apply:
+ If PostExtractionHook is configured, visual content in the document is ignored and not Indexed.

### Connector-specific Document Enrichment behavior
<a name="connector-visual-behavior"></a>

When you enable visual content in documents, PreExtractionHookConfiguration operations for the following connectors are limited to metadata updates only:
+ Web Crawler
+ ServiceNow
+ Confluence
+ Salesforce
+ SharePoint

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
