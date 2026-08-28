---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExtensionSummary.html
---

# ExtensionSummary
<a name="API_ExtensionSummary"></a>

Information about an extension. Call `GetExtension` to get more information about an extension.

## Contents
<a name="API_ExtensionSummary_Contents"></a>

 ** Arn **   <a name="appconfig-Type-ExtensionSummary-Arn"></a>
The system-generated Amazon Resource Name (ARN) for the extension.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: No

 ** Description **   <a name="appconfig-Type-ExtensionSummary-Description"></a>
Information about the extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Id **   <a name="appconfig-Type-ExtensionSummary-Id"></a>
The system-generated ID of the extension.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Name **   <a name="appconfig-Type-ExtensionSummary-Name"></a>
The extension name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** VersionNumber **   <a name="appconfig-Type-ExtensionSummary-VersionNumber"></a>
The extension version number.
Type: Integer
Required: No

## See Also
<a name="API_ExtensionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExtensionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExtensionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExtensionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
