---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html
---

# CreateGateway
<a name="API_CreateGateway"></a>

Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to AWS IoT SiteWise. For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_CreateGateway_RequestSyntax"></a>

```
POST /20200301/gateways HTTP/1.1
Content-type: application/json

{
   "gatewayName": "{{string}}",
   "gatewayPlatform": {
      "greengrass": {
         "groupArn": "{{string}}"
      },
      "greengrassV2": {
         "coreDeviceOperatingSystem": "{{string}}",
         "coreDeviceThingName": "{{string}}"
      },
      "siemensIE": {
         "iotCoreThingName": "{{string}}"
      }
   },
   "gatewayVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateGateway_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [gatewayName](#API_CreateGateway_RequestSyntax) **   <a name="iotsitewise-CreateGateway-request-gatewayName"></a>
A unique name for the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [gatewayPlatform](#API_CreateGateway_RequestSyntax) **   <a name="iotsitewise-CreateGateway-request-gatewayPlatform"></a>
The gateway's platform. You can only specify one platform in a gateway.
Type: [GatewayPlatform](API_GatewayPlatform.md) object
Required: Yes

 ** [gatewayVersion](#API_CreateGateway_RequestSyntax) **   <a name="iotsitewise-CreateGateway-request-gatewayVersion"></a>
The version of the gateway to create. Specify `3` to create an MQTT-enabled, V3 gateway and `2` to create a Classic streams, V2 gateway. If not specified, the default is `2` (Classic streams, V2 gateway).
When creating a V3 gateway (`gatewayVersion=3`) with the `GreengrassV2` platform, you must also specify the `coreDeviceOperatingSystem` parameter.
 We recommend creating an MQTT-enabled gateway for self-hosted gateways and Siemens Industrial Edge gateways. For more information on gateway versions, see [Use AWS IoT SiteWise Edge Edge gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** [tags](#API_CreateGateway_RequestSyntax) **   <a name="iotsitewise-CreateGateway-request-tags"></a>
A list of key-value pairs that contain metadata for the gateway. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateGateway_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "gatewayArn": "string",
   "gatewayId": "string"
}
```

## Response Elements
<a name="API_CreateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [gatewayArn](#API_CreateGateway_ResponseSyntax) **   <a name="iotsitewise-CreateGateway-response-gatewayArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the gateway, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [gatewayId](#API_CreateGateway_ResponseSyntax) **   <a name="iotsitewise-CreateGateway-response-gatewayId"></a>
The ID of the gateway device. You can use this ID when you call other AWS IoT SiteWise API operations.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_CreateGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** resourceArn **
The ARN of the resource that already exists.
 ** resourceId **
The ID of the resource that already exists.
HTTP Status Code: 409

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
