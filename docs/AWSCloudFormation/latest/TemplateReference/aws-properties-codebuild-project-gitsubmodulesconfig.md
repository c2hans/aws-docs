---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-gitsubmodulesconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project GitSubmodulesConfig
<a name="aws-properties-codebuild-project-gitsubmodulesconfig"></a>

`GitSubmodulesConfig` is a property of the [AWS CodeBuild Project Source](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html) property type that specifies information about the Git submodules configuration for the build project.

## Syntax
<a name="aws-properties-codebuild-project-gitsubmodulesconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-gitsubmodulesconfig-syntax.json"></a>

```
{
  "[FetchSubmodules](#cfn-codebuild-project-gitsubmodulesconfig-fetchsubmodules)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-codebuild-project-gitsubmodulesconfig-syntax.yaml"></a>

```
  [FetchSubmodules](#cfn-codebuild-project-gitsubmodulesconfig-fetchsubmodules): {{Boolean}}
```

## Properties
<a name="aws-properties-codebuild-project-gitsubmodulesconfig-properties"></a>

`FetchSubmodules`  <a name="cfn-codebuild-project-gitsubmodulesconfig-fetchsubmodules"></a>
 Set to true to fetch Git submodules for your AWS CodeBuild build project.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-codebuild-project-gitsubmodulesconfig--seealso"></a>
+ [ GitSubmodulesConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GitSubmodulesConfig.html) in the *AWS CodeBuild API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
