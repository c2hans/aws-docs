---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-rcsagent-testingagentinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::RcsAgent TestingAgentInformation
<a name="aws-properties-smsvoice-rcsagent-testingagentinformation"></a>

Contains details about the testing agent associated with an RCS agent.

## Syntax
<a name="aws-properties-smsvoice-rcsagent-testingagentinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-rcsagent-testingagentinformation-syntax.json"></a>

```
{
  "[RegistrationId](#cfn-smsvoice-rcsagent-testingagentinformation-registrationid)" : {{String}},
  "[TestingAgentId](#cfn-smsvoice-rcsagent-testingagentinformation-testingagentid)" : {{String}},
  "[TestingAgentStatus](#cfn-smsvoice-rcsagent-testingagentinformation-testingagentstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-rcsagent-testingagentinformation-syntax.yaml"></a>

```
  [RegistrationId](#cfn-smsvoice-rcsagent-testingagentinformation-registrationid): {{String}}
  [TestingAgentId](#cfn-smsvoice-rcsagent-testingagentinformation-testingagentid): {{String}}
  [TestingAgentStatus](#cfn-smsvoice-rcsagent-testingagentinformation-testingagentstatus): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-rcsagent-testingagentinformation-properties"></a>

`RegistrationId`  <a name="cfn-smsvoice-rcsagent-testingagentinformation-registrationid"></a>
The unique identifier of the registration associated with the testing agent.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestingAgentId`  <a name="cfn-smsvoice-rcsagent-testingagentinformation-testingagentid"></a>
The unique identifier for the testing agent.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestingAgentStatus`  <a name="cfn-smsvoice-rcsagent-testingagentinformation-testingagentstatus"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `CREATED | PENDING | ACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
