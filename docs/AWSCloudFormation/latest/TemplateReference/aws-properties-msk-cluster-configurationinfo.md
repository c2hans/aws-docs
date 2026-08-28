---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-configurationinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster ConfigurationInfo
<a name="aws-properties-msk-cluster-configurationinfo"></a>

Specifies the configuration to use for the brokers.

## Syntax
<a name="aws-properties-msk-cluster-configurationinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-configurationinfo-syntax.json"></a>

```
{
  "[Arn](#cfn-msk-cluster-configurationinfo-arn)" : {{String}},
  "[Revision](#cfn-msk-cluster-configurationinfo-revision)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-msk-cluster-configurationinfo-syntax.yaml"></a>

```
  [Arn](#cfn-msk-cluster-configurationinfo-arn): {{String}}
  [Revision](#cfn-msk-cluster-configurationinfo-revision): {{Integer}}
```

## Properties
<a name="aws-properties-msk-cluster-configurationinfo-properties"></a>

`Arn`  <a name="cfn-msk-cluster-configurationinfo-arn"></a>
ARN of the configuration to use.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Revision`  <a name="cfn-msk-cluster-configurationinfo-revision"></a>
The revision of the configuration to use.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
