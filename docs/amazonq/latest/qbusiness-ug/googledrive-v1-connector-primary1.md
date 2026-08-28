---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-connector-primary1.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Google Drive to Amazon Q Business (Original)
<a name="googledrive-v1-connector-primary1"></a>

**Note**
 This documentation covers the original version of the Google Drive connector. For new implementations, we recommend using the New Google Drive connector which offers significantly improved performance. The original connector remains available for customers requiring specific features not yet supported in new.

## Known limitations for the Amazon Q Business Google Drive connector
<a name="googledrive-v1-limitations-primary"></a>

The Amazon Q Google Drive connector has the following known limitations:
+ To make a document available to multiple users in Amazon Q Business, you need to explicitly add each user by their email address. Only documents with specific ACLs, including folder-level ACLs, will be available to your users for query responses within Amazon Q. The **Anyone with the link** feature is not supported.
+ Custom field mapping is not available for Google Drive connector as the Google Drive UI does not support creating custom fields.
+ Google Drive API does not support retrieving comments from a permanently deleted file. Comments are retrievable, however, for trashed files. When a file is trashed, the Amazon Q connector will delete comments from the Amazon Q index.
+ Google Drive API does not return comments present in a .docx file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
