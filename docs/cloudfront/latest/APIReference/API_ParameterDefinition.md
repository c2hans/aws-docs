---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ParameterDefinition.html
---

# ParameterDefinition
<a name="API_ParameterDefinition"></a>

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

## Contents
<a name="API_ParameterDefinition_Contents"></a>

 ** Definition **   <a name="cloudfront-Type-ParameterDefinition-Definition"></a>
The value that you assigned to the parameter.
Type: [ParameterDefinitionSchema](API_ParameterDefinitionSchema.md) object
Required: Yes

 ** Name **   <a name="cloudfront-Type-ParameterDefinition-Name"></a>
The name of the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## See Also
<a name="API_ParameterDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ParameterDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ParameterDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ParameterDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
