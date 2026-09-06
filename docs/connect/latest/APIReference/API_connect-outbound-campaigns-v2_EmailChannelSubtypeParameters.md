---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_EmailChannelSubtypeParameters.html
---

# EmailChannelSubtypeParameters
<a name="API_connect-outbound-campaigns-v2_EmailChannelSubtypeParameters"></a>

The overridden email parameters for an outbound request of a campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_EmailChannelSubtypeParameters_Contents"></a>

 ** destinationEmailAddress **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeParameters-destinationEmailAddress"></a>
The destination email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*[^\s@]+@[^\s@]+\.[^\s@]+.*`
Required: Yes

 ** templateParameters **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeParameters-templateParameters"></a>
The parameters for the Amazon Q in Connect template.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 32767.
Key Pattern: `[a-zA-Z0-9\-_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Value Pattern: `.*`
Required: Yes

 ** connectSourceEmailAddress **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeParameters-connectSourceEmailAddress"></a>
The Connect Customer source email address for the outbound request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*[^\s@]+@[^\s@]+\.[^\s@]+.*`
Required: No

 ** templateArn **   <a name="connect-Type-connect-outbound-campaigns-v2_EmailChannelSubtypeParameters-templateArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect template for the outbound request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_EmailChannelSubtypeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/EmailChannelSubtypeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/EmailChannelSubtypeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/EmailChannelSubtypeParameters)
