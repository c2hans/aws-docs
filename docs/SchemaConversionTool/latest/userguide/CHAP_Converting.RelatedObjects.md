---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.RelatedObjects.html
---

# Viewing related transformed objects in AWS Schema Conversion Tool
<a name="CHAP_Converting.RelatedObjects"></a>

After a schema conversion, in some cases AWS SCT might have created several objects for one schema object on the source database. For example, when performing an Oracle to PostgreSQL conversion, AWS SCT takes each Oracle trigger and transforms it into a trigger and trigger function on PostgreSQL target. Also, when AWS SCT converts an Oracle package function or procedure to PostgreSQL, it creates an equivalent function and an INIT function that should be run as init block before the procedure or function can be run.

The following procedure lets you see all related objects that were created after a schema conversion.

**To view related objects that were created during a schema conversion**

1. After the schema conversion, choose the converted object in the target tree view.

1. Choose the **Related Converted Objects** tab.

1. View the list of related target objects.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
