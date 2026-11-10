---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-telemetryrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert TelemetryRule
<a name="aws-properties-cloudwatch-alert-telemetryrule"></a>

A rule that queries telemetry, evaluates the result against a condition, and sets how missing data is handled.

## Syntax
<a name="aws-properties-cloudwatch-alert-telemetryrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-telemetryrule-syntax.json"></a>

```
{
  "[Condition](#cfn-cloudwatch-alert-telemetryrule-condition)" : {{Condition}},
  "[Evaluation](#cfn-cloudwatch-alert-telemetryrule-evaluation)" : {{Evaluation}},
  "[NoData](#cfn-cloudwatch-alert-telemetryrule-nodata)" : {{NoData}},
  "[Query](#cfn-cloudwatch-alert-telemetryrule-query)" : {{Query}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-telemetryrule-syntax.yaml"></a>

```
  [Condition](#cfn-cloudwatch-alert-telemetryrule-condition): {{
    Condition}}
  [Evaluation](#cfn-cloudwatch-alert-telemetryrule-evaluation): {{
    Evaluation}}
  [NoData](#cfn-cloudwatch-alert-telemetryrule-nodata): {{
    NoData}}
  [Query](#cfn-cloudwatch-alert-telemetryrule-query): {{
    Query}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-telemetryrule-properties"></a>

`Condition`  <a name="cfn-cloudwatch-alert-telemetryrule-condition"></a>
Property description not available.
*Required*: Yes
*Type*: [Condition](aws-properties-cloudwatch-alert-condition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Evaluation`  <a name="cfn-cloudwatch-alert-telemetryrule-evaluation"></a>
Property description not available.
*Required*: Yes
*Type*: [Evaluation](aws-properties-cloudwatch-alert-evaluation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoData`  <a name="cfn-cloudwatch-alert-telemetryrule-nodata"></a>
Property description not available.
*Required*: No
*Type*: [NoData](aws-properties-cloudwatch-alert-nodata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Query`  <a name="cfn-cloudwatch-alert-telemetryrule-query"></a>
Property description not available.
*Required*: Yes
*Type*: [Query](aws-properties-cloudwatch-alert-query.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
