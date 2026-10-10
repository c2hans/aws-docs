---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-githubpatdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service GitHubPatDetails
<a name="aws-properties-devopsagent-service-githubpatdetails"></a>

<a name="aws-properties-devopsagent-service-githubpatdetails-description"></a>The `GitHubPatDetails` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-githubpatdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-githubpatdetails-syntax.json"></a>

```
{
  "[OrganizationName](#cfn-devopsagent-service-githubpatdetails-organizationname)" : {{String}},
  "[TargetUrl](#cfn-devopsagent-service-githubpatdetails-targeturl)" : {{String}},
  "[TokenValue](#cfn-devopsagent-service-githubpatdetails-tokenvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-githubpatdetails-syntax.yaml"></a>

```
  [OrganizationName](#cfn-devopsagent-service-githubpatdetails-organizationname): {{String}}
  [TargetUrl](#cfn-devopsagent-service-githubpatdetails-targeturl): {{String}}
  [TokenValue](#cfn-devopsagent-service-githubpatdetails-tokenvalue): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-githubpatdetails-properties"></a>

`OrganizationName`  <a name="cfn-devopsagent-service-githubpatdetails-organizationname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](?:-?[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `39`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetUrl`  <a name="cfn-devopsagent-service-githubpatdetails-targeturl"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?(?::[0-9]{1,5})?/?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenValue`  <a name="cfn-devopsagent-service-githubpatdetails-tokenvalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
