---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBulkOperations.html
---

# ListBulkOperations
<a name="API_ListBulkOperations"></a>

Lists bulk operations that started within the past 90 days for the current AWS account and AWS Region, with the most recent operations first. Results are paginated. Use the `NextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListBulkOperations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBulkOperations_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [MaxResults](#API_ListBulkOperations_RequestSyntax) **   <a name="DDB-ListBulkOperations-request-MaxResults"></a>
The maximum number of bulk operation summaries to return in one page. If you don't specify a value, DynamoDB uses 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListBulkOperations_RequestSyntax) **   <a name="DDB-ListBulkOperations-request-NextToken"></a>
An optional string that, if supplied, must be copied from the output of a previous call to `ListBulkOperations`. When provided in this manner, the API fetches the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([0-9a-f]{16})+`
Required: No

## Response Syntax
<a name="API_ListBulkOperations_ResponseSyntax"></a>

```
{
   "BulkOperationsSummaryList": [
      {
         "BulkOperationArn": "string",
         "BulkOperationStatus": "string",
         "EndTime": number,
         "StartTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBulkOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BulkOperationsSummaryList](#API_ListBulkOperations_ResponseSyntax) **   <a name="DDB-ListBulkOperations-response-BulkOperationsSummaryList"></a>
A list of bulk operation summaries for the current AWS account and AWS Region.
Type: Array of [BulkOperationSummary](API_BulkOperationSummary.md) objects

 ** [NextToken](#API_ListBulkOperations_ResponseSyntax) **   <a name="DDB-ListBulkOperations-response-NextToken"></a>
If this value is returned, there are additional results to be displayed. To retrieve them, call `ListBulkOperations` again, with `NextToken` set to this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([0-9a-f]{16})+`

## Errors
<a name="API_ListBulkOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListBulkOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ListBulkOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ListBulkOperations)
