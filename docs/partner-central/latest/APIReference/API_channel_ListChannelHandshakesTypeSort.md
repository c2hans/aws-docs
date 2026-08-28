---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_ListChannelHandshakesTypeSort.html
---

# ListChannelHandshakesTypeSort
<a name="API_channel_ListChannelHandshakesTypeSort"></a>

Type-specific sorting options for listing channel handshakes.

## Contents
<a name="API_channel_ListChannelHandshakesTypeSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** programManagementAccountTypeSort **   <a name="AWSPartnerCentral-Type-channel_ListChannelHandshakesTypeSort-programManagementAccountTypeSort"></a>
Sorting options specific to program management account handshakes.
Type: [ProgramManagementAccountTypeSort](API_channel_ProgramManagementAccountTypeSort.md) object
Required: No

 ** revokeServicePeriodTypeSort **   <a name="AWSPartnerCentral-Type-channel_ListChannelHandshakesTypeSort-revokeServicePeriodTypeSort"></a>
Sorting options specific to revoke service period handshakes.
Type: [RevokeServicePeriodTypeSort](API_channel_RevokeServicePeriodTypeSort.md) object
Required: No

 ** startServicePeriodTypeSort **   <a name="AWSPartnerCentral-Type-channel_ListChannelHandshakesTypeSort-startServicePeriodTypeSort"></a>
Sorting options specific to start service period handshakes.
Type: [StartServicePeriodTypeSort](API_channel_StartServicePeriodTypeSort.md) object
Required: No

## See Also
<a name="API_channel_ListChannelHandshakesTypeSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/ListChannelHandshakesTypeSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/ListChannelHandshakesTypeSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/ListChannelHandshakesTypeSort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
