---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-mlflowapp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MlflowApp
<a name="aws-resource-sagemaker-mlflowapp"></a>

Creates an MLflow Tracking Server using a general purpose Amazon S3 bucket as the artifact store.

## Syntax
<a name="aws-resource-sagemaker-mlflowapp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-mlflowapp-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::MlflowApp",
  "Properties" : {
      "[ArtifactStoreUri](#cfn-sagemaker-mlflowapp-artifactstoreuri)" : {{String}},
      "[ModelRegistrationMode](#cfn-sagemaker-mlflowapp-modelregistrationmode)" : {{String}},
      "[Name](#cfn-sagemaker-mlflowapp-name)" : {{String}},
      "[RoleArn](#cfn-sagemaker-mlflowapp-rolearn)" : {{String}},
      "[Tags](#cfn-sagemaker-mlflowapp-tags)" : {{[ Tag, ... ]}},
      "[WeeklyMaintenanceWindowStart](#cfn-sagemaker-mlflowapp-weeklymaintenancewindowstart)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-mlflowapp-syntax.yaml"></a>

```
Type: AWS::SageMaker::MlflowApp
Properties:
  [ArtifactStoreUri](#cfn-sagemaker-mlflowapp-artifactstoreuri): {{String}}
  [ModelRegistrationMode](#cfn-sagemaker-mlflowapp-modelregistrationmode): {{String}}
  [Name](#cfn-sagemaker-mlflowapp-name): {{String}}
  [RoleArn](#cfn-sagemaker-mlflowapp-rolearn): {{String}}
  [Tags](#cfn-sagemaker-mlflowapp-tags): {{
    - Tag}}
  [WeeklyMaintenanceWindowStart](#cfn-sagemaker-mlflowapp-weeklymaintenancewindowstart): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-mlflowapp-properties"></a>

`ArtifactStoreUri`  <a name="cfn-sagemaker-mlflowapp-artifactstoreuri"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `(https|s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelRegistrationMode`  <a name="cfn-sagemaker-mlflowapp-modelregistrationmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AutoModelRegistrationEnabled | AutoModelRegistrationDisabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-mlflowapp-name"></a>
The name of the MLflow App.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-mlflowapp-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-mlflowapp-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-mlflowapp-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeeklyMaintenanceWindowStart`  <a name="cfn-sagemaker-mlflowapp-weeklymaintenancewindowstart"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
*Minimum*: `0`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-mlflowapp-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-mlflowapp-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-mlflowapp-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-mlflowapp-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of a listed MLflow App.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The creation time of a listed MLflow App.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The last modified time of a listed MLflow App.

`MlflowAppId`  <a name="MlflowAppId-fn::getatt"></a>
Property description not available.

`MlflowVersion`  <a name="MlflowVersion-fn::getatt"></a>
The version of a listed MLflow App.

`Status`  <a name="Status-fn::getatt"></a>
The status of the MLflow App.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
