---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile MachineLearningDetectionConfig
<a name="aws-properties-iot-securityprofile-machinelearningdetectionconfig"></a>

The `MachineLearningDetectionConfig` property type controls confidence of the machine learning model.

## Syntax
<a name="aws-properties-iot-securityprofile-machinelearningdetectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-machinelearningdetectionconfig-syntax.json"></a>

```
{
  "[ConfidenceLevel](#cfn-iot-securityprofile-machinelearningdetectionconfig-confidencelevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-machinelearningdetectionconfig-syntax.yaml"></a>

```
  [ConfidenceLevel](#cfn-iot-securityprofile-machinelearningdetectionconfig-confidencelevel): {{String}}
```

## Properties
<a name="aws-properties-iot-securityprofile-machinelearningdetectionconfig-properties"></a>

`ConfidenceLevel`  <a name="cfn-iot-securityprofile-machinelearningdetectionconfig-confidencelevel"></a>
The model confidence level.
There are three levels of confidence, `"high"`, `"medium"`, and `"low"`.
The higher the confidence level, the lower the sensitivity, and the lower the alarm frequency will be.
*Required*: No
*Type*: String
*Allowed values*: `LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
