---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-quickconnect-flowquickconnectconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::QuickConnect FlowQuickConnectConfig
<a name="aws-properties-connect-quickconnect-flowquickconnectconfig"></a>

 Configuration for quick connect.

## Syntax
<a name="aws-properties-connect-quickconnect-flowquickconnectconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-quickconnect-flowquickconnectconfig-syntax.json"></a>

```
{
  "[ContactFlowArn](#cfn-connect-quickconnect-flowquickconnectconfig-contactflowarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-quickconnect-flowquickconnectconfig-syntax.yaml"></a>

```
  [ContactFlowArn](#cfn-connect-quickconnect-flowquickconnectconfig-contactflowarn): {{String}}
```

## Properties
<a name="aws-properties-connect-quickconnect-flowquickconnectconfig-properties"></a>

`ContactFlowArn`  <a name="cfn-connect-quickconnect-flowquickconnectconfig-contactflowarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*(:[a-zA-Z0-9-]+)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
