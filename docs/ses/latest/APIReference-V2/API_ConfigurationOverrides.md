---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ConfigurationOverrides.html
---

# ConfigurationOverrides
<a name="API_ConfigurationOverrides"></a>

An object that overrides settings for a single email sending request. An override applies only to the message or messages in the request that contains it. It doesn't change your account-level settings, and it doesn't change the configuration set that the request uses.

A setting that you don't override keeps the value that would otherwise apply to the message. Depending on the setting, that value comes from the configuration set that the message uses, from your account-level settings, or from the Amazon SES default.

## Contents
<a name="API_ConfigurationOverrides_Contents"></a>

 ** Tracking **   <a name="SES-Type-ConfigurationOverrides-Tracking"></a>
An object that overrides the open and click tracking settings that would otherwise apply to the message.
Type: [TrackingConfigurationOverrides](API_TrackingConfigurationOverrides.md) object
Required: No

## See Also
<a name="API_ConfigurationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ConfigurationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ConfigurationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ConfigurationOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
