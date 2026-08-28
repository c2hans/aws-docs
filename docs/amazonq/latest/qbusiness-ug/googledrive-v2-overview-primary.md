---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v2-overview-primary.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Google Drive connector overview
<a name="googledrive-v2-overview-primary"></a>

The following table gives an overview of the Amazon Q Business Google Drive connector new and its supported features.

- ****Security****
  - **Feature:** Authentication type / **Support:** Service Account Based
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes.

- ****Crawl features****
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Files See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/exclude by shared drive IDs <br />+  Include/exclude by MIME types (e.g., `application/pdf`, `application/vnd.google-apps.document`) <br />+  Date range filtering
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all file types supported by Amazon Q. For more information see [Doc types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
