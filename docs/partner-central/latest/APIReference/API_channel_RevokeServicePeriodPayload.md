---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_RevokeServicePeriodPayload.html
---

# RevokeServicePeriodPayload
<a name="API_channel_RevokeServicePeriodPayload"></a>

Payload for revoke service period handshake requests.

## Contents
<a name="API_channel_RevokeServicePeriodPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** programManagementAccountIdentifier **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodPayload-programManagementAccountIdentifier"></a>
The identifier of the program management account.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/)?pma-[a-z0-9]{13}`
Required: Yes

 ** note **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodPayload-note"></a>
A note explaining the reason for revoking the service period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

## See Also
<a name="API_channel_RevokeServicePeriodPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/RevokeServicePeriodPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/RevokeServicePeriodPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/RevokeServicePeriodPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
