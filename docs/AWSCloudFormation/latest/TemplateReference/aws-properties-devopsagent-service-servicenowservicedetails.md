---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-servicenowservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service ServiceNowServiceDetails
<a name="aws-properties-devopsagent-service-servicenowservicedetails"></a>

Configuration details for registering a ServiceNow service.

## Syntax
<a name="aws-properties-devopsagent-service-servicenowservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-servicenowservicedetails-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-servicenowservicedetails-authorizationconfig)" : {{ServiceNowAuthorizationConfig}},
  "[InstanceUrl](#cfn-devopsagent-service-servicenowservicedetails-instanceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-servicenowservicedetails-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-servicenowservicedetails-authorizationconfig): {{
    ServiceNowAuthorizationConfig}}
  [InstanceUrl](#cfn-devopsagent-service-servicenowservicedetails-instanceurl): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-servicenowservicedetails-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-servicenowservicedetails-authorizationconfig"></a>
The authorization configuration for the ServiceNow service.
*Required*: No
*Type*: [ServiceNowAuthorizationConfig](aws-properties-devopsagent-service-servicenowauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceUrl`  <a name="cfn-devopsagent-service-servicenowservicedetails-instanceurl"></a>
The ServiceNow instance URL. Must be an HTTPS URL matching the format `https://<instance-name>.service-now.com`.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9-]+\.service-now\.com/?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
