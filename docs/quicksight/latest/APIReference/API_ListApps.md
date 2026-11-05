---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListApps.html
---

# ListApps
<a name="API_ListApps"></a>

Lists the apps in an AWS account. Results are paginated; use the `NextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListApps_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/apps?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListApps_RequestSyntax) **   <a name="QS-ListApps-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the apps.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListApps_RequestSyntax) **   <a name="QS-ListApps-request-uri-MaxResults"></a>
The maximum number of results to return in a single request. Valid range is 1 to 100. If you don't specify a value, the default is 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListApps_RequestSyntax) **   <a name="QS-ListApps-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Length Constraints: Minimum length of 1. Maximum length of 800.

## Request Body
<a name="API_ListApps_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppSummaryList": [
      {
         "AppId": "string",
         "Arn": "string",
         "CreatedTime": number,
         "LastUpdatedTime": number,
         "Name": "string",
         "Visibility": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppSummaryList](#API_ListApps_ResponseSyntax) **   <a name="QS-ListApps-response-AppSummaryList"></a>
A list of app summaries.
Type: Array of [AppSummary](API_AppSummary.md) objects

 ** [NextToken](#API_ListApps_ResponseSyntax) **   <a name="QS-ListApps-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [RequestId](#API_ListApps_ResponseSyntax) **   <a name="QS-ListApps-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_ListApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameter has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListApps)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListApps)
