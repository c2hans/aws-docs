---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-registeredpagerdutydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service RegisteredPagerDutyDetails
<a name="aws-properties-devopsagent-service-registeredpagerdutydetails"></a>

PagerDuty service details returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-registeredpagerdutydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-registeredpagerdutydetails-syntax.json"></a>

```
{
  "[Scopes](#cfn-devopsagent-service-registeredpagerdutydetails-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-registeredpagerdutydetails-syntax.yaml"></a>

```
  [Scopes](#cfn-devopsagent-service-registeredpagerdutydetails-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-service-registeredpagerdutydetails-properties"></a>

`Scopes`  <a name="cfn-devopsagent-service-registeredpagerdutydetails-scopes"></a>
The scopes that apply to the service.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
