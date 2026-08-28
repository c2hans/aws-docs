---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ManagedJobTemplateSummary.html
---

# ManagedJobTemplateSummary
<a name="API_ManagedJobTemplateSummary"></a>

An object that contains information about the managed template.

## Contents
<a name="API_ManagedJobTemplateSummary_Contents"></a>

 ** description **   <a name="iot-Type-ManagedJobTemplateSummary-description"></a>
The description for a managed template.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** environments **   <a name="iot-Type-ManagedJobTemplateSummary-environments"></a>
A list of environments that are supported with the managed job template.
Type: Array of strings
Pattern: `[^\p{C}]+`
Required: No

 ** templateArn **   <a name="iot-Type-ManagedJobTemplateSummary-templateArn"></a>
The Amazon Resource Name (ARN) for a managed template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** templateName **   <a name="iot-Type-ManagedJobTemplateSummary-templateName"></a>
The unique Name for a managed template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** templateVersion **   <a name="iot-Type-ManagedJobTemplateSummary-templateVersion"></a>
The version for a managed template.
Type: String
Pattern: `^[1-9]+.[0-9]+`
Required: No

## See Also
<a name="API_ManagedJobTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ManagedJobTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ManagedJobTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ManagedJobTemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
