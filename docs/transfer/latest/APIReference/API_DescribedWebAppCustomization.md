---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedWebAppCustomization.html
---

# DescribedWebAppCustomization
<a name="API_DescribedWebAppCustomization"></a>

A structure that contains the customization fields for the web app. You can provide a title, logo, and icon to customize the appearance of your web app.

## Contents
<a name="API_DescribedWebAppCustomization_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedWebAppCustomization-Arn"></a>
Returns the Amazon Resource Name (ARN) for the web app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** WebAppId **   <a name="TransferFamily-Type-DescribedWebAppCustomization-WebAppId"></a>
Returns the unique identifier for your web app.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

 ** FaviconFile **   <a name="TransferFamily-Type-DescribedWebAppCustomization-FaviconFile"></a>
Returns an icon file data string (in base64 encoding).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 20960.
Required: No

 ** LogoFile **   <a name="TransferFamily-Type-DescribedWebAppCustomization-LogoFile"></a>
Returns a logo file data string (in base64 encoding).
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** Title **   <a name="TransferFamily-Type-DescribedWebAppCustomization-Title"></a>
Returns the page title that you defined for your web app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_DescribedWebAppCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedWebAppCustomization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedWebAppCustomization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedWebAppCustomization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
