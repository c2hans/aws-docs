---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.UnionAllView.html
---

# Creating UNION ALL view in the AWS Schema Conversion Tool
<a name="CHAP_UserInterface.UnionAllView"></a>

If a source table is partitioned, AWS SCT creates *n* target tables, where *n* is the number of partitions on the source table. AWS SCT creates a UNION ALL view on top of the target tables to represent the source table. If you use an AWS SCT data extractor to migrate your data, the source table partitions will be extracted and loaded in parallel by separate subtasks.

**To use Union All view for a project**

1. Start AWS SCT. Create a new project or open an existing AWS SCT project.

1. On the **Settings** menu, choose **Conversion settings**.

1. Choose a pair of OLAP databases from the list at the top.

1. Turn on **Use Union all view?**
![Conversion settings](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/conversion-settings.png)

1. Choose **OK** to save the settings and close the **Conversion settings** dialog box.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
