---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html
---

# DescribeGateway
<a name="API_DescribeGateway"></a>

Retrieves information about a gateway.

## Request Syntax
<a name="API_DescribeGateway_RequestSyntax"></a>

```
GET /20200301/gateways/{{gatewayId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_DescribeGateway_RequestSyntax) **   <a name="iotsitewise-DescribeGateway-request-uri-gatewayId"></a>
The ID of the gateway device.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "gatewayArn": "string",
   "gatewayCapabilitySummaries": [
      {
         "capabilityNamespace": "string",
         "capabilitySyncStatus": "string"
      }
   ],
   "gatewayId": "string",
   "gatewayName": "string",
   "gatewayPlatform": {
      "greengrass": {
         "groupArn": "string"
      },
      "greengrassV2": {
         "coreDeviceOperatingSystem": "string",
         "coreDeviceThingName": "string"
      },
      "siemensIE": {
         "iotCoreThingName": "string"
      }
   },
   "gatewayVersion": "string",
   "lastUpdateDate": number
}
```

## Response Elements
<a name="API_DescribeGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-creationDate"></a>
The date the gateway was created, in Unix epoch time.
Type: Timestamp

 ** [gatewayArn](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-gatewayArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the gateway, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [gatewayCapabilitySummaries](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-gatewayCapabilitySummaries"></a>
A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use [DescribeGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html).
Type: Array of [GatewayCapabilitySummary](API_GatewayCapabilitySummary.md) objects

 ** [gatewayId](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-gatewayId"></a>
The ID of the gateway device.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [gatewayName](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-gatewayName"></a>
The name of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [gatewayPlatform](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-gatewayPlatform"></a>
The gateway's platform.
Type: [GatewayPlatform](API_GatewayPlatform.md) object

 ** [gatewayVersion](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-gatewayVersion"></a>
The version of the gateway. A value of `3` indicates an MQTT-enabled, V3 gateway, while `2` indicates a Classic streams, V2 gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`

 ** [lastUpdateDate](#API_DescribeGateway_ResponseSyntax) **   <a name="iotsitewise-DescribeGateway-response-lastUpdateDate"></a>
The date the gateway was last updated, in Unix epoch time.
Type: Timestamp

## Errors
<a name="API_DescribeGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeGateway)
