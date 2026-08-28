---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-featuregroup-ttlduration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::FeatureGroup TtlDuration
<a name="aws-properties-sagemaker-featuregroup-ttlduration"></a>

Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.

## Syntax
<a name="aws-properties-sagemaker-featuregroup-ttlduration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-featuregroup-ttlduration-syntax.json"></a>

```
{
  "[Unit](#cfn-sagemaker-featuregroup-ttlduration-unit)" : {{String}},
  "[Value](#cfn-sagemaker-featuregroup-ttlduration-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-featuregroup-ttlduration-syntax.yaml"></a>

```
  [Unit](#cfn-sagemaker-featuregroup-ttlduration-unit): {{String}}
  [Value](#cfn-sagemaker-featuregroup-ttlduration-value): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-featuregroup-ttlduration-properties"></a>

`Unit`  <a name="cfn-sagemaker-featuregroup-ttlduration-unit"></a>
`TtlDuration` time unit.
*Required*: No
*Type*: String
*Allowed values*: `Seconds | Minutes | Hours | Days | Weeks`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-featuregroup-ttlduration-value"></a>
`TtlDuration` time value.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
