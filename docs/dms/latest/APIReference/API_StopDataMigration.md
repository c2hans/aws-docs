---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StopDataMigration.html
---

# StopDataMigration
<a name="API_StopDataMigration"></a>

Stops the specified data migration.

## Request Syntax
<a name="API_StopDataMigration_RequestSyntax"></a>

```
{
   "DataMigrationIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_StopDataMigration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataMigrationIdentifier](#API_StopDataMigration_RequestSyntax) **   <a name="DMS-StopDataMigration-request-DataMigrationIdentifier"></a>
The identifier (name or ARN) of the data migration to stop.
Type: String
Required: Yes

## Response Syntax
<a name="API_StopDataMigration_ResponseSyntax"></a>

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
<a name="API_StopDataMigration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataMigration](#API_StopDataMigration_ResponseSyntax) **   <a name="DMS-StopDataMigration-response-DataMigration"></a>
The data migration that DMS stopped.
Type: [DataMigration](API_DataMigration.md) object

## Errors
<a name="API_StopDataMigration_Errors"></a>

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
<a name="API_StopDataMigration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StopDataMigration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StopDataMigration)
