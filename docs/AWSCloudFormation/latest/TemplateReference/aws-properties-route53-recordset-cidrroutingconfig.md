---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordset-cidrroutingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::RecordSet CidrRoutingConfig
<a name="aws-properties-route53-recordset-cidrroutingconfig"></a>

The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

A `LocationName` with an asterisk “\*” can be used to create a default CIDR record. `CollectionId` is still required for default record.

## Syntax
<a name="aws-properties-route53-recordset-cidrroutingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-recordset-cidrroutingconfig-syntax.json"></a>

```
{
  "[CollectionId](#cfn-route53-recordset-cidrroutingconfig-collectionid)" : {{String}},
  "[LocationName](#cfn-route53-recordset-cidrroutingconfig-locationname)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-recordset-cidrroutingconfig-syntax.yaml"></a>

```
  [CollectionId](#cfn-route53-recordset-cidrroutingconfig-collectionid): {{String}}
  [LocationName](#cfn-route53-recordset-cidrroutingconfig-locationname): {{String}}
```

## Properties
<a name="aws-properties-route53-recordset-cidrroutingconfig-properties"></a>

`CollectionId`  <a name="cfn-route53-recordset-cidrroutingconfig-collectionid"></a>
The CIDR collection ID.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationName`  <a name="cfn-route53-recordset-cidrroutingconfig-locationname"></a>
The CIDR collection location name.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9A-Za-z_\-\*]+`
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
