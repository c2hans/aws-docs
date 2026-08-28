---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-space.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space
<a name="aws-resource-sagemaker-space"></a>

Creates a private space or a space used for real time collaboration in a domain.

## Syntax
<a name="aws-resource-sagemaker-space-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-space-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Space",
  "Properties" : {
      "[DomainId](#cfn-sagemaker-space-domainid)" : {{String}},
      "[OwnershipSettings](#cfn-sagemaker-space-ownershipsettings)" : {{OwnershipSettings}},
      "[SpaceDisplayName](#cfn-sagemaker-space-spacedisplayname)" : {{String}},
      "[SpaceName](#cfn-sagemaker-space-spacename)" : {{String}},
      "[SpaceSettings](#cfn-sagemaker-space-spacesettings)" : {{SpaceSettings}},
      "[SpaceSharingSettings](#cfn-sagemaker-space-spacesharingsettings)" : {{SpaceSharingSettings}},
      "[Tags](#cfn-sagemaker-space-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-space-syntax.yaml"></a>

```
Type: AWS::SageMaker::Space
Properties:
  [DomainId](#cfn-sagemaker-space-domainid): {{String}}
  [OwnershipSettings](#cfn-sagemaker-space-ownershipsettings): {{
    OwnershipSettings}}
  [SpaceDisplayName](#cfn-sagemaker-space-spacedisplayname): {{String}}
  [SpaceName](#cfn-sagemaker-space-spacename): {{String}}
  [SpaceSettings](#cfn-sagemaker-space-spacesettings): {{
    SpaceSettings}}
  [SpaceSharingSettings](#cfn-sagemaker-space-spacesharingsettings): {{
    SpaceSharingSettings}}
  [Tags](#cfn-sagemaker-space-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-space-properties"></a>

`DomainId`  <a name="cfn-sagemaker-space-domainid"></a>
The ID of the associated domain.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OwnershipSettings`  <a name="cfn-sagemaker-space-ownershipsettings"></a>
The collection of ownership settings for a space.
*Required*: No
*Type*: [OwnershipSettings](aws-properties-sagemaker-space-ownershipsettings.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpaceDisplayName`  <a name="cfn-sagemaker-space-spacedisplayname"></a>
The name of the space that appears in the Studio UI.
*Required*: No
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceName`  <a name="cfn-sagemaker-space-spacename"></a>
The name of the space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpaceSettings`  <a name="cfn-sagemaker-space-spacesettings"></a>
A collection of space settings.
*Required*: No
*Type*: [SpaceSettings](aws-properties-sagemaker-space-spacesettings.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceSharingSettings`  <a name="cfn-sagemaker-space-spacesharingsettings"></a>
A collection of space sharing settings.
*Required*: No
*Type*: [SpaceSharingSettings](aws-properties-sagemaker-space-spacesharingsettings.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-space-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-space-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-space-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-space-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the domain that the space is associated with and the name of the space.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-space-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-space-return-values-fn--getatt-fn--getatt"></a>

`SpaceArn`  <a name="SpaceArn-fn::getatt"></a>
The space's Amazon Resource Name (ARN).

`Url`  <a name="Url-fn::getatt"></a>
Returns the URL of the space. If the space is created with AWS IAM Identity Center (Successor to AWS Single Sign-On) authentication, users can navigate to the URL after appending the respective redirect parameter for the application type to be federated through AWS IAM Identity Center.
The following application types are supported:
+ Studio Classic: `&redirect=JupyterServer`
+ JupyterLab: `&redirect=JupyterLab`
+ Code Editor, based on Code-OSS, Visual Studio Code - Open Source: `&redirect=CodeEditor`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
