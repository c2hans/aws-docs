---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

The `Parameter` data type.

## Contents
<a name="API_Parameter_Contents"></a>

 ** ParameterKey **
The key associated with the parameter. If you don't specify a key and value for a particular parameter, CloudFormation uses the default value that's specified in your template.
Type: String
Required: No

 ** ParameterValue **
The input value associated with the parameter.
Type: String
Required: No

 ** ResolvedValue **
Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for Systems Manager parameter types in the template. For more information, see [Specify existing resources at runtime with CloudFormation-supplied parameter types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-supplied-parameter-types.html) in the * AWS CloudFormation User Guide*.
Type: String
Required: No

 ** UsePreviousValue **
During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify `true`, do not specify a parameter value.
Type: Boolean
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Parameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
