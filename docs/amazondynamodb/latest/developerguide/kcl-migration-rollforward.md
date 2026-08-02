---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kcl-migration-rollforward.html
---

# Roll forward to KCL 3.x after a rollback
<a name="kcl-migration-rollforward"></a>

This topic explains how to roll forward your consumer application to KCL 3.x after a rollback. When you need to roll forward, you must complete a two-step process:

1. Run the [KCL Migration Tool](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client/scripts/KclMigrationTool.py).

1. Deploy the code with KCL 3.x.

## Step 1: Run the KCL Migration Tool
<a name="kcl-migration-rollforward-step1"></a>

Run the KCL Migration Tool with the following command to roll forward to KCL 3.x:

```
python3 ./KclMigrationTool.py --region {{region}} --mode rollforward [--application_name {{applicationName}}] [--coordinator_state_table_name {{coordinatorStateTableName}}]
```

### Parameters
<a name="kcl-migration-rollforward-parameters"></a>

`--region`
Replace {{region}} with your AWS Region.

`--application_name`
This parameter is required if you're using default names for your coordinator state table. If you have specified custom names for the coordinator state table, you can omit this parameter. Replace {{applicationName}} with your actual KCL application name. The tool uses this name to derive the default table names if custom names are not provided.

`--coordinator_state_table_name`
This parameter is needed when you have set a custom name for the coordinator state table in your KCL configuration. If you're using the default table name, you can omit this parameter. Replace {{coordinatorStateTableName}} with the custom table name you specified for your coordinator state table.

After you run the migration tool in roll-forward mode, KCL creates the following DynamoDB resources required for KCL 3.x:
+ A Global Secondary Index on the lease table
+ A worker metrics table

## Step 2: Deploy the code with KCL 3.x
<a name="kcl-migration-rollforward-step2"></a>

After running the KCL Migration Tool for a roll forward, deploy your code with KCL 3.x to your workers. To complete your migration, see [Step 8: Complete the migration](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-from-2-3.html#kcl-migration-from-2-3-finish).
