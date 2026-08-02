---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-cloudexadatainfrastructure-customercontact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudExadataInfrastructure CustomerContact
<a name="aws-properties-odb-cloudexadatainfrastructure-customercontact"></a>

A contact to receive notification from Oracle about maintenance updates for a specific Exadata infrastructure.

## Syntax
<a name="aws-properties-odb-cloudexadatainfrastructure-customercontact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-cloudexadatainfrastructure-customercontact-syntax.json"></a>

```
{
  "[Email](#cfn-odb-cloudexadatainfrastructure-customercontact-email)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-cloudexadatainfrastructure-customercontact-syntax.yaml"></a>

```
  [Email](#cfn-odb-cloudexadatainfrastructure-customercontact-email): {{String}}
```

## Properties
<a name="aws-properties-odb-cloudexadatainfrastructure-customercontact-properties"></a>

`Email`  <a name="cfn-odb-cloudexadatainfrastructure-customercontact-email"></a>
The email address of the contact.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `320`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
