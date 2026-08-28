---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::FunctionDefinition FunctionDefinitionVersion
<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion"></a>

<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion-description"></a>A function definition version contains a list of functions.

**Note**
After you create a function definition version that contains the functions you want to deploy, you must add it to your group version. For more information, see [`AWS::Greengrass::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion-inheritance"></a> In an CloudFormation template, `FunctionDefinitionVersion` is the property type of the `InitialVersion` property in the [`AWS::Greengrass::FunctionDefinition`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html) resource.

## Syntax
<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion-syntax.json"></a>

```
{
  "[DefaultConfig](#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig)" : {{DefaultConfig}},
  "[Functions](#cfn-greengrass-functiondefinition-functiondefinitionversion-functions)" : {{[ Function, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion-syntax.yaml"></a>

```
  [DefaultConfig](#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig): {{
    DefaultConfig}}
  [Functions](#cfn-greengrass-functiondefinition-functiondefinitionversion-functions): {{
    - Function}}
```

## Properties
<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion-properties"></a>

`DefaultConfig`  <a name="cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig"></a>
The default configuration that applies to all Lambda functions in the group. Individual Lambda functions can override these settings.
*Required*: No
*Type*: [DefaultConfig](aws-properties-greengrass-functiondefinition-defaultconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Functions`  <a name="cfn-greengrass-functiondefinition-functiondefinitionversion-functions"></a>
The functions in this version.
*Required*: Yes
*Type*: Array of [Function](aws-properties-greengrass-functiondefinition-function.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-functiondefinition-functiondefinitionversion--seealso"></a>
+ [FunctionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functiondefinitionversion.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
