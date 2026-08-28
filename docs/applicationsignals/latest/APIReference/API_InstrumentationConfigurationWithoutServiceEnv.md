---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_InstrumentationConfigurationWithoutServiceEnv.html
---

# InstrumentationConfigurationWithoutServiceEnv
<a name="API_InstrumentationConfigurationWithoutServiceEnv"></a>

An instrumentation configuration that omits service and environment because they are provided at a higher level, such as in a list response.

## Contents
<a name="API_InstrumentationConfigurationWithoutServiceEnv_Contents"></a>

 ** ARN **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-ARN"></a>
The ARN for the instrumentation configuration.
Type: String
Pattern: `arn:[^:]+:application-signals:[^:]+:[0-9]{12}:instrumentationConfig/.+/[0-9a-f]{16}`
Required: Yes

 ** CaptureConfiguration **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-CaptureConfiguration"></a>
The capture settings for this instrumentation configuration.
Type: [CaptureConfiguration](API_CaptureConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** CreatedAt **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-CreatedAt"></a>
The timestamp when this instrumentation configuration was created.
Type: Timestamp
Required: Yes

 ** InstrumentationType **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-InstrumentationType"></a>
The type of instrumentation for this configuration.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** Location **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-Location"></a>
The location where this instrumentation is applied.
Type: [Location](API_Location.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** LocationHash **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-LocationHash"></a>
The stable hash derived from the location that identifies this instrumentation point.
Type: String
Length Constraints: Fixed length of 16.
Required: Yes

 ** SignalType **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-SignalType"></a>
The telemetry signal type for this instrumentation configuration.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

 ** AttributeFilters **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-AttributeFilters"></a>
Client-side filters that determine which instances apply this instrumentation.
Type: Array of string to string maps
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Value Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Description **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-Description"></a>
An optional short description of the instrumentation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** ExpiresAt **   <a name="applicationsignals-Type-InstrumentationConfigurationWithoutServiceEnv-ExpiresAt"></a>
The timestamp when this configuration expires.
Type: Timestamp
Required: No

## See Also
<a name="API_InstrumentationConfigurationWithoutServiceEnv_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/InstrumentationConfigurationWithoutServiceEnv)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/InstrumentationConfigurationWithoutServiceEnv)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/InstrumentationConfigurationWithoutServiceEnv)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
