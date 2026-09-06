---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_PutPositionConfiguration.html
---

# PutPositionConfiguration
<a name="API_PutPositionConfiguration"></a>

 *This action has been deprecated.*

Put position configuration for a given resource.

**Important**
This action is no longer supported. Calls to update the position configuration should use the [UpdateResourcePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html) API operation instead.

## Request Syntax
<a name="API_PutPositionConfiguration_RequestSyntax"></a>

```
PUT /position-configurations/{{ResourceIdentifier}}?resourceType={{ResourceType}} HTTP/1.1
Content-type: application/json

{
   "Destination": "{{string}}",
   "Solvers": {
      "SemtechGnss": {
         "Fec": "{{string}}",
         "Status": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_PutPositionConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceIdentifier](#API_PutPositionConfiguration_RequestSyntax) **   <a name="iotwireless-PutPositionConfiguration-request-uri-ResourceIdentifier"></a>
Resource identifier used to update the position configuration.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** [ResourceType](#API_PutPositionConfiguration_RequestSyntax) **   <a name="iotwireless-PutPositionConfiguration-request-uri-ResourceType"></a>
Resource type of the resource for which you want to update the position configuration.
Valid Values: `WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_PutPositionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Destination](#API_PutPositionConfiguration_RequestSyntax) **   <a name="iotwireless-PutPositionConfiguration-request-Destination"></a>
The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [Solvers](#API_PutPositionConfiguration_RequestSyntax) **   <a name="iotwireless-PutPositionConfiguration-request-Solvers"></a>
The positioning solvers used to update the position configuration of the resource.
Type: [PositionSolverConfigurations](API_PositionSolverConfigurations.md) object
Required: No

## Response Syntax
<a name="API_PutPositionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutPositionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutPositionConfiguration_Errors"></a>

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
<a name="API_PutPositionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/PutPositionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/PutPositionConfiguration)
