---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_EventIntegration.html
---

# EventIntegration
<a name="API_connect-app-integrations_EventIntegration"></a>

The event integration.

## Contents
<a name="API_connect-app-integrations_EventIntegration_Contents"></a>

 ** Description **   <a name="connect-Type-connect-app-integrations_EventIntegration-Description"></a>
The event integration description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `.*`
Required: No

 ** EventBridgeBus **   <a name="connect-Type-connect-app-integrations_EventIntegration-EventBridgeBus"></a>
The Amazon EventBridge bus for the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

 ** EventFilter **   <a name="connect-Type-connect-app-integrations_EventIntegration-EventFilter"></a>
The event integration filter.
Type: [EventFilter](API_connect-app-integrations_EventFilter.md) object
Required: No

 ** EventIntegrationArn **   <a name="connect-Type-connect-app-integrations_EventIntegration-EventIntegrationArn"></a>
The Amazon Resource Name (ARN) of the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** Name **   <a name="connect-Type-connect-app-integrations_EventIntegration-Name"></a>
The name of the event integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

 ** Tags **   <a name="connect-Type-connect-app-integrations_EventIntegration-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-app-integrations_EventIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/EventIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/EventIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/EventIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
