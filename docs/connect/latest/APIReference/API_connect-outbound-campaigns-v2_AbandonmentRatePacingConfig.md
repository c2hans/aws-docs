---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_AbandonmentRatePacingConfig.html
---

# AbandonmentRatePacingConfig
<a name="API_connect-outbound-campaigns-v2_AbandonmentRatePacingConfig"></a>

The configuration for abandonment-rate-based dialer pacing. The dialer adjusts its dialing rate to keep the call abandonment rate at or below the target rate.

## Contents
<a name="API_connect-outbound-campaigns-v2_AbandonmentRatePacingConfig_Contents"></a>

 ** connectionStartPoint **   <a name="connect-Type-connect-outbound-campaigns-v2_AbandonmentRatePacingConfig-connectionStartPoint"></a>
The reference point from which `connectionThresholdSeconds` is measured.
Type: String
Valid Values: `CONNECTED_TO_SYSTEM | GREETING_START | GREETING_END`
Required: Yes

 ** connectionThresholdSeconds **   <a name="connect-Type-connect-outbound-campaigns-v2_AbandonmentRatePacingConfig-connectionThresholdSeconds"></a>
The number of seconds after the `connectionStartPoint` before an unconnected contact is counted as abandoned. The minimum value is 1 second.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** evaluationWindow **   <a name="connect-Type-connect-outbound-campaigns-v2_AbandonmentRatePacingConfig-evaluationWindow"></a>
The rolling time window over which the abandonment rate is calculated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5.
Pattern: `PT([1-9]|1[0-9]|2[0-4])H`
Required: Yes

 ** targetRate **   <a name="connect-Type-connect-outbound-campaigns-v2_AbandonmentRatePacingConfig-targetRate"></a>
The target call abandonment rate, expressed as a value between 0.0 and 1.0 (0 percent to 100 percent). The dialer paces outbound calls to keep the abandonment rate at or below this value.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns-v2_AbandonmentRatePacingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/AbandonmentRatePacingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/AbandonmentRatePacingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/AbandonmentRatePacingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
