---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started.html
---

# Getting started with Amazon File Cache
<a name="getting-started"></a>

Learn how to start using Amazon File Cache. These steps walk you through creating an Amazon File Cache resource and accessing it from your compute instances. Amazon File Cache can link to an Amazon Simple Storage Service (Amazon S3) or Network File System (NFS) data repository (but not to both types at the same time). This exercise uses an Amazon S3 bucket as the data repository, and shows how to use your cache to process the data in your Amazon S3 bucket with your file-based applications.

This getting started exercise includes the following steps.

**Topics**
+ [Prerequisites](prerequisites.md)
+ [Step 1: Create your cache](getting-started-step1.md)
+ [Step 2: Install and configure the Lustre client on your instance before mounting your cache](getting-started-step2.md)
+ [Step 3: Run your analysis](getting-started-step3.md)
+ [Step 4: Clean up resources](getting-started-step4.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
