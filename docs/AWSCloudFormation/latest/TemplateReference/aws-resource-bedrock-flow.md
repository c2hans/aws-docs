---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-flow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow
<a name="aws-resource-bedrock-flow"></a>

Creates a prompt flow that you can use to send an input through various steps to yield an output. You define a flow by configuring nodes, each of which corresponds to a step of the flow, and creating connections between the nodes to create paths to different outputs. You can define the flow in one of the following ways:
+ Define a [FlowDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-flow-flowdefinition.html) in the `Definition` property.
+ Provide the definition in the `DefinitionString` property as a JSON-formatted string matching the [FlowDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-flow-flowdefinition.html) property.
+ Provide an Amazon S3 location in the `DefinitionS3Location` property that matches the [FlowDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-flow-flowdefinition.html).

If you use the `DefinitionString` or `DefinitionS3Location` property, you can use the `DefinitionSubstitutions` property to define key-value pairs to replace at runtime.

For more information, see [How it works](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html) and [Create a prompt flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-resource-bedrock-flow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-flow-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::Flow",
  "Properties" : {
      "[CustomerEncryptionKeyArn](#cfn-bedrock-flow-customerencryptionkeyarn)" : {{String}},
      "[Definition](#cfn-bedrock-flow-definition)" : {{FlowDefinition}},
      "[DefinitionS3Location](#cfn-bedrock-flow-definitions3location)" : {{S3Location}},
      "[DefinitionString](#cfn-bedrock-flow-definitionstring)" : {{String}},
      "[DefinitionSubstitutions](#cfn-bedrock-flow-definitionsubstitutions)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Description](#cfn-bedrock-flow-description)" : {{String}},
      "[ExecutionRoleArn](#cfn-bedrock-flow-executionrolearn)" : {{String}},
      "[Name](#cfn-bedrock-flow-name)" : {{String}},
      "[Tags](#cfn-bedrock-flow-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TestAliasTags](#cfn-bedrock-flow-testaliastags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-flow-syntax.yaml"></a>

```
Type: AWS::Bedrock::Flow
Properties:
  [CustomerEncryptionKeyArn](#cfn-bedrock-flow-customerencryptionkeyarn): {{String}}
  [Definition](#cfn-bedrock-flow-definition): {{
    FlowDefinition}}
  [DefinitionS3Location](#cfn-bedrock-flow-definitions3location): {{
    S3Location}}
  [DefinitionString](#cfn-bedrock-flow-definitionstring): {{
    String}}
  [DefinitionSubstitutions](#cfn-bedrock-flow-definitionsubstitutions): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-bedrock-flow-description): {{String}}
  [ExecutionRoleArn](#cfn-bedrock-flow-executionrolearn): {{String}}
  [Name](#cfn-bedrock-flow-name): {{String}}
  [Tags](#cfn-bedrock-flow-tags): {{
    {{Key}}: {{Value}}}}
  [TestAliasTags](#cfn-bedrock-flow-testaliastags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrock-flow-properties"></a>

`CustomerEncryptionKeyArn`  <a name="cfn-bedrock-flow-customerencryptionkeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key that the flow is encrypted with.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Definition`  <a name="cfn-bedrock-flow-definition"></a>
The definition of the nodes and connections between the nodes in the flow.
*Required*: No
*Type*: [FlowDefinition](aws-properties-bedrock-flow-flowdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefinitionS3Location`  <a name="cfn-bedrock-flow-definitions3location"></a>
The Amazon S3 location of the flow definition.
*Required*: No
*Type*: [S3Location](aws-properties-bedrock-flow-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefinitionString`  <a name="cfn-bedrock-flow-definitionstring"></a>
The definition of the flow as a JSON-formatted string. The string must match the format in [FlowDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrock-flow-flowdefinition.html).
*Required*: No
*Type*: String
*Maximum*: `512000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefinitionSubstitutions`  <a name="cfn-bedrock-flow-definitionsubstitutions"></a>
A map that specifies the mappings for placeholder variables in the prompt flow definition. This enables the customer to inject values obtained at runtime. Variables can be template parameter names, resource logical IDs, resource attributes, or a variable in a key-value map. Only supported with the `DefinitionString` and `DefinitionS3Location` fields.
Substitutions must follow the syntax: `${key_name}` or `${variable_1,variable_2,...}`.
*Required*: No
*Type*: Object
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-flow-description"></a>
A description of the flow.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-bedrock-flow-executionrolearn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service row for flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-flow-name"></a>
The name of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrock-flow-tags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestAliasTags`  <a name="cfn-bedrock-flow-testaliastags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-flow-return-values"></a>

### Ref
<a name="aws-resource-bedrock-flow-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Number (ARN) of the flow.

For example, `{ "Ref": "myFlow" }` could return the value `""arn:aws:bedrock:us-east-1:123456789012:flow/FLOW123456""`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-flow-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-flow-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the flow.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the flow was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the flow.

`Status`  <a name="Status-fn::getatt"></a>
The status of the flow. The following statuses are possible:
+ NotPrepared – The flow has been created or updated, but hasn't been prepared. If you just created the flow, you can't test it. If you updated the flow, the `DRAFT` version won't contain the latest changes for testing. Send a [PrepareFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PrepareFlow.html) request to package the latest changes into the `DRAFT` version.
+ Preparing – The flow is being prepared so that the `DRAFT` version contains the latest changes for testing.
+ Prepared – The flow is prepared and the `DRAFT` version contains the latest changes for testing.
+ Failed – The last API operation that you invoked on the flow failed. Send a [GetFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html) request and check the error message in the `validations` field.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the flow was last updated.

`Validations`  <a name="Validations-fn::getatt"></a>
Property description not available.

`Version`  <a name="Version-fn::getatt"></a>
The latest version of the flow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
