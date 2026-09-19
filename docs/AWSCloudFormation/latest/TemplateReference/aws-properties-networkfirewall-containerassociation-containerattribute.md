---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-containerassociation-containerattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::ContainerAssociation ContainerAttribute
<a name="aws-properties-networkfirewall-containerassociation-containerattribute"></a>

A key-value filter pair used in container association monitoring configurations to narrow which containers are tracked.

## Syntax
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-syntax.json"></a>

```
{
  "[Key](#cfn-networkfirewall-containerassociation-containerattribute-key)" : {{String}},
  "[Value](#cfn-networkfirewall-containerassociation-containerattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-syntax.yaml"></a>

```
  [Key](#cfn-networkfirewall-containerassociation-containerattribute-key): {{String}}
  [Value](#cfn-networkfirewall-containerassociation-containerattribute-value): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-containerassociation-containerattribute-properties"></a>

`Key`  <a name="cfn-networkfirewall-containerassociation-containerattribute-key"></a>
The attribute key to filter on.
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkfirewall-containerassociation-containerattribute-value"></a>
The attribute value to match.
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
