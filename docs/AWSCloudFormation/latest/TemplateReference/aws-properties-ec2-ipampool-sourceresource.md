---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ipampool-sourceresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMPool SourceResource
<a name="aws-properties-ec2-ipampool-sourceresource"></a>

The resource used to provision CIDRs to a resource planning pool.

## Syntax
<a name="aws-properties-ec2-ipampool-sourceresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ipampool-sourceresource-syntax.json"></a>

```
{
  "[ResourceId](#cfn-ec2-ipampool-sourceresource-resourceid)" : {{String}},
  "[ResourceOwner](#cfn-ec2-ipampool-sourceresource-resourceowner)" : {{String}},
  "[ResourceRegion](#cfn-ec2-ipampool-sourceresource-resourceregion)" : {{String}},
  "[ResourceType](#cfn-ec2-ipampool-sourceresource-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ipampool-sourceresource-syntax.yaml"></a>

```
  [ResourceId](#cfn-ec2-ipampool-sourceresource-resourceid): {{String}}
  [ResourceOwner](#cfn-ec2-ipampool-sourceresource-resourceowner): {{String}}
  [ResourceRegion](#cfn-ec2-ipampool-sourceresource-resourceregion): {{String}}
  [ResourceType](#cfn-ec2-ipampool-sourceresource-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-ec2-ipampool-sourceresource-properties"></a>

`ResourceId`  <a name="cfn-ec2-ipampool-sourceresource-resourceid"></a>
The source resource ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceOwner`  <a name="cfn-ec2-ipampool-sourceresource-resourceowner"></a>
The source resource owner.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceRegion`  <a name="cfn-ec2-ipampool-sourceresource-resourceregion"></a>
The source resource Region.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceType`  <a name="cfn-ec2-ipampool-sourceresource-resourcetype"></a>
The source resource type.
*Required*: Yes
*Type*: String
*Allowed values*: `vpc`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
