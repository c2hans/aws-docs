---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-integration-gitlabinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Integration GitLabInput
<a name="aws-properties-securityagent-integration-gitlabinput"></a>

<a name="aws-properties-securityagent-integration-gitlabinput-description"></a>The `GitLabInput` property type specifies Property description not available. for an [AWS::SecurityAgent::Integration](aws-resource-securityagent-integration.md).

## Syntax
<a name="aws-properties-securityagent-integration-gitlabinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-integration-gitlabinput-syntax.json"></a>

```
{
  "[AccessToken](#cfn-securityagent-integration-gitlabinput-accesstoken)" : {{String}},
  "[GroupId](#cfn-securityagent-integration-gitlabinput-groupid)" : {{String}},
  "[TargetUrl](#cfn-securityagent-integration-gitlabinput-targeturl)" : {{String}},
  "[TokenType](#cfn-securityagent-integration-gitlabinput-tokentype)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-integration-gitlabinput-syntax.yaml"></a>

```
  [AccessToken](#cfn-securityagent-integration-gitlabinput-accesstoken): {{String}}
  [GroupId](#cfn-securityagent-integration-gitlabinput-groupid): {{String}}
  [TargetUrl](#cfn-securityagent-integration-gitlabinput-targeturl): {{String}}
  [TokenType](#cfn-securityagent-integration-gitlabinput-tokentype): {{String}}
```

## Properties
<a name="aws-properties-securityagent-integration-gitlabinput-properties"></a>

`AccessToken`  <a name="cfn-securityagent-integration-gitlabinput-accesstoken"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupId`  <a name="cfn-securityagent-integration-gitlabinput-groupid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetUrl`  <a name="cfn-securityagent-integration-gitlabinput-targeturl"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenType`  <a name="cfn-securityagent-integration-gitlabinput-tokentype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `PERSONAL | GROUP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
