---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-quickconnect-userquickconnectconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::QuickConnect UserQuickConnectConfig
<a name="aws-properties-connect-quickconnect-userquickconnectconfig"></a>

Contains information about the quick connect configuration settings for a user. The contact flow must be of type Transfer to Agent.

## Syntax
<a name="aws-properties-connect-quickconnect-userquickconnectconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-quickconnect-userquickconnectconfig-syntax.json"></a>

```
{
  "[ContactFlowArn](#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn)" : {{String}},
  "[UserArn](#cfn-connect-quickconnect-userquickconnectconfig-userarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-quickconnect-userquickconnectconfig-syntax.yaml"></a>

```
  [ContactFlowArn](#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn): {{String}}
  [UserArn](#cfn-connect-quickconnect-userquickconnectconfig-userarn): {{String}}
```

## Properties
<a name="aws-properties-connect-quickconnect-userquickconnectconfig-properties"></a>

`ContactFlowArn`  <a name="cfn-connect-quickconnect-userquickconnectconfig-contactflowarn"></a>
The Amazon Resource Name (ARN) of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*(:[a-zA-Z0-9-]+)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserArn`  <a name="cfn-connect-quickconnect-userquickconnectconfig-userarn"></a>
The Amazon Resource Name (ARN) of the user.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/agent/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
