---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationtask.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::ReplicationTask
<a name="aws-resource-dms-replicationtask"></a>

The `AWS::DMS::ReplicationTask` resource creates an AWS DMS replication task.

## Syntax
<a name="aws-resource-dms-replicationtask-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dms-replicationtask-syntax.json"></a>

```
{
  "Type" : "AWS::DMS::ReplicationTask",
  "Properties" : {
      "[CdcStartPosition](#cfn-dms-replicationtask-cdcstartposition)" : {{String}},
      "[CdcStartTime](#cfn-dms-replicationtask-cdcstarttime)" : {{Number}},
      "[CdcStopPosition](#cfn-dms-replicationtask-cdcstopposition)" : {{String}},
      "[MigrationType](#cfn-dms-replicationtask-migrationtype)" : {{String}},
      "[ReplicationInstanceArn](#cfn-dms-replicationtask-replicationinstancearn)" : {{String}},
      "[ReplicationTaskIdentifier](#cfn-dms-replicationtask-replicationtaskidentifier)" : {{String}},
      "[ReplicationTaskSettings](#cfn-dms-replicationtask-replicationtasksettings)" : {{String}},
      "[ResourceIdentifier](#cfn-dms-replicationtask-resourceidentifier)" : {{String}},
      "[SourceEndpointArn](#cfn-dms-replicationtask-sourceendpointarn)" : {{String}},
      "[TableMappings](#cfn-dms-replicationtask-tablemappings)" : {{String}},
      "[Tags](#cfn-dms-replicationtask-tags)" : {{[ Tag, ... ]}},
      "[TargetEndpointArn](#cfn-dms-replicationtask-targetendpointarn)" : {{String}},
      "[TaskData](#cfn-dms-replicationtask-taskdata)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-dms-replicationtask-syntax.yaml"></a>

```
Type: AWS::DMS::ReplicationTask
Properties:
  [CdcStartPosition](#cfn-dms-replicationtask-cdcstartposition): {{String}}
  [CdcStartTime](#cfn-dms-replicationtask-cdcstarttime): {{Number}}
  [CdcStopPosition](#cfn-dms-replicationtask-cdcstopposition): {{String}}
  [MigrationType](#cfn-dms-replicationtask-migrationtype): {{String}}
  [ReplicationInstanceArn](#cfn-dms-replicationtask-replicationinstancearn): {{String}}
  [ReplicationTaskIdentifier](#cfn-dms-replicationtask-replicationtaskidentifier): {{String}}
  [ReplicationTaskSettings](#cfn-dms-replicationtask-replicationtasksettings): {{String}}
  [ResourceIdentifier](#cfn-dms-replicationtask-resourceidentifier): {{String}}
  [SourceEndpointArn](#cfn-dms-replicationtask-sourceendpointarn): {{String}}
  [TableMappings](#cfn-dms-replicationtask-tablemappings): {{String}}
  [Tags](#cfn-dms-replicationtask-tags): {{
    - Tag}}
  [TargetEndpointArn](#cfn-dms-replicationtask-targetendpointarn): {{String}}
  [TaskData](#cfn-dms-replicationtask-taskdata): {{String}}
```

## Properties
<a name="aws-resource-dms-replicationtask-properties"></a>

`CdcStartPosition`  <a name="cfn-dms-replicationtask-cdcstartposition"></a>
Indicates when you want a change data capture (CDC) operation to start. Use either `CdcStartPosition` or `CdcStartTime` to specify when you want a CDC operation to start. Specifying both values results in an error.
 The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format.
Here is a date example: `--cdc-start-position "2018-03-08T12:12:12"`
Here is a checkpoint example: `--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"`
Here is an LSN example: `--cdc-start-position “mysql-bin-changelog.000024:373”`
When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the `slotName` extra connection attribute to the name of this logical replication slot. For more information, see [ Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib) in the *AWS Database Migration Service User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CdcStartTime`  <a name="cfn-dms-replicationtask-cdcstarttime"></a>
Indicates the start time for a change data capture (CDC) operation.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CdcStopPosition`  <a name="cfn-dms-replicationtask-cdcstopposition"></a>
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Here is a server time example: `--cdc-stop-position "server_time:2018-02-09T12:12:12"`
Here is a commit time example: `--cdc-stop-position "commit_time: 2018-02-09T12:12:12"`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MigrationType`  <a name="cfn-dms-replicationtask-migrationtype"></a>
The migration type. Valid values: `full-load` \| `cdc` \| `full-load-and-cdc`
*Required*: Yes
*Type*: String
*Allowed values*: `full-load | cdc | full-load-and-cdc`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationInstanceArn`  <a name="cfn-dms-replicationtask-replicationinstancearn"></a>
The Amazon Resource Name (ARN) of a replication instance.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReplicationTaskIdentifier`  <a name="cfn-dms-replicationtask-replicationtaskidentifier"></a>
An identifier for the replication task.
Constraints:
+ Must contain 1-255 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationTaskSettings`  <a name="cfn-dms-replicationtask-replicationtasksettings"></a>
Overall settings for the task, in JSON format. For more information, see [ Specifying Task Settings for AWS Database Migration Service Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html) in the *AWS Database Migration Service User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-dms-replicationtask-resourceidentifier"></a>
A display name for the resource identifier at the end of the `EndpointArn` response parameter that is returned in the created `Endpoint` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as `Example-App-ARN1`.
For example, this value might result in the `EndpointArn` value `arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`. If you don't specify a `ResourceIdentifier` value, AWS DMS generates a default identifier value for the end of `EndpointArn`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceEndpointArn`  <a name="cfn-dms-replicationtask-sourceendpointarn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableMappings`  <a name="cfn-dms-replicationtask-tablemappings"></a>
The table mappings for the task, in JSON format. For more information, see [ Using Table Mapping to Specify Task Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html) in the *AWS Database Migration Service User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dms-replicationtask-tags"></a>
One or more tags to be assigned to the replication task.
*Required*: No
*Type*: Array of [Tag](aws-properties-dms-replicationtask-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetEndpointArn`  <a name="cfn-dms-replicationtask-targetendpointarn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TaskData`  <a name="cfn-dms-replicationtask-taskdata"></a>
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see [Specifying Supplemental Data for Task Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html) in the *AWS Database Migration Service User Guide.*
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dms-replicationtask-return-values"></a>

### Ref
<a name="aws-resource-dms-replicationtask-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the replication task ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dms-replicationtask-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

## Examples
<a name="aws-resource-dms-replicationtask--examples"></a>

**Topics**
+ [Create a replication task](#aws-resource-dms-replicationtask--examples--Create_a_replication_task)
+ [Create a replication task with full load task settings](#aws-resource-dms-replicationtask--examples--Create_a_replication_task_with_full_load_task_settings)

### Create a replication task
<a name="aws-resource-dms-replicationtask--examples--Create_a_replication_task"></a>

The following example creates a replication task with a selection rule and action.

#### JSON
<a name="aws-resource-dms-replicationtask--examples--Create_a_replication_task--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "myReplicationTask": {
            "Type": "AWS::DMS::ReplicationTask",
            "Properties": {
                "SourceEndpointArn": 11,
                "TargetEndpointArn": "12ff",
                "ReplicationInstanceArn": "ert1",
                "MigrationType": "full-load",
                "TableMappings": "{ \"rules\": [ { \"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": { \"schema-name\": \"%\", \"table-name\": \"%\" }, \"rule-action\": \"include\" } ] }"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-dms-replicationtask--examples--Create_a_replication_task--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myReplicationTask:
    Type: AWS::DMS::ReplicationTask
    Properties:
      MigrationType: full-load
      ReplicationInstanceArn: ReplicationInstance
      SourceEndpointArn: SourceEndpoint
      TableMappings: "{ \"rules\": [ { \"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": { \"schema-name\": \"%\", \"table-name\": \"%\" }, \"rule-action\": \"include\" } ] }"
      TargetEndpointArn: TargetEndpoint
```

### Create a replication task with full load task settings
<a name="aws-resource-dms-replicationtask--examples--Create_a_replication_task_with_full_load_task_settings"></a>

The following example creates a replication task with a selection rule and full-load task settings. For more information about full-load task settings, see [Full-load task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.html).

#### JSON
<a name="aws-resource-dms-replicationtask--examples--Create_a_replication_task_with_full_load_task_settings--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "myReplicationTask": {
            "Type": "AWS::DMS::ReplicationTask",
            "Properties": {
                "SourceEndpointArn": "arn:aws:dms:eu-west-1:123456789012:endpoint:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                "TargetEndpointArn": "arn:aws:dms:eu-west-1:123456789012:endpoint:BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
                "ReplicationInstanceArn": "arn:aws:dms:eu-west-1:123456789012:rep:CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
                "MigrationType": "full-load",
                "TableMappings": "{ \"rules\": [ { \"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": { \"schema-name\": \"%\", \"table-name\": \"%\" }, \"rule-action\": \"include\" } ] }",
                "ReplicationTaskSettings": "{ \"FullLoadSettings\": { \"CommitRate\": 9000, \"TargetTablePrepMode\": \"DROP_AND_CREATE\", \"CreatePkAfterFullLoad\": true }, \"BeforeImageSettings\": null, \"ControlTablesSettings\": { \"historyTimeslotInMinutes\": 5, \"HistoryTimeslotInMinutes\": 5}}"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-dms-replicationtask--examples--Create_a_replication_task_with_full_load_task_settings--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myReplicationTask:
    Type: AWS::DMS::ReplicationTask
    Properties:
      MigrationType: full-load
      ReplicationInstanceArn: arn:aws:dms:eu-west-1:123456789012:rep:CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
      SourceEndpointArn: arn:aws:dms:eu-west-1:123456789012:endpoint:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
      TableMappings: "{ \"rules\": [ { \"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": { \"schema-name\": \"%\", \"table-name\": \"%\" }, \"rule-action\": \"include\" } ] }"
      ReplicationTaskSettings: "{ \"FullLoadSettings\": { \"CommitRate\": 9000, \"TargetTablePrepMode\": \"DROP_AND_CREATE\", \"CreatePkAfterFullLoad\": true }, \"BeforeImageSettings\": null, \"ControlTablesSettings\": { \"historyTimeslotInMinutes\": 5, \"HistoryTimeslotInMinutes\": 5}}"
      TargetEndpointArn: arn:aws:dms:eu-west-1:123456789012:endpoint:BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
```

## See also
<a name="aws-resource-dms-replicationtask--seealso"></a>
+ [ CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html) in the *AWS Database Migration Service API Reference*
+  [Managing AWS resources as a single unit with AWS CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
