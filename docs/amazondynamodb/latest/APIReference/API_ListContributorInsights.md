---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListContributorInsights.html
---

# ListContributorInsights
<a name="API_ListContributorInsights"></a>

Returns a list of ContributorInsightsSummary for a table and all its global secondary indexes.

## Request Syntax
<a name="API_ListContributorInsights_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListContributorInsights_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [MaxResults](#API_ListContributorInsights_RequestSyntax) **   <a name="DDB-ListContributorInsights-request-MaxResults"></a>
Maximum number of results to return per page.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [NextToken](#API_ListContributorInsights_RequestSyntax) **   <a name="DDB-ListContributorInsights-request-NextToken"></a>
A token to for the desired page, if there is one.
Type: String
Required: No

 ** [TableName](#API_ListContributorInsights_RequestSyntax) **   <a name="DDB-ListContributorInsights-request-TableName"></a>
The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListContributorInsights_ResponseSyntax"></a>

```
{
   "ContributorInsightsSummaries": [
      {
         "ContributorInsightsMode": "string",
         "ContributorInsightsStatus": "string",
         "IndexName": "string",
         "TableName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContributorInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContributorInsightsSummaries](#API_ListContributorInsights_ResponseSyntax) **   <a name="DDB-ListContributorInsights-response-ContributorInsightsSummaries"></a>
A list of ContributorInsightsSummary.
Type: Array of [ContributorInsightsSummary](API_ContributorInsightsSummary.md) objects

 ** [NextToken](#API_ListContributorInsights_ResponseSyntax) **   <a name="DDB-ListContributorInsights-response-NextToken"></a>
A token to go to the next page if there is one.
Type: String

## Errors
<a name="API_ListContributorInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ListContributorInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ListContributorInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ListContributorInsights)
