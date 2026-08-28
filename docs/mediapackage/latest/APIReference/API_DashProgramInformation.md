---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashProgramInformation.html
---

# DashProgramInformation
<a name="API_DashProgramInformation"></a>

Details about the content that you want MediaPackage to pass through in the manifest to the playback device.

## Contents
<a name="API_DashProgramInformation_Contents"></a>

 ** Copyright **   <a name="mediapackage-Type-DashProgramInformation-Copyright"></a>
A copyright statement about the content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** LanguageCode **   <a name="mediapackage-Type-DashProgramInformation-LanguageCode"></a>
The language code for this manifest.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]`
Required: No

 ** MoreInformationUrl **   <a name="mediapackage-Type-DashProgramInformation-MoreInformationUrl"></a>
An absolute URL that contains more information about this content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Source **   <a name="mediapackage-Type-DashProgramInformation-Source"></a>
Information about the content provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Title **   <a name="mediapackage-Type-DashProgramInformation-Title"></a>
The title for the manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_DashProgramInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashProgramInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashProgramInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashProgramInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
