---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html
---

# GetResourcePosition
<a name="API_GetResourcePosition"></a>

Get the position information for a given wireless device or a wireless gateway resource. The position information uses the [ World Geodetic System (WGS84)](https://gisgeography.com/wgs84-world-geodetic-system/).

## Request Syntax
<a name="API_GetResourcePosition_RequestSyntax"></a>

```
GET /resource-positions/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourcePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_GetResourcePosition_RequestSyntax) **   <a name="iotwireless-GetResourcePosition-request-uri-ResourceIdentifier"></a>
The identifier of the resource for which position information is retrieved. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [ResourceType](#API_GetResourcePosition_RequestSyntax) **   <a name="iotwireless-GetResourcePosition-request-uri-ResourceType"></a>
The type of resource for which position information is retrieved, which can be a wireless device or a wireless gateway.
Valid Values: `WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_GetResourcePosition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourcePosition_ResponseSyntax"></a>

```
HTTP/1.1 200

{{GeoJsonPayload}}
```

## Response Elements
<a name="API_GetResourcePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [GeoJsonPayload](#API_GetResourcePosition_ResponseSyntax) **   <a name="iotwireless-GetResourcePosition-response-GeoJsonPayload"></a>
The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see [GeoJSON](https://geojson.org/).

## Errors
<a name="API_GetResourcePosition_Errors"></a>

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
<a name="API_GetResourcePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetResourcePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetResourcePosition)
