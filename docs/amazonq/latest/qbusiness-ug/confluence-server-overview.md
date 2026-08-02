---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Confluence (Server/Data Center) connector overview
<a name="confluence-server-overview"></a>

The following table gives an overview of the Amazon Q Business Confluence (Server/Data Center) connector and its supported features.

****

- ****Security****
  - **Feature:** Authentication type / **Support:** Basic, OAuth 2.0 with Refresh Token Flow, Personal Access Token
  - **Feature:** Authentication credentials / **Support:** For Basic authentication:[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html)<br />For OAuth 2.0 authentication with Refresh Token Flow:[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html)<br />Personal Access Token[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html)
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html)See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-server-overview.html)
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental (new, modified, and deleted) sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
