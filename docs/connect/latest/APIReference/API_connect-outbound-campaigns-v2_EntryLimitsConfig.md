---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_EntryLimitsConfig.html
---

# EntryLimitsConfig
<a name="API_connect-outbound-campaigns-v2_EntryLimitsConfig"></a>

Contains entry limits configuration for an outbound campaign. Entry limits control how many times a participant can enter a campaign and the minimum time interval between re-entries.

## Contents
<a name="API_connect-outbound-campaigns-v2_EntryLimitsConfig_Contents"></a>

 ** maxEntryCount **   <a name="connect-Type-connect-outbound-campaigns-v2_EntryLimitsConfig-maxEntryCount"></a>
The maximum number of times a participant can enter the campaign. A value of `0` indicates unlimited entries. Values of `1` or greater specify the exact number of entries allowed.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** minEntryInterval **   <a name="connect-Type-connect-outbound-campaigns-v2_EntryLimitsConfig-minEntryInterval"></a>
The minimum time interval that must pass before a participant can enter the campaign again, specified as an ISO 8601 duration string (for example, `PT4H` for 4 hours). A value of zero (for example, `PT0H`) indicates no minimum interval restriction, allowing participants to re-enter regardless of when they last entered.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?`
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns-v2_EntryLimitsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/EntryLimitsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/EntryLimitsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/EntryLimitsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
