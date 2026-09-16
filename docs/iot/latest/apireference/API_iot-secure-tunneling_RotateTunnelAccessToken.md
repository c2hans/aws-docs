---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_RotateTunnelAccessToken.html
---

# RotateTunnelAccessToken
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken"></a>

Revokes the current client access token (CAT) and returns new CAT for clients to use when reconnecting to secure tunneling to access the same tunnel.

Requires permission to access the [RotateTunnelAccessToken](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

**Note**
Rotating the CAT doesn't extend the tunnel duration. For example, say the tunnel duration is 12 hours and the tunnel has already been open for 4 hours. When you rotate the access tokens, the new tokens that are generated can only be used for the remaining 8 hours.

## Request Syntax
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken_RequestSyntax"></a>

```
{
   "clientMode": "{{string}}",
   "destinationConfig": {
      "services": [ "{{string}}" ],
      "thingName": "{{string}}"
   },
   "tunnelId": "{{string}}"
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientMode](#API_iot-secure-tunneling_RotateTunnelAccessToken_RequestSyntax) **   <a name="iot-iot-secure-tunneling_RotateTunnelAccessToken-request-clientMode"></a>
The mode of the client that will use the client token, which can be either the source or destination, or both source and destination.
Type: String
Valid Values: `SOURCE | DESTINATION | ALL`
Required: Yes

 ** [destinationConfig](#API_iot-secure-tunneling_RotateTunnelAccessToken_RequestSyntax) **   <a name="iot-iot-secure-tunneling_RotateTunnelAccessToken-request-destinationConfig"></a>
The destination configuration. You can not use `DestinationConfig` with source `clientMode`.
Type: [DestinationConfig](API_iot-secure-tunneling_DestinationConfig.md) object
Required: No

 ** [tunnelId](#API_iot-secure-tunneling_RotateTunnelAccessToken_RequestSyntax) **   <a name="iot-iot-secure-tunneling_RotateTunnelAccessToken-request-tunnelId"></a>
The tunnel for which you want to rotate the access tokens.
Type: String
Pattern: `[a-zA-Z0-9_\-+=:]{1,128}`
Required: Yes

## Response Syntax
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken_ResponseSyntax"></a>

```
{
   "destinationAccessToken": "string",
   "sourceAccessToken": "string",
   "tunnelArn": "string"
}
```

## Response Elements
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationAccessToken](#API_iot-secure-tunneling_RotateTunnelAccessToken_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_RotateTunnelAccessToken-response-destinationAccessToken"></a>
The client access token that the destination local proxy uses to connect to AWS IoT Secure Tunneling.
Type: String

 ** [sourceAccessToken](#API_iot-secure-tunneling_RotateTunnelAccessToken_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_RotateTunnelAccessToken-response-sourceAccessToken"></a>
The client access token that the source local proxy uses to connect to AWS IoT Secure Tunneling.
Type: String

 ** [tunnelArn](#API_iot-secure-tunneling_RotateTunnelAccessToken_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_RotateTunnelAccessToken-response-tunnelArn"></a>
The Amazon Resource Name for the tunnel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.

## Errors
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken_Errors"></a>

 ** ResourceNotFoundException **
Thrown when an operation is attempted on a resource that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_RotateTunnelAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/RotateTunnelAccessToken)
