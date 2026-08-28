---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-coredefinition-coredefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::CoreDefinition CoreDefinitionVersion
<a name="aws-properties-greengrass-coredefinition-coredefinitionversion"></a>

<a name="aws-properties-greengrass-coredefinition-coredefinitionversion-description"></a> A core definition version contains a Greengrass [core](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html).

**Note**
After you create a core definition version that contains the core you want to deploy, you must add it to your group version. For more information, see [`AWS::Greengrass::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

<a name="aws-properties-greengrass-coredefinition-coredefinitionversion-inheritance"></a> In an CloudFormation template, `CoreDefinitionVersion` is the property type of the `InitialVersion` property in the [`AWS::Greengrass::CoreDefinition`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html) resource.

## Syntax
<a name="aws-properties-greengrass-coredefinition-coredefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-coredefinition-coredefinitionversion-syntax.json"></a>

```
{
  "[Cores](#cfn-greengrass-coredefinition-coredefinitionversion-cores)" : {{[ Core, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrass-coredefinition-coredefinitionversion-syntax.yaml"></a>

```
  [Cores](#cfn-greengrass-coredefinition-coredefinitionversion-cores): {{
    - Core}}
```

## Properties
<a name="aws-properties-greengrass-coredefinition-coredefinitionversion-properties"></a>

`Cores`  <a name="cfn-greengrass-coredefinition-coredefinitionversion-cores"></a>
The Greengrass core in this version. Currently, the `Cores` property for a core definition version can contain only one core.
*Required*: Yes
*Type*: Array of [Core](aws-properties-greengrass-coredefinition-core.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-coredefinition-coredefinitionversion--seealso"></a>
+ [CoreDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-coredefinitionversion.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
