---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-pagerdutydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service PagerDutyDetails
<a name="aws-properties-devopsagent-service-pagerdutydetails"></a>

Configuration details for registering a PagerDuty service.

## Syntax
<a name="aws-properties-devopsagent-service-pagerdutydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-pagerdutydetails-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-pagerdutydetails-authorizationconfig)" : {{PagerDutyAuthorizationConfig}},
  "[Scopes](#cfn-devopsagent-service-pagerdutydetails-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-pagerdutydetails-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-pagerdutydetails-authorizationconfig): {{
    PagerDutyAuthorizationConfig}}
  [Scopes](#cfn-devopsagent-service-pagerdutydetails-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-service-pagerdutydetails-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-pagerdutydetails-authorizationconfig"></a>
The authorization configuration for the PagerDuty service.
*Required*: Yes
*Type*: [PagerDutyAuthorizationConfig](aws-properties-devopsagent-service-pagerdutyauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-devopsagent-service-pagerdutydetails-scopes"></a>
The PagerDuty scopes that you grant to the service.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
