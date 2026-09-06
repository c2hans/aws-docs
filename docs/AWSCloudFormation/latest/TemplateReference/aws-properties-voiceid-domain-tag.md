---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-voiceid-domain-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VoiceID::Domain Tag
<a name="aws-properties-voiceid-domain-tag"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

## Syntax
<a name="aws-properties-voiceid-domain-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-voiceid-domain-tag-syntax.json"></a>

```
{
  "[Key](#cfn-voiceid-domain-tag-key)" : {{String}},
  "[Value](#cfn-voiceid-domain-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-voiceid-domain-tag-syntax.yaml"></a>

```
  [Key](#cfn-voiceid-domain-tag-key): {{String}}
  [Value](#cfn-voiceid-domain-tag-value): {{String}}
```

## Properties
<a name="aws-properties-voiceid-domain-tag-properties"></a>

`Key`  <a name="cfn-voiceid-domain-tag-key"></a>
The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag 'Department':'Sales', the key is 'Department'.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-voiceid-domain-tag-value"></a>
The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag 'Department':'Sales', the value is 'Sales'.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
