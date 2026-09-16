---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateEventLogConfiguration.html
---

# UpdateEventLogConfiguration
<a name="API_UpdateEventLogConfiguration"></a>

Update an event log configuration by log configuration ID.

## Request Syntax
<a name="API_UpdateEventLogConfiguration_RequestSyntax"></a>

```
PATCH /event-log-configurations/{{Id}} HTTP/1.1
Content-type: application/json

{
   "EventLogLevel": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEventLogConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-UpdateEventLogConfiguration-request-uri-Id"></a>
The log configuration id.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateEventLogConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EventLogLevel](#API_UpdateEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-UpdateEventLogConfiguration-request-EventLogLevel"></a>
The log level for the event in terms of severity.
Type: String
Valid Values: `DEBUG | ERROR | INFO | WARN`
Required: Yes

## Response Syntax
<a name="API_UpdateEventLogConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateEventLogConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateEventLogConfiguration_Errors"></a>

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
<a name="API_UpdateEventLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateEventLogConfiguration)
