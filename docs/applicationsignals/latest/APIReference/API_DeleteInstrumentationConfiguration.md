---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteInstrumentationConfiguration.html
---

# DeleteInstrumentationConfiguration
<a name="API_DeleteInstrumentationConfiguration"></a>

Deletes the specified instrumentation configuration. SDKs remove the instrumentation during their next sync after the configuration is deleted or expires.

## Request Syntax
<a name="API_DeleteInstrumentationConfiguration_RequestSyntax"></a>

```
POST /delete-instrumentation-configuration HTTP/1.1
Content-type: application/json

{
   "Environment": "{{string}}",
   "InstrumentationType": "{{string}}",
   "LocationIdentifier": { ... },
   "Service": "{{string}}",
   "SignalType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteInstrumentationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteInstrumentationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Environment](#API_DeleteInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-DeleteInstrumentationConfiguration-request-Environment"></a>
The environment name for the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [InstrumentationType](#API_DeleteInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-DeleteInstrumentationConfiguration-request-InstrumentationType"></a>
The type of instrumentation configuration (`BREAKPOINT` or `PROBE`). Required to identify the configuration to delete.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** [LocationIdentifier](#API_DeleteInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-DeleteInstrumentationConfiguration-request-LocationIdentifier"></a>
The location identifier - either the full code location or a pre-computed location hash.
Type: [LocationIdentifier](API_LocationIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Service](#API_DeleteInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-DeleteInstrumentationConfiguration-request-Service"></a>
The service name for the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [SignalType](#API_DeleteInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-DeleteInstrumentationConfiguration-request-SignalType"></a>
The telemetry signal type for instrumentation.
+  `SNAPSHOT` - Captures a snapshot of the instrumentation point.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

## Response Syntax
<a name="API_DeleteInstrumentationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeletionStatus": "string"
}
```

## Response Elements
<a name="API_DeleteInstrumentationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionStatus](#API_DeleteInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-DeleteInstrumentationConfiguration-response-DeletionStatus"></a>
The result of the delete request. The value is `DELETED` when the configuration has been removed.
Type: String
Valid Values: `DELETED`

## Errors
<a name="API_DeleteInstrumentationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteInstrumentationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/DeleteInstrumentationConfiguration)
