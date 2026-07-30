---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-deployment-deploymentcanarysettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::Deployment DeploymentCanarySettings
<a name="aws-properties-apigateway-deployment-deploymentcanarysettings"></a>

The `DeploymentCanarySettings` property type specifies settings for the canary deployment.

## Syntax
<a name="aws-properties-apigateway-deployment-deploymentcanarysettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-deployment-deploymentcanarysettings-syntax.json"></a>

```
{
  "[PercentTraffic](#cfn-apigateway-deployment-deploymentcanarysettings-percenttraffic)" : {{Number}},
  "[StageVariableOverrides](#cfn-apigateway-deployment-deploymentcanarysettings-stagevariableoverrides)" : {{{{{Key}}: {{Value}}, ...}}},
  "[UseStageCache](#cfn-apigateway-deployment-deploymentcanarysettings-usestagecache)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-apigateway-deployment-deploymentcanarysettings-syntax.yaml"></a>

```
  [PercentTraffic](#cfn-apigateway-deployment-deploymentcanarysettings-percenttraffic): {{Number}}
  [StageVariableOverrides](#cfn-apigateway-deployment-deploymentcanarysettings-stagevariableoverrides): {{
    {{Key}}: {{Value}}}}
  [UseStageCache](#cfn-apigateway-deployment-deploymentcanarysettings-usestagecache): {{Boolean}}
```

## Properties
<a name="aws-properties-apigateway-deployment-deploymentcanarysettings-properties"></a>

`PercentTraffic`  <a name="cfn-apigateway-deployment-deploymentcanarysettings-percenttraffic"></a>
The percentage (0.0-100.0) of traffic routed to the canary deployment.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StageVariableOverrides`  <a name="cfn-apigateway-deployment-deploymentcanarysettings-stagevariableoverrides"></a>
A stage variable overrides used for the canary release deployment. They can override existing stage variables or add new stage variables for the canary release deployment. These stage variables are represented as a string-to-string map between stage variable names and their values.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UseStageCache`  <a name="cfn-apigateway-deployment-deploymentcanarysettings-usestagecache"></a>
A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-apigateway-deployment-deploymentcanarysettings--seealso"></a>
+ [CreateDeployment](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateDeployment.html) in the *Amazon API Gateway REST API Reference*
