---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_EventParameters.html
---

# EventParameters
<a name="API_connect-customer-profiles_EventParameters"></a>

Configuration parameters for events in the personalization system.

## Contents
<a name="API_connect-customer-profiles_EventParameters_Contents"></a>

 ** EventType **   <a name="connect-Type-connect-customer-profiles_EventParameters-EventType"></a>
The type of event being tracked (e.g., 'click', 'purchase', 'view').
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** EventValueThreshold **   <a name="connect-Type-connect-customer-profiles_EventParameters-EventValueThreshold"></a>
The minimum value threshold that an event must meet to be considered valid.
Type: Double
Required: No

 ** EventWeight **   <a name="connect-Type-connect-customer-profiles_EventParameters-EventWeight"></a>
The weight of the event type. A higher weight means higher importance of the event type for the created solution.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## See Also
<a name="API_connect-customer-profiles_EventParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/EventParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/EventParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/EventParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
