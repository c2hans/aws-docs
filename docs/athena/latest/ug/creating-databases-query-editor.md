---
source_url: https://docs.aws.amazon.com/athena/latest/ug/creating-databases-query-editor.html
---

# Create a database
<a name="creating-databases-query-editor"></a>

After you have set up a query results location, creating a database in the Athena console query editor is straightforward.

**To create a database using the Athena query editor**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. On the **Editor** tab, in the query editor, enter the Hive data definition language (DDL) command `CREATE DATABASE {{myDataBase}}`. Replace {{myDatabase}} with the name that you want to use. For restrictions on database names, see [Name databases, tables, and columns](tables-databases-columns-names.md).

1. Choose **Run** or press **Ctrl\+ENTER**.

1. To make your database the current database, select it from the **Database** menu on the left of the query editor.

For information about controlling permissions to Athena databases, see [Configure access to databases and tables in the AWS Glue Data Catalog](fine-grained-access-to-glue-resources.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
