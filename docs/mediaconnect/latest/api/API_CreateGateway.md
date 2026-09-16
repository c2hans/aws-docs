---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateGateway.html
---

# CreateGateway
<a name="API_CreateGateway"></a>

 Creates a new gateway. The request must include at least one network (up to four).

## Request Syntax
<a name="API_CreateGateway_RequestSyntax"></a>

```
POST /v1/gateways HTTP/1.1
Content-type: application/json

{
   "egressCidrBlocks": [ "{{string}}" ],
   "name": "{{string}}",
   "networks": [
      {
         "cidrBlock": "{{string}}",
         "name": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateGateway_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [egressCidrBlocks](#API_CreateGateway_RequestSyntax) **   <a name="mediaconnect-CreateGateway-request-egressCidrBlocks"></a>
 The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: Array of strings
Required: Yes

 ** [name](#API_CreateGateway_RequestSyntax) **   <a name="mediaconnect-CreateGateway-request-name"></a>
 The name of the gateway. This name can not be modified after the gateway is created.
Type: String
Required: Yes

 ** [networks](#API_CreateGateway_RequestSyntax) **   <a name="mediaconnect-CreateGateway-request-networks"></a>
 The list of networks that you want to add to the gateway.
Type: Array of [GatewayNetwork](API_GatewayNetwork.md) objects
Required: Yes

## Response Syntax
<a name="API_CreateGateway_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "gateway": {
      "egressCidrBlocks": [ "string" ],
      "gatewayArn": "string",
      "gatewayMessages": [
         {
            "code": "string",
            "message": "string",
            "resourceName": "string"
         }
      ],
      "gatewayState": "string",
      "name": "string",
      "networks": [
         {
            "cidrBlock": "string",
            "name": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [gateway](#API_CreateGateway_ResponseSyntax) **   <a name="mediaconnect-CreateGateway-response-gateway"></a>
 The gateway that you created.
Type: [Gateway](API_Gateway.md) object

## Errors
<a name="API_CreateGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** CreateGateway420Exception **
Exception raised by AWS Elemental MediaConnect when creating the gateway. See the error message for the operation for more information on the cause of this exception.
HTTP Status Code: 420

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_CreateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/CreateGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/CreateGateway)
