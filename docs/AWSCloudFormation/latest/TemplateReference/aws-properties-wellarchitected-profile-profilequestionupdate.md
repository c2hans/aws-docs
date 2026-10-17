---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-profile-profilequestionupdate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::Profile ProfileQuestionUpdate
<a name="aws-properties-wellarchitected-profile-profilequestionupdate"></a>

An update to a profile question.

## Syntax
<a name="aws-properties-wellarchitected-profile-profilequestionupdate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-profile-profilequestionupdate-syntax.json"></a>

```
{
  "[QuestionId](#cfn-wellarchitected-profile-profilequestionupdate-questionid)" : {{String}},
  "[SelectedChoiceIds](#cfn-wellarchitected-profile-profilequestionupdate-selectedchoiceids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wellarchitected-profile-profilequestionupdate-syntax.yaml"></a>

```
  [QuestionId](#cfn-wellarchitected-profile-profilequestionupdate-questionid): {{String}}
  [SelectedChoiceIds](#cfn-wellarchitected-profile-profilequestionupdate-selectedchoiceids): {{
    - String}}
```

## Properties
<a name="aws-properties-wellarchitected-profile-profilequestionupdate-properties"></a>

`QuestionId`  <a name="cfn-wellarchitected-profile-profilequestionupdate-questionid"></a>
The ID of the question.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedChoiceIds`  <a name="cfn-wellarchitected-profile-profilequestionupdate-selectedchoiceids"></a>
The selected choices.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
