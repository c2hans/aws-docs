---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredgitlabservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredGitLabServiceDetails
<a name="aws-properties-devopsagent-service-registeredgitlabservicedetails"></a>

GitLab service details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registeredgitlabservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredgitlabservicedetails-syntax.json"></a>

```
{
  "[GroupId](#cfn-devopsagent-service-registeredgitlabservicedetails-groupid)" : {{String}},
  "[TargetUrl](#cfn-devopsagent-service-registeredgitlabservicedetails-targeturl)" : {{String}},
  "[TokenType](#cfn-devopsagent-service-registeredgitlabservicedetails-tokentype)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredgitlabservicedetails-syntax.yaml"></a>

```
  [GroupId](#cfn-devopsagent-service-registeredgitlabservicedetails-groupid): {{String}}
  [TargetUrl](#cfn-devopsagent-service-registeredgitlabservicedetails-targeturl): {{String}}
  [TokenType](#cfn-devopsagent-service-registeredgitlabservicedetails-tokentype): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredgitlabservicedetails-properties"></a>

`GroupId`  <a name="cfn-devopsagent-service-registeredgitlabservicedetails-groupid"></a>
The GitLab group ID for group-level access tokens.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetUrl`  <a name="cfn-devopsagent-service-registeredgitlabservicedetails-targeturl"></a>
The GitLab instance URL.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenType`  <a name="cfn-devopsagent-service-registeredgitlabservicedetails-tokentype"></a>
The type of GitLab access token.
*Allowed Values*: `personal` \| `group`
*Required*: Yes
*Type*: String
*Allowed values*: `personal | group`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
