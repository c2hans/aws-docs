---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-sourceauth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project SourceAuth
<a name="aws-properties-codebuild-project-sourceauth"></a>

`SourceAuth` is a property of the [AWS CodeBuild Project Source ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html) property type that specifies authorization settings for AWS CodeBuild to access the source code to be built.

## Syntax
<a name="aws-properties-codebuild-project-sourceauth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-sourceauth-syntax.json"></a>

```
{
  "[Resource](#cfn-codebuild-project-sourceauth-resource)" : {{String}},
  "[Type](#cfn-codebuild-project-sourceauth-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-sourceauth-syntax.yaml"></a>

```
  [Resource](#cfn-codebuild-project-sourceauth-resource): {{String}}
  [Type](#cfn-codebuild-project-sourceauth-type): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-sourceauth-properties"></a>

`Resource`  <a name="cfn-codebuild-project-sourceauth-resource"></a>
 The resource value that applies to the specified authorization type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-codebuild-project-sourceauth-type"></a>
The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS\_MANAGER.
*Required*: Yes
*Type*: String
*Allowed values*: `OAUTH | CODECONNECTIONS | SECRETS_MANAGER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
