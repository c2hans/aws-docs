---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListServiceViews.html
---

# ListServiceViews
<a name="API_ListServiceViews"></a>

Lists all Resource Explorer service views available in the current AWS account. This operation returns the ARNs of available service views.

## Request Syntax
<a name="API_ListServiceViews_RequestSyntax"></a>

```
POST /ListServiceViews HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListServiceViews_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListServiceViews_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListServiceViews_RequestSyntax) **   <a name="resourceexplorer-ListServiceViews-request-MaxResults"></a>
The maximum number of service view results to return in a single response. Valid values are between `1` and `50`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListServiceViews_RequestSyntax) **   <a name="resourceexplorer-ListServiceViews-request-NextToken"></a>
The pagination token from a previous `ListServiceViews` response. Use this token to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListServiceViews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ServiceViews": [ "string" ]
}
```

## Response Elements
<a name="API_ListServiceViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListServiceViews_ResponseSyntax) **   <a name="resourceexplorer-ListServiceViews-response-NextToken"></a>
The pagination token to use in a subsequent `ListServiceViews` request to retrieve the next set of results.
Type: String

 ** [ServiceViews](#API_ListServiceViews_ResponseSyntax) **   <a name="resourceexplorer-ListServiceViews-response-ServiceViews"></a>
A list of Amazon Resource Names (ARNs) for the service views available in the current AWS account.
Type: Array of strings

## Errors
<a name="API_ListServiceViews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListServiceViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListServiceViews)
