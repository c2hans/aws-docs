---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-testcase-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TestCase Tag
<a name="aws-properties-connect-testcase-tag"></a>

<a name="aws-properties-connect-testcase-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Connect::TestCase](aws-resource-connect-testcase.md).

## Syntax
<a name="aws-properties-connect-testcase-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-testcase-tag-syntax.json"></a>

```
{
  "[Key](#cfn-connect-testcase-tag-key)" : {{String}},
  "[Value](#cfn-connect-testcase-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-testcase-tag-syntax.yaml"></a>

```
  [Key](#cfn-connect-testcase-tag-key): {{String}}
  [Value](#cfn-connect-testcase-tag-value): {{String}}
```

## Properties
<a name="aws-properties-connect-testcase-tag-properties"></a>

`Key`  <a name="cfn-connect-testcase-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connect-testcase-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
