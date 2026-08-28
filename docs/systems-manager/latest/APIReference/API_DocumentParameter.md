---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentParameter.html
---

# DocumentParameter
<a name="API_DocumentParameter"></a>

Parameters specified in a Systems Manager document that run on the server when the command is run.

## Contents
<a name="API_DocumentParameter_Contents"></a>

 ** DefaultValue **   <a name="systemsmanager-Type-DocumentParameter-DefaultValue"></a>
If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.
Type: String
Required: No

 ** Description **   <a name="systemsmanager-Type-DocumentParameter-Description"></a>
A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-DocumentParameter-Name"></a>
The name of the parameter.
Type: String
Required: No

 ** Type **   <a name="systemsmanager-Type-DocumentParameter-Type"></a>
The type of parameter. The type can be either String or StringList.
Type: String
Valid Values: `String | StringList`
Required: No

## See Also
<a name="API_DocumentParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
