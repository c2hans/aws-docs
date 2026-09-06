---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-aps-anomalydetector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::AnomalyDetector
<a name="aws-resource-aps-anomalydetector"></a>

Anomaly detection uses the Random Cut Forest algorithm for time-series analysis. The anomaly detector analyzes Amazon Managed Service for Prometheus metrics to identify unusual patterns and behaviors.

## Syntax
<a name="aws-resource-aps-anomalydetector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-aps-anomalydetector-syntax.json"></a>

```
{
  "Type" : "AWS::APS::AnomalyDetector",
  "Properties" : {
      "[Alias](#cfn-aps-anomalydetector-alias)" : {{String}},
      "[Configuration](#cfn-aps-anomalydetector-configuration)" : {{AnomalyDetectorConfiguration}},
      "[EvaluationIntervalInSeconds](#cfn-aps-anomalydetector-evaluationintervalinseconds)" : {{Integer}},
      "[Labels](#cfn-aps-anomalydetector-labels)" : {{[ Label, ... ]}},
      "[MissingDataAction](#cfn-aps-anomalydetector-missingdataaction)" : {{MissingDataAction}},
      "[Tags](#cfn-aps-anomalydetector-tags)" : {{[ Tag, ... ]}},
      "[Workspace](#cfn-aps-anomalydetector-workspace)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-aps-anomalydetector-syntax.yaml"></a>

```
Type: AWS::APS::AnomalyDetector
Properties:
  [Alias](#cfn-aps-anomalydetector-alias): {{String}}
  [Configuration](#cfn-aps-anomalydetector-configuration): {{
    AnomalyDetectorConfiguration}}
  [EvaluationIntervalInSeconds](#cfn-aps-anomalydetector-evaluationintervalinseconds): {{Integer}}
  [Labels](#cfn-aps-anomalydetector-labels): {{
    - Label}}
  [MissingDataAction](#cfn-aps-anomalydetector-missingdataaction): {{
    MissingDataAction}}
  [Tags](#cfn-aps-anomalydetector-tags): {{
    - Tag}}
  [Workspace](#cfn-aps-anomalydetector-workspace): {{String}}
```

## Properties
<a name="aws-resource-aps-anomalydetector-properties"></a>

`Alias`  <a name="cfn-aps-anomalydetector-alias"></a>
The user-friendly name of the anomaly detector.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-aps-anomalydetector-configuration"></a>
The algorithm configuration of the anomaly detector.
*Required*: Yes
*Type*: [AnomalyDetectorConfiguration](aws-properties-aps-anomalydetector-anomalydetectorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationIntervalInSeconds`  <a name="cfn-aps-anomalydetector-evaluationintervalinseconds"></a>
The frequency, in seconds, at which the anomaly detector evaluates metrics.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Labels`  <a name="cfn-aps-anomalydetector-labels"></a>
The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.
*Required*: No
*Type*: Array of [Label](aws-properties-aps-anomalydetector-label.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MissingDataAction`  <a name="cfn-aps-anomalydetector-missingdataaction"></a>
The action taken when data is missing during evaluation.
*Required*: No
*Type*: [MissingDataAction](aws-properties-aps-anomalydetector-missingdataaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-aps-anomalydetector-tags"></a>
The tags applied to the anomaly detector.
*Required*: No
*Type*: Array of [Tag](aws-properties-aps-anomalydetector-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workspace`  <a name="cfn-aps-anomalydetector-workspace"></a>
An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):aps:[a-z0-9-]+:[0-9]+:workspace/[a-zA-Z0-9-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-aps-anomalydetector-return-values"></a>

### Ref
<a name="aws-resource-aps-anomalydetector-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "Id" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-aps-anomalydetector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-aps-anomalydetector-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the anomaly detector.
