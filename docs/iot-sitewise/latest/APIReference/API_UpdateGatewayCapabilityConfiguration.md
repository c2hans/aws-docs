---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateGatewayCapabilityConfiguration.html
---

# UpdateGatewayCapabilityConfiguration
<a name="API_UpdateGatewayCapabilityConfiguration"></a>

Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway.

Important workflow notes:

Each gateway capability defines data sources for a gateway. This is the namespace of the gateway capability.

. The namespace follows the format `service:capability:version`, where:
+  `service` - The service providing the capability, or `iotsitewise`.
+  `capability` - The specific capability type. Options include: `opcuacollector` for the OPC UA data source collector, or `publisher` for data publisher capability.
+  `version` - The version number of the capability. Option include `2` for Classic streams, V2 gateways, and `3` for MQTT-enabled, V3 gateways.

After updating a capability configuration, the sync status becomes `OUT_OF_SYNC` until the gateway processes the configuration.Use `DescribeGatewayCapabilityConfiguration` to check the sync status and verify the configuration was applied.

A gateway can have multiple capability configurations with different namespaces.

## Request Syntax
<a name="API_UpdateGatewayCapabilityConfiguration_RequestSyntax"></a>

```
POST /20200301/gateways/{{gatewayId}}/capability HTTP/1.1
Content-type: application/json

{
   "capabilityConfiguration": "{{string}}",
   "capabilityNamespace": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateGatewayCapabilityConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_UpdateGatewayCapabilityConfiguration_RequestSyntax) **   <a name="iotsitewise-UpdateGatewayCapabilityConfiguration-request-uri-gatewayId"></a>
The ID of the gateway to be updated.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateGatewayCapabilityConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capabilityConfiguration](#API_UpdateGatewayCapabilityConfiguration_RequestSyntax) **   <a name="iotsitewise-UpdateGatewayCapabilityConfiguration-request-capabilityConfiguration"></a>
The JSON document that defines the configuration for the gateway capability. For more information, see [Configuring data sources (CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000000.
Required: Yes

 ** [capabilityNamespace](#API_UpdateGatewayCapabilityConfiguration_RequestSyntax) **   <a name="iotsitewise-UpdateGatewayCapabilityConfiguration-request-capabilityNamespace"></a>
The namespace of the gateway capability configuration to be updated. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace `iotsitewise:opcuacollector:3`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z]+:[a-zA-Z]+:[0-9]+$`
Required: Yes

## Response Syntax
<a name="API_UpdateGatewayCapabilityConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "capabilityNamespace": "string",
   "capabilitySyncStatus": "string"
}
```

## Response Elements
<a name="API_UpdateGatewayCapabilityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [capabilityNamespace](#API_UpdateGatewayCapabilityConfiguration_ResponseSyntax) **   <a name="iotsitewise-UpdateGatewayCapabilityConfiguration-response-capabilityNamespace"></a>
The namespace of the gateway capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z]+:[a-zA-Z]+:[0-9]+$`

 ** [capabilitySyncStatus](#API_UpdateGatewayCapabilityConfiguration_ResponseSyntax) **   <a name="iotsitewise-UpdateGatewayCapabilityConfiguration-response-capabilitySyncStatus"></a>
The synchronization status of the gateway capability configuration. The sync status can be one of the following:
+  `IN_SYNC` - The gateway is running with the latest configuration.
+  `OUT_OF_SYNC` - The gateway hasn't received the latest configuration.
+  `SYNC_FAILED` - The gateway rejected the latest configuration.
+  `UNKNOWN` - The gateway hasn't reported its sync status.
+  `NOT_APPLICABLE` - The gateway doesn't support this capability. This is most common when integrating partner data sources, because the data integration is handled externally by the partner.
After you update a capability configuration, its sync status is `OUT_OF_SYNC` until the gateway receives and applies or rejects the updated configuration.
Type: String
Valid Values: `IN_SYNC | OUT_OF_SYNC | SYNC_FAILED | UNKNOWN | NOT_APPLICABLE`

## Errors
<a name="API_UpdateGatewayCapabilityConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

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

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_UpdateGatewayCapabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdateGatewayCapabilityConfiguration)
