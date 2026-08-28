---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyDataMigration.html
---

# ModifyDataMigration
<a name="API_ModifyDataMigration"></a>

Modifies an existing AWS DMS data migration.

## Request Syntax
<a name="API_ModifyDataMigration_RequestSyntax"></a>

```
{
   "DataMigrationIdentifier": "{{string}}",
   "DataMigrationName": "{{string}}",
   "DataMigrationType": "{{string}}",
   "EnableCloudwatchLogs": {{boolean}},
   "NumberOfJobs": {{number}},
   "SelectionRules": "{{string}}",
   "ServiceAccessRoleArn": "{{string}}",
   "SourceDataSettings": [
      {
         "CDCStartPosition": "{{string}}",
         "CDCStartTime": "{{string}}",
         "CDCStopTime": "{{string}}",
         "SlotName": "{{string}}"
      }
   ],
   "TargetDataSettings": [
      {
         "TablePreparationMode": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ModifyDataMigration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataMigrationIdentifier](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-DataMigrationIdentifier"></a>
The identifier (name or ARN) of the data migration to modify.
Type: String
Required: Yes

 ** [DataMigrationName](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-DataMigrationName"></a>
The new name for the data migration.
Type: String
Required: No

 ** [DataMigrationType](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-DataMigrationType"></a>
The new migration type for the data migration.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** [EnableCloudwatchLogs](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-EnableCloudwatchLogs"></a>
Whether to enable Cloudwatch logs for the data migration.
Type: Boolean
Required: No

 ** [NumberOfJobs](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-NumberOfJobs"></a>
The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.
Type: Integer
Required: No

 ** [SelectionRules](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-SelectionRules"></a>
A JSON-formatted string that defines what objects to include and exclude from the migration.
Type: String
Required: No

 ** [ServiceAccessRoleArn](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-ServiceAccessRoleArn"></a>
The new service access role ARN for the data migration.
Type: String
Required: No

 ** [SourceDataSettings](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-SourceDataSettings"></a>
The new information about the source data provider for the data migration.
Type: Array of [SourceDataSetting](API_SourceDataSetting.md) objects
Required: No

 ** [TargetDataSettings](#API_ModifyDataMigration_RequestSyntax) **   <a name="DMS-ModifyDataMigration-request-TargetDataSettings"></a>
The new information about the target data provider for the data migration.
Type: Array of [TargetDataSetting](API_TargetDataSetting.md) objects
Required: No

## Response Syntax
<a name="API_ModifyDataMigration_ResponseSyntax"></a>

```
{
   "DataMigration": {
      "DataMigrationArn": "string",
      "DataMigrationCidrBlocks": [ "string" ],
      "DataMigrationCreateTime": "string",
      "DataMigrationEndTime": "string",
      "DataMigrationName": "string",
      "DataMigrationSettings": {
         "CloudwatchLogsEnabled": boolean,
         "NumberOfJobs": number,
         "SelectionRules": "string"
      },
      "DataMigrationStartTime": "string",
      "DataMigrationStatistics": {
         "CDCLatency": number,
         "ElapsedTimeMillis": number,
         "FullLoadPercentage": number,
         "StartTime": "string",
         "StopTime": "string",
         "TablesErrored": number,
         "TablesLoaded": number,
         "TablesLoading": number,
         "TablesQueued": number
      },
      "DataMigrationStatus": "string",
      "DataMigrationType": "string",
      "LastFailureMessage": "string",
      "MigrationProjectArn": "string",
      "PublicIpAddresses": [ "string" ],
      "ServiceAccessRoleArn": "string",
      "SourceDataSettings": [
         {
            "CDCStartPosition": "string",
            "CDCStartTime": "string",
            "CDCStopTime": "string",
            "SlotName": "string"
         }
      ],
      "StopReason": "string",
      "TargetDataSettings": [
         {
            "TablePreparationMode": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_ModifyDataMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataMigration](#API_ModifyDataMigration_ResponseSyntax) **   <a name="DMS-ModifyDataMigration-response-DataMigration"></a>
Information about the modified data migration.
Type: [DataMigration](API_DataMigration.md) object

## Errors
<a name="API_ModifyDataMigration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ModifyDataMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyDataMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyDataMigration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
