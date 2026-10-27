---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-otaupdate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate
<a name="aws-resource-iot-otaupdate"></a>

Creates an AWS IoT OTA update on a target group of things or groups.

Requires permission to access the [CreateOTAUpdate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Syntax
<a name="aws-resource-iot-otaupdate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-otaupdate-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::OTAUpdate",
  "Properties" : {
      "[AdditionalParameters](#cfn-iot-otaupdate-additionalparameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[AwsJobAbortConfig](#cfn-iot-otaupdate-awsjobabortconfig)" : {{AwsJobAbortConfig}},
      "[AwsJobExecutionsRolloutConfig](#cfn-iot-otaupdate-awsjobexecutionsrolloutconfig)" : {{AwsJobExecutionsRolloutConfig}},
      "[AwsJobPresignedUrlConfig](#cfn-iot-otaupdate-awsjobpresignedurlconfig)" : {{AwsJobPresignedUrlConfig}},
      "[AwsJobTimeoutConfig](#cfn-iot-otaupdate-awsjobtimeoutconfig)" : {{AwsJobTimeoutConfig}},
      "[Description](#cfn-iot-otaupdate-description)" : {{String}},
      "[Files](#cfn-iot-otaupdate-files)" : {{[ OTAUpdateFile, ... ]}},
      "[OtaUpdateId](#cfn-iot-otaupdate-otaupdateid)" : {{String}},
      "[Protocols](#cfn-iot-otaupdate-protocols)" : {{[ String, ... ]}},
      "[RoleArn](#cfn-iot-otaupdate-rolearn)" : {{String}},
      "[Tags](#cfn-iot-otaupdate-tags)" : {{[ Tag, ... ]}},
      "[Targets](#cfn-iot-otaupdate-targets)" : {{[ String, ... ]}},
      "[TargetSelection](#cfn-iot-otaupdate-targetselection)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-otaupdate-syntax.yaml"></a>

```
Type: AWS::IoT::OTAUpdate
Properties:
  [AdditionalParameters](#cfn-iot-otaupdate-additionalparameters): {{
    {{Key}}: {{Value}}}}
  [AwsJobAbortConfig](#cfn-iot-otaupdate-awsjobabortconfig): {{
    AwsJobAbortConfig}}
  [AwsJobExecutionsRolloutConfig](#cfn-iot-otaupdate-awsjobexecutionsrolloutconfig): {{
    AwsJobExecutionsRolloutConfig}}
  [AwsJobPresignedUrlConfig](#cfn-iot-otaupdate-awsjobpresignedurlconfig): {{
    AwsJobPresignedUrlConfig}}
  [AwsJobTimeoutConfig](#cfn-iot-otaupdate-awsjobtimeoutconfig): {{
    AwsJobTimeoutConfig}}
  [Description](#cfn-iot-otaupdate-description): {{String}}
  [Files](#cfn-iot-otaupdate-files): {{
    - OTAUpdateFile}}
  [OtaUpdateId](#cfn-iot-otaupdate-otaupdateid): {{String}}
  [Protocols](#cfn-iot-otaupdate-protocols): {{
    - String}}
  [RoleArn](#cfn-iot-otaupdate-rolearn): {{String}}
  [Tags](#cfn-iot-otaupdate-tags): {{
    - Tag}}
  [Targets](#cfn-iot-otaupdate-targets): {{
    - String}}
  [TargetSelection](#cfn-iot-otaupdate-targetselection): {{String}}
```

## Properties
<a name="aws-resource-iot-otaupdate-properties"></a>

`AdditionalParameters`  <a name="cfn-iot-otaupdate-additionalparameters"></a>
A collection of name/value pairs
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsJobAbortConfig`  <a name="cfn-iot-otaupdate-awsjobabortconfig"></a>
The criteria that determine when and how a job abort takes place.
*Required*: No
*Type*: [AwsJobAbortConfig](aws-properties-iot-otaupdate-awsjobabortconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsJobExecutionsRolloutConfig`  <a name="cfn-iot-otaupdate-awsjobexecutionsrolloutconfig"></a>
Configuration for the rollout of OTA updates.
*Required*: No
*Type*: [AwsJobExecutionsRolloutConfig](aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsJobPresignedUrlConfig`  <a name="cfn-iot-otaupdate-awsjobpresignedurlconfig"></a>
Configuration information for pre-signed URLs. Valid when `protocols` contains HTTP.
*Required*: No
*Type*: [AwsJobPresignedUrlConfig](aws-properties-iot-otaupdate-awsjobpresignedurlconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AwsJobTimeoutConfig`  <a name="cfn-iot-otaupdate-awsjobtimeoutconfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
*Required*: No
*Type*: [AwsJobTimeoutConfig](aws-properties-iot-otaupdate-awsjobtimeoutconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-iot-otaupdate-description"></a>
A description of the OTA update.
*Required*: No
*Type*: String
*Pattern*: `^[^\p{C}]+$`
*Maximum*: `2028`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Files`  <a name="cfn-iot-otaupdate-files"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [OTAUpdateFile](aws-properties-iot-otaupdate-otaupdatefile.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OtaUpdateId`  <a name="cfn-iot-otaupdate-otaupdateid"></a>
The OTA update ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocols`  <a name="cfn-iot-otaupdate-protocols"></a>
The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.
*Required*: No
*Type*: Array of String
*Allowed values*: `MQTT | HTTP`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-iot-otaupdate-rolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iot-otaupdate-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-otaupdate-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-iot-otaupdate-targets"></a>
The targets of the OTA update.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetSelection`  <a name="cfn-iot-otaupdate-targetselection"></a>
Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a thing when a change is detected in a target. For example, an OTA update will run on a thing when the thing is added to a target group, even after the OTA update was completed by all things originally in the group.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUOUS | SNAPSHOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iot-otaupdate-return-values"></a>

### Ref
<a name="aws-resource-iot-otaupdate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iot-otaupdate-return-values-fn--getatt"></a>

####
<a name="aws-resource-iot-otaupdate-return-values-fn--getatt-fn--getatt"></a>

`CreationDate`  <a name="CreationDate-fn::getatt"></a>
The date when the OTA update was created.

`LastModifiedDate`  <a name="LastModifiedDate-fn::getatt"></a>
The date when the OTA update was last updated.

`OtaUpdateArn`  <a name="OtaUpdateArn-fn::getatt"></a>
The OTA update ARN.

`OtaUpdateStatus`  <a name="OtaUpdateStatus-fn::getatt"></a>
The status of the OTA update.
