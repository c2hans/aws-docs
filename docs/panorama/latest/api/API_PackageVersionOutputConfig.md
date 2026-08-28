---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_PackageVersionOutputConfig.html
---

# PackageVersionOutputConfig
<a name="API_PackageVersionOutputConfig"></a>

A package version output configuration.

## Contents
<a name="API_PackageVersionOutputConfig_Contents"></a>

 ** PackageName **   <a name="panorama-Type-PackageVersionOutputConfig-PackageName"></a>
The output's package name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** PackageVersion **   <a name="panorama-Type-PackageVersionOutputConfig-PackageVersion"></a>
The output's package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: Yes

 ** MarkLatest **   <a name="panorama-Type-PackageVersionOutputConfig-MarkLatest"></a>
Indicates that the version is recommended for all users.
Type: Boolean
Required: No

## See Also
<a name="API_PackageVersionOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/PackageVersionOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/PackageVersionOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/PackageVersionOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
