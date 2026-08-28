---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientLoginBannerOptions.html
---

# ClientLoginBannerOptions
<a name="API_ClientLoginBannerOptions"></a>

Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.

## Contents
<a name="API_ClientLoginBannerOptions_Contents"></a>

 ** BannerText **
Customizable text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.
Type: String
Required: No

 ** Enabled **
Enable or disable a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
Valid values: `true | false`
Default value: `false`
Type: Boolean
Required: No

## See Also
<a name="API_ClientLoginBannerOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientLoginBannerOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientLoginBannerOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientLoginBannerOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
