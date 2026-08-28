---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment IoTJobRateIncreaseCriteria
<a name="aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria"></a>

Contains information about criteria to meet before a job increases its rollout rate. Specify either `numberOfNotifiedThings` or `numberOfSucceededThings`.

## Syntax
<a name="aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria-syntax.json"></a>

```
{
  "[NumberOfNotifiedThings](#cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofnotifiedthings)" : {{Integer}},
  "[NumberOfSucceededThings](#cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofsucceededthings)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria-syntax.yaml"></a>

```
  [NumberOfNotifiedThings](#cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofnotifiedthings): {{Integer}}
  [NumberOfSucceededThings](#cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofsucceededthings): {{Integer}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria-properties"></a>

`NumberOfNotifiedThings`  <a name="cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofnotifiedthings"></a>
The number of devices to receive the job notification before the rollout rate increases.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NumberOfSucceededThings`  <a name="cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofsucceededthings"></a>
The number of devices to successfully run the configuration job before the rollout rate increases.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
