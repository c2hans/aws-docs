---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-schemaversion-schema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::SchemaVersion Schema
<a name="aws-properties-glue-schemaversion-schema"></a>

A wrapper structure to contain schema identity fields. Either `SchemaArn`, or `SchemaName` and `RegistryName` has to be provided.

## Syntax
<a name="aws-properties-glue-schemaversion-schema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-schemaversion-schema-syntax.json"></a>

```
{
  "[RegistryName](#cfn-glue-schemaversion-schema-registryname)" : {{String}},
  "[SchemaArn](#cfn-glue-schemaversion-schema-schemaarn)" : {{String}},
  "[SchemaName](#cfn-glue-schemaversion-schema-schemaname)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-schemaversion-schema-syntax.yaml"></a>

```
  [RegistryName](#cfn-glue-schemaversion-schema-registryname): {{String}}
  [SchemaArn](#cfn-glue-schemaversion-schema-schemaarn): {{String}}
  [SchemaName](#cfn-glue-schemaversion-schema-schemaname): {{String}}
```

## Properties
<a name="aws-properties-glue-schemaversion-schema-properties"></a>

`RegistryName`  <a name="cfn-glue-schemaversion-schema-registryname"></a>
The name of the registry where the schema is stored. Either `SchemaArn`, or `SchemaName` and `RegistryName` has to be provided.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaArn`  <a name="cfn-glue-schemaversion-schema-schemaarn"></a>
The Amazon Resource Name (ARN) of the schema. Either `SchemaArn`, or `SchemaName` and `RegistryName` has to be provided.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):glue:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaName`  <a name="cfn-glue-schemaversion-schema-schemaname"></a>
The name of the schema. Either `SchemaArn`, or `SchemaName` and `RegistryName` has to be provided.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
