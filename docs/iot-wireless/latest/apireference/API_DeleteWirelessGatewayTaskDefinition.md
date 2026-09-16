---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessGatewayTaskDefinition.html
---

# DeleteWirelessGatewayTaskDefinition
<a name="API_DeleteWirelessGatewayTaskDefinition"></a>

Deletes a wireless gateway task definition. Deleting this task definition does not affect tasks that are currently in progress.

## Request Syntax
<a name="API_DeleteWirelessGatewayTaskDefinition_RequestSyntax"></a>

```
DELETE /wireless-gateway-task-definitions/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWirelessGatewayTaskDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-DeleteWirelessGatewayTaskDefinition-request-uri-Id"></a>
The ID of the resource to delete.
Length Constraints: Maximum length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_DeleteWirelessGatewayTaskDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWirelessGatewayTaskDefinition_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteWirelessGatewayTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteWirelessGatewayTaskDefinition_Errors"></a>

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
<a name="API_DeleteWirelessGatewayTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/DeleteWirelessGatewayTaskDefinition)
