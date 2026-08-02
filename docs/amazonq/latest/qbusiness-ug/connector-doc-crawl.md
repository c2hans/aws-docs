---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# What is a document?
<a name="connector-doc-crawl"></a>

When you connect Amazon Q Business to a data source, what Amazon Q Business considers—and crawls—as a document varies by connector.

The following table outlines what each connector crawls as a document.

| Data source connector | Supports crawling | Document definition |
| --- | --- | --- |
| Adobe Experience Manager (Cloud and Server) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Alfresco (Cloud and Server) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Amazon FSx (Windows) | Files | Each File is considered a single document. |
|  Amazon S3  | Objects | Each Object is considered a single document. Any {{object-name.metadata.json}} file and access control list (ACL) file is considered metadata for the object it is associated with and not treated as a separate document. |
| Amazon Q Business Web Crawler |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
|  WorkDocs  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Box |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Confluence (Cloud and Server) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Database data sources [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  | Each row in a table and view is considered a single document. |
| Dropbox |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Drupal |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| GitHub (Cloud and Server) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Gmail |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Google Calendar |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  | Each calendar is considered a single document. |
| Google Drive |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Jira |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Microsoft Exchange |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Microsoft OneDrive |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Microsoft SharePoint (Online and Server) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Microsoft Teams |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Microsoft Yammer |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Quip |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Salesforce |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| ServiceNow |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Slack |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
| Zendesk |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html)  |
