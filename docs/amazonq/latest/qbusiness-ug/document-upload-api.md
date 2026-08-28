---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/document-upload-api.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Upload documents directly into a Amazon Q Business application using APIs
<a name="document-upload-api"></a>

Amazon Q Business supports direct document uploads into an Amazon Q Business index using both the console and the APIs.

| API action | API description | Relevant User Guide topic |
| --- | --- | --- |
| [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html) | Adds one or more documents to an Amazon Q Business index | [Upload documents](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/upload-docs.html) |
| [BatchDeleteDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchDeleteDocument.html) | Asynchronously deletes one or more documents added using the BatchPutDocument API from an Amazon Q Business index | [Deleting uploaded documents](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/delete-doc-upload.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
