---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_DescribeTunnel.html
---

# DescribeTunnel
<a name="API_iot-secure-tunneling_DescribeTunnel"></a>

Gets information about a tunnel identified by the unique tunnel id.

Requires permission to access the [DescribeTunnel](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-secure-tunneling_DescribeTunnel_RequestSyntax"></a>

```
{
   "tunnelId": "{{string}}"
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_DescribeTunnel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [tunnelId](#API_iot-secure-tunneling_DescribeTunnel_RequestSyntax) **   <a name="iot-iot-secure-tunneling_DescribeTunnel-request-tunnelId"></a>
The tunnel to describe.
Type: String
Pattern: `[a-zA-Z0-9_\-+=:]{1,128}`
Required: Yes

## Response Syntax
<a name="API_iot-secure-tunneling_DescribeTunnel_ResponseSyntax"></a>

```
{
   "tunnel": {
      "createdAt": number,
      "description": "string",
      "destinationConfig": {
         "services": [ "string" ],
         "thingName": "string"
      },
      "destinationConnectionState": {
         "lastUpdatedAt": number,
         "status": "string"
      },
      "lastUpdatedAt": number,
      "sourceConnectionState": {
         "lastUpdatedAt": number,
         "status": "string"
      },
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "timeoutConfig": {
         "maxLifetimeTimeoutMinutes": number
      },
      "tunnelArn": "string",
      "tunnelId": "string"
   }
}
```

## Response Elements
<a name="API_iot-secure-tunneling_DescribeTunnel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tunnel](#API_iot-secure-tunneling_DescribeTunnel_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_DescribeTunnel-response-tunnel"></a>
The tunnel being described.
Type: [Tunnel](API_iot-secure-tunneling_Tunnel.md) object

## Errors
<a name="API_iot-secure-tunneling_DescribeTunnel_Errors"></a>

 ** ResourceNotFoundException **
Thrown when an operation is attempted on a resource that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_iot-secure-tunneling_DescribeTunnel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/DescribeTunnel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/DescribeTunnel)
