---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-overview.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Overview
<a name="onedrive-new-overview"></a>

The following table gives an overview of the Amazon Q Business Microsoft OneDrive new connector and its supported features.

- ****Security****
  - **Feature:** Authentication type / **Support:** OAuth 2.0 with Client Credentials Flow
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-new-acl-crawling.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes.

- ****Crawl features****
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  File See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Filter by date <br />+  Include or exclude using file path
  - **Feature:** Sync mode / **Support:** Incremental sync only (automatic).
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all file types supported by Amazon Q.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
