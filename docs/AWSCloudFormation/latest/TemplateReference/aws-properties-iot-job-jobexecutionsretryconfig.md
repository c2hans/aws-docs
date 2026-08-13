---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-jobexecutionsretryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job JobExecutionsRetryConfig
<a name="aws-properties-iot-job-jobexecutionsretryconfig"></a>

The configuration that determines how many retries are allowed for each failure type for a job.

## Syntax
<a name="aws-properties-iot-job-jobexecutionsretryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-jobexecutionsretryconfig-syntax.json"></a>

```
{
  "[CriteriaList](#cfn-iot-job-jobexecutionsretryconfig-criterialist)" : {{[ RetryCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-job-jobexecutionsretryconfig-syntax.yaml"></a>

```
  [CriteriaList](#cfn-iot-job-jobexecutionsretryconfig-criterialist): {{
    - RetryCriteria}}
```

## Properties
<a name="aws-properties-iot-job-jobexecutionsretryconfig-properties"></a>

`CriteriaList`  <a name="cfn-iot-job-jobexecutionsretryconfig-criterialist"></a>
The list of criteria that determines how many retries are allowed for each failure type for a job.
*Required*: Yes
*Type*: Array of [RetryCriteria](aws-properties-iot-job-retrycriteria.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
