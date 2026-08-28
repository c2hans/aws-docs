---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.stream.html
---

# Add new tags to a stream
<a name="Tagging.Operations.existing.stream"></a>

You can add new tags to an existing stream in Amazon Keyspaces using the CQL or the AWS CLI. You can only add tags to the latest stream.

------
#### [ Console ]

**Add tags to an existing stream (console)**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables**, and then choose the table with the stream that you want to tag.

1. Choose the **Streams** tab.

1. In the **Tags** section, choose **Manage tags**.

1. Choose **Add new tag** to add a new tag. You can create up to 50 tags by repeating this step.

1. Choose **Save changes**.

------
#### [ Cassandra Query Language (CQL) ]

**Add tags to a stream using CQL**
+ The following statement shows how to add tags to an existing stream.

  ```
  ALTER TABLE mykeyspace.mytable ADD TAGS_FOR_CDC {'key1':'val1', 'key2':'val2'};
  ```

------
#### [ CLI ]

**Add tags to a stream using the AWS CLI**
+ The following example shows how to add new tags to an existing stream.

  ```
  aws keyspaces tag-resource --resource-arn '{{arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/my_keyspace/table/my_table/stream/2025-05-11T21:21:33.291}}' --tags 'key=key3,value=val3' 'key=key4,value=val4'
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
