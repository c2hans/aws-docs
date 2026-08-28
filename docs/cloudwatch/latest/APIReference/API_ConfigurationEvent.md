---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ConfigurationEvent.html
---

# ConfigurationEvent
<a name="API_ConfigurationEvent"></a>

 The event information.

## Contents
<a name="API_ConfigurationEvent_Contents"></a>

 ** AccountId **   <a name="appinsights-Type-ConfigurationEvent-AccountId"></a>
The AWS account ID for the owner of the application to which the configuration event belongs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** EventDetail **   <a name="appinsights-Type-ConfigurationEvent-EventDetail"></a>
 The details of the event in plain text.
Type: String
Required: No

 ** EventResourceName **   <a name="appinsights-Type-ConfigurationEvent-EventResourceName"></a>
 The name of the resource Application Insights attempted to configure.
Type: String
Required: No

 ** EventResourceType **   <a name="appinsights-Type-ConfigurationEvent-EventResourceType"></a>
 The resource type that Application Insights attempted to configure, for example, CLOUDWATCH\_ALARM.
Type: String
Valid Values: `CLOUDWATCH_ALARM | CLOUDWATCH_LOG | CLOUDFORMATION | SSM_ASSOCIATION`
Required: No

 ** EventStatus **   <a name="appinsights-Type-ConfigurationEvent-EventStatus"></a>
 The status of the configuration update event. Possible values include INFO, WARN, and ERROR.
Type: String
Valid Values: `INFO | WARN | ERROR`
Required: No

 ** EventTime **   <a name="appinsights-Type-ConfigurationEvent-EventTime"></a>
 The timestamp of the event.
Type: Timestamp
Required: No

 ** MonitoredResourceARN **   <a name="appinsights-Type-ConfigurationEvent-MonitoredResourceARN"></a>
 The resource monitored by Application Insights.
Type: String
Required: No

 ** ResourceGroupName **   <a name="appinsights-Type-ConfigurationEvent-ResourceGroupName"></a>
The name of the resource group of the application to which the configuration event belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

## See Also
<a name="API_ConfigurationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ConfigurationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ConfigurationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ConfigurationEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
