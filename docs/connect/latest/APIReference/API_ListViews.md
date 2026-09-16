---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListViews.html
---

# ListViews
<a name="API_ListViews"></a>

Returns views in the given instance.

Results are sorted primarily by type, and secondarily by name.

## Request Syntax
<a name="API_ListViews_RequestSyntax"></a>

```
GET /views/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&type={{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListViews_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListViews_RequestSyntax) **   <a name="connect-ListViews-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\_\-:\/]+$`
Required: Yes

 ** [MaxResults](#API_ListViews_RequestSyntax) **   <a name="connect-ListViews-request-uri-MaxResults"></a>
The maximum number of results to return per page. The default MaxResult size is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListViews_RequestSyntax) **   <a name="connect-ListViews-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[a-zA-Z0-9=\/+_.-]+$`

 ** [Type](#API_ListViews_RequestSyntax) **   <a name="connect-ListViews-request-uri-Type"></a>
The type of the view.
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`

## Request Body
<a name="API_ListViews_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListViews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ViewsSummaryList": [
      {
         "Arn": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "Status": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListViews_ResponseSyntax) **   <a name="connect-ListViews-response-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^[a-zA-Z0-9=\/+_.-]+$`

 ** [ViewsSummaryList](#API_ListViews_ResponseSyntax) **   <a name="connect-ListViews-response-ViewsSummaryList"></a>
A list of view summaries.
Type: Array of [ViewSummary](API_ViewSummary.md) objects

## Errors
<a name="API_ListViews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** TooManyRequestsException **
Displayed when rate-related API limits are exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListViews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListViews)
