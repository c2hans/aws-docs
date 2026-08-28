---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-revisionlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup RevisionLocation
<a name="aws-properties-codedeploy-deploymentgroup-revisionlocation"></a>

`RevisionLocation` is a property that defines the location of the CodeDeploy application revision to deploy.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-revisionlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-revisionlocation-syntax.json"></a>

```
{
  "[GitHubLocation](#cfn-codedeploy-deploymentgroup-revisionlocation-githublocation)" : {{GitHubLocation}},
  "[RevisionType](#cfn-codedeploy-deploymentgroup-revisionlocation-revisiontype)" : {{String}},
  "[S3Location](#cfn-codedeploy-deploymentgroup-revisionlocation-s3location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-revisionlocation-syntax.yaml"></a>

```
  [GitHubLocation](#cfn-codedeploy-deploymentgroup-revisionlocation-githublocation): {{
    GitHubLocation}}
  [RevisionType](#cfn-codedeploy-deploymentgroup-revisionlocation-revisiontype): {{String}}
  [S3Location](#cfn-codedeploy-deploymentgroup-revisionlocation-s3location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-revisionlocation-properties"></a>

`GitHubLocation`  <a name="cfn-codedeploy-deploymentgroup-revisionlocation-githublocation"></a>
Information about the location of application artifacts stored in GitHub.
*Required*: No
*Type*: [GitHubLocation](aws-properties-codedeploy-deploymentgroup-githublocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RevisionType`  <a name="cfn-codedeploy-deploymentgroup-revisionlocation-revisiontype"></a>
The type of application revision:
+ S3: An application revision stored in Amazon S3.
+ GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
+ String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
+ AppSpecContent: An `AppSpecContent` object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
*Required*: No
*Type*: String
*Allowed values*: `S3 | GitHub | String | AppSpecContent | SystemsManagerPatchBaseline`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Location`  <a name="cfn-codedeploy-deploymentgroup-revisionlocation-s3location"></a>
Information about the location of a revision stored in Amazon S3.
*Required*: No
*Type*: [S3Location](aws-properties-codedeploy-deploymentgroup-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
