---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-githubdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service GitHubDetails
<a name="aws-properties-devopsagent-service-githubdetails"></a>

<a name="aws-properties-devopsagent-service-githubdetails-description"></a>The `GitHubDetails` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-githubdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-githubdetails-syntax.json"></a>

```
{
  "[AppVerification](#cfn-devopsagent-service-githubdetails-appverification)" : {{GitHubAppVerificationDetails}},
  "[DirectAccess](#cfn-devopsagent-service-githubdetails-directaccess)" : {{GitHubPatDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-githubdetails-syntax.yaml"></a>

```
  [AppVerification](#cfn-devopsagent-service-githubdetails-appverification): {{
    GitHubAppVerificationDetails}}
  [DirectAccess](#cfn-devopsagent-service-githubdetails-directaccess): {{
    GitHubPatDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-githubdetails-properties"></a>

`AppVerification`  <a name="cfn-devopsagent-service-githubdetails-appverification"></a>
Property description not available.
*Required*: No
*Type*: [GitHubAppVerificationDetails](aws-properties-devopsagent-service-githubappverificationdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DirectAccess`  <a name="cfn-devopsagent-service-githubdetails-directaccess"></a>
Property description not available.
*Required*: No
*Type*: [GitHubPatDetails](aws-properties-devopsagent-service-githubpatdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
