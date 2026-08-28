---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-application-idcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Application IdCConfiguration
<a name="aws-properties-securityagent-application-idcconfiguration"></a>

The IAM Identity Center configuration for an application.

## Syntax
<a name="aws-properties-securityagent-application-idcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-application-idcconfiguration-syntax.json"></a>

```
{
  "[IdCApplicationArn](#cfn-securityagent-application-idcconfiguration-idcapplicationarn)" : {{String}},
  "[IdCInstanceArn](#cfn-securityagent-application-idcconfiguration-idcinstancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-application-idcconfiguration-syntax.yaml"></a>

```
  [IdCApplicationArn](#cfn-securityagent-application-idcconfiguration-idcapplicationarn): {{String}}
  [IdCInstanceArn](#cfn-securityagent-application-idcconfiguration-idcinstancearn): {{String}}
```

## Properties
<a name="aws-properties-securityagent-application-idcconfiguration-properties"></a>

`IdCApplicationArn`  <a name="cfn-securityagent-application-idcconfiguration-idcapplicationarn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center application.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdCInstanceArn`  <a name="cfn-securityagent-application-idcconfiguration-idcinstancearn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
