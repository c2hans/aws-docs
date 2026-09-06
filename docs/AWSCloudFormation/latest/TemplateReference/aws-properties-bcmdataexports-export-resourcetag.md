---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-resourcetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export ResourceTag
<a name="aws-properties-bcmdataexports-export-resourcetag"></a>

The tag structure that contains a tag key and value.

## Syntax
<a name="aws-properties-bcmdataexports-export-resourcetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-resourcetag-syntax.json"></a>

```
{
  "[Key](#cfn-bcmdataexports-export-resourcetag-key)" : {{String}},
  "[Value](#cfn-bcmdataexports-export-resourcetag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-resourcetag-syntax.yaml"></a>

```
  [Key](#cfn-bcmdataexports-export-resourcetag-key): {{String}}
  [Value](#cfn-bcmdataexports-export-resourcetag-value): {{String}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-resourcetag-properties"></a>

`Key`  <a name="cfn-bcmdataexports-export-resourcetag-key"></a>
The key that's associated with the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bcmdataexports-export-resourcetag-value"></a>
The value that's associated with the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
