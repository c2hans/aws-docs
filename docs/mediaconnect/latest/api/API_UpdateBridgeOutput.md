---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridgeOutput.html
---

# UpdateBridgeOutput
<a name="API_UpdateBridgeOutput"></a>

 Updates an existing bridge output.

## Request Syntax
<a name="API_UpdateBridgeOutput_RequestSyntax"></a>

```
PUT /v1/bridges/{{bridgeArn}}/outputs/{{outputName}} HTTP/1.1
Content-type: application/json

{
   "networkOutput": {
      "ipAddress": "{{string}}",
      "networkName": "{{string}}",
      "port": {{number}},
      "protocol": "{{string}}",
      "ttl": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateBridgeOutput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bridgeArn](#API_UpdateBridgeOutput_RequestSyntax) **   <a name="mediaconnect-UpdateBridgeOutput-request-uri-bridgeArn"></a>
 The Amazon Resource Name (ARN) of the bridge that you want to update.
Pattern: `arn:.+:mediaconnect.+:bridge:.+`
Required: Yes

 ** [outputName](#API_UpdateBridgeOutput_RequestSyntax) **   <a name="mediaconnect-UpdateBridgeOutput-request-uri-outputName"></a>
 Tname of the output that you want to update.
Required: Yes

## Request Body
<a name="API_UpdateBridgeOutput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [networkOutput](#API_UpdateBridgeOutput_RequestSyntax) **   <a name="mediaconnect-UpdateBridgeOutput-request-networkOutput"></a>
 The network of the bridge output.
Type: [UpdateBridgeNetworkOutputRequest](API_UpdateBridgeNetworkOutputRequest.md) object
Required: No

## Response Syntax
<a name="API_UpdateBridgeOutput_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "bridgeArn": "string",
   "output": {
      "flowOutput": {
         "flowArn": "string",
         "flowSourceArn": "string",
         "name": "string"
      },
      "networkOutput": {
         "ipAddress": "string",
         "name": "string",
         "networkName": "string",
         "port": number,
         "protocol": "string",
         "ttl": number
      }
   }
}
```

## Response Elements
<a name="API_UpdateBridgeOutput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [bridgeArn](#API_UpdateBridgeOutput_ResponseSyntax) **   <a name="mediaconnect-UpdateBridgeOutput-response-bridgeArn"></a>
 The ARN of the bridge that was updated.
Type: String

 ** [output](#API_UpdateBridgeOutput_ResponseSyntax) **   <a name="mediaconnect-UpdateBridgeOutput-response-output"></a>
 The bridge output that was updated.
Type: [BridgeOutput](API_BridgeOutput.md) object

## Errors
<a name="API_UpdateBridgeOutput_Errors"></a>

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
<a name="API_UpdateBridgeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateBridgeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateBridgeOutput)
