---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-delete-cdc.html
---

# Disable a CDC stream in Amazon Keyspaces
<a name="keyspaces-delete-cdc"></a>

To disable a CDC stream in a keyspace, you can use the `ALTER TABLE` statement in CQL, the `update-table` command with the AWS CLI, or the console.

------
#### [ Cassandra Query Language (CQL) ]

**Disable a stream (CDC stream) with CQL**

1. To disable a stream, you can use the following statement.

   ```
   ALTER TABLE mykeyspace.mytable
   WITH cdc = FALSE;
   ```

1. To confirm that the stream is disabled, you can use the following statement.

   ```
   SELECT keyspace_name, table_name, cdc, custom_properties FROM system_schema_mcs.tables WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
   ```

   The output of that statement looks similar to this.

   ```
    keyspace_name | table_name | cdc   | custom_properties
   ---------------+------------+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      mykeyspace  |   mytable  | False | {'capacity_mode': {'last_update_to_pay_per_request_timestamp': '1741385668642', 'throughput_mode': 'PAY_PER_REQUEST'}, 'encryption_specification': {'encryption_type': 'AWS_OWNED_KMS_KEY'}, 'point_in_time_recovery': {'status': 'disabled'}}
   ```

------
#### [ CLI ]

**Disable a stream (CDC stream) with the AWS CLI**

1. To disable a stream, you can use the following command.

   ```
   aws keyspaces update-table \
   --keyspace-name 'mykeyspace' \
   --table-name 'mytable' \
   --cdc-specification status=DISABLED
   ```

1. The output of the command looks similar to this example.

   ```
   {
       "keyspaceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/",
       "streamName": "my_stream"
   }
   ```

------
#### [ Console ]

**Disable a stream (CDC stream) with the Amazon Keyspaces console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables**, and then choose a table from the list.

1. Choose the **Streams** tab.

1. Choose **Edit**.

1. Unselect **Turn on streams**.

1. Choose **Save changes** to disable the stream.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
