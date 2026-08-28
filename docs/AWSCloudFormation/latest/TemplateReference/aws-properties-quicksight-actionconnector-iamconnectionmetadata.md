---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-iamconnectionmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector IAMConnectionMetadata
<a name="aws-properties-quicksight-actionconnector-iamconnectionmetadata"></a>

Authentication metadata for IAM-based connections, used for first-party AWS service integrations.

## Syntax
<a name="aws-properties-quicksight-actionconnector-iamconnectionmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-iamconnectionmetadata-syntax.json"></a>

```
{
  "[RoleArn](#cfn-quicksight-actionconnector-iamconnectionmetadata-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-iamconnectionmetadata-syntax.yaml"></a>

```
  [RoleArn](#cfn-quicksight-actionconnector-iamconnectionmetadata-rolearn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-iamconnectionmetadata-properties"></a>

`RoleArn`  <a name="cfn-quicksight-actionconnector-iamconnectionmetadata-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to assume for authentication with AWS services. This IAM role should be in the same account as Quick Sight.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
