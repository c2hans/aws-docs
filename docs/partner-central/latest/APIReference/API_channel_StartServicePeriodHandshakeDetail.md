---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_StartServicePeriodHandshakeDetail.html
---

# StartServicePeriodHandshakeDetail
<a name="API_channel_StartServicePeriodHandshakeDetail"></a>

Details specific to start service period handshakes.

## Contents
<a name="API_channel_StartServicePeriodHandshakeDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** endDate **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodHandshakeDetail-endDate"></a>
The end date of the service period.
Type: Timestamp
Required: No

 ** minimumNoticeDays **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodHandshakeDetail-minimumNoticeDays"></a>
The minimum number of days notice required for changes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

 ** note **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodHandshakeDetail-note"></a>
A note providing additional information about the service period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

 ** servicePeriodType **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodHandshakeDetail-servicePeriodType"></a>
The type of service period being started.
Type: String
Valid Values: `MINIMUM_NOTICE_PERIOD | FIXED_COMMITMENT_PERIOD`
Required: No

 ** startDate **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodHandshakeDetail-startDate"></a>
The start date of the service period.
Type: Timestamp
Required: No

## See Also
<a name="API_channel_StartServicePeriodHandshakeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/StartServicePeriodHandshakeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/StartServicePeriodHandshakeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/StartServicePeriodHandshakeDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
