---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TriggerConfig.html
---

# TriggerConfig
<a name="API_connect-customer-profiles_TriggerConfig"></a>

The trigger settings that determine how and when Amazon AppFlow runs the specified flow.

## Contents
<a name="API_connect-customer-profiles_TriggerConfig_Contents"></a>

 ** TriggerType **   <a name="connect-Type-connect-customer-profiles_TriggerConfig-TriggerType"></a>
Specifies the type of flow trigger. It can be OnDemand, Scheduled, or Event.
Type: String
Valid Values: `Scheduled | Event | OnDemand`
Required: Yes

 ** TriggerProperties **   <a name="connect-Type-connect-customer-profiles_TriggerConfig-TriggerProperties"></a>
Specifies the configuration details of a schedule-triggered flow that you define. Currently, these settings only apply to the Scheduled trigger type.
Type: [TriggerProperties](API_connect-customer-profiles_TriggerProperties.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_TriggerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/TriggerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/TriggerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/TriggerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
