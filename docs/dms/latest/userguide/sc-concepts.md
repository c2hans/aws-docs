---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/sc-concepts.html
---

# DMS Schema Conversion concepts
<a name="sc-concepts"></a>

DMS Schema Conversion in AWS Database Migration Service converts database schemas and code objects from a source database engine to a compatible format for a target database engine. Understanding the following core concepts helps you control which objects to convert and how to convert them.

This section describes how DMS Schema Conversion represents your database schema as a metadata model, how you use selection rules to define the scope of your operations, and how you use transformation rules to customize naming and data type mappings during conversion.

**Topics**
+ [Metadata model in DMS Schema Conversion](sc-metadata-model.md)
+ [Selection rules in DMS Schema Conversion](sc-selection-rules.md)
+ [Transformation rules in DMS Schema Conversion](sc-transformation-rules.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
