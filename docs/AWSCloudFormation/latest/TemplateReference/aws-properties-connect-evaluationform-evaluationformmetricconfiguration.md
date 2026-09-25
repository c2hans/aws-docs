---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformmetricconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormMetricConfiguration
<a name="aws-properties-connect-evaluationform-evaluationformmetricconfiguration"></a>

Information about the metric configuration for an evaluation form question. Use this to associate a business outcome metric with a question.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformmetricconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformmetricconfiguration-syntax.json"></a>

```
{
  "[MetricName](#cfn-connect-evaluationform-evaluationformmetricconfiguration-metricname)" : {{String}},
  "[MetricType](#cfn-connect-evaluationform-evaluationformmetricconfiguration-metrictype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformmetricconfiguration-syntax.yaml"></a>

```
  [MetricName](#cfn-connect-evaluationform-evaluationformmetricconfiguration-metricname): {{String}}
  [MetricType](#cfn-connect-evaluationform-evaluationformmetricconfiguration-metrictype): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformmetricconfiguration-properties"></a>

`MetricName`  <a name="cfn-connect-evaluationform-evaluationformmetricconfiguration-metricname"></a>
The name of the metric. Valid values are:
+ `SALE_SUCCESS` – Sale success.
+ `CSAT` – Customer satisfaction.
+ `CHURN_PROPENSITY` – Churn propensity.
+ `SELF_SERVICE_SUCCESS` – Self-service success.
+ `PARTIAL_SELF_SERVICE_SUCCESS` – Partial self-service success.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\p{C}]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricType`  <a name="cfn-connect-evaluationform-evaluationformmetricconfiguration-metrictype"></a>
The type of metric. Currently, only `BUSINESS_OUTCOME` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `BUSINESS_OUTCOME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
