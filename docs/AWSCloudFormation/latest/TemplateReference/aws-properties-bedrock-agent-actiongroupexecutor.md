---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-actiongroupexecutor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent ActionGroupExecutor
<a name="aws-properties-bedrock-agent-actiongroupexecutor"></a>

 Contains details about the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.

## Syntax
<a name="aws-properties-bedrock-agent-actiongroupexecutor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-actiongroupexecutor-syntax.json"></a>

```
{
  "[CustomControl](#cfn-bedrock-agent-actiongroupexecutor-customcontrol)" : {{String}},
  "[Lambda](#cfn-bedrock-agent-actiongroupexecutor-lambda)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-actiongroupexecutor-syntax.yaml"></a>

```
  [CustomControl](#cfn-bedrock-agent-actiongroupexecutor-customcontrol): {{String}}
  [Lambda](#cfn-bedrock-agent-actiongroupexecutor-lambda): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-actiongroupexecutor-properties"></a>

`CustomControl`  <a name="cfn-bedrock-agent-actiongroupexecutor-customcontrol"></a>
 To return the action group invocation results directly in the `InvokeInlineAgent` response, specify `RETURN_CONTROL`.
*Required*: No
*Type*: String
*Allowed values*: `RETURN_CONTROL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lambda`  <a name="cfn-bedrock-agent-actiongroupexecutor-lambda"></a>
 The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z0-9-]{1,20}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
