---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LookoutEquipment::InferenceScheduler DataOutputConfiguration
<a name="aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration"></a>

<a name="aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration-description"></a>The `DataOutputConfiguration` property type specifies Property description not available. for an [AWS::LookoutEquipment::InferenceScheduler](aws-resource-lookoutequipment-inferencescheduler.md).

## Syntax
<a name="aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-kmskeyid)" : {{String}},
  "[S3OutputConfiguration](#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-s3outputconfiguration)" : {{S3OutputConfiguration}}
}
```

### YAML
<a name="aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-kmskeyid): {{String}}
  [S3OutputConfiguration](#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-s3outputconfiguration): {{
    S3OutputConfiguration}}
```

## Properties
<a name="aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-kmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3OutputConfiguration`  <a name="cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-s3outputconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [S3OutputConfiguration](aws-properties-lookoutequipment-inferencescheduler-s3outputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
