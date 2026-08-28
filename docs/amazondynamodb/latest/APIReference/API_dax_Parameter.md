---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Parameter.html
---

# Parameter
<a name="API_dax_Parameter"></a>

Describes an individual setting that controls some aspect of DAX behavior.

## Contents
<a name="API_dax_Parameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllowedValues **   <a name="DDB-Type-dax_Parameter-AllowedValues"></a>
A range of values within which the parameter can be set.
Type: String
Required: No

 ** ChangeType **   <a name="DDB-Type-dax_Parameter-ChangeType"></a>
The conditions under which changes to this parameter can be applied. For example, `requires-reboot` indicates that a new value for this parameter will only take effect if a node is rebooted.
Type: String
Valid Values: `IMMEDIATE | REQUIRES_REBOOT`
Required: No

 ** DataType **   <a name="DDB-Type-dax_Parameter-DataType"></a>
The data type of the parameter. For example, `integer`:
Type: String
Required: No

 ** Description **   <a name="DDB-Type-dax_Parameter-Description"></a>
A description of the parameter
Type: String
Required: No

 ** IsModifiable **   <a name="DDB-Type-dax_Parameter-IsModifiable"></a>
Whether the customer is allowed to modify the parameter.
Type: String
Valid Values: `TRUE | FALSE | CONDITIONAL`
Required: No

 ** NodeTypeSpecificValues **   <a name="DDB-Type-dax_Parameter-NodeTypeSpecificValues"></a>
A list of node types, and specific parameter values for each node.
Type: Array of [NodeTypeSpecificValue](API_dax_NodeTypeSpecificValue.md) objects
Required: No

 ** ParameterName **   <a name="DDB-Type-dax_Parameter-ParameterName"></a>
The name of the parameter.
Type: String
Required: No

 ** ParameterType **   <a name="DDB-Type-dax_Parameter-ParameterType"></a>
Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.
Type: String
Valid Values: `DEFAULT | NODE_TYPE_SPECIFIC`
Required: No

 ** ParameterValue **   <a name="DDB-Type-dax_Parameter-ParameterValue"></a>
The value for the parameter.
Type: String
Required: No

 ** Source **   <a name="DDB-Type-dax_Parameter-Source"></a>
How the parameter is defined. For example, `system` denotes a system-defined parameter.
Type: String
Required: No

## See Also
<a name="API_dax_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/Parameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
