---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-tableoptimizer-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableOptimizer VpcConfiguration
<a name="aws-properties-glue-tableoptimizer-vpcconfiguration"></a>

 An object that describes the VPC configuration for a table optimizer. This configuration is necessary to perform optimization on tables that are in a customer VPC.

## Syntax
<a name="aws-properties-glue-tableoptimizer-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-tableoptimizer-vpcconfiguration-syntax.json"></a>

```
{
  "[GlueConnectionName](#cfn-glue-tableoptimizer-vpcconfiguration-glueconnectionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-tableoptimizer-vpcconfiguration-syntax.yaml"></a>

```
  [GlueConnectionName](#cfn-glue-tableoptimizer-vpcconfiguration-glueconnectionname): {{String}}
```

## Properties
<a name="aws-properties-glue-tableoptimizer-vpcconfiguration-properties"></a>

`GlueConnectionName`  <a name="cfn-glue-tableoptimizer-vpcconfiguration-glueconnectionname"></a>
The name of the AWS Glue connection used for the VPC for the table optimizer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
