---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idnamespace-idnamespaceinputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdNamespace IdNamespaceInputSource
<a name="aws-properties-entityresolution-idnamespace-idnamespaceinputsource"></a>

An object containing `inputSourceARN` and `schemaName`.

## Syntax
<a name="aws-properties-entityresolution-idnamespace-idnamespaceinputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idnamespace-idnamespaceinputsource-syntax.json"></a>

```
{
  "[InputSourceARN](#cfn-entityresolution-idnamespace-idnamespaceinputsource-inputsourcearn)" : {{String}},
  "[SchemaName](#cfn-entityresolution-idnamespace-idnamespaceinputsource-schemaname)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idnamespace-idnamespaceinputsource-syntax.yaml"></a>

```
  [InputSourceARN](#cfn-entityresolution-idnamespace-idnamespaceinputsource-inputsourcearn): {{String}}
  [SchemaName](#cfn-entityresolution-idnamespace-idnamespaceinputsource-schemaname): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idnamespace-idnamespaceinputsource-properties"></a>

`InputSourceARN`  <a name="cfn-entityresolution-idnamespace-idnamespaceinputsource-inputsourcearn"></a>
An AWS Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaName`  <a name="cfn-entityresolution-idnamespace-idnamespaceinputsource-schemaname"></a>
The name of the schema.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
