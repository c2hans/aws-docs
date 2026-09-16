---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdatePosition.html
---

# UpdatePosition
<a name="API_UpdatePosition"></a>

 *This action has been deprecated.*

Update the position information of a resource.

**Important**
This action is no longer supported. Calls to update the position information should use the [UpdateResourcePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html) API operation instead.

## Request Syntax
<a name="API_UpdatePosition_RequestSyntax"></a>

```
PATCH /positions/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1
Content-type: application/json

{
   "Position": [ {{number}} ]
}
```

## URI Request Parameters
<a name="API_UpdatePosition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_UpdatePosition_RequestSyntax) **   <a name="iotwireless-UpdatePosition-request-uri-ResourceIdentifier"></a>
Resource identifier of the resource for which position is updated.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [ResourceType](#API_UpdatePosition_RequestSyntax) **   <a name="iotwireless-UpdatePosition-request-uri-ResourceType"></a>
Resource type of the resource for which position is updated.
Valid Values: `WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_UpdatePosition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Position](#API_UpdatePosition_RequestSyntax) **   <a name="iotwireless-UpdatePosition-request-Position"></a>
The position information of the resource.
Type: Array of floats
Required: Yes

## Response Syntax
<a name="API_UpdatePosition_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdatePosition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdatePosition_Errors"></a>

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
<a name="API_UpdatePosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdatePosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdatePosition)
