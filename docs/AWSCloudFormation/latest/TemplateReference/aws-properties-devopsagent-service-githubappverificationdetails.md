---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-githubappverificationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service GitHubAppVerificationDetails
<a name="aws-properties-devopsagent-service-githubappverificationdetails"></a>

<a name="aws-properties-devopsagent-service-githubappverificationdetails-description"></a>The `GitHubAppVerificationDetails` property type specifies Property description not available. for an [AWS::DevOpsAgent::Service](aws-resource-devopsagent-service.md).

## Syntax
<a name="aws-properties-devopsagent-service-githubappverificationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-githubappverificationdetails-syntax.json"></a>

```
{
  "[AppVariant](#cfn-devopsagent-service-githubappverificationdetails-appvariant)" : {{String}},
  "[OrganizationName](#cfn-devopsagent-service-githubappverificationdetails-organizationname)" : {{String}},
  "[TargetUrl](#cfn-devopsagent-service-githubappverificationdetails-targeturl)" : {{String}},
  "[TokenValue](#cfn-devopsagent-service-githubappverificationdetails-tokenvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-githubappverificationdetails-syntax.yaml"></a>

```
  [AppVariant](#cfn-devopsagent-service-githubappverificationdetails-appvariant): {{String}}
  [OrganizationName](#cfn-devopsagent-service-githubappverificationdetails-organizationname): {{String}}
  [TargetUrl](#cfn-devopsagent-service-githubappverificationdetails-targeturl): {{String}}
  [TokenValue](#cfn-devopsagent-service-githubappverificationdetails-tokenvalue): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-githubappverificationdetails-properties"></a>

`AppVariant`  <a name="cfn-devopsagent-service-githubappverificationdetails-appvariant"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `READ_ONLY | READ_WRITE | CUSTOM_APP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationName`  <a name="cfn-devopsagent-service-githubappverificationdetails-organizationname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](?:-?[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `39`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetUrl`  <a name="cfn-devopsagent-service-githubappverificationdetails-targeturl"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?(?::[0-9]{1,5})?/?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenValue`  <a name="cfn-devopsagent-service-githubappverificationdetails-tokenvalue"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
