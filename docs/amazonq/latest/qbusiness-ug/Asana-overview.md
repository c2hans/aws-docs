---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Asana-overview.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Asana connector overview (Preview)
<a name="Asana-overview"></a>

The following table gives an overview of the Amazon Q Business Asana connector and its supported features.

| Category | Feature | Support |
| --- | --- | --- |
| Security | Authentication type | Service Account and PAT |
| Authentication credentials | +  Service Account Tokens <br />+  Personal Access Token  |
| [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling | No. For preview, this connector only scans public Asana projects. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-user-management.html).  |
| [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) | No |
| [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) | Yes |
| Crawl features | Custom metadata | No |
| Entities | Yes. The following entities are supported: +  Project <br />+  Tasks <br />+  Comments   Each instance of an entity is crawled as a single document.  |
| [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) | Yes. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-field-mappings.html). |
| Filters | Yes. The following filters are supported: +  Specific Projects <br />+  Project inclusion regex pattern <br />+  Project exclusion regex pattern  |
| [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) | Supports full and incremental sync. |
| [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) | +  Project <br />+  Task <br />+  Comment  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
