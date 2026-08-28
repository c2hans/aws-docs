---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_channel_StartServicePeriodPayload.html
---

# StartServicePeriodPayload
<a name="API_channel_StartServicePeriodPayload"></a>

Payload for start service period handshake requests.

## Contents
<a name="API_channel_StartServicePeriodPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** programManagementAccountIdentifier **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodPayload-programManagementAccountIdentifier"></a>
The identifier of the program management account.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/program-management-account/)?pma-[a-z0-9]{13}`
Required: Yes

 ** servicePeriodType **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodPayload-servicePeriodType"></a>
The type of service period being started.
Type: String
Valid Values: `MINIMUM_NOTICE_PERIOD | FIXED_COMMITMENT_PERIOD`
Required: Yes

 ** endDate **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodPayload-endDate"></a>
The end date of the service period.
Type: Timestamp
Required: No

 ** minimumNoticeDays **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodPayload-minimumNoticeDays"></a>
The minimum number of days notice required for changes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]*`
Required: No

 ** note **   <a name="AWSPartnerCentral-Type-channel_StartServicePeriodPayload-note"></a>
A note providing additional information about the service period.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[^\x00-\x1F\x7F]*`
Required: No

## See Also
<a name="API_channel_StartServicePeriodPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-channel-2024-03-18/StartServicePeriodPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-channel-2024-03-18/StartServicePeriodPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-channel-2024-03-18/StartServicePeriodPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
