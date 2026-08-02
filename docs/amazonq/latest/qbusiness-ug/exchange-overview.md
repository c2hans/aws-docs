---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-overview.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Microsoft Exchange connector overview
<a name="exchange-overview"></a>

The following table shows the Amazon Q Business Microsoft Exchange connector features and capabilities.

****

- ****Security****
  - **Feature:** Authentication type / **Latest Connector:** OAuth 2.0 with Client Credentials Flow / **Legacy Connector:** OAuth 2.0 with Client Credentials Flow
  - **Feature:** Authentication credentials / **Latest Connector:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-overview.html) / **Legacy Connector:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-overview.html)
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Latest Connector:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-connector.html#exchange-user-management). / **Legacy Connector:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-connector.html#exchange-user-management).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Latest Connector:** Yes / **Legacy Connector:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Latest Connector:** No / **Legacy Connector:** Yes

- ****
  - **Feature:** Customer Managed Key (CMK) support
  - **Latest Connector:** No
  - **Legacy Connector:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Latest Connector:** No / **Legacy Connector:** No
  - **Feature:** Entities / **Latest Connector:** Mail only (automatic) / **Legacy Connector:** Yes. The following entities are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-overview.html)See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Latest Connector:** Yes (Automatic) / **Legacy Connector:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-field-mappings.html).
  - **Feature:** Filters / **Latest Connector:** Date range only / **Legacy Connector:** Yes. The following filters are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-overview.html)
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Latest Connector:** Full sync only / **Legacy Connector:** Supports full and incremental sync

- ****[File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html)****
  - **Feature:** File types
  - **Latest Connector:** No
  - **Legacy Connector:** Supports all files supported by Amazon Q.
