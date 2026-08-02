---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-flywheel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::Flywheel
<a name="aws-resource-comprehend-flywheel"></a>

A flywheel is an AWS resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.

When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.

To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.

To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.

For more information about flywheels, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Syntax
<a name="aws-resource-comprehend-flywheel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-flywheel-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::Flywheel",
  "Properties" : {
      "[ActiveModelArn](#cfn-comprehend-flywheel-activemodelarn)" : {{String}},
      "[DataAccessRoleArn](#cfn-comprehend-flywheel-dataaccessrolearn)" : {{String}},
      "[DataLakeS3Uri](#cfn-comprehend-flywheel-datalakes3uri)" : {{String}},
      "[DataSecurityConfig](#cfn-comprehend-flywheel-datasecurityconfig)" : {{DataSecurityConfig}},
      "[FlywheelName](#cfn-comprehend-flywheel-flywheelname)" : {{String}},
      "[ModelType](#cfn-comprehend-flywheel-modeltype)" : {{String}},
      "[Tags](#cfn-comprehend-flywheel-tags)" : {{[ Tag, ... ]}},
      "[TaskConfig](#cfn-comprehend-flywheel-taskconfig)" : {{TaskConfig}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-flywheel-syntax.yaml"></a>

```
Type: AWS::Comprehend::Flywheel
Properties:
  [ActiveModelArn](#cfn-comprehend-flywheel-activemodelarn): {{String}}
  [DataAccessRoleArn](#cfn-comprehend-flywheel-dataaccessrolearn): {{String}}
  [DataLakeS3Uri](#cfn-comprehend-flywheel-datalakes3uri): {{String}}
  [DataSecurityConfig](#cfn-comprehend-flywheel-datasecurityconfig): {{
    DataSecurityConfig}}
  [FlywheelName](#cfn-comprehend-flywheel-flywheelname): {{String}}
  [ModelType](#cfn-comprehend-flywheel-modeltype): {{String}}
  [Tags](#cfn-comprehend-flywheel-tags): {{
    - Tag}}
  [TaskConfig](#cfn-comprehend-flywheel-taskconfig): {{
    TaskConfig}}
```

## Properties
<a name="aws-resource-comprehend-flywheel-properties"></a>

`ActiveModelArn`  <a name="cfn-comprehend-flywheel-activemodelarn"></a>
The Amazon Resource Number (ARN) of the active model version.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataAccessRoleArn`  <a name="cfn-comprehend-flywheel-dataaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLakeS3Uri`  <a name="cfn-comprehend-flywheel-datalakes3uri"></a>
Amazon S3 URI of the data lake location.
*Required*: Yes
*Type*: String
*Pattern*: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSecurityConfig`  <a name="cfn-comprehend-flywheel-datasecurityconfig"></a>
Data security configuration.
*Required*: No
*Type*: [DataSecurityConfig](aws-properties-comprehend-flywheel-datasecurityconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlywheelName`  <a name="cfn-comprehend-flywheel-flywheelname"></a>
Name for the flywheel.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelType`  <a name="cfn-comprehend-flywheel-modeltype"></a>
Model type of the flywheel's model.
*Required*: No
*Type*: String
*Allowed values*: `DOCUMENT_CLASSIFIER | ENTITY_RECOGNIZER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-flywheel-tags"></a>
Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-flywheel-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskConfig`  <a name="cfn-comprehend-flywheel-taskconfig"></a>
Configuration about the model associated with a flywheel.
*Required*: No
*Type*: [TaskConfig](aws-properties-comprehend-flywheel-taskconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-flywheel-return-values"></a>

### Ref
<a name="aws-resource-comprehend-flywheel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the flywheel.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-comprehend-flywheel-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-comprehend-flywheel-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the flywheel.
