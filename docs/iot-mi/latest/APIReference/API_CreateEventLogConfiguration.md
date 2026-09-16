---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateEventLogConfiguration.html
---

# CreateEventLogConfiguration
<a name="API_CreateEventLogConfiguration"></a>

Set the event log configuration for the account, resource type, or specific resource.

## Request Syntax
<a name="API_CreateEventLogConfiguration_RequestSyntax"></a>

```
POST /event-log-configurations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "EventLogLevel": "{{string}}",
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateEventLogConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEventLogConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateEventLogConfiguration-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [EventLogLevel](#API_CreateEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateEventLogConfiguration-request-EventLogLevel"></a>
The logging level for the event log configuration.
Type: String
Valid Values: `DEBUG | ERROR | INFO | WARN`
Required: Yes

 ** [ResourceId](#API_CreateEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateEventLogConfiguration-request-ResourceId"></a>
The identifier of the resource for the event log configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9+*]*`
Required: No

 ** [ResourceType](#API_CreateEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateEventLogConfiguration-request-ResourceType"></a>
The type of resource for the event log configuration.
Type: String
Pattern: `[*]$|^(managed-thing|credential-locker|provisioning-profile|ota-task|account-association)`
Required: Yes

## Response Syntax
<a name="API_CreateEventLogConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateEventLogConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_CreateEventLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-CreateEventLogConfiguration-response-Id"></a>
The identifier of the event log configuration request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

## Errors
<a name="API_CreateEventLogConfiguration_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded for this request.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateEventLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateEventLogConfiguration)
