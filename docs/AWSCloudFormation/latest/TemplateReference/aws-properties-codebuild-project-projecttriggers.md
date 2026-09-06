---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-projecttriggers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project ProjectTriggers
<a name="aws-properties-codebuild-project-projecttriggers"></a>

`ProjectTriggers` is a property of the [AWS CodeBuild Project](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html) resource that specifies webhooks that trigger an AWS CodeBuild build.

**Note**
The Webhook feature isn't available in AWS CloudFormation for GitHub Enterprise projects. Use the AWS CLI or AWS CodeBuild console to create the webhook.

## Syntax
<a name="aws-properties-codebuild-project-projecttriggers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-projecttriggers-syntax.json"></a>

```
{
  "[BuildType](#cfn-codebuild-project-projecttriggers-buildtype)" : {{String}},
  "[FilterGroups](#cfn-codebuild-project-projecttriggers-filtergroups)" : {{[ Json, ... ]}},
  "[PullRequestBuildPolicy](#cfn-codebuild-project-projecttriggers-pullrequestbuildpolicy)" : {{PullRequestBuildPolicy}},
  "[ScopeConfiguration](#cfn-codebuild-project-projecttriggers-scopeconfiguration)" : {{ScopeConfiguration}},
  "[Webhook](#cfn-codebuild-project-projecttriggers-webhook)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-codebuild-project-projecttriggers-syntax.yaml"></a>

```
  [BuildType](#cfn-codebuild-project-projecttriggers-buildtype): {{String}}
  [FilterGroups](#cfn-codebuild-project-projecttriggers-filtergroups): {{
    - Json}}
  [PullRequestBuildPolicy](#cfn-codebuild-project-projecttriggers-pullrequestbuildpolicy): {{
    PullRequestBuildPolicy}}
  [ScopeConfiguration](#cfn-codebuild-project-projecttriggers-scopeconfiguration): {{
    ScopeConfiguration}}
  [Webhook](#cfn-codebuild-project-projecttriggers-webhook): {{Boolean}}
```

## Properties
<a name="aws-properties-codebuild-project-projecttriggers-properties"></a>

`BuildType`  <a name="cfn-codebuild-project-projecttriggers-buildtype"></a>
 Specifies the type of build this webhook will trigger. Allowed values are:
BUILD
A single build
BUILD\_BATCH
A batch build
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterGroups`  <a name="cfn-codebuild-project-projecttriggers-filtergroups"></a>
 A list of lists of `WebhookFilter` objects used to determine which webhook events are triggered. At least one `WebhookFilter` in the array must specify `EVENT` as its type.
*Required*: No
*Type*: Array of Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PullRequestBuildPolicy`  <a name="cfn-codebuild-project-projecttriggers-pullrequestbuildpolicy"></a>
Property description not available.
*Required*: No
*Type*: [PullRequestBuildPolicy](aws-properties-codebuild-project-pullrequestbuildpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeConfiguration`  <a name="cfn-codebuild-project-projecttriggers-scopeconfiguration"></a>
Contains configuration information about the scope for a webhook.
*Required*: No
*Type*: [ScopeConfiguration](aws-properties-codebuild-project-scopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Webhook`  <a name="cfn-codebuild-project-projecttriggers-webhook"></a>
 Specifies whether or not to begin automatically rebuilding the source code every time a code change is pushed to the repository.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
