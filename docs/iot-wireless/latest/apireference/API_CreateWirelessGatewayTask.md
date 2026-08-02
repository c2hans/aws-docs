---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGatewayTask.html
---

# CreateWirelessGatewayTask
<a name="API_CreateWirelessGatewayTask"></a>

Creates a task for a wireless gateway.

## Request Syntax
<a name="API_CreateWirelessGatewayTask_RequestSyntax"></a>

```
POST /wireless-gateways/{{Id}}/tasks HTTP/1.1
Content-type: application/json

{
   "WirelessGatewayTaskDefinitionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWirelessGatewayTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_CreateWirelessGatewayTask_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTask-request-uri-Id"></a>
The ID of the resource to update.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_CreateWirelessGatewayTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [WirelessGatewayTaskDefinitionId](#API_CreateWirelessGatewayTask_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTask-request-WirelessGatewayTaskDefinitionId"></a>
The ID of the WirelessGatewayTaskDefinition.
Type: String
Length Constraints: Maximum length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_CreateWirelessGatewayTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Status": "string",
   "WirelessGatewayTaskDefinitionId": "string"
}
```

## Response Elements
<a name="API_CreateWirelessGatewayTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_CreateWirelessGatewayTask_ResponseSyntax) **   <a name="iotwireless-CreateWirelessGatewayTask-response-Status"></a>
The status of the request.
Type: String
Valid Values: `PENDING | IN_PROGRESS | FIRST_RETRY | SECOND_RETRY | COMPLETED | FAILED`

 ** [WirelessGatewayTaskDefinitionId](#API_CreateWirelessGatewayTask_ResponseSyntax) **   <a name="iotwireless-CreateWirelessGatewayTask-response-WirelessGatewayTaskDefinitionId"></a>
The ID of the WirelessGatewayTaskDefinition.
Type: String
Length Constraints: Maximum length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

## Errors
<a name="API_CreateWirelessGatewayTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

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
<a name="API_CreateWirelessGatewayTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/CreateWirelessGatewayTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CreateWirelessGatewayTask)
