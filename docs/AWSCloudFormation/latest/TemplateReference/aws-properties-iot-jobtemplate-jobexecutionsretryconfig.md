---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-jobtemplate-jobexecutionsretryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::JobTemplate JobExecutionsRetryConfig
<a name="aws-properties-iot-jobtemplate-jobexecutionsretryconfig"></a>

The configuration that determines how many retries are allowed for each failure type for a job.

## Syntax
<a name="aws-properties-iot-jobtemplate-jobexecutionsretryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-jobtemplate-jobexecutionsretryconfig-syntax.json"></a>

```
{
  "[RetryCriteriaList](#cfn-iot-jobtemplate-jobexecutionsretryconfig-retrycriterialist)" : {{[ RetryCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-jobtemplate-jobexecutionsretryconfig-syntax.yaml"></a>

```
  [RetryCriteriaList](#cfn-iot-jobtemplate-jobexecutionsretryconfig-retrycriterialist): {{
    - RetryCriteria}}
```

## Properties
<a name="aws-properties-iot-jobtemplate-jobexecutionsretryconfig-properties"></a>

`RetryCriteriaList`  <a name="cfn-iot-jobtemplate-jobexecutionsretryconfig-retrycriterialist"></a>
The list of criteria that determines how many retries are allowed for each failure type for a job.
*Required*: No
*Type*: Array of [RetryCriteria](aws-properties-iot-jobtemplate-retrycriteria.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
