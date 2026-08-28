---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConfigurationObject.html
---

# ConfigurationObject
<a name="API_ConfigurationObject"></a>

Specifies the values that an admin sets for each job or session parameter configured in a AWS Glue usage profile.

## Contents
<a name="API_ConfigurationObject_Contents"></a>

 ** AllowedValues **   <a name="Glue-Type-ConfigurationObject-AllowedValues"></a>
A list of allowed values for the parameter.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** DefaultValue **   <a name="Glue-Type-ConfigurationObject-DefaultValue"></a>
A default value for the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** MaxValue **   <a name="Glue-Type-ConfigurationObject-MaxValue"></a>
A maximum allowed value for the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** MinValue **   <a name="Glue-Type-ConfigurationObject-MinValue"></a>
A minimum allowed value for the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_ConfigurationObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConfigurationObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConfigurationObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConfigurationObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
