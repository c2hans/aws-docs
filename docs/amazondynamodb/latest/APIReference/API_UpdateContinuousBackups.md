---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContinuousBackups.html
---

# UpdateContinuousBackups
<a name="API_UpdateContinuousBackups"></a>

 `UpdateContinuousBackups` enables or disables point in time recovery for the specified table. A successful `UpdateContinuousBackups` call returns the current `ContinuousBackupsDescription`. Continuous backups are `ENABLED` on all tables at table creation. If point in time recovery is enabled, `PointInTimeRecoveryStatus` will be set to ENABLED.

 Once continuous backups and point in time recovery are enabled, you can restore to any point in time within `EarliestRestorableDateTime` and `LatestRestorableDateTime`.

 `LatestRestorableDateTime` is typically 5 minutes before the current time. You can restore your table to any point in time in the last 35 days. You can set the `RecoveryPeriodInDays` to any value between 1 and 35 days.

## Request Syntax
<a name="API_UpdateContinuousBackups_RequestSyntax"></a>

```
{
   "PointInTimeRecoverySpecification": {
      "PointInTimeRecoveryEnabled": {{boolean}},
      "RecoveryPeriodInDays": {{number}}
   },
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateContinuousBackups_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [PointInTimeRecoverySpecification](#API_UpdateContinuousBackups_RequestSyntax) **   <a name="DDB-UpdateContinuousBackups-request-PointInTimeRecoverySpecification"></a>
Represents the settings used to enable point in time recovery.
Type: [PointInTimeRecoverySpecification](API_PointInTimeRecoverySpecification.md) object
Required: Yes

 ** [TableName](#API_UpdateContinuousBackups_RequestSyntax) **   <a name="DDB-UpdateContinuousBackups-request-TableName"></a>
The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_UpdateContinuousBackups_ResponseSyntax"></a>

```
{
   "ContinuousBackupsDescription": {
      "ContinuousBackupsStatus": "string",
      "PointInTimeRecoveryDescription": {
         "EarliestRestorableDateTime": number,
         "LatestRestorableDateTime": number,
         "PointInTimeRecoveryStatus": "string",
         "RecoveryPeriodInDays": number
      }
   }
}
```

## Response Elements
<a name="API_UpdateContinuousBackups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContinuousBackupsDescription](#API_UpdateContinuousBackups_ResponseSyntax) **   <a name="DDB-UpdateContinuousBackups-response-ContinuousBackupsDescription"></a>
Represents the continuous backups and point in time recovery settings on the table.
Type: [ContinuousBackupsDescription](API_ContinuousBackupsDescription.md) object

## Errors
<a name="API_UpdateContinuousBackups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ContinuousBackupsUnavailableException **
Backups have not yet been enabled for this table.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** TableNotFoundException **
A source table with the name `TableName` does not currently exist within the subscriber's account or the subscriber is operating in the wrong AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_UpdateContinuousBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UpdateContinuousBackups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateContinuousBackups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
