---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateNetworkAnalyzerConfiguration.html
---

# UpdateNetworkAnalyzerConfiguration
<a name="API_UpdateNetworkAnalyzerConfiguration"></a>

Update network analyzer configuration.

## Request Syntax
<a name="API_UpdateNetworkAnalyzerConfiguration_RequestSyntax"></a>

```
PATCH /network-analyzer-configurations/{{ConfigurationName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "MulticastGroupsToAdd": [ "{{string}}" ],
   "MulticastGroupsToRemove": [ "{{string}}" ],
   "TraceContent": {
      "LogLevel": "{{string}}",
      "MulticastFrameInfo": "{{string}}",
      "WirelessDeviceFrameInfo": "{{string}}"
   },
   "WirelessDevicesToAdd": [ "{{string}}" ],
   "WirelessDevicesToRemove": [ "{{string}}" ],
   "WirelessGatewaysToAdd": [ "{{string}}" ],
   "WirelessGatewaysToRemove": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateNetworkAnalyzerConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationName](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-uri-ConfigurationName"></a>
Name of the network analyzer configuration.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_UpdateNetworkAnalyzerConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [MulticastGroupsToAdd](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-MulticastGroupsToAdd"></a>
Multicast group resources to add to the network analyzer configuration. Provide the `MulticastGroupId` of the resource to add in the input array.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Maximum length of 256.
Required: No

 ** [MulticastGroupsToRemove](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-MulticastGroupsToRemove"></a>
Multicast group resources to remove from the network analyzer configuration. Provide the `MulticastGroupId` of the resources to remove in the input array.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Maximum length of 256.
Required: No

 ** [TraceContent](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-TraceContent"></a>
Trace content for your wireless devices, gateways, and multicast groups.
Type: [TraceContent](API_TraceContent.md) object
Required: No

 ** [WirelessDevicesToAdd](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-WirelessDevicesToAdd"></a>
Wireless device resources to add to the network analyzer configuration. Provide the `WirelessDeviceId` of the resource to add in the input array.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Length Constraints: Maximum length of 256.
Required: No

 ** [WirelessDevicesToRemove](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-WirelessDevicesToRemove"></a>
Wireless device resources to remove from the network analyzer configuration. Provide the `WirelessDeviceId` of the resources to remove in the input array.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Length Constraints: Maximum length of 256.
Required: No

 ** [WirelessGatewaysToAdd](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-WirelessGatewaysToAdd"></a>
Wireless gateway resources to add to the network analyzer configuration. Provide the `WirelessGatewayId` of the resource to add in the input array.
Type: Array of strings
Length Constraints: Maximum length of 256.
Required: No

 ** [WirelessGatewaysToRemove](#API_UpdateNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-UpdateNetworkAnalyzerConfiguration-request-WirelessGatewaysToRemove"></a>
Wireless gateway resources to remove from the network analyzer configuration. Provide the `WirelessGatewayId` of the resources to remove in the input array.
Type: Array of strings
Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateNetworkAnalyzerConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateNetworkAnalyzerConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateNetworkAnalyzerConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNetworkAnalyzerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateNetworkAnalyzerConfiguration)
