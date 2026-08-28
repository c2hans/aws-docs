---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_database-migration-service_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# AWS DMS examples using Tools for PowerShell V5
<a name="powershell_database-migration-service_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with AWS DMS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `New-DMSReplicationTask`
<a name="database-migration-service_CreateReplicationTask_powershell_topic"></a>

The following code example shows how to use `New-DMSReplicationTask`.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
