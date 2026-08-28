---
source_url: https://docs.aws.amazon.com/athena/latest/ug/creating-row.html
---

# Create a `ROW`
<a name="creating-row"></a>

**Note**
The examples in this section use `ROW` as a means to create sample data to work with. When you query tables within Athena, you do not need to create `ROW` data types, as they are already created from your data source. When you use `CREATE_TABLE`, Athena defines a `STRUCT` in it, populates it with data, and creates the `ROW` data type for you, for each row in the dataset. The underlying `ROW` data type consists of named fields of any supported SQL data types.

```
WITH dataset AS (
 SELECT
   ROW('Bob', 38) AS users
 )
SELECT * FROM dataset
```

This query returns:

```
+-------------------------+
| users                   |
+-------------------------+
| {field0=Bob, field1=38} |
+-------------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
