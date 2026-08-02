---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-loganomalydetector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::LogAnomalyDetector
<a name="aws-resource-logs-loganomalydetector"></a>

Creates or updates an *anomaly detector* that regularly scans one or more log groups and look for patterns and anomalies in the logs.

An anomaly detector can help surface issues by automatically discovering anomalies in your log event traffic. An anomaly detector uses machine learning algorithms to scan log events and find *patterns*. A pattern is a shared text structure that recurs among your log fields. Patterns provide a useful tool for analyzing large sets of logs because a large number of log events can often be compressed into a few patterns.

The anomaly detector uses pattern recognition to find `anomalies`, which are unusual log events. It compares current log events and patterns with trained baselines.

Fields within a pattern are called *tokens*. Fields that vary within a pattern, such as a request ID or timestamp, are referred to as *dynamic tokens* and represented by `<*>`.

For more information see [Log anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html).

## Syntax
<a name="aws-resource-logs-loganomalydetector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-loganomalydetector-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::LogAnomalyDetector",
  "Properties" : {
      "[AccountId](#cfn-logs-loganomalydetector-accountid)" : {{String}},
      "[AnomalyVisibilityTime](#cfn-logs-loganomalydetector-anomalyvisibilitytime)" : {{Number}},
      "[DetectorName](#cfn-logs-loganomalydetector-detectorname)" : {{String}},
      "[EvaluationFrequency](#cfn-logs-loganomalydetector-evaluationfrequency)" : {{String}},
      "[FilterPattern](#cfn-logs-loganomalydetector-filterpattern)" : {{String}},
      "[KmsKeyId](#cfn-logs-loganomalydetector-kmskeyid)" : {{String}},
      "[LogGroupArnList](#cfn-logs-loganomalydetector-loggrouparnlist)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-loganomalydetector-syntax.yaml"></a>

```
Type: AWS::Logs::LogAnomalyDetector
Properties:
  [AccountId](#cfn-logs-loganomalydetector-accountid): {{String}}
  [AnomalyVisibilityTime](#cfn-logs-loganomalydetector-anomalyvisibilitytime): {{Number}}
  [DetectorName](#cfn-logs-loganomalydetector-detectorname): {{String}}
  [EvaluationFrequency](#cfn-logs-loganomalydetector-evaluationfrequency): {{String}}
  [FilterPattern](#cfn-logs-loganomalydetector-filterpattern): {{String}}
  [KmsKeyId](#cfn-logs-loganomalydetector-kmskeyid): {{String}}
  [LogGroupArnList](#cfn-logs-loganomalydetector-loggrouparnlist): {{
    - String}}
```

## Properties
<a name="aws-resource-logs-loganomalydetector-properties"></a>

`AccountId`  <a name="cfn-logs-loganomalydetector-accountid"></a>
The ID of the account to create the anomaly detector in.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AnomalyVisibilityTime`  <a name="cfn-logs-loganomalydetector-anomalyvisibilitytime"></a>
The number of days to have visibility on an anomaly. After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in `AnomalyVisibilityTime`, it will be considered normal going forward and will not be detected as an anomaly.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorName`  <a name="cfn-logs-loganomalydetector-detectorname"></a>
A name for this anomaly detector.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationFrequency`  <a name="cfn-logs-loganomalydetector-evaluationfrequency"></a>
Specifies how often the anomaly detector is to run and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for `EvaluationFrequency` .
*Required*: No
*Type*: String
*Allowed values*: `FIVE_MIN | TEN_MIN | FIFTEEN_MIN | THIRTY_MIN | ONE_HOUR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterPattern`  <a name="cfn-logs-loganomalydetector-filterpattern"></a>
You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here. For more information, see [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-logs-loganomalydetector-kmskeyid"></a>
Optionally assigns a AWS KMS key to secure this anomaly detector and its findings. If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds.
For more information about using a AWS KMS key and to see the required IAM policy, see [Use a AWS KMS key with an anomaly detector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html).
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupArnList`  <a name="cfn-logs-loganomalydetector-loggrouparnlist"></a>
The ARN of the log group that is associated with this anomaly detector. You can specify only one log group ARN.
*Required*: No
*Type*: Array of String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-loganomalydetector-return-values"></a>

### Ref
<a name="aws-resource-logs-loganomalydetector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-loganomalydetector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-logs-loganomalydetector-return-values-fn--getatt-fn--getatt"></a>

`AnomalyDetectorArn`  <a name="AnomalyDetectorArn-fn::getatt"></a>
The ARN of the anomaly detector.

`AnomalyDetectorStatus`  <a name="AnomalyDetectorStatus-fn::getatt"></a>
Specifies whether the anomaly detector is currently active.

`CreationTimeStamp`  <a name="CreationTimeStamp-fn::getatt"></a>
The time that the anomaly detector was created.

`LastModifiedTimeStamp`  <a name="LastModifiedTimeStamp-fn::getatt"></a>
The time that the anomaly detector was most recently modified.
