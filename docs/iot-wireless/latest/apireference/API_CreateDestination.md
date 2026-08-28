---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDestination.html
---

# CreateDestination
<a name="API_CreateDestination"></a>

Creates a new destination that maps a device message to an AWS IoT rule.

## Request Syntax
<a name="API_CreateDestination_RequestSyntax"></a>

```
POST /destinations HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "Expression": "{{string}}",
   "ExpressionType": "{{string}}",
   "Name": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-ClientRequestToken"></a>
Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Description](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [Expression](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-Expression"></a>
The rule name or topic rule to send messages to.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

 ** [ExpressionType](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-ExpressionType"></a>
The type of value in `Expression`.
Type: String
Valid Values: `RuleName | MqttTopic`
Required: Yes

 ** [Name](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-Name"></a>
The name of the new resource.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** [RoleArn](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-RoleArn"></a>
The ARN of the IAM Role that authorizes the destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [Tags](#API_CreateDestination_RequestSyntax) **   <a name="iotwireless-CreateDestination-request-Tags"></a>
The tags to attach to the new destination. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateDestination_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDestination_ResponseSyntax) **   <a name="iotwireless-CreateDestination-response-Arn"></a>
The Amazon Resource Name of the new resource.
Type: String

 ** [Name](#API_CreateDestination_ResponseSyntax) **   <a name="iotwireless-CreateDestination-response-Name"></a>
The name of the new resource.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

## Errors
<a name="API_CreateDestination_Errors"></a>

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
<a name="API_CreateDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/CreateDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CreateDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
