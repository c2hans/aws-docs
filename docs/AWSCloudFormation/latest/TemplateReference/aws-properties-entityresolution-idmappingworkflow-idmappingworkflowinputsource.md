---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow IdMappingWorkflowInputSource
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource"></a>

An object containing `inputSourceARN`, `schemaName`, and `type`.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource-syntax.json"></a>

```
{
  "[InputSourceARN](#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-inputsourcearn)" : {{String}},
  "[SchemaArn](#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-schemaarn)" : {{String}},
  "[Type](#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource-syntax.yaml"></a>

```
  [InputSourceARN](#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-inputsourcearn): {{String}}
  [SchemaArn](#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-schemaarn): {{String}}
  [Type](#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-type): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource-properties"></a>

`InputSourceARN`  <a name="cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-inputsourcearn"></a>
An AWS Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaArn`  <a name="cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-schemaarn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `SchemaMapping`.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(schemamapping/.*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-type"></a>
The type of ID namespace. There are two types: `SOURCE` and `TARGET`.
The `SOURCE` contains configurations for `sourceId` data that will be processed in an ID mapping workflow.
The `TARGET` contains a configuration of `targetId` which all `sourceIds` will resolve to.
*Required*: No
*Type*: String
*Allowed values*: `SOURCE | TARGET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
