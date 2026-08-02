---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_OpenTunnel.html
---

# OpenTunnel
<a name="API_iot-secure-tunneling_OpenTunnel"></a>

Creates a new tunnel, and returns two client access tokens for clients to use to connect to the AWS IoT Secure Tunneling proxy server.

Requires permission to access the [OpenTunnel](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-secure-tunneling_OpenTunnel_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "destinationConfig": {
      "services": [ "{{string}}" ],
      "thingName": "{{string}}"
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "timeoutConfig": {
      "maxLifetimeTimeoutMinutes": {{number}}
   }
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_OpenTunnel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_iot-secure-tunneling_OpenTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-request-description"></a>
A short text description of the tunnel.
Type: String
Pattern: `[^\p{C}]{1,2048}`
Required: No

 ** [destinationConfig](#API_iot-secure-tunneling_OpenTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-request-destinationConfig"></a>
The destination configuration for the OpenTunnel request.
Type: [DestinationConfig](API_iot-secure-tunneling_DestinationConfig.md) object
Required: No

 ** [tags](#API_iot-secure-tunneling_OpenTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-request-tags"></a>
A collection of tag metadata.
Type: Array of [Tag](API_iot-secure-tunneling_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** [timeoutConfig](#API_iot-secure-tunneling_OpenTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-request-timeoutConfig"></a>
Timeout configuration for a tunnel.
Type: [TimeoutConfig](API_iot-secure-tunneling_TimeoutConfig.md) object
Required: No

## Response Syntax
<a name="API_iot-secure-tunneling_OpenTunnel_ResponseSyntax"></a>

```
{
   "destinationAccessToken": "string",
   "sourceAccessToken": "string",
   "tunnelArn": "string",
   "tunnelId": "string"
}
```

## Response Elements
<a name="API_iot-secure-tunneling_OpenTunnel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationAccessToken](#API_iot-secure-tunneling_OpenTunnel_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-response-destinationAccessToken"></a>
The access token the destination local proxy uses to connect to AWS IoT Secure Tunneling.
Type: String

 ** [sourceAccessToken](#API_iot-secure-tunneling_OpenTunnel_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-response-sourceAccessToken"></a>
The access token the source local proxy uses to connect to AWS IoT Secure Tunneling.
Type: String

 ** [tunnelArn](#API_iot-secure-tunneling_OpenTunnel_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-response-tunnelArn"></a>
The Amazon Resource Name for the tunnel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

 ** [tunnelId](#API_iot-secure-tunneling_OpenTunnel_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_OpenTunnel-response-tunnelId"></a>
A unique alpha-numeric tunnel ID.
Type: String
Pattern: `[a-zA-Z0-9_\-+=:]{1,128}`

## Errors
<a name="API_iot-secure-tunneling_OpenTunnel_Errors"></a>

 ** LimitExceededException **
Thrown when a tunnel limit is exceeded.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_OpenTunnel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/OpenTunnel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/OpenTunnel)
