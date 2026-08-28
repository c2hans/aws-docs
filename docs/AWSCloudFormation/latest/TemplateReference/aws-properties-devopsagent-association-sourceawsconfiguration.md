---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-sourceawsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association SourceAwsConfiguration
<a name="aws-properties-devopsagent-association-sourceawsconfiguration"></a>

Configuration for AWS source account integration. Specifies the account ID, assumable role ARN, and resources to be monitored in the source account.

## Syntax
<a name="aws-properties-devopsagent-association-sourceawsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-sourceawsconfiguration-syntax.json"></a>

```
{
  "[AccountId](#cfn-devopsagent-association-sourceawsconfiguration-accountid)" : {{String}},
  "[AccountType](#cfn-devopsagent-association-sourceawsconfiguration-accounttype)" : {{String}},
  "[AssumableRoleArn](#cfn-devopsagent-association-sourceawsconfiguration-assumablerolearn)" : {{String}},
  "[Resources](#cfn-devopsagent-association-sourceawsconfiguration-resources)" : {{[ AWSResource, ... ]}},
  "[Tags](#cfn-devopsagent-association-sourceawsconfiguration-tags)" : {{[ KeyValuePair, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-sourceawsconfiguration-syntax.yaml"></a>

```
  [AccountId](#cfn-devopsagent-association-sourceawsconfiguration-accountid): {{String}}
  [AccountType](#cfn-devopsagent-association-sourceawsconfiguration-accounttype): {{String}}
  [AssumableRoleArn](#cfn-devopsagent-association-sourceawsconfiguration-assumablerolearn): {{String}}
  [Resources](#cfn-devopsagent-association-sourceawsconfiguration-resources): {{
    - AWSResource}}
  [Tags](#cfn-devopsagent-association-sourceawsconfiguration-tags): {{
    - KeyValuePair}}
```

## Properties
<a name="aws-properties-devopsagent-association-sourceawsconfiguration-properties"></a>

`AccountId`  <a name="cfn-devopsagent-association-sourceawsconfiguration-accountid"></a>
The 12-digit AWS account ID corresponding to the provided resources.
*Required*: Yes
*Type*: String
*Pattern*: `\d{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AccountType`  <a name="cfn-devopsagent-association-sourceawsconfiguration-accounttype"></a>
The account type for AWS DevOps Agent monitoring.
*Allowed Values*: `source`
*Required*: Yes
*Type*: String
*Allowed values*: `source`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssumableRoleArn`  <a name="cfn-devopsagent-association-sourceawsconfiguration-assumablerolearn"></a>
Role ARN to be assumed by AWS DevOps Agent to operate on behalf of customer.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resources`  <a name="cfn-devopsagent-association-sourceawsconfiguration-resources"></a>
List of resources to monitor.
*Required*: No
*Type*: Array of [AWSResource](aws-properties-devopsagent-association-awsresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-devopsagent-association-sourceawsconfiguration-tags"></a>
List of tags as key-value pairs, used to identify resources for topology crawl.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-devopsagent-association-keyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
