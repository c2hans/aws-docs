---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetachThingPrincipal.html
---

# DetachThingPrincipal
<a name="API_DetachThingPrincipal"></a>

Detaches the specified principal from the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.

**Note**
This call is asynchronous. It might take several seconds for the detachment to propagate.

Requires permission to access the [DetachThingPrincipal](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DetachThingPrincipal_RequestSyntax"></a>

```
DELETE /things/{{thingName}}/principals HTTP/1.1
x-amzn-principal: {{principal}}
```

## URI Request Parameters
<a name="API_DetachThingPrincipal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [principal](#API_DetachThingPrincipal_RequestSyntax) **   <a name="iot-DetachThingPrincipal-request-principal"></a>
If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
Required: Yes

 ** [thingName](#API_DetachThingPrincipal_RequestSyntax) **   <a name="iot-DetachThingPrincipal-request-uri-thingName"></a>
The name of the thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DetachThingPrincipal_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DetachThingPrincipal_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DetachThingPrincipal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DetachThingPrincipal_Errors"></a>

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
<a name="API_DetachThingPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DetachThingPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetachThingPrincipal)
