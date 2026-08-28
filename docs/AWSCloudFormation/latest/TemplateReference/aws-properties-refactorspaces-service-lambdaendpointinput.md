---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-refactorspaces-service-lambdaendpointinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Service LambdaEndpointInput
<a name="aws-properties-refactorspaces-service-lambdaendpointinput"></a>

The input for the AWS Lambda endpoint type.

## Syntax
<a name="aws-properties-refactorspaces-service-lambdaendpointinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-refactorspaces-service-lambdaendpointinput-syntax.json"></a>

```
{
  "[Arn](#cfn-refactorspaces-service-lambdaendpointinput-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-refactorspaces-service-lambdaendpointinput-syntax.yaml"></a>

```
  [Arn](#cfn-refactorspaces-service-lambdaendpointinput-arn): {{String}}
```

## Properties
<a name="aws-properties-refactorspaces-service-lambdaendpointinput-properties"></a>

`Arn`  <a name="cfn-refactorspaces-service-lambdaendpointinput-arn"></a>
The Amazon Resource Name (ARN) of the Lambda function or alias.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
