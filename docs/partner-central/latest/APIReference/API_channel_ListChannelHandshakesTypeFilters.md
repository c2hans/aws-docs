---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListChannelHandshakesTypeFilters.html
---

# ListChannelHandshakesTypeFilters
<a name="API_channel_ListChannelHandshakesTypeFilters"></a>

Type-specific filters for listing channel handshakes.

## Contents
<a name="API_channel_ListChannelHandshakesTypeFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** programManagementAccountTypeFilters **   <a name="AWSPartnerCentral-Type-channel_ListChannelHandshakesTypeFilters-programManagementAccountTypeFilters"></a>
Filters specific to program management account handshakes.
Type: [ProgramManagementAccountTypeFilters](API_channel_ProgramManagementAccountTypeFilters.md) object
Required: No

 ** revokeServicePeriodTypeFilters **   <a name="AWSPartnerCentral-Type-channel_ListChannelHandshakesTypeFilters-revokeServicePeriodTypeFilters"></a>
Filters specific to revoke service period handshakes.
Type: [RevokeServicePeriodTypeFilters](API_channel_RevokeServicePeriodTypeFilters.md) object
Required: No

 ** startServicePeriodTypeFilters **   <a name="AWSPartnerCentral-Type-channel_ListChannelHandshakesTypeFilters-startServicePeriodTypeFilters"></a>
Filters specific to start service period handshakes.
Type: [StartServicePeriodTypeFilters](API_channel_StartServicePeriodTypeFilters.md) object
Required: No

## See Also
<a name="API_channel_ListChannelHandshakesTypeFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ListChannelHandshakesTypeFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ListChannelHandshakesTypeFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ListChannelHandshakesTypeFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
