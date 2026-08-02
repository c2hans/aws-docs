---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-overview.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Zendesk connector overview
<a name="zendesk-overview"></a>

The following table gives an overview of the Zendesk connector and its supported features.

****

- ****Security****
  - **Feature:** Authentication type / **Support:** OAuth 2.0 with implicit grant authentication, OAuth 2.0 authentication
  - **Feature:** Authentication credentials / **Support:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-overview.html)
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-overview.html) Each instance of an entity is crawled as a single document. See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-overview.html)
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
  - **Feature:** [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) / **Support:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-overview.html)
