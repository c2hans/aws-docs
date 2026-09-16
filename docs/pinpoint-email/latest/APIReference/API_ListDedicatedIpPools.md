---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDedicatedIpPools.html
---

# ListDedicatedIpPools
<a name="API_ListDedicatedIpPools"></a>

List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.

## Request Syntax
<a name="API_ListDedicatedIpPools_RequestSyntax"></a>

```
GET /v1/email/dedicated-ip-pools?NextToken={{NextToken}}&PageSize={{PageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDedicatedIpPools_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_ListDedicatedIpPools_RequestSyntax) **   <a name="pinpoint-ListDedicatedIpPools-request-uri-NextToken"></a>
A token returned from a previous call to `ListDedicatedIpPools` to indicate the position in the list of dedicated IP pools.

 ** [PageSize](#API_ListDedicatedIpPools_RequestSyntax) **   <a name="pinpoint-ListDedicatedIpPools-request-uri-PageSize"></a>
The number of results to show in a single call to `ListDedicatedIpPools`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.

## Request Body
<a name="API_ListDedicatedIpPools_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDedicatedIpPools_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DedicatedIpPools": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDedicatedIpPools_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DedicatedIpPools](#API_ListDedicatedIpPools_ResponseSyntax) **   <a name="pinpoint-ListDedicatedIpPools-response-DedicatedIpPools"></a>
A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint account.
Type: Array of strings

 ** [NextToken](#API_ListDedicatedIpPools_ResponseSyntax) **   <a name="pinpoint-ListDedicatedIpPools-response-NextToken"></a>
A token that indicates that there are additional IP pools to list. To view additional IP pools, issue another request to `ListDedicatedIpPools`, passing this token in the `NextToken` parameter.
Type: String

## Errors
<a name="API_ListDedicatedIpPools_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_ListDedicatedIpPools_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/ListDedicatedIpPools)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/ListDedicatedIpPools)
