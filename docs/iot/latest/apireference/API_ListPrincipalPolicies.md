---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalPolicies.html
---

# ListPrincipalPolicies
<a name="API_ListPrincipalPolicies"></a>

Lists the policies attached to the specified principal. If you use an Cognito identity, the ID must be in [AmazonCognito Identity format](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html#API_GetCredentialsForIdentity_RequestSyntax).

 **Note:** This action is deprecated and works as expected for backward compatibility, but we won't add enhancements. Use [ListAttachedPolicies](API_ListAttachedPolicies.md) instead.

Requires permission to access the [ListPrincipalPolicies](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListPrincipalPolicies_RequestSyntax"></a>

```
GET /principal-policies?isAscendingOrder={{ascendingOrder}}&marker={{marker}}&pageSize={{pageSize}} HTTP/1.1
x-amzn-iot-principal: {{principal}}
```

## URI Request Parameters
<a name="API_ListPrincipalPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ascendingOrder](#API_ListPrincipalPolicies_RequestSyntax) **   <a name="iot-ListPrincipalPolicies-request-uri-ascendingOrder"></a>
Specifies the order for results. If true, results are returned in ascending creation order.

 ** [marker](#API_ListPrincipalPolicies_RequestSyntax) **   <a name="iot-ListPrincipalPolicies-request-uri-marker"></a>
The marker for the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListPrincipalPolicies_RequestSyntax) **   <a name="iot-ListPrincipalPolicies-request-uri-pageSize"></a>
The result page size.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [principal](#API_ListPrincipalPolicies_RequestSyntax) **   <a name="iot-ListPrincipalPolicies-request-principal"></a>
The principal. Valid principals are CertificateArn (arn:aws:iot:*region*:*accountId*:cert/*certificateId*), thingGroupArn (arn:aws:iot:*region*:*accountId*:thinggroup/*groupName*) and CognitoId (*region*:*id*).
Required: Yes

## Request Body
<a name="API_ListPrincipalPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPrincipalPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextMarker": "string",
   "policies": [
      {
         "policyArn": "string",
         "policyName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPrincipalPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextMarker](#API_ListPrincipalPolicies_ResponseSyntax) **   <a name="iot-ListPrincipalPolicies-response-nextMarker"></a>
The marker for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [policies](#API_ListPrincipalPolicies_ResponseSyntax) **   <a name="iot-ListPrincipalPolicies-response-policies"></a>
The policies.
Type: Array of [Policy](API_Policy.md) objects

## Errors
<a name="API_ListPrincipalPolicies_Errors"></a>

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
<a name="API_ListPrincipalPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListPrincipalPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListPrincipalPolicies)
