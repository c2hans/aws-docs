---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchApps.html
---

# SearchApps
<a name="API_SearchApps"></a>

Searches for apps in an AWS account using the specified filters. This operation is eventually consistent; the results might not reflect very recent updates. Results are paginated; use the `NextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_SearchApps_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/apps HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchApps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchApps_RequestSyntax) **   <a name="QS-SearchApps-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the apps to search.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_SearchApps_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchApps_RequestSyntax) **   <a name="QS-SearchApps-request-Filters"></a>
The filters to apply to the search.
Type: Array of [SearchAppsFilter](API_SearchAppsFilter.md) objects
Required: Yes

 ** [MaxResults](#API_SearchApps_RequestSyntax) **   <a name="QS-SearchApps-request-MaxResults"></a>
The maximum number of results to return in a single request. Valid range is 1 to 100. If you don't specify a value, the default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchApps_RequestSyntax) **   <a name="QS-SearchApps-request-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.
Required: No

## Response Syntax
<a name="API_SearchApps_ResponseSyntax"></a>

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
<a name="API_SearchApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppSummaryList](#API_SearchApps_ResponseSyntax) **   <a name="QS-SearchApps-response-AppSummaryList"></a>
A list of app summaries that match the search criteria.
Type: Array of [AppSummary](API_AppSummary.md) objects

 ** [NextToken](#API_SearchApps_ResponseSyntax) **   <a name="QS-SearchApps-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [RequestId](#API_SearchApps_ResponseSyntax) **   <a name="QS-SearchApps-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_SearchApps_Errors"></a>

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
<a name="API_SearchApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchApps)
