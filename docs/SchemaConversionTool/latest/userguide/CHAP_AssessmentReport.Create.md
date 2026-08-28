---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Create.html
---

# Creating an assessment report in AWS Schema Conversion Tool
<a name="CHAP_AssessmentReport.Create"></a>

Use the following procedure to create a database migration assessment report.

**To create a database migration assessment report**

1. Make sure that you created a mapping rule for the source database schema to create an assessment report for. For more information, see [Mapping new data types in the AWS Schema Conversion Tool](CHAP_Mapping.New.md).

1. On the **View** menu, choose **Main view**.

1. In the left panel that displays your source database schema, choose a schema object to create an assessment report for. To include multiple database schemas into the report, choose the parent node, for example **Schemas**.

   Make sure that you selected the check boxes for all schema objects to create an assessment report for.

1. Open the context (right-click) menu for the object, and then choose **Create report**.
![Create database migration assessment report](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/create_assessment_report.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
