---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_HandshakeDetail.html
---

# HandshakeDetail
<a name="API_channel_HandshakeDetail"></a>

Contains detailed information about different types of handshakes.

## Contents
<a name="API_channel_HandshakeDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** programManagementAccountHandshakeDetail **   <a name="AWSPartnerCentral-Type-channel_HandshakeDetail-programManagementAccountHandshakeDetail"></a>
Details for a program management account handshake.
Type: [ProgramManagementAccountHandshakeDetail](API_channel_ProgramManagementAccountHandshakeDetail.md) object
Required: No

 ** revokeServicePeriodHandshakeDetail **   <a name="AWSPartnerCentral-Type-channel_HandshakeDetail-revokeServicePeriodHandshakeDetail"></a>
Details for a revoke service period handshake.
Type: [RevokeServicePeriodHandshakeDetail](API_channel_RevokeServicePeriodHandshakeDetail.md) object
Required: No

 ** startServicePeriodHandshakeDetail **   <a name="AWSPartnerCentral-Type-channel_HandshakeDetail-startServicePeriodHandshakeDetail"></a>
Details for a start service period handshake.
Type: [StartServicePeriodHandshakeDetail](API_channel_StartServicePeriodHandshakeDetail.md) object
Required: No

## See Also
<a name="API_channel_HandshakeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/HandshakeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/HandshakeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/HandshakeDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
