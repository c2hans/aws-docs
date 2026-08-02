---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ListScheduledQueries.html
---

# ListScheduledQueries
<a name="API_query_ListScheduledQueries"></a>

Gets a list of all scheduled queries in the caller's Amazon account and Region. `ListScheduledQueries` is eventually consistent.

## Request Syntax
<a name="API_query_ListScheduledQueries_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_query_ListScheduledQueries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_query_ListScheduledQueries_RequestSyntax) **   <a name="timestream-query_ListScheduledQueries-request-MaxResults"></a>
The maximum number of items to return in the output. If the total number of items available is more than the value specified, a `NextToken` is provided in the output. To resume pagination, provide the `NextToken` value as the argument to the subsequent call to `ListScheduledQueriesRequest`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_query_ListScheduledQueries_RequestSyntax) **   <a name="timestream-query_ListScheduledQueries-request-NextToken"></a>
 A pagination token to resume pagination.
Type: String
Required: No

## Response Syntax
<a name="API_query_ListScheduledQueries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ScheduledQueries": [
      {
         "Arn": "string",
         "CreationTime": number,
         "ErrorReportConfiguration": {
            "S3Configuration": {
               "BucketName": "string",
               "EncryptionOption": "string",
               "ObjectKeyPrefix": "string"
            }
         },
         "LastRunStatus": "string",
         "Name": "string",
         "NextInvocationTime": number,
         "PreviousInvocationTime": number,
         "State": "string",
         "TargetDestination": {
            "TimestreamDestination": {
               "DatabaseName": "string",
               "TableName": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_query_ListScheduledQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_query_ListScheduledQueries_ResponseSyntax) **   <a name="timestream-query_ListScheduledQueries-response-NextToken"></a>
A token to specify where to start paginating. This is the NextToken from a previously truncated response.
Type: String

 ** [ScheduledQueries](#API_query_ListScheduledQueries_ResponseSyntax) **   <a name="timestream-query_ListScheduledQueries-response-ScheduledQueries"></a>
A list of scheduled queries.
Type: Array of [ScheduledQuery](API_query_ScheduledQuery.md) objects

## Errors
<a name="API_query_ListScheduledQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the necessary permissions to access the account settings.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_query_ListScheduledQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/ListScheduledQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ListScheduledQueries)
