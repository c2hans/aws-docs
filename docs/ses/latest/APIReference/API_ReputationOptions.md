---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ReputationOptions.html
---

# ReputationOptions
<a name="API_ReputationOptions"></a>

Contains information about the reputation settings for a configuration set.

## Contents
<a name="API_ReputationOptions_Contents"></a>

 ** LastFreshStart **
The date and time at which the reputation metrics for the configuration set were last reset. Resetting these metrics is known as a *fresh start*.
When you disable email sending for a configuration set using [UpdateConfigurationSetSendingEnabled](API_UpdateConfigurationSetSendingEnabled.md) and later re-enable it, the reputation metrics for the configuration set (but not for the entire Amazon SES account) are reset.
If email sending for the configuration set has never been disabled and later re-enabled, the value of this attribute is `null`.
Type: Timestamp
Required: No

 ** ReputationMetricsEnabled **
Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.
If the value is `true`, reputation metrics are published. If the value is `false`, reputation metrics are not published. The default value is `false`.
Type: Boolean
Required: No

 ** SendingEnabled **
Describes whether email sending is enabled or disabled for the configuration set. If the value is `true`, then Amazon SES sends emails that use the configuration set. If the value is `false`, Amazon SES does not send emails that use the configuration set. The default value is `true`. You can change this setting using [UpdateConfigurationSetSendingEnabled](API_UpdateConfigurationSetSendingEnabled.md).
Type: Boolean
Required: No

## See Also
<a name="API_ReputationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ReputationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ReputationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ReputationOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
