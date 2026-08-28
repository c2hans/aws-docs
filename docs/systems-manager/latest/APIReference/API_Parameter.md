---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

An AWS Systems Manager parameter in Parameter Store.

## Contents
<a name="API_Parameter_Contents"></a>

 ** ARN **   <a name="systemsmanager-Type-Parameter-ARN"></a>
The Amazon Resource Name (ARN) of the parameter.
Type: String
Required: No

 ** DataType **   <a name="systemsmanager-Type-Parameter-DataType"></a>
The data type of the parameter, such as `text` or `aws:ec2:image`. The default is `text`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** LastModifiedDate **   <a name="systemsmanager-Type-Parameter-LastModifiedDate"></a>
Date the parameter was last changed or updated and the parameter version was created.
Type: Timestamp
Required: No

 ** Name **   <a name="systemsmanager-Type-Parameter-Name"></a>
The name of the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Selector **   <a name="systemsmanager-Type-Parameter-Selector"></a>
Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:
parameter\_name:version
parameter\_name:label
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** SourceResult **   <a name="systemsmanager-Type-Parameter-SourceResult"></a>
Applies to parameters that reference information in other AWS services. `SourceResult` is the raw result or response from the source.
Type: String
Required: No

 ** Type **   <a name="systemsmanager-Type-Parameter-Type"></a>
The type of parameter. Valid values include the following: `String`, `StringList`, and `SecureString`.
If type is `StringList`, the system returns a comma-separated string with no spaces between commas in the `Value` field.
Type: String
Valid Values: `String | StringList | SecureString`
Required: No

 ** Value **   <a name="systemsmanager-Type-Parameter-Value"></a>
The parameter value.
If type is `StringList`, the system returns a comma-separated string with no spaces between commas in the `Value` field.
Type: String
Required: No

 ** Version **   <a name="systemsmanager-Type-Parameter-Version"></a>
The parameter version.
Type: Long
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Parameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
