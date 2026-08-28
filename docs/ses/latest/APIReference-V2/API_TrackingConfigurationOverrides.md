---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_TrackingConfigurationOverrides.html
---

# TrackingConfigurationOverrides
<a name="API_TrackingConfigurationOverrides"></a>

An object that overrides, for a single email sending request, the engagement tracking settings that would otherwise apply. Use these overrides to turn open tracking or click tracking on or off for an individual message, for example to suppress tracking in a transactional message that you send from an account or a configuration set that has tracking enabled.

Without an override, engagement tracking is determined by your account-level `EngagementMetrics` setting, which you configure using the `PutAccountVdmAttributes` operation, by the `EngagementMetrics` setting of the configuration set that the message uses, which you configure using the `PutConfigurationSetVdmOptions` operation, and by whether that configuration set has an event destination whose `MatchingEventTypes` include the `OPEN` or `CLICK` event types.

For more information about tracking open and click events, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/event-publishing.html).

## Contents
<a name="API_TrackingConfigurationOverrides_Contents"></a>

 ** ClickTrackingEnabled **   <a name="SES-Type-TrackingConfigurationOverrides-ClickTrackingEnabled"></a>
Specifies whether Amazon SES tracks when the recipient clicks a link in this message. Can be one of the following:
+  `ENABLED` – Amazon SES tracks clicks for this message, even when your account-level and configuration set settings don't enable click tracking.
+  `DISABLED` – Amazon SES doesn't track clicks for this message, even when your account-level or configuration set settings enable click tracking. Amazon SES doesn't rewrite the links in the message.
If you don't specify this value, Amazon SES uses the click tracking setting that would otherwise apply to the message.
Enabling open or click tracking with an override doesn't create an event destination. Amazon SES records the resulting open and click events in VDM, where you can review them using VDM metrics and Message Insights. To also receive these events at a destination that you own, the configuration set that the message uses must have an event destination that publishes open and click events.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** OpenTrackingEnabled **   <a name="SES-Type-TrackingConfigurationOverrides-OpenTrackingEnabled"></a>
Specifies whether Amazon SES tracks when the recipient opens this message. Can be one of the following:
+  `ENABLED` – Amazon SES tracks opens for this message, even when your account-level and configuration set settings don't enable open tracking.
+  `DISABLED` – Amazon SES doesn't track opens for this message, even when your account-level or configuration set settings enable open tracking. Amazon SES doesn't add the tracking image to the message.
If you don't specify this value, Amazon SES uses the open tracking setting that would otherwise apply to the message.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_TrackingConfigurationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/TrackingConfigurationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/TrackingConfigurationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/TrackingConfigurationOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
