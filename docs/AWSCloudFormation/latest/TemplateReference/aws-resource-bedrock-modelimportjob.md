---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-modelimportjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelImportJob
<a name="aws-resource-bedrock-modelimportjob"></a>

Creates a model import job to import model that you have customized in other environments, such as Amazon SageMaker. For more information, see [Import a customized model](https://docs.aws.amazon.com//bedrock/latest/userguide/model-customization-import-model.html)

## Syntax
<a name="aws-resource-bedrock-modelimportjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-modelimportjob-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::ModelImportJob",
  "Properties" : {
      "[ImportedModelKmsKeyArn](#cfn-bedrock-modelimportjob-importedmodelkmskeyarn)" : {{String}},
      "[ModelDataSource](#cfn-bedrock-modelimportjob-modeldatasource)" : {{ModelDataSource}},
      "[RoleArn](#cfn-bedrock-modelimportjob-rolearn)" : {{String}},
      "[Tags](#cfn-bedrock-modelimportjob-tags)" : {{[ Tag, ... ]}},
      "[VpcConfig](#cfn-bedrock-modelimportjob-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-modelimportjob-syntax.yaml"></a>

```
Type: AWS::Bedrock::ModelImportJob
Properties:
  [ImportedModelKmsKeyArn](#cfn-bedrock-modelimportjob-importedmodelkmskeyarn): {{String}}
  [ModelDataSource](#cfn-bedrock-modelimportjob-modeldatasource): {{
    ModelDataSource}}
  [RoleArn](#cfn-bedrock-modelimportjob-rolearn): {{String}}
  [Tags](#cfn-bedrock-modelimportjob-tags): {{
    - Tag}}
  [VpcConfig](#cfn-bedrock-modelimportjob-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-bedrock-modelimportjob-properties"></a>

`ImportedModelKmsKeyArn`  <a name="cfn-bedrock-modelimportjob-importedmodelkmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelDataSource`  <a name="cfn-bedrock-modelimportjob-modeldatasource"></a>
The data source of the model to import.
*Required*: Yes
*Type*: [ModelDataSource](aws-properties-bedrock-modelimportjob-modeldatasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-bedrock-modelimportjob-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-modelimportjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-modelimportjob-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-bedrock-modelimportjob-vpcconfig"></a>
The configuration of a virtual private cloud (VPC). For more information, see [Protect your data using Amazon Virtual Private Cloud and AWS PrivateLink](https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html).
*Required*: No
*Type*: [VpcConfig](aws-properties-bedrock-modelimportjob-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-modelimportjob-return-values"></a>

### Ref
<a name="aws-resource-bedrock-modelimportjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-modelimportjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-modelimportjob-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time import job was created.

`EndTime`  <a name="EndTime-fn::getatt"></a>
The time when import job ended.

`ImportedModelName`  <a name="ImportedModelName-fn::getatt"></a>
The name of the imported model.

`JobArn`  <a name="JobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the import job.

`JobName`  <a name="JobName-fn::getatt"></a>
The name of the import job.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time when the import job was last modified.

`Status`  <a name="Status-fn::getatt"></a>
The status of the imported job.
