---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_EmailOutboundConfig.html
---

# EmailOutboundConfig
<a name="API_connect-outbound-campaigns-v2_EmailOutboundConfig"></a>

The outbound configuration for email.

## Contents
<a name="API_connect-outbound-campaigns-v2_EmailOutboundConfig_Contents"></a>

 ** connectSourceEmailAddress **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailOutboundConfig-connectSourceEmailAddress"></a>
The Connect Customer source email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*[^\s@]+@[^\s@]+\.[^\s@]+.*`
Required: Yes

 ** wisdomTemplateArn **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailOutboundConfig-wisdomTemplateArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: Yes

 ** sourceEmailAddressDisplayName **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailOutboundConfig-sourceEmailAddressDisplayName"></a>
The display name for the Connect Customer source email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_EmailOutboundConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/EmailOutboundConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/EmailOutboundConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/EmailOutboundConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
