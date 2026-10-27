---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-awsjobabortconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate AwsJobAbortConfig
<a name="aws-properties-iot-otaupdate-awsjobabortconfig"></a>

The criteria that determine when and how a job abort takes place.

## Syntax
<a name="aws-properties-iot-otaupdate-awsjobabortconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-awsjobabortconfig-syntax.json"></a>

```
{
  "[AbortCriteriaList](#cfn-iot-otaupdate-awsjobabortconfig-abortcriterialist)" : {{[ AwsJobAbortCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-awsjobabortconfig-syntax.yaml"></a>

```
  [AbortCriteriaList](#cfn-iot-otaupdate-awsjobabortconfig-abortcriterialist): {{
    - AwsJobAbortCriteria}}
```

## Properties
<a name="aws-properties-iot-otaupdate-awsjobabortconfig-properties"></a>

`AbortCriteriaList`  <a name="cfn-iot-otaupdate-awsjobabortconfig-abortcriterialist"></a>
The list of criteria that determine when and how to abort the job.
*Required*: Yes
*Type*: Array of [AwsJobAbortCriteria](aws-properties-iot-otaupdate-awsjobabortcriteria.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
