---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.ActionItems.html
---

# Assessment report action items
<a name="CHAP_AssessmentReport.ActionItems"></a>

The assessment report view also includes an **Action Items** tab. This tab contains a list of items that can't be converted automatically to the database engine of your target Amazon RDS DB instance. If you select an action item from the list, AWS SCT highlights the item from your schema that the action item applies to.

The report also contains recommendations for how to manually convert the schema item. For example, after the assessment runs, detailed reports for the database/schema show you the effort required to design and implement the recommendations for converting Action items. For more information about deciding how to handle manual conversions, see [Converting schemas using AWS SCT](CHAP_Converting.Manual.md).

![Action items tab](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/action_items_tab.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
