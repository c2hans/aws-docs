---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-agentspace-idpauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::AgentSpace IdpAuthConfiguration
<a name="aws-properties-devopsagent-agentspace-idpauthconfiguration"></a>

<a name="aws-properties-devopsagent-agentspace-idpauthconfiguration-description"></a>The `IdpAuthConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::AgentSpace](aws-resource-devopsagent-agentspace.md).

## Syntax
<a name="aws-properties-devopsagent-agentspace-idpauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-agentspace-idpauthconfiguration-syntax.json"></a>

```
{
  "[ClientId](#cfn-devopsagent-agentspace-idpauthconfiguration-clientid)" : {{String}},
  "[ClientSecret](#cfn-devopsagent-agentspace-idpauthconfiguration-clientsecret)" : {{String}},
  "[CreatedAt](#cfn-devopsagent-agentspace-idpauthconfiguration-createdat)" : {{String}},
  "[IssuerUrl](#cfn-devopsagent-agentspace-idpauthconfiguration-issuerurl)" : {{String}},
  "[OperatorAppRoleArn](#cfn-devopsagent-agentspace-idpauthconfiguration-operatorapprolearn)" : {{String}},
  "[Provider](#cfn-devopsagent-agentspace-idpauthconfiguration-provider)" : {{String}},
  "[UpdatedAt](#cfn-devopsagent-agentspace-idpauthconfiguration-updatedat)" : {{String}},
  "[UserIdClaim](#cfn-devopsagent-agentspace-idpauthconfiguration-useridclaim)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-agentspace-idpauthconfiguration-syntax.yaml"></a>

```
  [ClientId](#cfn-devopsagent-agentspace-idpauthconfiguration-clientid): {{String}}
  [ClientSecret](#cfn-devopsagent-agentspace-idpauthconfiguration-clientsecret): {{String}}
  [CreatedAt](#cfn-devopsagent-agentspace-idpauthconfiguration-createdat): {{String}}
  [IssuerUrl](#cfn-devopsagent-agentspace-idpauthconfiguration-issuerurl): {{String}}
  [OperatorAppRoleArn](#cfn-devopsagent-agentspace-idpauthconfiguration-operatorapprolearn): {{String}}
  [Provider](#cfn-devopsagent-agentspace-idpauthconfiguration-provider): {{String}}
  [UpdatedAt](#cfn-devopsagent-agentspace-idpauthconfiguration-updatedat): {{String}}
  [UserIdClaim](#cfn-devopsagent-agentspace-idpauthconfiguration-useridclaim): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-agentspace-idpauthconfiguration-properties"></a>

`ClientId`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-clientid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-clientsecret"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedAt`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-createdat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IssuerUrl`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-issuerurl"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+(?::[0-9]+)?(?:/.*)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatorAppRoleArn`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-operatorapprolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Provider`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-provider"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `okta | entra`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdatedAt`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-updatedat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserIdClaim`  <a name="cfn-devopsagent-agentspace-idpauthconfiguration-useridclaim"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
