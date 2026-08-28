---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordsetgroup-cidrroutingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::RecordSetGroup CidrRoutingConfig
<a name="aws-properties-route53-recordsetgroup-cidrroutingconfig"></a>

The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

A `LocationName` with an asterisk “\*” can be used to create a default CIDR record. `CollectionId` is still required for default record.

## Syntax
<a name="aws-properties-route53-recordsetgroup-cidrroutingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-recordsetgroup-cidrroutingconfig-syntax.json"></a>

```
{
  "[CollectionId](#cfn-route53-recordsetgroup-cidrroutingconfig-collectionid)" : {{String}},
  "[LocationName](#cfn-route53-recordsetgroup-cidrroutingconfig-locationname)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-recordsetgroup-cidrroutingconfig-syntax.yaml"></a>

```
  [CollectionId](#cfn-route53-recordsetgroup-cidrroutingconfig-collectionid): {{String}}
  [LocationName](#cfn-route53-recordsetgroup-cidrroutingconfig-locationname): {{String}}
```

## Properties
<a name="aws-properties-route53-recordsetgroup-cidrroutingconfig-properties"></a>

`CollectionId`  <a name="cfn-route53-recordsetgroup-cidrroutingconfig-collectionid"></a>
The CIDR collection ID.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationName`  <a name="cfn-route53-recordsetgroup-cidrroutingconfig-locationname"></a>
The CIDR collection location name.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9A-Za-z_\-\*]+`
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
