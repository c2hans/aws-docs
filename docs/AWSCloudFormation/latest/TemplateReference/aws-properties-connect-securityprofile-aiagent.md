---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-aiagent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile AIAgent
<a name="aws-properties-connect-securityprofile-aiagent"></a>

Information about an AI agent that a security profile allows access to for Agent-to-Agent authorization.

## Syntax
<a name="aws-properties-connect-securityprofile-aiagent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-aiagent-syntax.json"></a>

```
{
  "[Arn](#cfn-connect-securityprofile-aiagent-arn)" : {{String}},
  "[Type](#cfn-connect-securityprofile-aiagent-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-aiagent-syntax.yaml"></a>

```
  [Arn](#cfn-connect-securityprofile-aiagent-arn): {{String}}
  [Type](#cfn-connect-securityprofile-aiagent-type): {{String}}
```

## Properties
<a name="aws-properties-connect-securityprofile-aiagent-properties"></a>

`Arn`  <a name="cfn-connect-securityprofile-aiagent-arn"></a>
The Amazon Resource Name (ARN) of the AI agent.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:app-integrations:[-a-z0-9]*:[0-9]{12}:application/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-securityprofile-aiagent-type"></a>
The type of the AI agent. The valid value is `THIRD_PARTY`.
*Required*: Yes
*Type*: String
*Allowed values*: `THIRD_PARTY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
