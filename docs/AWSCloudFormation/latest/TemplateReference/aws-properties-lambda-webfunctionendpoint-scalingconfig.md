---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionendpoint-scalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint ScalingConfig
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig"></a>

(Amazon SQS only) The scaling configuration for the event source. To remove the configuration, pass an empty value.

## Syntax
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-syntax.json"></a>

```
{
  "[MaxEnvironments](#cfn-lambda-webfunctionendpoint-scalingconfig-maxenvironments)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-syntax.yaml"></a>

```
  [MaxEnvironments](#cfn-lambda-webfunctionendpoint-scalingconfig-maxenvironments): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-webfunctionendpoint-scalingconfig-properties"></a>

`MaxEnvironments`  <a name="cfn-lambda-webfunctionendpoint-scalingconfig-maxenvironments"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
