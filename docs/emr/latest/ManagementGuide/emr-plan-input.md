---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-input.html
---

# Prepare input data for processing with Amazon EMR
<a name="emr-plan-input"></a>

Most clusters load input data and then process that data. In order to load data, it needs to be in a location that the cluster can access and in a format the cluster can process. The most common scenario is to upload input data into Amazon S3. Amazon EMR provides tools for your cluster to import or read data from Amazon S3.

The default input format in Hadoop is text files, though you can customize Hadoop and use tools to import data stored in other formats.

**Topics**
+ [Types of input Amazon EMR can accept](emr-plan-input-accept.md)
+ [Different ways to get data into Amazon EMR](emr-plan-get-data-in.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
