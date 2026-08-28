---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.table.html
---

# Add tags to a table
<a name="Tagging.Operations.existing.table"></a>

You can add tags to an existing table in Amazon Keyspaces using the console, CQL or the AWS CLI.

------
#### [ Console ]

**Add tags to a table using the Amazon Keyspaces console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables**.

1. Choose a table from the list and choose the **Tags** tab.

1. Choose **Manage tags** to add tags to the table.

1. Choose **Save changes**.

------
#### [ Cassandra Query Language (CQL) ]

**Add tags to a table using CQL**
+ The following statement shows how to add tags to an existing table.

  ```
  ALTER TABLE mykeyspace.mytable ADD TAGS {'key1':'val1', 'key2':'val2'};
  ```

------
#### [ CLI ]

**Add tags to a table using the AWS CLI**
+ The following example shows how to add new tags to an existing table.

  ```
  aws keyspaces tag-resource --resource-arn '{{arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/myKeyspace/table/myTable}}' --tags 'key=key3,value=val3' 'key=key4,value=val4'
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
