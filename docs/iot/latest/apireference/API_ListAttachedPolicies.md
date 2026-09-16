---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListAttachedPolicies.html
---

# ListAttachedPolicies
<a name="API_ListAttachedPolicies"></a>

Lists the policies attached to the specified thing group.

Requires permission to access the [ListAttachedPolicies](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListAttachedPolicies_RequestSyntax"></a>

```
POST /attached-policies/{{target}}?marker={{marker}}&pageSize={{pageSize}}&recursive={{recursive}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAttachedPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [marker](#API_ListAttachedPolicies_RequestSyntax) **   <a name="iot-ListAttachedPolicies-request-uri-marker"></a>
The token to retrieve the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListAttachedPolicies_RequestSyntax) **   <a name="iot-ListAttachedPolicies-request-uri-pageSize"></a>
The maximum number of results to be returned per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [recursive](#API_ListAttachedPolicies_RequestSyntax) **   <a name="iot-ListAttachedPolicies-request-uri-recursive"></a>
When true, recursively list attached policies.

 ** [target](#API_ListAttachedPolicies_RequestSyntax) **   <a name="iot-ListAttachedPolicies-request-uri-target"></a>
The group or principal for which the policies will be listed. Valid principals are CertificateArn (arn:aws:iot:*region*:*accountId*:cert/*certificateId*), thingGroupArn (arn:aws:iot:*region*:*accountId*:thinggroup/*groupName*) and CognitoId (*region*:*id*).
Required: Yes

## Request Body
<a name="API_ListAttachedPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAttachedPolicies_ResponseSyntax"></a>

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
<a name="API_ListAttachedPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextMarker](#API_ListAttachedPolicies_ResponseSyntax) **   <a name="iot-ListAttachedPolicies-response-nextMarker"></a>
The token to retrieve the next set of results, or ``null`` if there are no more results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [policies](#API_ListAttachedPolicies_ResponseSyntax) **   <a name="iot-ListAttachedPolicies-response-policies"></a>
The policies.
Type: Array of [Policy](API_Policy.md) objects

## Errors
<a name="API_ListAttachedPolicies_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

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
<a name="API_ListAttachedPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListAttachedPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListAttachedPolicies)
