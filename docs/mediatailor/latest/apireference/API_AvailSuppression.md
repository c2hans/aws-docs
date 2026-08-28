---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AvailSuppression.html
---

# AvailSuppression
<a name="API_AvailSuppression"></a>

The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).

## Contents
<a name="API_AvailSuppression_Contents"></a>

 ** FillPolicy **   <a name="mediatailor-Type-AvailSuppression-FillPolicy"></a>
Defines the policy to apply to the avail suppression mode. `BEHIND_LIVE_EDGE` will always use the full avail suppression policy. `AFTER_LIVE_EDGE` mode can be used to invoke partial ad break fills when a session starts mid-break.
Type: String
Valid Values: `FULL_AVAIL_ONLY | PARTIAL_AVAIL`
Required: No

 ** Mode **   <a name="mediatailor-Type-AvailSuppression-Mode"></a>
Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to `BEHIND_LIVE_EDGE`, ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to `AFTER_LIVE_EDGE`, ad suppression is active and MediaTailor won't fill ad breaks that are within the live edge plus the avail suppression value.
Type: String
Valid Values: `OFF | BEHIND_LIVE_EDGE | AFTER_LIVE_EDGE`
Required: No

 ** Value **   <a name="mediatailor-Type-AvailSuppression-Value"></a>
A live edge offset time in HH:MM:SS. MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.
Type: String
Required: No

## See Also
<a name="API_AvailSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AvailSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AvailSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AvailSuppression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
