---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-clientconnectoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint ClientConnectOptions
<a name="aws-properties-ec2-clientvpnendpoint-clientconnectoptions"></a>

Indicates whether client connect options are enabled. The default is `false` (not enabled).

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-clientconnectoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-clientconnectoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-ec2-clientvpnendpoint-clientconnectoptions-enabled)" : {{Boolean}},
  "[LambdaFunctionArn](#cfn-ec2-clientvpnendpoint-clientconnectoptions-lambdafunctionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-clientconnectoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-ec2-clientvpnendpoint-clientconnectoptions-enabled): {{Boolean}}
  [LambdaFunctionArn](#cfn-ec2-clientvpnendpoint-clientconnectoptions-lambdafunctionarn): {{String}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-clientconnectoptions-properties"></a>

`Enabled`  <a name="cfn-ec2-clientvpnendpoint-clientconnectoptions-enabled"></a>
Indicates whether client connect options are enabled. The default is `false` (not enabled).
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaFunctionArn`  <a name="cfn-ec2-clientvpnendpoint-clientconnectoptions-lambdafunctionarn"></a>
The Amazon Resource Name (ARN) of the AWS Lambda function used for connection authorization.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
