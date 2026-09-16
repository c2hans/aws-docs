---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeregisterGatewayInstance.html
---

# DeregisterGatewayInstance
<a name="API_DeregisterGatewayInstance"></a>

 Deregisters an instance. Before you deregister an instance, all bridges running on the instance must be stopped. If you want to deregister an instance without stopping the bridges, you must use the --force option.

## Request Syntax
<a name="API_DeregisterGatewayInstance_RequestSyntax"></a>

```
DELETE /v1/gateway-instances/{{gatewayInstanceArn}}?force={{force}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeregisterGatewayInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [force](#API_DeregisterGatewayInstance_RequestSyntax) **   <a name="mediaconnect-DeregisterGatewayInstance-request-uri-force"></a>
 Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.

 ** [gatewayInstanceArn](#API_DeregisterGatewayInstance_RequestSyntax) **   <a name="mediaconnect-DeregisterGatewayInstance-request-uri-gatewayInstanceArn"></a>
 The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.
Pattern: `arn:.+:mediaconnect.+:gateway:.+:instance:.+`
Required: Yes

## Request Body
<a name="API_DeregisterGatewayInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeregisterGatewayInstance_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "gatewayInstanceArn": "string",
   "instanceState": "string"
}
```

## Response Elements
<a name="API_DeregisterGatewayInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [gatewayInstanceArn](#API_DeregisterGatewayInstance_ResponseSyntax) **   <a name="mediaconnect-DeregisterGatewayInstance-response-gatewayInstanceArn"></a>
 The ARN of the instance.
Type: String

 ** [instanceState](#API_DeregisterGatewayInstance_ResponseSyntax) **   <a name="mediaconnect-DeregisterGatewayInstance-response-instanceState"></a>
 The status of the instance.
Type: String
Valid Values: `REGISTERING | ACTIVE | DEREGISTERING | DEREGISTERED | REGISTRATION_ERROR | DEREGISTRATION_ERROR`

## Errors
<a name="API_DeregisterGatewayInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_DeregisterGatewayInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/DeregisterGatewayInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DeregisterGatewayInstance)
