---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthchecksource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource

<a name="aws-resource-route53-healthchecksource-description"></a>The `AWS::Route53::HealthCheckSource` resource Property description not available. for Route53.

## Syntax
<a name="aws-resource-route53-healthchecksource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-healthchecksource-syntax.json"></a>

```
{
  "Type" : "AWS::Route53::HealthCheckSource",
  "Properties" : {
      "[HealthCheckSourceConfig](#cfn-route53-healthchecksource-healthchecksourceconfig)" : {{HealthCheckSourceConfig}},
      "[Tags](#cfn-route53-healthchecksource-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53-healthchecksource-syntax.yaml"></a>

```
Type: AWS::Route53::HealthCheckSource
Properties:
  [HealthCheckSourceConfig](#cfn-route53-healthchecksource-healthchecksourceconfig): {{
    HealthCheckSourceConfig}}
  [Tags](#cfn-route53-healthchecksource-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53-healthchecksource-properties"></a>

`HealthCheckSourceConfig`  <a name="cfn-route53-healthchecksource-healthchecksourceconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [HealthCheckSourceConfig](aws-properties-route53-healthchecksource-healthchecksourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53-healthchecksource-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53-healthchecksource-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53-healthchecksource-return-values"></a>

### Ref
<a name="aws-resource-route53-healthchecksource-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53-healthchecksource-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53-healthchecksource-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`HealthCheckSourceId`  <a name="HealthCheckSourceId-fn::getatt"></a>
Property description not available.

`HealthCheckSourceStatus`  <a name="HealthCheckSourceStatus-fn::getatt"></a>
Property description not available.
