---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-profile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::Profile
<a name="aws-resource-wellarchitected-profile"></a>

A profile.

## Syntax
<a name="aws-resource-wellarchitected-profile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-profile-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::Profile",
  "Properties" : {
      "[ProfileDescription](#cfn-wellarchitected-profile-profiledescription)" : {{String}},
      "[ProfileName](#cfn-wellarchitected-profile-profilename)" : {{String}},
      "[ProfileQuestions](#cfn-wellarchitected-profile-profilequestions)" : {{[ ProfileQuestionUpdate, ... ]}},
      "[Tags](#cfn-wellarchitected-profile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-profile-syntax.yaml"></a>

```
Type: AWS::WellArchitected::Profile
Properties:
  [ProfileDescription](#cfn-wellarchitected-profile-profiledescription): {{String}}
  [ProfileName](#cfn-wellarchitected-profile-profilename): {{String}}
  [ProfileQuestions](#cfn-wellarchitected-profile-profilequestions): {{
    - ProfileQuestionUpdate}}
  [Tags](#cfn-wellarchitected-profile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wellarchitected-profile-properties"></a>

`ProfileDescription`  <a name="cfn-wellarchitected-profile-profiledescription"></a>
The profile description.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileName`  <a name="cfn-wellarchitected-profile-profilename"></a>
The profile name.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileQuestions`  <a name="cfn-wellarchitected-profile-profilequestions"></a>
Profile questions.
*Required*: Yes
*Type*: Array of [ProfileQuestionUpdate](aws-properties-wellarchitected-profile-profilequestionupdate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wellarchitected-profile-tags"></a>
The tags assigned to the profile.
*Required*: No
*Type*: Array of [Tag](aws-properties-wellarchitected-profile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-profile-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-profile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the profile ARN.

### Fn::GetAtt
<a name="aws-resource-wellarchitected-profile-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-profile-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the profile was created.

`Owner`  <a name="Owner-fn::getatt"></a>
The owner of the profile.

`ProfileArn`  <a name="ProfileArn-fn::getatt"></a>
The profile ARN.

`ProfileVersion`  <a name="ProfileVersion-fn::getatt"></a>
The profile version.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the profile was last updated.
