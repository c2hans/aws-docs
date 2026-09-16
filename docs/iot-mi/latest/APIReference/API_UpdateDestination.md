---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateDestination.html
---

# UpdateDestination
<a name="API_UpdateDestination"></a>

 Update a destination specified by name.

## Request Syntax
<a name="API_UpdateDestination_RequestSyntax"></a>

```
PUT /destinations/{{Name}} HTTP/1.1
Content-type: application/json

{
   "DeliveryDestinationArn": "{{string}}",
   "DeliveryDestinationType": "{{string}}",
   "Description": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_UpdateDestination_RequestSyntax) **   <a name="managedintegrations-UpdateDestination-request-uri-Name"></a>
The name of the customer-managed destination.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: Yes

## Request Body
<a name="API_UpdateDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeliveryDestinationArn](#API_UpdateDestination_RequestSyntax) **   <a name="managedintegrations-UpdateDestination-request-DeliveryDestinationArn"></a>
The Amazon Resource Name (ARN) of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:[0-9a-zA-Z]+:[0-9a-zA-Z-]+:[0-9]+:[0-9a-zA-Z]+/[0-9a-zA-Z._-]+`
Required: No

 ** [DeliveryDestinationType](#API_UpdateDestination_RequestSyntax) **   <a name="managedintegrations-UpdateDestination-request-DeliveryDestinationType"></a>
The destination type for the customer-managed destination.
Type: String
Valid Values: `KINESIS`
Required: No

 ** [Description](#API_UpdateDestination_RequestSyntax) **   <a name="managedintegrations-UpdateDestination-request-Description"></a>
The description of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [RoleArn](#API_UpdateDestination_RequestSyntax) **   <a name="managedintegrations-UpdateDestination-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the delivery destination role.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateDestination_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_UpdateDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_UpdateDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateDestination)
