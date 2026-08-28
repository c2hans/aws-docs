---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LookoutEquipment::InferenceScheduler S3InputConfiguration
<a name="aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration"></a>

<a name="aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration-description"></a>The `S3InputConfiguration` property type specifies Property description not available. for an [AWS::LookoutEquipment::InferenceScheduler](aws-resource-lookoutequipment-inferencescheduler.md).

## Syntax
<a name="aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration-syntax.json"></a>

```
{
  "[Bucket](#cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-bucket)" : {{String}},
  "[Prefix](#cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration-syntax.yaml"></a>

```
  [Bucket](#cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-bucket): {{String}}
  [Prefix](#cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-prefix): {{String}}
```

## Properties
<a name="aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration-properties"></a>

`Bucket`  <a name="cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-bucket"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
