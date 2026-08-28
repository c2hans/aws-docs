---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_RevokeServicePeriodHandshakeDetail.html
---

# RevokeServicePeriodHandshakeDetail
<a name="API_channel_RevokeServicePeriodHandshakeDetail"></a>

Details specific to revoke service period handshakes.

## Contents
<a name="API_channel_RevokeServicePeriodHandshakeDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** endDate **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodHandshakeDetail-endDate"></a>
The end date of the service period being revoked.
Type: Timestamp
Required: No

 ** minimumNoticeDays **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodHandshakeDetail-minimumNoticeDays"></a>
The minimum number of days notice required for revocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

 ** note **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodHandshakeDetail-note"></a>
A note explaining the reason for revoking the service period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** servicePeriodType **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodHandshakeDetail-servicePeriodType"></a>
The type of service period being revoked.
Type: String
Valid Values: `MINIMUM_NOTICE_PERIOD | FIXED_COMMITMENT_PERIOD`
Required: No

 ** startDate **   <a name="AWSPartnerCentral-Type-channel_RevokeServicePeriodHandshakeDetail-startDate"></a>
The start date of the service period being revoked.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_RevokeServicePeriodHandshakeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/RevokeServicePeriodHandshakeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/RevokeServicePeriodHandshakeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/RevokeServicePeriodHandshakeDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
