---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateDestination.html
---

# UpdateDestination
<a name="API_UpdateDestination"></a>

Updates properties of a destination.

## Request Syntax
<a name="API_UpdateDestination_RequestSyntax"></a>

```
PATCH /destinations/{{Name}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Expression": "{{string}}",
   "ExpressionType": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_UpdateDestination_RequestSyntax) **   <a name="iotwireless-UpdateDestination-request-uri-Name"></a>
The new name of the resource.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_UpdateDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDestination_RequestSyntax) **   <a name="iotwireless-UpdateDestination-request-Description"></a>
A new description of the resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [Expression](#API_UpdateDestination_RequestSyntax) **   <a name="iotwireless-UpdateDestination-request-Expression"></a>
The new rule name or topic rule to send messages to.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [ExpressionType](#API_UpdateDestination_RequestSyntax) **   <a name="iotwireless-UpdateDestination-request-ExpressionType"></a>
The type of value in `Expression`.
Type: String
Valid Values: `RuleName | MqttTopic`
Required: No

 ** [RoleArn](#API_UpdateDestination_RequestSyntax) **   <a name="iotwireless-UpdateDestination-request-RoleArn"></a>
The ARN of the IAM Role that authorizes the destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateDestination_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateDestination_Errors"></a>

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
<a name="API_UpdateDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
