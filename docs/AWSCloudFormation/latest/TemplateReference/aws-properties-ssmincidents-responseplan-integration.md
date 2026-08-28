---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan Integration
<a name="aws-properties-ssmincidents-responseplan-integration"></a>

Information about third-party services integrated into a response plan.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-integration-syntax.json"></a>

```
{
  "[PagerDutyConfiguration](#cfn-ssmincidents-responseplan-integration-pagerdutyconfiguration)" : {{PagerDutyConfiguration}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-integration-syntax.yaml"></a>

```
  [PagerDutyConfiguration](#cfn-ssmincidents-responseplan-integration-pagerdutyconfiguration): {{
    PagerDutyConfiguration}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-integration-properties"></a>

`PagerDutyConfiguration`  <a name="cfn-ssmincidents-responseplan-integration-pagerdutyconfiguration"></a>
Information about the PagerDuty service where the response plan creates an incident.
*Required*: No
*Type*: [PagerDutyConfiguration](aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
