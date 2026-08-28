---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-generatedtemplate-templateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GeneratedTemplate TemplateConfiguration
<a name="aws-properties-cloudformation-generatedtemplate-templateconfiguration"></a>

The configuration details of a generated template.

## Syntax
<a name="aws-properties-cloudformation-generatedtemplate-templateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-generatedtemplate-templateconfiguration-syntax.json"></a>

```
{
  "[DeletionPolicy](#cfn-cloudformation-generatedtemplate-templateconfiguration-deletionpolicy)" : {{String}},
  "[UpdateReplacePolicy](#cfn-cloudformation-generatedtemplate-templateconfiguration-updatereplacepolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-generatedtemplate-templateconfiguration-syntax.yaml"></a>

```
  [DeletionPolicy](#cfn-cloudformation-generatedtemplate-templateconfiguration-deletionpolicy): {{String}}
  [UpdateReplacePolicy](#cfn-cloudformation-generatedtemplate-templateconfiguration-updatereplacepolicy): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-generatedtemplate-templateconfiguration-properties"></a>

`DeletionPolicy`  <a name="cfn-cloudformation-generatedtemplate-templateconfiguration-deletionpolicy"></a>
The `DeletionPolicy` assigned to resources in the generated template. Supported values are:
+ `DELETE` - delete all resources when the stack is deleted.
+ `RETAIN` - retain all resources when the stack is deleted.
For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) in the *AWS CloudFormation User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `DELETE | RETAIN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateReplacePolicy`  <a name="cfn-cloudformation-generatedtemplate-templateconfiguration-updatereplacepolicy"></a>
The `UpdateReplacePolicy` assigned to resources in the generated template. Supported values are:
+ `DELETE` - delete all resources when the resource is replaced during an update operation.
+ `RETAIN` - retain all resources when the resource is replaced during an update operation.
For more information, see [UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html) in the *AWS CloudFormation User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `DELETE | RETAIN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
