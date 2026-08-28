---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_IdeConfiguration.html
---

# IdeConfiguration
<a name="API_IdeConfiguration"></a>

Information about the configuration of an integrated development environment (IDE) for a Dev Environment.

## Contents
<a name="API_IdeConfiguration_Contents"></a>

 ** name **   <a name="codecatalyst-Type-IdeConfiguration-name"></a>
The name of the IDE. Valid values include `Cloud9`, `IntelliJ`, `PyCharm`, `GoLand`, and `VSCode`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** runtime **   <a name="codecatalyst-Type-IdeConfiguration-runtime"></a>
A link to the IDE runtime image.
This parameter is not required for `VSCode`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

## See Also
<a name="API_IdeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/IdeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/IdeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/IdeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
