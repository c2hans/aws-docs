---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetDestination.html
---

# GetDestination
<a name="API_GetDestination"></a>

Gets a destination by name.

## Request Syntax
<a name="API_GetDestination_RequestSyntax"></a>

```
GET /destinations/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetDestination_RequestSyntax) **   <a name="managedintegrations-GetDestination-request-uri-Name"></a>
The name of the customer-managed destination.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
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
   "CreatedAt": number,
   "DeliveryDestinationArn": "string",
   "DeliveryDestinationType": "string",
   "Description": "string",
   "Name": "string",
   "RoleArn": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-CreatedAt"></a>
The timestamp value of when the destination creation requset occurred.
Type: Timestamp

 ** [DeliveryDestinationArn](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-DeliveryDestinationArn"></a>
The Amazon Resource Name (ARN) of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:[0-9a-zA-Z]+:[0-9a-zA-Z-]+:[0-9]+:[0-9a-zA-Z]+/[0-9a-zA-Z._-]+`

 ** [DeliveryDestinationType](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-DeliveryDestinationType"></a>
The destination type for the customer-managed destination.
Type: String
Valid Values: `KINESIS`

 ** [Description](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-Description"></a>
The description of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`

 ** [Name](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-Name"></a>
The name of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`

 ** [RoleArn](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the delivery destination role.
Type: String

 ** [Tags](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-Tags"></a>
 *This parameter has been deprecated.*
A set of key/value pairs that are used to manage the customer-managed destination.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [UpdatedAt](#API_GetDestination_ResponseSyntax) **   <a name="managedintegrations-GetDestination-response-UpdatedAt"></a>
The timestamp value of when the destination update requset occurred.
Type: Timestamp

## Errors
<a name="API_GetDestination_Errors"></a>

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
<a name="API_GetDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetDestination)
