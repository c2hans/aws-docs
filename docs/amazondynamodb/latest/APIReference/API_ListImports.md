---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListImports.html
---

# ListImports
<a name="API_ListImports"></a>

 Lists completed imports within the past 90 days.

## Request Syntax
<a name="API_ListImports_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "PageSize": {{number}},
   "TableArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListImports_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [NextToken](#API_ListImports_RequestSyntax) **   <a name="DDB-ListImports-request-NextToken"></a>
 An optional string that, if supplied, must be copied from the output of a previous call to `ListImports`. When provided in this manner, the API fetches the next page of results.
Type: String
Length Constraints: Minimum length of 112. Maximum length of 1024.
Pattern: `([0-9a-f]{16})+`
Required: No

 ** [PageSize](#API_ListImports_RequestSyntax) **   <a name="DDB-ListImports-request-PageSize"></a>
 The number of `ImportSummary `objects returned in a single page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [TableArn](#API_ListImports_RequestSyntax) **   <a name="DDB-ListImports-request-TableArn"></a>
 The Amazon Resource Name (ARN) associated with the table that was imported to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListImports_ResponseSyntax"></a>

```
{
   "ImportSummaryList": [
      {
         "CloudWatchLogGroupArn": "string",
         "EndTime": number,
         "ImportArn": "string",
         "ImportStatus": "string",
         "InputFormat": "string",
         "S3BucketSource": {
            "S3Bucket": "string",
            "S3BucketOwner": "string",
            "S3KeyPrefix": "string"
         },
         "StartTime": number,
         "TableArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListImports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportSummaryList](#API_ListImports_ResponseSyntax) **   <a name="DDB-ListImports-response-ImportSummaryList"></a>
 A list of `ImportSummary` objects.
Type: Array of [ImportSummary](API_ImportSummary.md) objects

 ** [NextToken](#API_ListImports_ResponseSyntax) **   <a name="DDB-ListImports-response-NextToken"></a>
 If this value is returned, there are additional results to be displayed. To retrieve them, call `ListImports` again, with `NextToken` set to this value.
Type: String
Length Constraints: Minimum length of 112. Maximum length of 1024.
Pattern: `([0-9a-f]{16})+`

## Errors
<a name="API_ListImports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
There is no limit to the number of daily on-demand backups that can be taken.
For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include `CreateTable`, `UpdateTable`, `DeleteTable`,`UpdateTimeToLive`, `RestoreTableFromBackup`, and `RestoreTableToPointInTime`.
When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.
When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.
There is a soft account quota of 2,500 tables.
GetRecords was called with a value of more than 1000 for the limit request parameter.
More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.
 ** message **
Too many operations for a given subscriber.
HTTP Status Code: 400

## See Also
<a name="API_ListImports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ListImports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ListImports)
