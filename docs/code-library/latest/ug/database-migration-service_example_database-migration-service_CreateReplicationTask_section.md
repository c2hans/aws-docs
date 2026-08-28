---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/database-migration-service_example_database-migration-service_CreateReplicationTask_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateReplicationTask` with a CLI
<a name="database-migration-service_example_database-migration-service_CreateReplicationTask_section"></a>

The following code examples show how to use `CreateReplicationTask`.

------
#### [ CLI ]

**AWS CLI**
**To create a replication task**
The following `create-replication-task` example creates a replication task.

```
aws dms create-replication-task \
    --replication-task-identifier {{movedata}} \
    --source-endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA}} \
    --target-endpoint-arn {{arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U}} \
    --replication-instance-arn {{$RI_ARN}} \
    --migration-type {{full-load}} \
    --table-mappings {{file://table-mappings.json}}
```
Contents of `table-mappings.json`:

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "prodrep",
                "table-name": "%"
            },
            "rule-action": "include",
            "filters": []
        }
    ]
}
```
Output:

```
{
    "ReplicationTask": {
        "ReplicationTaskIdentifier": "moveit2",
        "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA",
        "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE",
        "MigrationType": "full-load",
        "TableMappings": ...output omitted... ,
        "ReplicationTaskSettings": ...output omitted... ,
        "Status": "creating",
        "ReplicationTaskCreationDate": 1590524772.505,
        "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"
    }
}
```
For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the *AWS Database Migration Service User Guide*.
+  For API details, see [CreateReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-task.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new AWS Database Migration Service replication task that uses CdcStartTime instead of CdcStartPosition. The MigrationType is set to "full-load-and-cdc", meaning the target table must be empty. The new task is tagged with a tag that has a key of Stage and a key value of Test. For more information about the values used by this cmdlet, see Creating a Task (https://docs.aws.amazon.com/dms/latest/userguide/CHAP\_Tasks.Creating.html) in the AWS Database Migration Service User Guide.**

```
New-DMSReplicationTask -ReplicationInstanceArn "arn:aws:dms:us-east-1:123456789012:rep:EXAMPLE66XFJUWATDJGBEXAMPLE"`
  -CdcStartTime "2019-08-08T12:12:12"`
  -CdcStopPosition "server_time:2019-08-09T12:12:12"`
  -MigrationType "full-load-and-cdc"`
  -ReplicationTaskIdentifier "task1"`
  -ReplicationTaskSetting ""`
  -SourceEndpointArn "arn:aws:dms:us-east-1:123456789012:endpoint:EXAMPLEW5UANC7Y3P4EEXAMPLE"`
  -TableMapping "file:////home/testuser/table-mappings.json"`
  -Tag @{"Key"="Stage";"Value"="Test"}`
  -TargetEndpointArn "arn:aws:dms:us-east-1:123456789012:endpoint:EXAMPLEJZASXWHTWCLNEXAMPLE"
```
+  For API details, see [CreateReplicationTask](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new AWS Database Migration Service replication task that uses CdcStartTime instead of CdcStartPosition. The MigrationType is set to "full-load-and-cdc", meaning the target table must be empty. The new task is tagged with a tag that has a key of Stage and a key value of Test. For more information about the values used by this cmdlet, see Creating a Task (https://docs.aws.amazon.com/dms/latest/userguide/CHAP\_Tasks.Creating.html) in the AWS Database Migration Service User Guide.**

```
New-DMSReplicationTask -ReplicationInstanceArn "arn:aws:dms:us-east-1:123456789012:rep:EXAMPLE66XFJUWATDJGBEXAMPLE"`
  -CdcStartTime "2019-08-08T12:12:12"`
  -CdcStopPosition "server_time:2019-08-09T12:12:12"`
  -MigrationType "full-load-and-cdc"`
  -ReplicationTaskIdentifier "task1"`
  -ReplicationTaskSetting ""`
  -SourceEndpointArn "arn:aws:dms:us-east-1:123456789012:endpoint:EXAMPLEW5UANC7Y3P4EEXAMPLE"`
  -TableMapping "file:////home/testuser/table-mappings.json"`
  -Tag @{"Key"="Stage";"Value"="Test"}`
  -TargetEndpointArn "arn:aws:dms:us-east-1:123456789012:endpoint:EXAMPLEJZASXWHTWCLNEXAMPLE"
```
+  For API details, see [CreateReplicationTask](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
