---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AllowedExtension.html
---

# AllowedExtension
<a name="API_AllowedExtension"></a>

Information about an allowed file extension.

## Contents
<a name="API_AllowedExtension_Contents"></a>

 ** Extension **   <a name="connect-Type-AllowedExtension-Extension"></a>
The file extension. The extension must be between 1 and 10 characters and can contain only alphanumeric characters, hyphens, and underscores.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

## See Also
<a name="API_AllowedExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AllowedExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AllowedExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AllowedExtension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
