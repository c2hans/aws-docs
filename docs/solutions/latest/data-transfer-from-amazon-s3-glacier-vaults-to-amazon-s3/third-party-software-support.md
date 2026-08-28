---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/third-party-software-support.html
---

# Third-party software support
<a name="third-party-software-support"></a>

 This Guidance uses the value stored in the **ArchiveDescription** for each Amazon Glacier vault archive (as listed in the Amazon Glacier inventory file) as the key name for the new S3 object that it creates. The Guidance supports copying Amazon Glacier vaults using either FastGlacier or CloudBerry software as follows.
+  **FastGlacier (v1-v4)** – The Guidance extracts the value for `/ArchiveMetadata/Path` of `/m/p` from the XML metadata stored in the **ArchiveDescription** field in the Amazon Glacier inventory file. It then converts that value to a string that forms the S3 object key name.
+  **CloudBerry (v5.9)** – The Guidance extracts the value for **Path** from the JSON metadata stored in the **ArchiveDescription** field in the Amazon Glacier inventory file. It then converts that value to a string that forms the S3 object key name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
