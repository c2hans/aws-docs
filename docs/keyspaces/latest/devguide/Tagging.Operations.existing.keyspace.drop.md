---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.keyspace.drop.html
---

# Delete tags from a keyspace
<a name="Tagging.Operations.existing.keyspace.drop"></a>

------
#### [ Console ]

**Delete a tag from an existing keyspace using the console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Keyspaces**.

1. Choose a keyspace from the list. Then choose the **Tags** tab where you can view the tags of the keyspace.

1. Choose **Manage tags** and delete the tags you don't need anymore.

1. Choose **Save changes**.

------
#### [ Cassandra Query Language (CQL) ]

**Delete a tag from an existing keyspace using CQL**
+

  ```
  ALTER KEYSPACE mykeyspace DROP TAGS {'key1':'val1', 'key2':'val2'};
  ```

------
#### [ CLI ]

**Delete a tag from an existing keyspace using the AWS CLI**
+ The following statement removes the specified tags from a keyspace.

  ```
  aws keyspaces untag-resource --resource-arn '{{arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/myKeyspace/}}' --tags 'key=key3,value=val3' 'key=key4,value=val4'
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
