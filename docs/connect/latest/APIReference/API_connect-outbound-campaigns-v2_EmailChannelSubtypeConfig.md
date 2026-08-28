---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_EmailChannelSubtypeConfig.html
---

# EmailChannelSubtypeConfig
<a name="API_connect-outbound-campaigns-v2_EmailChannelSubtypeConfig"></a>

The configuration for email channel subtype.

## Contents
<a name="API_connect-outbound-campaigns-v2_EmailChannelSubtypeConfig_Contents"></a>

 ** defaultOutboundConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeConfig-defaultOutboundConfig"></a>
The default email outbound configuration of an outbound campaign.
Type: [EmailOutboundConfig](API_connect-outbound-campaigns-v2_EmailOutboundConfig.md) object
Required: Yes

 ** outboundMode **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeConfig-outboundMode"></a>
The outbound mode of email for an outbound campaign.
Type: [EmailOutboundMode](API_connect-outbound-campaigns-v2_EmailOutboundMode.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** capacity **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeConfig-capacity"></a>
The allocation of email capacity between multiple running outbound campaigns.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 1.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_EmailChannelSubtypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/EmailChannelSubtypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/EmailChannelSubtypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/EmailChannelSubtypeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
