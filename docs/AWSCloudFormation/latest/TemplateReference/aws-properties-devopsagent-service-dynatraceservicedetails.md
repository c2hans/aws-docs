---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-dynatraceservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service DynatraceServiceDetails
<a name="aws-properties-devopsagent-service-dynatraceservicedetails"></a>

Configuration details for registering a Dynatrace service.

## Syntax
<a name="aws-properties-devopsagent-service-dynatraceservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-dynatraceservicedetails-syntax.json"></a>

```
{
  "[AccountUrn](#cfn-devopsagent-service-dynatraceservicedetails-accounturn)" : {{String}},
  "[AuthorizationConfig](#cfn-devopsagent-service-dynatraceservicedetails-authorizationconfig)" : {{DynatraceAuthorizationConfig}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-dynatraceservicedetails-syntax.yaml"></a>

```
  [AccountUrn](#cfn-devopsagent-service-dynatraceservicedetails-accounturn): {{String}}
  [AuthorizationConfig](#cfn-devopsagent-service-dynatraceservicedetails-authorizationconfig): {{
    DynatraceAuthorizationConfig}}
```

## Properties
<a name="aws-properties-devopsagent-service-dynatraceservicedetails-properties"></a>

`AccountUrn`  <a name="cfn-devopsagent-service-dynatraceservicedetails-accounturn"></a>
The Dynatrace account URN.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationConfig`  <a name="cfn-devopsagent-service-dynatraceservicedetails-authorizationconfig"></a>
The authorization configuration for the Dynatrace service.
*Required*: No
*Type*: [DynatraceAuthorizationConfig](aws-properties-devopsagent-service-dynatraceauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
