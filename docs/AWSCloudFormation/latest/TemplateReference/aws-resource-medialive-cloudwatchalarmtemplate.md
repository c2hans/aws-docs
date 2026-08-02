---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-cloudwatchalarmtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::CloudWatchAlarmTemplate
<a name="aws-resource-medialive-cloudwatchalarmtemplate"></a>

<a name="aws-resource-medialive-cloudwatchalarmtemplate-description"></a>The `AWS::MediaLive::CloudWatchAlarmTemplate` resource Property description not available. for MediaLive.

## Syntax
<a name="aws-resource-medialive-cloudwatchalarmtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-cloudwatchalarmtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::CloudWatchAlarmTemplate",
  "Properties" : {
      "[ComparisonOperator](#cfn-medialive-cloudwatchalarmtemplate-comparisonoperator)" : {{String}},
      "[DatapointsToAlarm](#cfn-medialive-cloudwatchalarmtemplate-datapointstoalarm)" : {{Number}},
      "[Description](#cfn-medialive-cloudwatchalarmtemplate-description)" : {{String}},
      "[EvaluationPeriods](#cfn-medialive-cloudwatchalarmtemplate-evaluationperiods)" : {{Number}},
      "[GroupIdentifier](#cfn-medialive-cloudwatchalarmtemplate-groupidentifier)" : {{String}},
      "[MetricName](#cfn-medialive-cloudwatchalarmtemplate-metricname)" : {{String}},
      "[Name](#cfn-medialive-cloudwatchalarmtemplate-name)" : {{String}},
      "[Period](#cfn-medialive-cloudwatchalarmtemplate-period)" : {{Number}},
      "[Statistic](#cfn-medialive-cloudwatchalarmtemplate-statistic)" : {{String}},
      "[Tags](#cfn-medialive-cloudwatchalarmtemplate-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TargetResourceType](#cfn-medialive-cloudwatchalarmtemplate-targetresourcetype)" : {{String}},
      "[Threshold](#cfn-medialive-cloudwatchalarmtemplate-threshold)" : {{Number}},
      "[TreatMissingData](#cfn-medialive-cloudwatchalarmtemplate-treatmissingdata)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-medialive-cloudwatchalarmtemplate-syntax.yaml"></a>

```
Type: AWS::MediaLive::CloudWatchAlarmTemplate
Properties:
  [ComparisonOperator](#cfn-medialive-cloudwatchalarmtemplate-comparisonoperator): {{String}}
  [DatapointsToAlarm](#cfn-medialive-cloudwatchalarmtemplate-datapointstoalarm): {{Number}}
  [Description](#cfn-medialive-cloudwatchalarmtemplate-description): {{String}}
  [EvaluationPeriods](#cfn-medialive-cloudwatchalarmtemplate-evaluationperiods): {{Number}}
  [GroupIdentifier](#cfn-medialive-cloudwatchalarmtemplate-groupidentifier): {{String}}
  [MetricName](#cfn-medialive-cloudwatchalarmtemplate-metricname): {{String}}
  [Name](#cfn-medialive-cloudwatchalarmtemplate-name): {{String}}
  [Period](#cfn-medialive-cloudwatchalarmtemplate-period): {{Number}}
  [Statistic](#cfn-medialive-cloudwatchalarmtemplate-statistic): {{String}}
  [Tags](#cfn-medialive-cloudwatchalarmtemplate-tags): {{
    {{Key}}: {{Value}}}}
  [TargetResourceType](#cfn-medialive-cloudwatchalarmtemplate-targetresourcetype): {{String}}
  [Threshold](#cfn-medialive-cloudwatchalarmtemplate-threshold): {{Number}}
  [TreatMissingData](#cfn-medialive-cloudwatchalarmtemplate-treatmissingdata): {{String}}
```

## Properties
<a name="aws-resource-medialive-cloudwatchalarmtemplate-properties"></a>

`ComparisonOperator`  <a name="cfn-medialive-cloudwatchalarmtemplate-comparisonoperator"></a>
The comparison operator used to compare the specified statistic and the threshold.
*Required*: Yes
*Type*: String
*Allowed values*: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatapointsToAlarm`  <a name="cfn-medialive-cloudwatchalarmtemplate-datapointstoalarm"></a>
The number of datapoints within the evaluation period that must be breaching to trigger the alarm.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-medialive-cloudwatchalarmtemplate-description"></a>
A resource's optional description.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationPeriods`  <a name="cfn-medialive-cloudwatchalarmtemplate-evaluationperiods"></a>
The number of periods over which data is compared to the specified threshold.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupIdentifier`  <a name="cfn-medialive-cloudwatchalarmtemplate-groupidentifier"></a>
A cloudwatch alarm template group's identifier. Can be either be its id or current name.
*Required*: No
*Type*: String
*Pattern*: `^[^\s]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-medialive-cloudwatchalarmtemplate-metricname"></a>
The name of the metric associated with the alarm. Must be compatible with targetResourceType.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-cloudwatchalarmtemplate-name"></a>
A resource's name. Names must be unique within the scope of a resource type in a specific region.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Period`  <a name="cfn-medialive-cloudwatchalarmtemplate-period"></a>
The period, in seconds, over which the specified statistic is applied.
*Required*: Yes
*Type*: Number
*Minimum*: `10`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Statistic`  <a name="cfn-medialive-cloudwatchalarmtemplate-statistic"></a>
The statistic to apply to the alarm's metric data.
*Required*: Yes
*Type*: String
*Allowed values*: `SampleCount | Average | Sum | Minimum | Maximum`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-cloudwatchalarmtemplate-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetResourceType`  <a name="cfn-medialive-cloudwatchalarmtemplate-targetresourcetype"></a>
The resource type this template should dynamically generate CloudWatch metric alarms for.
*Required*: Yes
*Type*: String
*Allowed values*: `CLOUDFRONT_DISTRIBUTION | MEDIALIVE_MULTIPLEX | MEDIALIVE_CHANNEL | MEDIALIVE_INPUT_DEVICE | MEDIAPACKAGE_CHANNEL | MEDIAPACKAGE_ORIGIN_ENDPOINT | MEDIACONNECT_FLOW | MEDIATAILOR_PLAYBACK_CONFIGURATION | S3_BUCKET`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-medialive-cloudwatchalarmtemplate-threshold"></a>
The threshold value to compare with the specified statistic.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TreatMissingData`  <a name="cfn-medialive-cloudwatchalarmtemplate-treatmissingdata"></a>
Specifies how missing data points are treated when evaluating the alarm's condition.
*Required*: Yes
*Type*: String
*Allowed values*: `notBreaching | breaching | ignore | missing`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-cloudwatchalarmtemplate-return-values"></a>

### Ref
<a name="aws-resource-medialive-cloudwatchalarmtemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-cloudwatchalarmtemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-cloudwatchalarmtemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
A cloudwatch alarm template's ARN (Amazon Resource Name)

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time of resource creation.

`GroupId`  <a name="GroupId-fn::getatt"></a>
A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>

`Id`  <a name="Id-fn::getatt"></a>
A cloudwatch alarm template's id. Amazon Web Services provided templates have ids that start with <code>`aws-`</code>.

`Identifier`  <a name="Identifier-fn::getatt"></a>
Property description not available.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The date and time of latest resource modification.
