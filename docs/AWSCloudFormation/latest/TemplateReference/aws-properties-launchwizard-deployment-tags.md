---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-launchwizard-deployment-tags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LaunchWizard::Deployment Tags
<a name="aws-properties-launchwizard-deployment-tags"></a>

The tags to add to the deployment.

## Syntax
<a name="aws-properties-launchwizard-deployment-tags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-launchwizard-deployment-tags-syntax.json"></a>

```
{
  "[Key](#cfn-launchwizard-deployment-tags-key)" : {{String}},
  "[Value](#cfn-launchwizard-deployment-tags-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-launchwizard-deployment-tags-syntax.yaml"></a>

```
  [Key](#cfn-launchwizard-deployment-tags-key): {{String}}
  [Value](#cfn-launchwizard-deployment-tags-value): {{String}}
```

## Properties
<a name="aws-properties-launchwizard-deployment-tags-properties"></a>

`Key`  <a name="cfn-launchwizard-deployment-tags-key"></a>
The key name of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-launchwizard-deployment-tags-value"></a>
The value for the tag.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
