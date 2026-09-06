---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDestination.html
---

# GetDestination
<a name="API_GetDestination"></a>

Gets information about a destination.

## Request Syntax
<a name="API_GetDestination_RequestSyntax"></a>

```
GET /destinations/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetDestination_RequestSyntax) **   <a name="iotwireless-GetDestination-request-uri-Name"></a>
The name of the resource to get.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_GetDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Description": "string",
   "Expression": "string",
   "ExpressionType": "string",
   "Name": "string",
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_GetDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetDestination_ResponseSyntax) **   <a name="iotwireless-GetDestination-response-Arn"></a>
The Amazon Resource Name of the resource.
Type: String

 ** [Description](#API_GetDestination_ResponseSyntax) **   <a name="iotwireless-GetDestination-response-Description"></a>
The description of the resource.
Type: String
Length Constraints: Maximum length of 2048.

 ** [Expression](#API_GetDestination_ResponseSyntax) **   <a name="iotwireless-GetDestination-response-Expression"></a>
The rule name or topic rule to send messages to.
Type: String
Length Constraints: Maximum length of 2048.

 ** [ExpressionType](#API_GetDestination_ResponseSyntax) **   <a name="iotwireless-GetDestination-response-ExpressionType"></a>
The type of value in `Expression`.
Type: String
Valid Values: `RuleName | MqttTopic`

 ** [Name](#API_GetDestination_ResponseSyntax) **   <a name="iotwireless-GetDestination-response-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [RoleArn](#API_GetDestination_ResponseSyntax) **   <a name="iotwireless-GetDestination-response-RoleArn"></a>
The ARN of the IAM Role that authorizes the destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_GetDestination_Errors"></a>

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
<a name="API_GetDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetDestination)
