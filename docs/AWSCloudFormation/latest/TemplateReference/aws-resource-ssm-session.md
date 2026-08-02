---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-session.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::Session
<a name="aws-resource-ssm-session"></a>

Information about a Session Manager connection to a managed node.

## Syntax
<a name="aws-resource-ssm-session-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-session-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::Session",
  "Properties" : {
      "[Reason](#cfn-ssm-session-reason)" : {{String}},
      "[Target](#cfn-ssm-session-target)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssm-session-syntax.yaml"></a>

```
Type: AWS::SSM::Session
Properties:
  [Reason](#cfn-ssm-session-reason): {{String}}
  [Target](#cfn-ssm-session-target): {{String}}
```

## Properties
<a name="aws-resource-ssm-session-properties"></a>

`Reason`  <a name="cfn-ssm-session-reason"></a>
The reason for connecting to the instance.
*Required*: No
*Type*: String
*Pattern*: `^.{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Target`  <a name="cfn-ssm-session-target"></a>
The managed node that the Session Manager session connected to.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ssm-session-return-values"></a>

### Ref
<a name="aws-resource-ssm-session-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-session-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-session-return-values-fn--getatt-fn--getatt"></a>

`AccessType`  <a name="AccessType-fn::getatt"></a>
`Standard` access type is the default for Session Manager sessions. `JustInTime` is the access type for [Just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html).

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Owner`  <a name="Owner-fn::getatt"></a>
The ID of the Amazon Web Services user that started the session.

`SessionId`  <a name="SessionId-fn::getatt"></a>
The ID of the session.

`StartDate`  <a name="StartDate-fn::getatt"></a>
The date and time, in ISO-8601 Extended format, when the session began.

`Status`  <a name="Status-fn::getatt"></a>
The status of the session. For example, "Connected" or "Terminated".
