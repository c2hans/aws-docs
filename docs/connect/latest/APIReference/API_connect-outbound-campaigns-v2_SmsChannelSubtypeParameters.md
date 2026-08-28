---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_SmsChannelSubtypeParameters.html
---

# SmsChannelSubtypeParameters
<a name="API_connect-outbound-campaigns-v2_SmsChannelSubtypeParameters"></a>

The overridden SMS parameters for an outbound request of a campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_SmsChannelSubtypeParameters_Contents"></a>

 ** destinationPhoneNumber **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeParameters-destinationPhoneNumber"></a>
The destination phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `[\d\-+]*`
Required: Yes

 ** templateParameters **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeParameters-templateParameters"></a>
The parameters for the Amazon Q in Connect template.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 32767.
Key Pattern: `[a-zA-Z0-9\-_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Value Pattern: `.*`
Required: Yes

 ** connectSourcePhoneNumberArn **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeParameters-connectSourcePhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the Connect Customer source phone number for the outbound request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: No

 ** templateArn **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeParameters-templateArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect template for the outbound request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_SmsChannelSubtypeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/SmsChannelSubtypeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/SmsChannelSubtypeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/SmsChannelSubtypeParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
