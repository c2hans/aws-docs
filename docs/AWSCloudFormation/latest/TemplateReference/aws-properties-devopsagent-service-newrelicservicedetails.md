---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-newrelicservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service NewRelicServiceDetails
<a name="aws-properties-devopsagent-service-newrelicservicedetails"></a>

Configuration details for registering a New Relic service.

## Syntax
<a name="aws-properties-devopsagent-service-newrelicservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-newrelicservicedetails-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-devopsagent-service-newrelicservicedetails-authorizationconfig)" : {{NewRelicAuthorizationConfig}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-newrelicservicedetails-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-devopsagent-service-newrelicservicedetails-authorizationconfig): {{
    NewRelicAuthorizationConfig}}
```

## Properties
<a name="aws-properties-devopsagent-service-newrelicservicedetails-properties"></a>

`AuthorizationConfig`  <a name="cfn-devopsagent-service-newrelicservicedetails-authorizationconfig"></a>
The authorization configuration for the New Relic service.
*Required*: Yes
*Type*: [NewRelicAuthorizationConfig](aws-properties-devopsagent-service-newrelicauthorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
