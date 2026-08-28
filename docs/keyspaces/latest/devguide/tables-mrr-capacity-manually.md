---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-capacity-manually.html
---

# Set the provisioned capacity of a multi-Region table manually in Amazon Keyspaces
<a name="tables-mrr-capacity-manually"></a>

If you have to turn off auto scaling for a multi-Region table, you can provision the table's read capacity for a replica table manually using CQL or the AWS CLI.

**Note**
We recommend using auto scaling for multi-Region tables that use provisioned capacity mode. For more information, see [Estimate and provision capacity for a multi-Region table in Amazon Keyspaces](tables-multi-region-capacity.md).

------
#### [ Cassandra Query Language (CQL) ]

**Setting the provisioned capacity of a multi-Region table manually using CQL**
+ You can use `ALTER TABLE` to provision the table's read capacity for a replica table manually.

  ```
  ALTER TABLE mykeyspace.mytable
  WITH CUSTOM_PROPERTIES = {
      'capacity_mode': {
          'throughput_mode': 'PROVISIONED',
          'read_capacity_units': 1,
          'write_capacity_units': 1
      },
      'replica_updates': {
          'us-east-1': {
              'read_capacity_units': 2
           }
      }
  };
  ```

------
#### [ CLI ]

**Set the provisioned capacity of a multi-Region table manually using the AWS CLI**
+ If you have to turn off auto scaling for a multi-Region table, you can use `update-table` to provision the table's read capacity for a replica table manually.

  ```
  aws keyspaces update-table --keyspace-name mykeyspace --table-name mytable \
  --capacity-specification throughputMode=PROVISIONED,readCapacityUnits=1,writeCapacityUnits=1 \
  --replica-specifications region="us-east-1",readCapacityUnits=5
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
