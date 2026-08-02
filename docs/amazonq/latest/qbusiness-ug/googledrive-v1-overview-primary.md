---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-overview-primary.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Google Drive connector overview
<a name="googledrive-v1-overview-primary"></a>

The following table gives an overview of the Amazon Q Business Google Drive connector and its supported features.

****

- ****Security****
  - **Feature:** Authentication type / **Support:** Google Service Account, OAuth 2.0 with Refresh Token Flow
  - **Feature:** Authentication credentials / **Support:** [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-overview-primary.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-overview-primary.html)  Admin privileges required.
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes. Supported only with Google service account authentication.
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** No
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-overview-primary.html)See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports default field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-drive-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-overview-primary.html)
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
