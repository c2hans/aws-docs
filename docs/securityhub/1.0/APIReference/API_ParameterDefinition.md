---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ParameterDefinition.html
---

# ParameterDefinition
<a name="API_ParameterDefinition"></a>

 An object that describes a security control parameter and the options for customizing it.

## Contents
<a name="API_ParameterDefinition_Contents"></a>

 ** ConfigurationOptions **   <a name="securityhub-Type-ParameterDefinition-ConfigurationOptions"></a>
 The options for customizing a control parameter. Customization options vary based on the data type of the parameter.
Type: [ConfigurationOptions](API_ConfigurationOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Description **   <a name="securityhub-Type-ParameterDefinition-Description"></a>
 Description of a control parameter.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ParameterDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ParameterDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ParameterDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ParameterDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
