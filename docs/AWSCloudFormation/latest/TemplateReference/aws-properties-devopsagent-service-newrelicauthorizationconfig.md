---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-newrelicauthorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service NewRelicAuthorizationConfig
<a name="aws-properties-devopsagent-service-newrelicauthorizationconfig"></a>

The authorization configuration for a New Relic service.

## Syntax
<a name="aws-properties-devopsagent-service-newrelicauthorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-newrelicauthorizationconfig-syntax.json"></a>

```
{
  "[ApiKey](#cfn-devopsagent-service-newrelicauthorizationconfig-apikey)" : {{NewRelicApiKeyConfig}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-newrelicauthorizationconfig-syntax.yaml"></a>

```
  [ApiKey](#cfn-devopsagent-service-newrelicauthorizationconfig-apikey): {{
    NewRelicApiKeyConfig}}
```

## Properties
<a name="aws-properties-devopsagent-service-newrelicauthorizationconfig-properties"></a>

`ApiKey`  <a name="cfn-devopsagent-service-newrelicauthorizationconfig-apikey"></a>
The API key configuration for authenticating with New Relic.
*Required*: Yes
*Type*: [NewRelicApiKeyConfig](aws-properties-devopsagent-service-newrelicapikeyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
