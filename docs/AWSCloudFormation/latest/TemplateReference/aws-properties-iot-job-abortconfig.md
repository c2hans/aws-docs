---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-abortconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job AbortConfig
<a name="aws-properties-iot-job-abortconfig"></a>

The criteria that determine when and how a job abort takes place.

## Syntax
<a name="aws-properties-iot-job-abortconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-abortconfig-syntax.json"></a>

```
{
  "[CriteriaList](#cfn-iot-job-abortconfig-criterialist)" : {{[ AbortCriteria, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-job-abortconfig-syntax.yaml"></a>

```
  [CriteriaList](#cfn-iot-job-abortconfig-criterialist): {{
    - AbortCriteria}}
```

## Properties
<a name="aws-properties-iot-job-abortconfig-properties"></a>

`CriteriaList`  <a name="cfn-iot-job-abortconfig-criterialist"></a>
The list of criteria that determine when and how to abort the job.
*Required*: Yes
*Type*: Array of [AbortCriteria](aws-properties-iot-job-abortcriteria.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
