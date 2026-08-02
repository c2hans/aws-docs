---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-tenant-resourceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Tenant ResourceAssociation
<a name="aws-properties-ses-tenant-resourceassociation"></a>

The resource to associate with the tenant.

## Syntax
<a name="aws-properties-ses-tenant-resourceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-tenant-resourceassociation-syntax.json"></a>

```
{
  "[ResourceArn](#cfn-ses-tenant-resourceassociation-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-tenant-resourceassociation-syntax.yaml"></a>

```
  [ResourceArn](#cfn-ses-tenant-resourceassociation-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-ses-tenant-resourceassociation-properties"></a>

`ResourceArn`  <a name="cfn-ses-tenant-resourceassociation-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource associated with the tenant.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
