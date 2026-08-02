---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_InstrumentationConfiguration.html
---

# InstrumentationConfiguration
<a name="API_InstrumentationConfiguration"></a>

The full instrumentation configuration, including the instrumentation type, service, environment, signal type, location details, stable location hash, capture settings, filters, expiration, creation time, and ARN.

## Contents
<a name="API_InstrumentationConfiguration_Contents"></a>

 ** ARN **   <a name="applicationsignals-Type-InstrumentationConfiguration-ARN"></a>
The ARN for the instrumentation configuration.
Type: String
Pattern: `arn:[^:]+:application-signals:[^:]+:[0-9]{12}:instrumentationConfig/.+/[0-9a-f]{16}`
Required: Yes

 ** CaptureConfiguration **   <a name="applicationsignals-Type-InstrumentationConfiguration-CaptureConfiguration"></a>
The capture settings for this instrumentation configuration.
Type: [CaptureConfiguration](API_CaptureConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** CreatedAt **   <a name="applicationsignals-Type-InstrumentationConfiguration-CreatedAt"></a>
The timestamp when this instrumentation configuration was created.
Type: Timestamp
Required: Yes

 ** Environment **   <a name="applicationsignals-Type-InstrumentationConfiguration-Environment"></a>
The environment where the service is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** InstrumentationType **   <a name="applicationsignals-Type-InstrumentationConfiguration-InstrumentationType"></a>
The type of instrumentation for this configuration.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** Location **   <a name="applicationsignals-Type-InstrumentationConfiguration-Location"></a>
The location where this instrumentation is applied.
Type: [Location](API_Location.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** LocationHash **   <a name="applicationsignals-Type-InstrumentationConfiguration-LocationHash"></a>
The stable hash derived from the location that uniquely identifies this instrumentation point within the service and environment.
Type: String
Length Constraints: Fixed length of 16.
Required: Yes

 ** Service **   <a name="applicationsignals-Type-InstrumentationConfiguration-Service"></a>
The service that this instrumentation configuration targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** SignalType **   <a name="applicationsignals-Type-InstrumentationConfiguration-SignalType"></a>
The telemetry signal type for this instrumentation configuration.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

 ** AttributeFilters **   <a name="applicationsignals-Type-InstrumentationConfiguration-AttributeFilters"></a>
Client-side filters that determine which instances apply this instrumentation.
Type: Array of string to string maps
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Value Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Description **   <a name="applicationsignals-Type-InstrumentationConfiguration-Description"></a>
An optional short description of the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** ExpiresAt **   <a name="applicationsignals-Type-InstrumentationConfiguration-ExpiresAt"></a>
The timestamp when this configuration expires.
Type: Timestamp
Required: No

## See Also
<a name="API_InstrumentationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/InstrumentationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/InstrumentationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/InstrumentationConfiguration)
