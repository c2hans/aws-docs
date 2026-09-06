---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-globalcluster-globalendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::GlobalCluster GlobalEndpoint
<a name="aws-properties-rds-globalcluster-globalendpoint"></a>

 The writer endpoint for the new global database cluster. This endpoint always points to the writer DB instance in the current primary cluster.

## Syntax
<a name="aws-properties-rds-globalcluster-globalendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-globalcluster-globalendpoint-syntax.json"></a>

```
{
  "[Address](#cfn-rds-globalcluster-globalendpoint-address)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-globalcluster-globalendpoint-syntax.yaml"></a>

```
  [Address](#cfn-rds-globalcluster-globalendpoint-address): {{String}}
```

## Properties
<a name="aws-properties-rds-globalcluster-globalendpoint-properties"></a>

`Address`  <a name="cfn-rds-globalcluster-globalendpoint-address"></a>
 The writer endpoint for the new global database cluster. This endpoint always points to the writer DB instance in the current primary cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
