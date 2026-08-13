---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lookoutequipment-inferencescheduler.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LookoutEquipment::InferenceScheduler
<a name="aws-resource-lookoutequipment-inferencescheduler"></a>

 Creates a scheduled inference. Scheduling an inference is setting up a continuous real-time inference plan to analyze new measurement data. When setting up the schedule, you provide an Amazon S3 bucket location for the input data, assign it a delimiter between separate entries in the data, set an offset delay if desired, and set the frequency of inferencing. You must also provide an Amazon S3 bucket location for the output data.

**Note**
Updating some properties below (for example, InferenceSchedulerName and ServerSideKmsKeyId) triggers a resource replacement, which requires a new model. To replace such a property using CloudFormation, but without creating a completely new stack, you must replace ModelName. If you need to replace the property, but want to use the same model, delete the current stack and create a new one with the updated properties.

## Syntax
<a name="aws-resource-lookoutequipment-inferencescheduler-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lookoutequipment-inferencescheduler-syntax.json"></a>

```
{
  "Type" : "AWS::LookoutEquipment::InferenceScheduler",
  "Properties" : {
      "[DataDelayOffsetInMinutes](#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes)" : {{Integer}},
      "[DataInputConfiguration](#cfn-lookoutequipment-inferencescheduler-datainputconfiguration)" : {{DataInputConfiguration}},
      "[DataOutputConfiguration](#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration)" : {{DataOutputConfiguration}},
      "[DataUploadFrequency](#cfn-lookoutequipment-inferencescheduler-datauploadfrequency)" : {{String}},
      "[InferenceSchedulerName](#cfn-lookoutequipment-inferencescheduler-inferenceschedulername)" : {{String}},
      "[ModelName](#cfn-lookoutequipment-inferencescheduler-modelname)" : {{String}},
      "[RoleArn](#cfn-lookoutequipment-inferencescheduler-rolearn)" : {{String}},
      "[ServerSideKmsKeyId](#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid)" : {{String}},
      "[Tags](#cfn-lookoutequipment-inferencescheduler-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lookoutequipment-inferencescheduler-syntax.yaml"></a>

```
Type: AWS::LookoutEquipment::InferenceScheduler
Properties:
  [DataDelayOffsetInMinutes](#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes): {{Integer}}
  [DataInputConfiguration](#cfn-lookoutequipment-inferencescheduler-datainputconfiguration): {{
    DataInputConfiguration}}
  [DataOutputConfiguration](#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration): {{
    DataOutputConfiguration}}
  [DataUploadFrequency](#cfn-lookoutequipment-inferencescheduler-datauploadfrequency): {{String}}
  [InferenceSchedulerName](#cfn-lookoutequipment-inferencescheduler-inferenceschedulername): {{String}}
  [ModelName](#cfn-lookoutequipment-inferencescheduler-modelname): {{String}}
  [RoleArn](#cfn-lookoutequipment-inferencescheduler-rolearn): {{String}}
  [ServerSideKmsKeyId](#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid): {{String}}
  [Tags](#cfn-lookoutequipment-inferencescheduler-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lookoutequipment-inferencescheduler-properties"></a>

`DataDelayOffsetInMinutes`  <a name="cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes"></a>
A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if an offset delay time of five minutes was selected, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataInputConfiguration`  <a name="cfn-lookoutequipment-inferencescheduler-datainputconfiguration"></a>
Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.
*Required*: Yes
*Type*: [DataInputConfiguration](aws-properties-lookoutequipment-inferencescheduler-datainputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataOutputConfiguration`  <a name="cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration"></a>
Specifies configuration information for the output results for the inference scheduler, including the Amazon S3 location for the output.
*Required*: Yes
*Type*: [DataOutputConfiguration](aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataUploadFrequency`  <a name="cfn-lookoutequipment-inferencescheduler-datauploadfrequency"></a>
How often data is uploaded to the source S3 bucket for the input data. This value is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes.
*Required*: Yes
*Type*: String
*Allowed values*: `PT5M | PT10M | PT15M | PT30M | PT1H`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceSchedulerName`  <a name="cfn-lookoutequipment-inferencescheduler-inferenceschedulername"></a>
The name of the inference scheduler.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-zA-Z_-]{1,200}$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelName`  <a name="cfn-lookoutequipment-inferencescheduler-modelname"></a>
The name of the machine learning model used for the inference scheduler.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z_-]{1,200}$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-lookoutequipment-inferencescheduler-rolearn"></a>
The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideKmsKeyId`  <a name="cfn-lookoutequipment-inferencescheduler-serversidekmskeyid"></a>
Provides the identifier of the AWS KMS key used to encrypt inference scheduler data by Amazon Lookout for Equipment.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lookoutequipment-inferencescheduler-tags"></a>
Any tags associated with the inference scheduler.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-lookoutequipment-inferencescheduler-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lookoutequipment-inferencescheduler-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-lookoutequipment-inferencescheduler-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lookoutequipment-inferencescheduler-return-values-fn--getatt-fn--getatt"></a>

`InferenceSchedulerArn`  <a name="InferenceSchedulerArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the inference scheduler being created.

## Examples
<a name="aws-resource-lookoutequipment-inferencescheduler--examples"></a>

### Inference Scheduler
<a name="aws-resource-lookoutequipment-inferencescheduler--examples--Inference_Scheduler"></a>

Creates a schedule inference

#### JSON
<a name="aws-resource-lookoutequipment-inferencescheduler--examples--Inference_Scheduler--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "Name": {
      "Type": "String"
    }
  },
  "Resources": {
    "MyInferenceScheduler": {
      "Type": "AWS::LookoutEquipment::InferenceScheduler",
      "Properties": {
        "InferenceSchedulerName": {"Ref": "Name"},
        "ModelName": "my-test-model",
        "DataUploadFrequency": "PT5M",
        "RoleArn": {"Fn::ImportValue": "MyExportRole"},
        "DataInputConfiguration": {
          "S3InputConfiguration": {
            "Bucket": {"Fn::ImportValue":"MyExportBucket"},
            "Prefix": "myTestData/"
          }
        },
        "DataOutputConfiguration": {
          "S3OutputConfiguration": {
            "Bucket": {"Fn::ImportValue": "MyExportBucket"},
            "Prefix": "myTestData/"
          }
        }
      }
    }
  },
  "Outputs": {
    "PrimaryId": {
      "Value": {
        "Ref": "MyInferenceScheduler"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-lookoutequipment-inferencescheduler--examples--Inference_Scheduler--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  Name:
    Type: String
Resources:
  MyInferenceScheduler:
    Type: 'AWS::LookoutEquipment::InferenceScheduler'
    Properties:
      InferenceSchedulerName: !Ref Name
      ModelName: my-test-model
      DataUploadFrequency: PT5M
      RoleArn: !ImportValue MyExportRole
      DataInputConfiguration:
        S3InputConfiguration:
          Bucket: !ImportValue MyExportBucket
          Prefix: myTestData/
      DataOutputConfiguration:
        S3OutputConfiguration:
          Bucket: !ImportValue MyExportBucket
          Prefix: myTestData/
Outputs:
  PrimaryId:
    Value: !Ref MyInferenceScheduler
```
