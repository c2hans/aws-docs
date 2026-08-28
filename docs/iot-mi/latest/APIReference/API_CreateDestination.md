---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateDestination.html
---

# CreateDestination
<a name="API_CreateDestination"></a>

 Create a notification destination such as Kinesis Data Streams that receive events and notifications from Managed integrations. Managed integrations uses the destination to determine where to deliver notifications.

## Request Syntax
<a name="API_CreateDestination_RequestSyntax"></a>

```
POST /destinations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "DeliveryDestinationArn": "{{string}}",
   "DeliveryDestinationType": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [DeliveryDestinationArn](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-DeliveryDestinationArn"></a>
The Amazon Resource Name (ARN) of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:[0-9a-zA-Z]+:[0-9a-zA-Z-]+:[0-9]+:[0-9a-zA-Z]+/[0-9a-zA-Z._-]+`
Required: Yes

 ** [DeliveryDestinationType](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-DeliveryDestinationType"></a>
The destination type for the customer-managed destination.
Type: String
Valid Values: `KINESIS`
Required: Yes

 ** [Description](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-Description"></a>
The description of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [Name](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-Name"></a>
The name of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: Yes

 ** [RoleArn](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the delivery destination role.
Type: String
Required: Yes

 ** [Tags](#API_CreateDestination_RequestSyntax) **   <a name="managedintegrations-CreateDestination-request-Tags"></a>
 *This parameter has been deprecated.*
A set of key/value pairs that are used to manage the destination.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDestination_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateDestination_ResponseSyntax) **   <a name="managedintegrations-CreateDestination-response-Name"></a>
The name of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`

## Errors
<a name="API_CreateDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
