---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Mapping.Limitations.html
---

# Limitations of data type mapping in the AWS Schema Conversion Tool
<a name="CHAP_Mapping.Limitations"></a>

The following limitations apply when converting schemas using multiple servers in a single AWS SCT project:
+ You can add the same server to a project only once.
+ You can't map server schemas to a specific target schema, only to a target server. AWS SCT creates the target schema during conversion.
+ You can't map lower-level source objects to the target server.
+ You can map one source schema to only one target server in a project.
+ Make sure to map a source to a target server to create an assessment report, convert schemas, or extract data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
