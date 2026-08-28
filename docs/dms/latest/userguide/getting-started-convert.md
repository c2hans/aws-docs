---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/getting-started-convert.html
---

# Convert your source code in DMS Schema Conversion
<a name="getting-started-convert"></a>

You can convert your source database schema using the following procedure. Then you can save the converted code as SQL scripts in a text file.

**To convert your database schema**

1. In the source database pane, choose the database schema to convert. Also, select the check box for the name of this schema.

1. In the source database pane, choose **Convert** in the **Actions** menu. The **Convert** dialog box appears.

1. Choose **Convert** in the dialog box to confirm your choice.

1. Choose a database object in the source database pane. DMS Schema Conversion displays the source code and the converted code for this object. You can edit the converted SQL code for a database object using the Edit SQL feature. For more information, see [Editing and saving your converted SQL code](schema-conversion-convert.md#schema-conversion-convert-editsql).

1. In the target database pane, choose the converted database schema. Also, select the check box for the name of this schema.

1. For **Actions**, choose **Save as SQL**. The **Save** dialog box appears.

1. Choose **Save as SQL** to confirm your choice.

1. Choose **S3 bucket**. The Amazon S3 console opens.

1. Choose **Download** to save your SQL scripts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
