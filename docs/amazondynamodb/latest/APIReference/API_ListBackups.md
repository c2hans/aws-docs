---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html
---

# ListBackups
<a name="API_ListBackups"></a>

List DynamoDB backups that are associated with an AWS account and weren't made with AWS Backup. To list these backups for a given table, specify `TableName`. `ListBackups` returns a paginated list of results with at most 1 MB worth of items in a page. You can also specify a maximum number of entries to be returned in a page.

In the request, start time is inclusive, but end time is exclusive. Note that these boundaries are for the time at which the original backup was requested.

You can call `ListBackups` a maximum of five times per second.

If you want to retrieve the complete list of backups made with AWS Backup, use the [AWS Backup list API.](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobs.html)

## Request Syntax
<a name="API_ListBackups_RequestSyntax"></a>

```
{
   "BackupType": "{{string}}",
   "ExclusiveStartBackupArn": "{{string}}",
   "Limit": {{number}},
   "TableName": "{{string}}",
   "TimeRangeLowerBound": {{number}},
   "TimeRangeUpperBound": {{number}}
}
```

## Request Parameters
<a name="API_ListBackups_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BackupType](#API_ListBackups_RequestSyntax) **   <a name="DDB-ListBackups-request-BackupType"></a>
The backups from the table specified by `BackupType` are listed.
Where `BackupType` can be:
+  `USER` - On-demand backup created by you. (The default setting if no other backup types are specified.)
+  `SYSTEM` - On-demand backup automatically created by DynamoDB.
+  `ALL` - All types of on-demand backups (USER and SYSTEM).
Type: String
Valid Values: `USER | SYSTEM | AWS_BACKUP | ALL`
Required: No

 ** [ExclusiveStartBackupArn](#API_ListBackups_RequestSyntax) **   <a name="DDB-ListBackups-request-ExclusiveStartBackupArn"></a>
 `LastEvaluatedBackupArn` is the Amazon Resource Name (ARN) of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the `ExclusiveStartBackupArn` of a new `ListBackups` operation in order to fetch the next page of results.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** [Limit](#API_ListBackups_RequestSyntax) **   <a name="DDB-ListBackups-request-Limit"></a>
Maximum number of backups to return at once.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [TableName](#API_ListBackups_RequestSyntax) **   <a name="DDB-ListBackups-request-TableName"></a>
Lists the backups from the table specified in `TableName`. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [TimeRangeLowerBound](#API_ListBackups_RequestSyntax) **   <a name="DDB-ListBackups-request-TimeRangeLowerBound"></a>
Only backups created after this time are listed. `TimeRangeLowerBound` is inclusive.
Type: Timestamp
Required: No

 ** [TimeRangeUpperBound](#API_ListBackups_RequestSyntax) **   <a name="DDB-ListBackups-request-TimeRangeUpperBound"></a>
Only backups created before this time are listed. `TimeRangeUpperBound` is exclusive.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListBackups_ResponseSyntax"></a>

```
{
   "BackupSummaries": [
      {
         "BackupArn": "string",
         "BackupCreationDateTime": number,
         "BackupExpiryDateTime": number,
         "BackupName": "string",
         "BackupSizeBytes": number,
         "BackupStatus": "string",
         "BackupType": "string",
         "TableArn": "string",
         "TableId": "string",
         "TableName": "string"
      }
   ],
   "LastEvaluatedBackupArn": "string"
}
```

## Response Elements
<a name="API_ListBackups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupSummaries](#API_ListBackups_ResponseSyntax) **   <a name="DDB-ListBackups-response-BackupSummaries"></a>
List of `BackupSummary` objects.
Type: Array of [BackupSummary](API_BackupSummary.md) objects

 ** [LastEvaluatedBackupArn](#API_ListBackups_ResponseSyntax) **   <a name="DDB-ListBackups-response-LastEvaluatedBackupArn"></a>
 The ARN of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the `ExclusiveStartBackupArn` of a new `ListBackups` operation in order to fetch the next page of results.
 If `LastEvaluatedBackupArn` is empty, then the last page of results has been processed and there are no more results to be retrieved.
 If `LastEvaluatedBackupArn` is not empty, this may or may not indicate that there is more data to be returned. All results are guaranteed to have been returned if and only if no value for `LastEvaluatedBackupArn` is returned.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.

## Errors
<a name="API_ListBackups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

## See Also
<a name="API_ListBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ListBackups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ListBackups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
