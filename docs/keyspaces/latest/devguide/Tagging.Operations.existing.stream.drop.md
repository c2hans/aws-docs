---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.stream.drop.html
---

# Delete tags from a stream
<a name="Tagging.Operations.existing.stream.drop"></a>

To delete tags from a stream, you can use CQL or the AWS CLI. You can only delete the tags for the latest stream.

------
#### [ Console ]

**Delete tags from a table using the Amazon Keyspaces console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables**.

1. Choose a table from the list and choose the **Streams** tab.

1. In the **Tags** section choose **Manage tags** to delete tags from the table.

1. After the tag you want to delete, choose **Remove**.

1. Choose **Save changes**.

------
#### [ Cassandra Query Language (CQL) ]

**Delete tags from a stream using CQL**
+ The following statement shows how to delete tags from an existing stream.

  ```
  ALTER TABLE mytable DROP TAGS_FOR_CDC {'key3':'val3', 'key4':'val4'};
  ```

------
#### [ CLI ]

**Delete tags from a stream using the AWS CLI**
+ The following statement removes the specified tags from a stream.

  ```
  aws keyspaces untag-resource --resource-arn '{{arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/my_keyspace/table/my_table/stream/2025-05-11T21:21:33.291}}' --tags 'key=key3,value=val3' 'key=key4,value=val4'
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
