---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ParameterDefinition.html
---

# ParameterDefinition
<a name="API_ParameterDefinition"></a>

Defines a parameter that a role template accepts. You supply values for these parameters when you create a role with [AcquireRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html).

## Contents
<a name="API_ParameterDefinition_Contents"></a>

 ** Name **
The name of the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Type **
The data type of the parameter. Valid values are `String`, `StringList`, `Number`, `NumberList`, `Arn`, and `ArnList`.
Type: String
Valid Values: `String | StringList | Number | NumberList | Arn | ArnList`
Required: Yes

 ** DefaultValue **
The value that the service uses for the parameter when you do not supply one.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Description **
A description of the parameter.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** Immutable **
Specifies whether you can change the parameter value after you create the role.
Type: Boolean
Required: No

 ** IsRequired **
Specifies whether you must supply a value for the parameter when you create a role from the template.
Type: Boolean
Required: No

 ** SubType **
An optional subtype that further constrains the values that are allowed for the parameter.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ParameterDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ParameterDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ParameterDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ParameterDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
