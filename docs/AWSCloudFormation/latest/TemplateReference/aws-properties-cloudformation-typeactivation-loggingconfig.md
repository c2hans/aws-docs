---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-typeactivation-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::TypeActivation LoggingConfig
<a name="aws-properties-cloudformation-typeactivation-loggingconfig"></a>

Contains logging configuration information for an extension.

## Syntax
<a name="aws-properties-cloudformation-typeactivation-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-typeactivation-loggingconfig-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-cloudformation-typeactivation-loggingconfig-loggroupname)" : {{String}},
  "[LogRoleArn](#cfn-cloudformation-typeactivation-loggingconfig-logrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudformation-typeactivation-loggingconfig-syntax.yaml"></a>

```
  [LogGroupName](#cfn-cloudformation-typeactivation-loggingconfig-loggroupname): {{String}}
  [LogRoleArn](#cfn-cloudformation-typeactivation-loggingconfig-logrolearn): {{String}}
```

## Properties
<a name="aws-properties-cloudformation-typeactivation-loggingconfig-properties"></a>

`LogGroupName`  <a name="cfn-cloudformation-typeactivation-loggingconfig-loggroupname"></a>
The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogRoleArn`  <a name="cfn-cloudformation-typeactivation-loggingconfig-logrolearn"></a>
The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
