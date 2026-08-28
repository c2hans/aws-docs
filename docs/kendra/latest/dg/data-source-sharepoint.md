---
source_url: https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html
---

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Microsoft SharePoint
<a name="data-source-sharepoint"></a>

SharePoint is a collaborative website building service that you can use to customize web content and create pages, sites, document libraries, and lists. You can use Amazon Kendra to index your SharePoint data source.

Amazon Kendra currently supports SharePoint Online and SharePoint Server (versions 2013 and Subscription Edition).

You can connect Amazon Kendra to your SharePoint data source using either the [Amazon Kendra console](https://console.aws.amazon.com/kendra/), the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API, or the [SharePointConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SharePointConfiguration.html) API.

Amazon Kendra has two versions of the SharePoint connector. Supported features of each version include:

**SharePoint Connector V1.0 / [SharePointConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SharePointConfiguration.html) API**
+ Field mappings
+ User access control
+ Inclusion/exclusion filters
+ Change log
+ Virtual private cloud (VPC)

**SharePoint Connector V2.0 / [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API**
+ Field mappings
+ User access control
+ Inclusion/exclusion filters
+ Full and incremental content syncs
+ Virtual private cloud (VPC)

**Note**
SharePoint connector V1.0 / SharePointConfiguration API ended in 2023. We recommend migrating to or using SharePoint connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra SharePoint data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md).

**Topics**
+ [SharePoint connector V1.0](data-source-v1-sharepoint.md)
+ [SharePoint connector V2.0](data-source-v2-sharepoint.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
