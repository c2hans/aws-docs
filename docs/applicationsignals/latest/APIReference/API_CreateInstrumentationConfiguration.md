---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateInstrumentationConfiguration.html
---

# CreateInstrumentationConfiguration
<a name="API_CreateInstrumentationConfiguration"></a>

Creates a dynamic instrumentation configuration for a specific code or endpoint location within a service and environment. Configurations are immutable after creation.

For `BREAKPOINT` type configurations, they expire after 24 hours unless a shorter expiration is provided. For `PROBE` type configurations, they persist until explicitly deleted; an expiration cannot be set for `PROBE` configurations.

If a configuration already exists for the same service, environment, signal type, and location, this operation returns a conflict instead of overwriting it. Use attribute filters and capture settings to control where the instrumentation runs and which data is collected.

## Request Syntax
<a name="API_CreateInstrumentationConfiguration_RequestSyntax"></a>

```
POST /create-instrumentation-configuration HTTP/1.1
Content-type: application/json

{
   "AttributeFilters": [
      {
         "{{string}}" : "{{string}}"
      }
   ],
   "CaptureConfiguration": { ... },
   "Description": "{{string}}",
   "Environment": "{{string}}",
   "ExpiresAt": {{number}},
   "InstrumentationType": "{{string}}",
   "Location": { ... },
   "Service": "{{string}}",
   "SignalType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateInstrumentationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateInstrumentationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttributeFilters](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-AttributeFilters"></a>
Client-side filters that target specific instances. Each object in the array is AND-matched on its keys, and multiple objects are OR-matched to decide where to apply the instrumentation.
Type: Array of string to string maps
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Value Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [CaptureConfiguration](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-CaptureConfiguration"></a>
Specifies what to capture when the instrumentation point is hit. Specify `CodeCapture` for code-level capture settings.
Type: [CaptureConfiguration](API_CaptureConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Description](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-Description"></a>
An optional short description (up to 50 characters) that explains the purpose of this instrumentation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [Environment](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-Environment"></a>
The environment that the service is running in, such as `eks:cluster-prod/namespace` or `ec2:production`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9:/+=,.@_-]+`
Required: Yes

 ** [ExpiresAt](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-ExpiresAt"></a>
For `BREAKPOINT`: optional, defaults to 24 hours, and must be between 5 minutes and 24 hours. For `PROBE`: not supported. `PROBE` configurations are permanent and persist until explicitly deleted.
Type: Timestamp
Required: No

 ** [InstrumentationType](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-InstrumentationType"></a>
The type of instrumentation: `BREAKPOINT` (temporary) or `PROBE` (permanent).
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** [Location](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-Location"></a>
The location where instrumentation should be applied. Specify a `CodeLocation` for code-level instrumentation.
Type: [Location](API_Location.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Service](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-Service"></a>
The name of the service to instrument. This should match the `service.name` resource attribute reported by the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9:/+=,.@_-]+`
Required: Yes

 ** [SignalType](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-SignalType"></a>
The telemetry signal type to emit for this instrumentation. The supported value is `SNAPSHOT`.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

 ** [Tags](#API_CreateInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-request-Tags"></a>
An optional list of key-value pairs to associate with the instrumentation configuration. Tags can help you organize and categorize your resources.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateInstrumentationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ARN": "string",
   "AttributeFilters": [
      {
         "string" : "string"
      }
   ],
   "CaptureConfiguration": { ... },
   "CreatedAt": number,
   "Description": "string",
   "Environment": "string",
   "ExpiresAt": number,
   "InstrumentationType": "string",
   "Location": { ... },
   "LocationHash": "string",
   "Service": "string",
   "SignalType": "string"
}
```

## Response Elements
<a name="API_CreateInstrumentationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-ARN"></a>
The ARN of the created instrumentation configuration.
Type: String
Pattern: `arn:[^:]+:application-signals:[^:]+:[0-9]{12}:instrumentationConfig/.+/[0-9a-f]{16}`

 ** [AttributeFilters](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-AttributeFilters"></a>
The attribute filters returned with the configuration so SDKs can perform client-side targeting.
Type: Array of string to string maps
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Value Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [CaptureConfiguration](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-CaptureConfiguration"></a>
The capture settings that were stored for this instrumentation configuration.
Type: [CaptureConfiguration](API_CaptureConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreatedAt](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-CreatedAt"></a>
The server-generated creation timestamp for this instrumentation configuration.
Type: Timestamp

 ** [Description](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-Description"></a>
The optional description that was stored with the instrumentation configuration.
Type: String

 ** [Environment](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-Environment"></a>
The environment for the instrumentation configuration, echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [ExpiresAt](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-ExpiresAt"></a>
The timestamp after which this configuration is no longer served to clients. Present only for `BREAKPOINT` configurations; `PROBE` configurations do not expire.
Type: Timestamp

 ** [InstrumentationType](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-InstrumentationType"></a>
The type of instrumentation that was created, echoed from the request.
Type: String
Valid Values: `BREAKPOINT | PROBE`

 ** [Location](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-Location"></a>
The location where instrumentation is applied, echoed from the request.
Type: [Location](API_Location.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [LocationHash](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-LocationHash"></a>
A stable hash computed from the location that uniquely identifies this instrumentation point within the service, environment, and signal type.
Type: String
Length Constraints: Fixed length of 16.

 ** [Service](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-Service"></a>
The service name for the instrumentation configuration, echoed from the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SignalType](#API_CreateInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-CreateInstrumentationConfiguration-response-SignalType"></a>
The telemetry signal type for the instrumentation configuration, echoed from the request.
Type: String
Valid Values: `SNAPSHOT`

## Errors
<a name="API_CreateInstrumentationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateInstrumentationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/CreateInstrumentationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CreateInstrumentationConfiguration)
