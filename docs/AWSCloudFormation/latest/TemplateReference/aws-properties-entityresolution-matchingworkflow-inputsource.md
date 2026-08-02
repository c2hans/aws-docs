---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-inputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow InputSource
<a name="aws-properties-entityresolution-matchingworkflow-inputsource"></a>

An object containing `inputSourceARN`, `schemaName`, and `applyNormalization`.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-inputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-inputsource-syntax.json"></a>

```
{
  "[ApplyNormalization](#cfn-entityresolution-matchingworkflow-inputsource-applynormalization)" : {{Boolean}},
  "[InputSourceARN](#cfn-entityresolution-matchingworkflow-inputsource-inputsourcearn)" : {{String}},
  "[SchemaArn](#cfn-entityresolution-matchingworkflow-inputsource-schemaarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-inputsource-syntax.yaml"></a>

```
  [ApplyNormalization](#cfn-entityresolution-matchingworkflow-inputsource-applynormalization): {{Boolean}}
  [InputSourceARN](#cfn-entityresolution-matchingworkflow-inputsource-inputsourcearn): {{String}}
  [SchemaArn](#cfn-entityresolution-matchingworkflow-inputsource-schemaarn): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-inputsource-properties"></a>

`ApplyNormalization`  <a name="cfn-entityresolution-matchingworkflow-inputsource-applynormalization"></a>
Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an `AttributeType` of `PHONE_NUMBER`, and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSourceARN`  <a name="cfn-entityresolution-matchingworkflow-inputsource-inputsourcearn"></a>
An object containing `inputSourceARN`, `schemaName`, and `applyNormalization`.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):.*:.*:[0-9]+:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaArn`  <a name="cfn-entityresolution-matchingworkflow-inputsource-schemaarn"></a>
The name of the schema.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(schemamapping/.*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
