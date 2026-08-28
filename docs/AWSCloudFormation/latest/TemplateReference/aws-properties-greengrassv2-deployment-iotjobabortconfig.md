---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-iotjobabortconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment IoTJobAbortConfig
<a name="aws-properties-greengrassv2-deployment-iotjobabortconfig"></a>

Contains a list of criteria that define when and how to cancel a configuration deployment.

## Syntax
<a name="aws-properties-greengrassv2-deployment-iotjobabortconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-iotjobabortconfig-syntax.json"></a>

```
{
  "[CriteriaList](#cfn-greengrassv2-deployment-iotjobabortconfig-criterialist)" : {{[ IoTJobAbortCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-iotjobabortconfig-syntax.yaml"></a>

```
  [CriteriaList](#cfn-greengrassv2-deployment-iotjobabortconfig-criterialist): {{
    - IoTJobAbortCriteria}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-iotjobabortconfig-properties"></a>

`CriteriaList`  <a name="cfn-greengrassv2-deployment-iotjobabortconfig-criterialist"></a>
The list of criteria that define when and how to cancel the configuration deployment.
*Required*: Yes
*Type*: Array of [IoTJobAbortCriteria](aws-properties-greengrassv2-deployment-iotjobabortcriteria.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
