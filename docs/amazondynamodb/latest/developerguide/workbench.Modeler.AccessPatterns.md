---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.AccessPatterns.html
---

# Adding and validating access patterns
<a name="workbench.Modeler.AccessPatterns"></a>

You can use NoSQL Workbench for Amazon DynamoDB to create, store, and validate *access patterns*.

**Note**
 See [Identify your data access patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step3.html) for more details on identifying the right access patterns.

**To create an access pattern**

1.  Open NoSQL Workbench, and on the main screen, choose the name of the model that you want to add access patterns to.

1.  On the left side, choose the **Access patterns** tab, and choose the **\+** icon.

1.  On the next screen, provide a **Name**, an optional **Description**, the **Type** of the access pattern, and the **Table** or **Global Secondary Index** to test the access pattern against.
**Note**
 NoSQL Workbench currently supports the following operations for access patterns: `Scan`, `Query`, `GetItem`, `PutItem`, `UpdateItem`, `DeleteItem`. Amazon DynamoDB supports a broader list of operations.

1.  After you create an access pattern, you can switch to the **Validate** tab to verify that your data model is designed to return expected results for the access pattern. See [Adding sample data to a data model](workbench.Modeler.AddData.md) for details on how to auto-generate sample data for your tables. Different types of access patterns support different input parameters.
**Note**
To validate access patterns, NoSQL Workbench starts a separate DynamoDB local database on port `8001` (by default) with tables and indexes stored in memory.
NoSQL Workbench automatically adds the sample data from your model to the temporary tables.
If you edit the sample data or the data model itself, NoSQL Workbench updates the temporary tables.
This temporary database is erased when you close the application.

**To edit your access patterns**

1.  Open NoSQL Workbench, and on the main screen, choose the name of the model that you want to edit access patterns for.

1.  On the left side, choose the **Access patterns** tab.

1. To edit an access pattern, choose it from the list on the left.

1. In the top bar, choose **Edit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
