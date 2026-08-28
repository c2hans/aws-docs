---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetEventLogConfiguration.html
---

# GetEventLogConfiguration
<a name="API_GetEventLogConfiguration"></a>

Get an event log configuration.

## Request Syntax
<a name="API_GetEventLogConfiguration_RequestSyntax"></a>

```
GET /event-log-configurations/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEventLogConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetEventLogConfiguration_RequestSyntax) **   <a name="managedintegrations-GetEventLogConfiguration-request-uri-Id"></a>
The identifier of the event log configuration.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetEventLogConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEventLogConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventLogLevel": "string",
   "Id": "string",
   "ResourceId": "string",
   "ResourceType": "string"
}
```

## Response Elements
<a name="API_GetEventLogConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventLogLevel](#API_GetEventLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetEventLogConfiguration-response-EventLogLevel"></a>
The logging level for the event log configuration.
Type: String
Valid Values: `DEBUG | ERROR | INFO | WARN`

 ** [Id](#API_GetEventLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetEventLogConfiguration-response-Id"></a>
The identifier of the event log configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

 ** [ResourceId](#API_GetEventLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetEventLogConfiguration-response-ResourceId"></a>
The identifier of the resource for the event log configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9+*]*`

 ** [ResourceType](#API_GetEventLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetEventLogConfiguration-response-ResourceType"></a>
The type of resource for the event log configuration.
Type: String
Pattern: `[*]$|^(managed-thing|credential-locker|provisioning-profile|ota-task|account-association)`

## Errors
<a name="API_GetEventLogConfiguration_Errors"></a>

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
<a name="API_GetEventLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetEventLogConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
