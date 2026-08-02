---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Salesforce Online connector overview
<a name="salesforce-overview"></a>

The following table gives an overview of the Salesforce Online connector and its supported features.

****

- ****Security****
  - **Feature:** Authentication type / **Support:** OAuth 2.0 with Resource Owner Password Flow Note that Require Proof Key for Code Exchange (PKCE) is not supported and must be disabled.
  - **Feature:** Authentication credentials / **Support:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html)
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-user-management).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes
  - **Feature:** Supported versions / **Support:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html)

- ****Crawl features****
  - **Feature:** Custom objects / **Support:** Yes
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html)See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-field-mappings).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html)
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports incremental sync only if ACL is turned off, otherwise only full sync will be used.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
  - **Feature:** [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) / **Support:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-overview.html)
