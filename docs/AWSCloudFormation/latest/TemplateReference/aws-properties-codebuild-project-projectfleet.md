---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-projectfleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project ProjectFleet
<a name="aws-properties-codebuild-project-projectfleet"></a>

Information about the compute fleet of the build project. For more information, see [Working with reserved capacity in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html).

## Syntax
<a name="aws-properties-codebuild-project-projectfleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-projectfleet-syntax.json"></a>

```
{
  "[FleetArn](#cfn-codebuild-project-projectfleet-fleetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-projectfleet-syntax.yaml"></a>

```
  [FleetArn](#cfn-codebuild-project-projectfleet-fleetarn): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-projectfleet-properties"></a>

`FleetArn`  <a name="cfn-codebuild-project-projectfleet-fleetarn"></a>
Specifies the compute fleet ARN for the build project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
