---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetInstrumentationConfiguration.html
---

# GetInstrumentationConfiguration
<a name="API_GetInstrumentationConfiguration"></a>

Returns the details of a single instrumentation configuration identified by service, environment, signal type, and location. Use this to audit or display configuration details.

## Request Syntax
<a name="API_GetInstrumentationConfiguration_RequestSyntax"></a>

```
POST /get-instrumentation-configuration HTTP/1.1
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
<a name="API_GetInstrumentationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInstrumentationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Environment](#API_GetInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfiguration-request-Environment"></a>
The environment name for the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [InstrumentationType](#API_GetInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfiguration-request-InstrumentationType"></a>
The type of instrumentation configuration (`BREAKPOINT` or `PROBE`). Required to identify the configuration to retrieve.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** [LocationIdentifier](#API_GetInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfiguration-request-LocationIdentifier"></a>
The location identifier - either the full code location or a pre-computed location hash.
Type: [LocationIdentifier](API_LocationIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Service](#API_GetInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfiguration-request-Service"></a>
The service name for the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [SignalType](#API_GetInstrumentationConfiguration_RequestSyntax) **   <a name="applicationsignals-GetInstrumentationConfiguration-request-SignalType"></a>
The telemetry signal type for instrumentation.
+  `SNAPSHOT` - Captures a snapshot of the instrumentation point.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

## Response Syntax
<a name="API_GetInstrumentationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Configuration": {
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
}
```

## Response Elements
<a name="API_GetInstrumentationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configuration](#API_GetInstrumentationConfiguration_ResponseSyntax) **   <a name="applicationsignals-GetInstrumentationConfiguration-response-Configuration"></a>
The complete instrumentation configuration, including its location hash, capture settings, filters, expiration, and creation time.
Type: [InstrumentationConfiguration](API_InstrumentationConfiguration.md) object

## Errors
<a name="API_GetInstrumentationConfiguration_Errors"></a>

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
<a name="API_GetInstrumentationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/GetInstrumentationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/GetInstrumentationConfiguration)
