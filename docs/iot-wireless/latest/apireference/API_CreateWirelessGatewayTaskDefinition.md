---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGatewayTaskDefinition.html
---

# CreateWirelessGatewayTaskDefinition
<a name="API_CreateWirelessGatewayTaskDefinition"></a>

Creates a gateway task definition.

## Request Syntax
<a name="API_CreateWirelessGatewayTaskDefinition_RequestSyntax"></a>

```
POST /wireless-gateway-task-definitions HTTP/1.1
Content-type: application/json

{
   "AutoCreateTasks": {{boolean}},
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Update": {
      "LoRaWAN": {
         "CurrentVersion": {
            "Model": "{{string}}",
            "PackageVersion": "{{string}}",
            "Station": "{{string}}"
         },
         "SigKeyCrc": {{number}},
         "UpdateSignature": "{{string}}",
         "UpdateVersion": {
            "Model": "{{string}}",
            "PackageVersion": "{{string}}",
            "Station": "{{string}}"
         }
      },
      "UpdateDataRole": "{{string}}",
      "UpdateDataSource": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateWirelessGatewayTaskDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWirelessGatewayTaskDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AutoCreateTasks](#API_CreateWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-request-AutoCreateTasks"></a>
Whether to automatically create tasks using this task definition for all gateways with the specified current version. If `false`, the task must me created by calling `CreateWirelessGatewayTask`.
Type: Boolean
Required: Yes

 ** [ClientRequestToken](#API_CreateWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-request-ClientRequestToken"></a>
Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Name](#API_CreateWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-request-Name"></a>
The name of the new resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Tags](#API_CreateWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-request-Tags"></a>
The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Update](#API_CreateWirelessGatewayTaskDefinition_RequestSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-request-Update"></a>
Information about the gateways to update.
Type: [UpdateWirelessGatewayTaskCreate](API_UpdateWirelessGatewayTaskCreate.md) object
Required: No

## Response Syntax
<a name="API_CreateWirelessGatewayTaskDefinition_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateWirelessGatewayTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateWirelessGatewayTaskDefinition_ResponseSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-response-Arn"></a>
The Amazon Resource Name of the resource.
Type: String

 ** [Id](#API_CreateWirelessGatewayTaskDefinition_ResponseSyntax) **   <a name="iotwireless-CreateWirelessGatewayTaskDefinition-response-Id"></a>
The ID of the new wireless gateway task definition.
Type: String
Length Constraints: Maximum length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

## Errors
<a name="API_CreateWirelessGatewayTaskDefinition_Errors"></a>

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
<a name="API_CreateWirelessGatewayTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CreateWirelessGatewayTaskDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
