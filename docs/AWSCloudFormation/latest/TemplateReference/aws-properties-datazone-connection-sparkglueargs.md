---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-sparkglueargs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection SparkGlueArgs
<a name="aws-properties-datazone-connection-sparkglueargs"></a>

The Spark AWS Glue args.

## Syntax
<a name="aws-properties-datazone-connection-sparkglueargs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-sparkglueargs-syntax.json"></a>

```
{
  "[Connection](#cfn-datazone-connection-sparkglueargs-connection)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-sparkglueargs-syntax.yaml"></a>

```
  [Connection](#cfn-datazone-connection-sparkglueargs-connection): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-sparkglueargs-properties"></a>

`Connection`  <a name="cfn-datazone-connection-sparkglueargs-connection"></a>
The connection in the Spark AWS Glue args.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
