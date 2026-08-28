---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_EventLogConfigurationSummary.html
---

# EventLogConfigurationSummary
<a name="API_EventLogConfigurationSummary"></a>

List of event log configurations.

## Contents
<a name="API_EventLogConfigurationSummary_Contents"></a>

 ** EventLogLevel **   <a name="managedintegrations-Type-EventLogConfigurationSummary-EventLogLevel"></a>
The logging level for the event log configuration.
Type: String
Valid Values: `DEBUG | ERROR | INFO | WARN`
Required: No

 ** Id **   <a name="managedintegrations-Type-EventLogConfigurationSummary-Id"></a>
The identifier of the event log configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** ResourceId **   <a name="managedintegrations-Type-EventLogConfigurationSummary-ResourceId"></a>
The identifier of the resource for the event log configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9+*]*`
Required: No

 ** ResourceType **   <a name="managedintegrations-Type-EventLogConfigurationSummary-ResourceType"></a>
The type of resource for the event log configuration.
Type: String
Pattern: `[*]$|^(managed-thing|credential-locker|provisioning-profile|ota-task|account-association)`
Required: No

## See Also
<a name="API_EventLogConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/EventLogConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/EventLogConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/EventLogConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
