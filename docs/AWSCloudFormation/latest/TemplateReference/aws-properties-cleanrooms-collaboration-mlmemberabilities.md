---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-mlmemberabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration MLMemberAbilities
<a name="aws-properties-cleanrooms-collaboration-mlmemberabilities"></a>

The ML member abilities for a collaboration member.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-mlmemberabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-mlmemberabilities-syntax.json"></a>

```
{
  "[CustomMLMemberAbilities](#cfn-cleanrooms-collaboration-mlmemberabilities-custommlmemberabilities)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-mlmemberabilities-syntax.yaml"></a>

```
  [CustomMLMemberAbilities](#cfn-cleanrooms-collaboration-mlmemberabilities-custommlmemberabilities): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-mlmemberabilities-properties"></a>

`CustomMLMemberAbilities`  <a name="cfn-cleanrooms-collaboration-mlmemberabilities-custommlmemberabilities"></a>
The custom ML member abilities for a collaboration member.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
