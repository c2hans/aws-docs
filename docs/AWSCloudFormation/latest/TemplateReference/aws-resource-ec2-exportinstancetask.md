---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-exportinstancetask.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ExportInstanceTask
<a name="aws-resource-ec2-exportinstancetask"></a>

<a name="aws-resource-ec2-exportinstancetask-description"></a>The `AWS::EC2::ExportInstanceTask` resource Property description not available. for EC2.

## Syntax
<a name="aws-resource-ec2-exportinstancetask-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-exportinstancetask-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::ExportInstanceTask",
  "Properties" : {
      "[Description](#cfn-ec2-exportinstancetask-description)" : {{String}},
      "[ExportToS3Task](#cfn-ec2-exportinstancetask-exporttos3task)" : {{ExportToS3Task}},
      "[InstanceId](#cfn-ec2-exportinstancetask-instanceid)" : {{String}},
      "[Tags](#cfn-ec2-exportinstancetask-tags)" : {{[ Tag, ... ]}},
      "[TargetEnvironment](#cfn-ec2-exportinstancetask-targetenvironment)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-exportinstancetask-syntax.yaml"></a>

```
Type: AWS::EC2::ExportInstanceTask
Properties:
  [Description](#cfn-ec2-exportinstancetask-description): {{String}}
  [ExportToS3Task](#cfn-ec2-exportinstancetask-exporttos3task): {{
    ExportToS3Task}}
  [InstanceId](#cfn-ec2-exportinstancetask-instanceid): {{String}}
  [Tags](#cfn-ec2-exportinstancetask-tags): {{
    - Tag}}
  [TargetEnvironment](#cfn-ec2-exportinstancetask-targetenvironment): {{String}}
```

## Properties
<a name="aws-resource-ec2-exportinstancetask-properties"></a>

`Description`  <a name="cfn-ec2-exportinstancetask-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExportToS3Task`  <a name="cfn-ec2-exportinstancetask-exporttos3task"></a>
Describes the format and location for the export task.
*Required*: No
*Type*: [ExportToS3Task](aws-properties-ec2-exportinstancetask-exporttos3task.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceId`  <a name="cfn-ec2-exportinstancetask-instanceid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-exportinstancetask-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-exportinstancetask-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetEnvironment`  <a name="cfn-ec2-exportinstancetask-targetenvironment"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `citrix | vmware | microsoft`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-exportinstancetask-return-values"></a>

### Ref
<a name="aws-resource-ec2-exportinstancetask-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-exportinstancetask-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-exportinstancetask-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`ExportTaskId`  <a name="ExportTaskId-fn::getatt"></a>
Property description not available.

`ExportToS3Task.S3Key`  <a name="ExportToS3Task.S3Key-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.
