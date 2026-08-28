---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::LoggerDefinition LoggerDefinitionVersion
<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion"></a>

<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion-description"></a> A logger definition version contains a list of [loggers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html).

**Note**
After you create a logger definition version that contains the loggers you want to deploy, you must add it to your group version. For more information, see [`AWS::Greengrass::Group`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html).

<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion-inheritance"></a> In an CloudFormation template, `LoggerDefinitionVersion` is the property type of the `InitialVersion` property in the [`AWS::Greengrass::LoggerDefinition`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html) resource.

## Syntax
<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion-syntax.json"></a>

```
{
  "[Loggers](#cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers)" : {{[ Logger, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion-syntax.yaml"></a>

```
  [Loggers](#cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers): {{
    - Logger}}
```

## Properties
<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion-properties"></a>

`Loggers`  <a name="cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers"></a>
The loggers in this version.
*Required*: Yes
*Type*: Array of [Logger](aws-properties-greengrass-loggerdefinition-logger.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-loggerdefinition-loggerdefinitionversion--seealso"></a>
+ [LoggerDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-loggerdefinitionversion.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
