---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterNetworkInterface.html
---

# UpdateRouterNetworkInterface
<a name="API_UpdateRouterNetworkInterface"></a>

Updates the configuration of an existing router network interface in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_UpdateRouterNetworkInterface_RequestSyntax"></a>

```
PUT /v1/routerNetworkInterface/{{arn}} HTTP/1.1
Content-type: application/json

{
   "configuration": { ... },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRouterNetworkInterface_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_UpdateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-UpdateRouterNetworkInterface-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the router network interface that you want to update.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateRouterNetworkInterface_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-UpdateRouterNetworkInterface-request-configuration"></a>
The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.
Type: [RouterNetworkInterfaceConfiguration](API_RouterNetworkInterfaceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [name](#API_UpdateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-UpdateRouterNetworkInterface-request-name"></a>
The updated name for the router network interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?`
Required: No

## Response Syntax
<a name="API_UpdateRouterNetworkInterface_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "routerNetworkInterface": {
      "arn": "string",
      "associatedInputCount": number,
      "associatedOutputCount": number,
      "configuration": { ... },
      "createdAt": "string",
      "id": "string",
      "name": "string",
      "networkInterfaceType": "string",
      "regionName": "string",
      "state": "string",
      "tags": {
         "string" : "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateRouterNetworkInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [routerNetworkInterface](#API_UpdateRouterNetworkInterface_ResponseSyntax) **   <a name="mediaconnect-UpdateRouterNetworkInterface-response-routerNetworkInterface"></a>
The updated router network interface.
Type: [RouterNetworkInterface](API_RouterNetworkInterface.md) object

## Errors
<a name="API_UpdateRouterNetworkInterface_Errors"></a>

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

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_UpdateRouterNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateRouterNetworkInterface)
