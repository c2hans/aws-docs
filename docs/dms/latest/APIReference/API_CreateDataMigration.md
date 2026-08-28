---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateDataMigration.html
---

# CreateDataMigration
<a name="API_CreateDataMigration"></a>

Creates a data migration using the provided settings.

## Request Syntax
<a name="API_CreateDataMigration_RequestSyntax"></a>

```
{
   "DataMigrationName": "{{string}}",
   "DataMigrationType": "{{string}}",
   "EnableCloudwatchLogs": {{boolean}},
   "MigrationProjectIdentifier": "{{string}}",
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
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
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
<a name="API_CreateDataMigration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataMigrationName](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-DataMigrationName"></a>
A user-friendly name for the data migration. Data migration names have the following constraints:
+ Must begin with a letter, and can only contain ASCII letters, digits, and hyphens.
+ Can't end with a hyphen or contain two consecutive hyphens.
+ Length must be from 1 to 255 characters.
Type: String
Required: No

 ** [DataMigrationType](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-DataMigrationType"></a>
Specifies if the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: Yes

 ** [EnableCloudwatchLogs](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-EnableCloudwatchLogs"></a>
Specifies whether to enable CloudWatch logs for the data migration.
Type: Boolean
Required: No

 ** [MigrationProjectIdentifier](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-MigrationProjectIdentifier"></a>
An identifier for the migration project.
Type: String
Required: Yes

 ** [NumberOfJobs](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-NumberOfJobs"></a>
The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.
Type: Integer
Required: No

 ** [SelectionRules](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-SelectionRules"></a>
An optional JSON string specifying what tables, views, and schemas to include or exclude from the migration.
Type: String
Required: No

 ** [ServiceAccessRoleArn](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) for the service access role that you want to use to create the data migration.
Type: String
Required: Yes

 ** [SourceDataSettings](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-SourceDataSettings"></a>
Specifies information about the source data provider.
Type: Array of [SourceDataSetting](API_SourceDataSetting.md) objects
Required: No

 ** [Tags](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-Tags"></a>
One or more tags to be assigned to the data migration.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TargetDataSettings](#API_CreateDataMigration_RequestSyntax) **   <a name="DMS-CreateDataMigration-request-TargetDataSettings"></a>
Specifies information about the target data provider.
Type: Array of [TargetDataSetting](API_TargetDataSetting.md) objects
Required: No

## Response Syntax
<a name="API_CreateDataMigration_ResponseSyntax"></a>

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
<a name="API_CreateDataMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataMigration](#API_CreateDataMigration_ResponseSyntax) **   <a name="DMS-CreateDataMigration-response-DataMigration"></a>
Information about the created data migration.
Type: [DataMigration](API_DataMigration.md) object

## Errors
<a name="API_CreateDataMigration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FailedDependencyFault **
A dependency threw an exception.
HTTP Status Code: 400

 ** InvalidOperationFault **
The action or operation requested isn't valid.
HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_CreateDataMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateDataMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateDataMigration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
