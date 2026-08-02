---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayTaskDefinition.html
---

# GetWirelessGatewayTaskDefinition
<a name="API_GetWirelessGatewayTaskDefinition"></a>

Gets information about a wireless gateway task definition.

## Request Syntax
<a name="API_GetWirelessGatewayTaskDefinition_RequestSyntax"></a>

```
GET /wireless-gateway-task-definitions/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWirelessGatewayTaskDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-GetWirelessGatewayTaskDefinition-request-uri-Id"></a>
The ID of the resource to get.
Length Constraints: Maximum length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetWirelessGatewayTaskDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWirelessGatewayTaskDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AutoCreateTasks": boolean,
   "Name": "string",
   "Update": {
      "LoRaWAN": {
         "CurrentVersion": {
            "Model": "string",
            "PackageVersion": "string",
            "Station": "string"
         },
         "SigKeyCrc": number,
         "UpdateSignature": "string",
         "UpdateVersion": {
            "Model": "string",
            "PackageVersion": "string",
            "Station": "string"
         }
      },
      "UpdateDataRole": "string",
      "UpdateDataSource": "string"
   }
}
```

## Response Elements
<a name="API_GetWirelessGatewayTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetWirelessGatewayTaskDefinition_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayTaskDefinition-response-Arn"></a>
The Amazon Resource Name of the resource.
Type: String

 ** [AutoCreateTasks](#API_GetWirelessGatewayTaskDefinition_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayTaskDefinition-response-AutoCreateTasks"></a>
Whether to automatically create tasks using this task definition for all gateways with the specified current version. If `false`, the task must me created by calling `CreateWirelessGatewayTask`.
Type: Boolean

 ** [Name](#API_GetWirelessGatewayTaskDefinition_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayTaskDefinition-response-Name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Update](#API_GetWirelessGatewayTaskDefinition_ResponseSyntax) **   <a name="iotwireless-GetWirelessGatewayTaskDefinition-response-Update"></a>
Information about the gateways to update.
Type: [UpdateWirelessGatewayTaskCreate](API_UpdateWirelessGatewayTaskCreate.md) object

## Errors
<a name="API_GetWirelessGatewayTaskDefinition_Errors"></a>

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
<a name="API_GetWirelessGatewayTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetWirelessGatewayTaskDefinition)
