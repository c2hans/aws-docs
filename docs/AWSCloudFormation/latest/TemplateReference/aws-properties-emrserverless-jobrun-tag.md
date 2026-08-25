---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun Tag
<a name="aws-properties-emrserverless-jobrun-tag"></a>

<a name="aws-properties-emrserverless-jobrun-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::EMRServerless::JobRun](aws-resource-emrserverless-jobrun.md).

## Syntax
<a name="aws-properties-emrserverless-jobrun-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-tag-syntax.json"></a>

```
{
  "[Key](#cfn-emrserverless-jobrun-tag-key)" : {{String}},
  "[Value](#cfn-emrserverless-jobrun-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-tag-syntax.yaml"></a>

```
  [Key](#cfn-emrserverless-jobrun-tag-key): {{String}}
  [Value](#cfn-emrserverless-jobrun-tag-value): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-tag-properties"></a>

`Key`  <a name="cfn-emrserverless-jobrun-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 /_.:=+@-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-emrserverless-jobrun-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 /_.:=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
