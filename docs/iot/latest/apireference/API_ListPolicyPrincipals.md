---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicyPrincipals.html
---

# ListPolicyPrincipals
<a name="API_ListPolicyPrincipals"></a>

Lists the principals associated with the specified policy.

 **Note:** This action is deprecated and works as expected for backward compatibility, but we won't add enhancements. Use [ListTargetsForPolicy](API_ListTargetsForPolicy.md) instead.

Requires permission to access the [ListPolicyPrincipals](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListPolicyPrincipals_RequestSyntax"></a>

```
GET /policy-principals?isAscendingOrder={{ascendingOrder}}&marker={{marker}}&pageSize={{pageSize}} HTTP/1.1
x-amzn-iot-policy: {{policyName}}
```

## URI Request Parameters
<a name="API_ListPolicyPrincipals_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ascendingOrder](#API_ListPolicyPrincipals_RequestSyntax) **   <a name="iot-ListPolicyPrincipals-request-uri-ascendingOrder"></a>
Specifies the order for results. If true, the results are returned in ascending creation order.

 ** [marker](#API_ListPolicyPrincipals_RequestSyntax) **   <a name="iot-ListPolicyPrincipals-request-uri-marker"></a>
The marker for the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListPolicyPrincipals_RequestSyntax) **   <a name="iot-ListPolicyPrincipals-request-uri-pageSize"></a>
The result page size.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [policyName](#API_ListPolicyPrincipals_RequestSyntax) **   <a name="iot-ListPolicyPrincipals-request-policyName"></a>
The policy name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Request Body
<a name="API_ListPolicyPrincipals_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPolicyPrincipals_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextMarker": "string",
   "principals": [ "string" ]
}
```

## Response Elements
<a name="API_ListPolicyPrincipals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextMarker](#API_ListPolicyPrincipals_ResponseSyntax) **   <a name="iot-ListPolicyPrincipals-response-nextMarker"></a>
The marker for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [principals](#API_ListPolicyPrincipals_ResponseSyntax) **   <a name="iot-ListPolicyPrincipals-response-principals"></a>
The descriptions of the principals.
Type: Array of strings

## Errors
<a name="API_ListPolicyPrincipals_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_ListPolicyPrincipals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListPolicyPrincipals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListPolicyPrincipals)
