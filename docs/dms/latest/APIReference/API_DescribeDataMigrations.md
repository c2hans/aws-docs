---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeDataMigrations.html
---

# DescribeDataMigrations
<a name="API_DescribeDataMigrations"></a>

Returns information about data migrations.

## Request Syntax
<a name="API_DescribeDataMigrations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "WithoutSettings": {{boolean}},
   "WithoutStatistics": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeDataMigrations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeDataMigrations_RequestSyntax) **   <a name="DMS-DescribeDataMigrations-request-Filters"></a>
Filters applied to the data migrations.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeDataMigrations_RequestSyntax) **   <a name="DMS-DescribeDataMigrations-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [MaxRecords](#API_DescribeDataMigrations_RequestSyntax) **   <a name="DMS-DescribeDataMigrations-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [WithoutSettings](#API_DescribeDataMigrations_RequestSyntax) **   <a name="DMS-DescribeDataMigrations-request-WithoutSettings"></a>
An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose `true`; otherwise, choose `false` (the default).
Type: Boolean
Required: No

 ** [WithoutStatistics](#API_DescribeDataMigrations_RequestSyntax) **   <a name="DMS-DescribeDataMigrations-request-WithoutStatistics"></a>
An option to set to avoid returning information about statistics. Use this to reduce overhead when statistics information is too large. To use this option, choose `true`; otherwise, choose `false` (the default).
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeDataMigrations_ResponseSyntax"></a>

```
{
   "DataMigrations": [
      {
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
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeDataMigrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataMigrations](#API_DescribeDataMigrations_ResponseSyntax) **   <a name="DMS-DescribeDataMigrations-response-DataMigrations"></a>
Returns information about the data migrations used in the project.
Type: Array of [DataMigration](API_DataMigration.md) objects

 ** [Marker](#API_DescribeDataMigrations_ResponseSyntax) **   <a name="DMS-DescribeDataMigrations-response-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Maximum length of 1024.

## Errors
<a name="API_DescribeDataMigrations_Errors"></a>

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
<a name="API_DescribeDataMigrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeDataMigrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeDataMigrations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
