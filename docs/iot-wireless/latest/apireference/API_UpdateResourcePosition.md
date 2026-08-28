---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html
---

# UpdateResourcePosition
<a name="API_UpdateResourcePosition"></a>

Update the position information of a given wireless device or a wireless gateway resource. The position coordinates are based on the [ World Geodetic System (WGS84)](https://gisgeography.com/wgs84-world-geodetic-system/).

## Request Syntax
<a name="API_UpdateResourcePosition_RequestSyntax"></a>

```
PATCH /resource-positions/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1

{{GeoJsonPayload}}
```

## URI Request Parameters
<a name="API_UpdateResourcePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_UpdateResourcePosition_RequestSyntax) **   <a name="iotwireless-UpdateResourcePosition-request-uri-ResourceIdentifier"></a>
The identifier of the resource for which position information is updated. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [ResourceType](#API_UpdateResourcePosition_RequestSyntax) **   <a name="iotwireless-UpdateResourcePosition-request-uri-ResourceType"></a>
The type of resource for which position information is updated, which can be a wireless device or a wireless gateway.
Valid Values: `WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_UpdateResourcePosition_RequestBody"></a>

The request accepts the following binary data.

 ** [GeoJsonPayload](#API_UpdateResourcePosition_RequestSyntax) **   <a name="iotwireless-UpdateResourcePosition-request-GeoJsonPayload"></a>
The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see [GeoJSON](https://geojson.org/).

## Response Syntax
<a name="API_UpdateResourcePosition_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateResourcePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateResourcePosition_Errors"></a>

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
<a name="API_UpdateResourcePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateResourcePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateResourcePosition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
