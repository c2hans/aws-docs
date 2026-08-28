---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_Campaign.html
---

# Campaign
<a name="API_connect-outbound-campaigns_Campaign"></a>

Contains information about an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns_Campaign_Contents"></a>

 ** arn **   <a name="connect-Type-connect-outbound-campaigns_Campaign-arn"></a>
The Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Required: Yes

 ** connectInstanceId **   <a name="connect-Type-connect-outbound-campaigns_Campaign-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** dialerConfig **   <a name="connect-Type-connect-outbound-campaigns_Campaign-dialerConfig"></a>
Contains information about the dialer configuration.
Type: [DialerConfig](API_connect-outbound-campaigns_DialerConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** id **   <a name="connect-Type-connect-outbound-campaigns_Campaign-id"></a>
The identifier of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="connect-Type-connect-outbound-campaigns_Campaign-name"></a>
The name of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** outboundCallConfig **   <a name="connect-Type-connect-outbound-campaigns_Campaign-outboundCallConfig"></a>
Contains information about the outbound call configuration.
Type: [OutboundCallConfig](API_connect-outbound-campaigns_OutboundCallConfig.md) object
Required: Yes

 ** tags **   <a name="connect-Type-connect-outbound-campaigns_Campaign-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_connect-outbound-campaigns_Campaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/Campaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/Campaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/Campaign)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
