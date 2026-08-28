---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::MaintenanceWindowTask MaintenanceWindowLambdaParameters
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters"></a>

The `MaintenanceWindowLambdaParameters` property type specifies the parameters for a `LAMBDA` task type for a maintenance window task in AWS Systems Manager.

`MaintenanceWindowLambdaParameters` is a property of the [TaskInvocationParameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html) property type.

## Syntax
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-syntax.json"></a>

```
{
  "[ClientContext](#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext)" : {{String}},
  "[Payload](#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload)" : {{String}},
  "[Qualifier](#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-syntax.yaml"></a>

```
  [ClientContext](#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext): {{String}}
  [Payload](#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload): {{String}}
  [Qualifier](#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier): {{String}}
```

## Properties
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-properties"></a>

`ClientContext`  <a name="cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext"></a>
Client-specific information to pass to the AWS Lambda function that you're invoking. You can then use the `context` variable to process the client information in your AWS Lambda function.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `8000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Payload`  <a name="cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload"></a>
JSON to provide to your AWS Lambda function as input.
Although `Type` is listed as "String" for this property, the payload content must be formatted as a Base64-encoded binary data object.
*Length Constraint:* 4096
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Qualifier`  <a name="cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier"></a>
An AWS Lambda function version or alias name. If you specify a function version, the action uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version that the alias points to.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
