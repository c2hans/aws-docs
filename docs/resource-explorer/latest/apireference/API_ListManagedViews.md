---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListManagedViews.html
---

# ListManagedViews
<a name="API_ListManagedViews"></a>

Lists the Amazon resource names (ARNs) of the [AWS-managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html) available in the AWS Region in which you call this operation.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:ListManagedViews`

   **Resource**: The ARN of the specified view.

## Request Syntax
<a name="API_ListManagedViews_RequestSyntax"></a>

```
POST /ListManagedViews HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServicePrincipal": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListManagedViews_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListManagedViews_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListManagedViews_RequestSyntax) **   <a name="resourceexplorer-ListManagedViews-request-MaxResults"></a>
The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListManagedViews_RequestSyntax) **   <a name="resourceexplorer-ListManagedViews-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ServicePrincipal](#API_ListManagedViews_RequestSyntax) **   <a name="resourceexplorer-ListManagedViews-request-ServicePrincipal"></a>
Specifies a service principal name. If specified, then the operation only returns the managed views that are managed by the input service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListManagedViews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ManagedViews": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedViews](#API_ListManagedViews_ResponseSyntax) **   <a name="resourceexplorer-ListManagedViews-response-ManagedViews"></a>
The list of managed views available in the AWS Region in which you called this operation.
Type: Array of strings

 ** [NextToken](#API_ListManagedViews_ResponseSyntax) **   <a name="resourceexplorer-ListManagedViews-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String

## Errors
<a name="API_ListManagedViews_Errors"></a>

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

 ** UnauthorizedException **
The principal making the request isn't permitted to perform the operation.
HTTP Status Code: 401

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_ListManagedViews_Examples"></a>

### Example
<a name="API_ListManagedViews_Example_1"></a>

The following example shows the call response listing available managed views.

#### Sample Request
<a name="API_ListManagedViews_Example_1_Request"></a>

```
POST /ListManagedViews HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
    // optional field, if not provided a default value 50 will be used.
    "MaxResults": 5,

    // this is next token from previous call in order to get the next page, if not provided, just get the first page results.
    "NextToken": "AQICAHi3bTZbEXAMPLE..._fzaYt0J8jB4oUnWMgimJHA",

    // optional field, if not provided, API will try to iterate all managed views created by all services. If specified, the API only tries to retry managed views created/managed by the input service.
    "ServicePrincipal": "sampleservice.amazonaws.com"
}
```

#### Sample Response
<a name="API_ListManagedViews_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
  "ManagedViews": [
    "arn:aws:resource-explorer-2:us-east-1:111122223333:managed-view/ManagedViewNameA/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "arn:aws:resource-explorer-2:us-east-1:444455556666:managed-view/ManagedViewNameB/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222"
  ]
}
```

## See Also
<a name="API_ListManagedViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListManagedViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListManagedViews)
