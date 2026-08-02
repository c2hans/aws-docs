---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-owner-owneruserproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Owner OwnerUserProperties
<a name="aws-properties-datazone-owner-owneruserproperties"></a>

The properties of the owner user.

## Syntax
<a name="aws-properties-datazone-owner-owneruserproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-owner-owneruserproperties-syntax.json"></a>

```
{
  "[UserIdentifier](#cfn-datazone-owner-owneruserproperties-useridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-owner-owneruserproperties-syntax.yaml"></a>

```
  [UserIdentifier](#cfn-datazone-owner-owneruserproperties-useridentifier): {{String}}
```

## Properties
<a name="aws-properties-datazone-owner-owneruserproperties-properties"></a>

`UserIdentifier`  <a name="cfn-datazone-owner-owneruserproperties-useridentifier"></a>
The ID of the owner user.
*Required*: No
*Type*: String
*Pattern*: `(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\d{12}:.+$)`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
