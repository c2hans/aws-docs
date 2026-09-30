---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-keyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program KeyValuePair
<a name="aws-properties-mediatailor-program-keyvaluepair"></a>

For `SCTE35_ENHANCED` output, defines a key and corresponding value. MediaTailor generates these pairs within the `EXT-X-ASSET`tag.

## Syntax
<a name="aws-properties-mediatailor-program-keyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-keyvaluepair-syntax.json"></a>

```
{
  "[Key](#cfn-mediatailor-program-keyvaluepair-key)" : {{String}},
  "[Value](#cfn-mediatailor-program-keyvaluepair-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-keyvaluepair-syntax.yaml"></a>

```
  [Key](#cfn-mediatailor-program-keyvaluepair-key): {{String}}
  [Value](#cfn-mediatailor-program-keyvaluepair-value): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-program-keyvaluepair-properties"></a>

`Key`  <a name="cfn-mediatailor-program-keyvaluepair-key"></a>
For `SCTE35_ENHANCED` output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the `EXT-X-ASSET`tag. If you specify a key, you must also specify a corresponding value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mediatailor-program-keyvaluepair-value"></a>
For `SCTE35_ENHANCED` output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the `EXT-X-ASSET`tag. If you specify a value, you must also specify a corresponding key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
