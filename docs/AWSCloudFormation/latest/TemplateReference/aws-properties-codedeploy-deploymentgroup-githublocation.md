---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-githublocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup GitHubLocation
<a name="aws-properties-codedeploy-deploymentgroup-githublocation"></a>

`GitHubLocation` is a property of the [CodeDeploy DeploymentGroup Revision](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html) property that specifies the location of an application revision that is stored in GitHub.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-githublocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-githublocation-syntax.json"></a>

```
{
  "[CommitId](#cfn-codedeploy-deploymentgroup-githublocation-commitid)" : {{String}},
  "[Repository](#cfn-codedeploy-deploymentgroup-githublocation-repository)" : {{String}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-githublocation-syntax.yaml"></a>

```
  [CommitId](#cfn-codedeploy-deploymentgroup-githublocation-commitid): {{String}}
  [Repository](#cfn-codedeploy-deploymentgroup-githublocation-repository): {{String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-githublocation-properties"></a>

`CommitId`  <a name="cfn-codedeploy-deploymentgroup-githublocation-commitid"></a>
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Repository`  <a name="cfn-codedeploy-deploymentgroup-githublocation-repository"></a>
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specify the value as `account/repository`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
