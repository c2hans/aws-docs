---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetNetworkAnalyzerConfiguration.html
---

# GetNetworkAnalyzerConfiguration
<a name="API_GetNetworkAnalyzerConfiguration"></a>

Get network analyzer configuration.

## Request Syntax
<a name="API_GetNetworkAnalyzerConfiguration_RequestSyntax"></a>

```
GET /network-analyzer-configurations/{{ConfigurationName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNetworkAnalyzerConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationName](#API_GetNetworkAnalyzerConfiguration_RequestSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-request-uri-ConfigurationName"></a>
Name of the network analyzer configuration.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_GetNetworkAnalyzerConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNetworkAnalyzerConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Description": "string",
   "MulticastGroups": [ "string" ],
   "Name": "string",
   "TraceContent": {
      "LogLevel": "string",
      "MulticastFrameInfo": "string",
      "WirelessDeviceFrameInfo": "string"
   },
   "WirelessDevices": [ "string" ],
   "WirelessGateways": [ "string" ]
}
```

## Response Elements
<a name="API_GetNetworkAnalyzerConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-Arn"></a>
The Amazon Resource Name of the new resource.
Type: String
Length Constraints: Maximum length of 1124.

 ** [Description](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.

 ** [MulticastGroups](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-MulticastGroups"></a>
List of multicast group resources that have been added to the network analyzer configuration.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Maximum length of 256.

 ** [Name](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-Name"></a>
Name of the network analyzer configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9-_]+`

 ** [TraceContent](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-TraceContent"></a>
Trace content for your wireless devices, gateways, and multicast groups.
Type: [TraceContent](API_TraceContent.md) object

 ** [WirelessDevices](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-WirelessDevices"></a>
List of wireless device resources that have been added to the network analyzer configuration.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Length Constraints: Maximum length of 256.

 ** [WirelessGateways](#API_GetNetworkAnalyzerConfiguration_ResponseSyntax) **   <a name="iotwireless-GetNetworkAnalyzerConfiguration-response-WirelessGateways"></a>
List of wireless gateway resources that have been added to the network analyzer configuration.
Type: Array of strings
Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetNetworkAnalyzerConfiguration_Errors"></a>

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
<a name="API_GetNetworkAnalyzerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetNetworkAnalyzerConfiguration)
