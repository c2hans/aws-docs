---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Resolver LambdaConflictHandlerConfig
<a name="aws-properties-appsync-resolver-lambdaconflicthandlerconfig"></a>

The `LambdaConflictHandlerConfig` when configuring LAMBDA as the Conflict Handler.

## Syntax
<a name="aws-properties-appsync-resolver-lambdaconflicthandlerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-resolver-lambdaconflicthandlerconfig-syntax.json"></a>

```
{
  "[LambdaConflictHandlerArn](#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-resolver-lambdaconflicthandlerconfig-syntax.yaml"></a>

```
  [LambdaConflictHandlerArn](#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn): {{String}}
```

## Properties
<a name="aws-properties-appsync-resolver-lambdaconflicthandlerconfig-properties"></a>

`LambdaConflictHandlerArn`  <a name="cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn"></a>
The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
