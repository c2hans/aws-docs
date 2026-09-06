---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-awsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association AWSConfiguration
<a name="aws-properties-devopsagent-association-awsconfiguration"></a>

Configuration for AWS monitor account integration. Specifies the account ID, assumable role ARN, and resources to be monitored in the primary monitoring account.

## Syntax
<a name="aws-properties-devopsagent-association-awsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-awsconfiguration-syntax.json"></a>

```
{
  "[AccountId](#cfn-devopsagent-association-awsconfiguration-accountid)" : {{String}},
  "[AccountType](#cfn-devopsagent-association-awsconfiguration-accounttype)" : {{String}},
  "[AssumableRoleArn](#cfn-devopsagent-association-awsconfiguration-assumablerolearn)" : {{String}},
  "[Resources](#cfn-devopsagent-association-awsconfiguration-resources)" : {{[ AWSResource, ... ]}},
  "[Tags](#cfn-devopsagent-association-awsconfiguration-tags)" : {{[ KeyValuePair, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-awsconfiguration-syntax.yaml"></a>

```
  [AccountId](#cfn-devopsagent-association-awsconfiguration-accountid): {{String}}
  [AccountType](#cfn-devopsagent-association-awsconfiguration-accounttype): {{String}}
  [AssumableRoleArn](#cfn-devopsagent-association-awsconfiguration-assumablerolearn): {{String}}
  [Resources](#cfn-devopsagent-association-awsconfiguration-resources): {{
    - AWSResource}}
  [Tags](#cfn-devopsagent-association-awsconfiguration-tags): {{
    - KeyValuePair}}
```

## Properties
<a name="aws-properties-devopsagent-association-awsconfiguration-properties"></a>

`AccountId`  <a name="cfn-devopsagent-association-awsconfiguration-accountid"></a>
The 12-digit AWS account ID corresponding to the provided resources.
*Required*: Yes
*Type*: String
*Pattern*: `\d{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AccountType`  <a name="cfn-devopsagent-association-awsconfiguration-accounttype"></a>
The account type for AWS DevOps Agent monitoring.
*Allowed Values*: `monitor`
*Required*: Yes
*Type*: String
*Allowed values*: `monitor`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssumableRoleArn`  <a name="cfn-devopsagent-association-awsconfiguration-assumablerolearn"></a>
Role ARN used by AWS DevOps Agent to access resources in the primary account.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resources`  <a name="cfn-devopsagent-association-awsconfiguration-resources"></a>
List of resources to monitor.
*Required*: No
*Type*: Array of [AWSResource](aws-properties-devopsagent-association-awsresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-devopsagent-association-awsconfiguration-tags"></a>
List of tags as key-value pairs, used to identify resources for topology crawl.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-devopsagent-association-keyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
