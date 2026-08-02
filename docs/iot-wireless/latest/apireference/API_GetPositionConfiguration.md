---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPositionConfiguration.html
---

# GetPositionConfiguration
<a name="API_GetPositionConfiguration"></a>

 *This action has been deprecated.*

Get position configuration for a given resource.

**Important**
This action is no longer supported. Calls to retrieve the position configuration should use the [GetResourcePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html) API operation instead.

## Request Syntax
<a name="API_GetPositionConfiguration_RequestSyntax"></a>

```
GET /position-configurations/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPositionConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_GetPositionConfiguration_RequestSyntax) **   <a name="iotwireless-GetPositionConfiguration-request-uri-ResourceIdentifier"></a>
Resource identifier used in a position configuration.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [ResourceType](#API_GetPositionConfiguration_RequestSyntax) **   <a name="iotwireless-GetPositionConfiguration-request-uri-ResourceType"></a>
Resource type of the resource for which position configuration is retrieved.
Valid Values: `WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_GetPositionConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPositionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Destination": "string",
   "Solvers": {
      "SemtechGnss": {
         "Fec": "string",
         "Provider": "string",
         "Status": "string",
         "Type": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetPositionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Destination](#API_GetPositionConfiguration_ResponseSyntax) **   <a name="iotwireless-GetPositionConfiguration-response-Destination"></a>
The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [Solvers](#API_GetPositionConfiguration_ResponseSyntax) **   <a name="iotwireless-GetPositionConfiguration-response-Solvers"></a>
The wrapper for the solver configuration details object.
Type: [PositionSolverDetails](API_PositionSolverDetails.md) object

## Errors
<a name="API_GetPositionConfiguration_Errors"></a>

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
<a name="API_GetPositionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetPositionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetPositionConfiguration)
