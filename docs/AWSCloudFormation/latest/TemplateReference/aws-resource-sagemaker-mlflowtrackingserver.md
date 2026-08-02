---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-mlflowtrackingserver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MlflowTrackingServer
<a name="aws-resource-sagemaker-mlflowtrackingserver"></a>

Creates an MLflow Tracking Server using a general purpose Amazon S3 bucket as the artifact store. For more information, see [Create an MLflow Tracking Server](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html).

## Syntax
<a name="aws-resource-sagemaker-mlflowtrackingserver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-mlflowtrackingserver-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::MlflowTrackingServer",
  "Properties" : {
      "[ArtifactStoreUri](#cfn-sagemaker-mlflowtrackingserver-artifactstoreuri)" : {{String}},
      "[AutomaticModelRegistration](#cfn-sagemaker-mlflowtrackingserver-automaticmodelregistration)" : {{Boolean}},
      "[MlflowVersion](#cfn-sagemaker-mlflowtrackingserver-mlflowversion)" : {{String}},
      "[RoleArn](#cfn-sagemaker-mlflowtrackingserver-rolearn)" : {{String}},
      "[Tags](#cfn-sagemaker-mlflowtrackingserver-tags)" : {{[ Tag, ... ]}},
      "[TrackingServerName](#cfn-sagemaker-mlflowtrackingserver-trackingservername)" : {{String}},
      "[TrackingServerSize](#cfn-sagemaker-mlflowtrackingserver-trackingserversize)" : {{String}},
      "[WeeklyMaintenanceWindowStart](#cfn-sagemaker-mlflowtrackingserver-weeklymaintenancewindowstart)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-mlflowtrackingserver-syntax.yaml"></a>

```
Type: AWS::SageMaker::MlflowTrackingServer
Properties:
  [ArtifactStoreUri](#cfn-sagemaker-mlflowtrackingserver-artifactstoreuri): {{String}}
  [AutomaticModelRegistration](#cfn-sagemaker-mlflowtrackingserver-automaticmodelregistration): {{Boolean}}
  [MlflowVersion](#cfn-sagemaker-mlflowtrackingserver-mlflowversion): {{String}}
  [RoleArn](#cfn-sagemaker-mlflowtrackingserver-rolearn): {{String}}
  [Tags](#cfn-sagemaker-mlflowtrackingserver-tags): {{
    - Tag}}
  [TrackingServerName](#cfn-sagemaker-mlflowtrackingserver-trackingservername): {{String}}
  [TrackingServerSize](#cfn-sagemaker-mlflowtrackingserver-trackingserversize): {{String}}
  [WeeklyMaintenanceWindowStart](#cfn-sagemaker-mlflowtrackingserver-weeklymaintenancewindowstart): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-mlflowtrackingserver-properties"></a>

`ArtifactStoreUri`  <a name="cfn-sagemaker-mlflowtrackingserver-artifactstoreuri"></a>
The S3 URI for a general purpose bucket to use as the MLflow Tracking Server artifact store.
*Required*: Yes
*Type*: String
*Pattern*: `^s3:\/\/([^\/]+)\/?(.*)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticModelRegistration`  <a name="cfn-sagemaker-mlflowtrackingserver-automaticmodelregistration"></a>
Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to `True`. To disable automatic model registration, set this value to `False`. If not specified, `AutomaticModelRegistration` defaults to `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MlflowVersion`  <a name="cfn-sagemaker-mlflowtrackingserver-mlflowversion"></a>
The version of MLflow that the tracking server uses. To see which MLflow versions are available to use, see [How it works](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html#mlflow-create-tracking-server-how-it-works).
*Required*: No
*Type*: String
*Pattern*: `^\d+(\.\d+)+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`RoleArn`  <a name="cfn-sagemaker-mlflowtrackingserver-rolearn"></a>
The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow Tracking Server uses to access the artifact store in Amazon S3. The role should have `AmazonS3FullAccess` permissions. For more information on IAM permissions for tracking server creation, see [Set up IAM permissions for MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server-iam.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role\/?[a-zA-Z_0-9+=,.@\-_\/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-sagemaker-mlflowtrackingserver-tags"></a>
Tags consisting of key-value pairs used to manage metadata for the tracking server.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-mlflowtrackingserver-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrackingServerName`  <a name="cfn-sagemaker-mlflowtrackingserver-trackingservername"></a>
A unique string identifying the tracking server name. This string is part of the tracking server ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrackingServerSize`  <a name="cfn-sagemaker-mlflowtrackingserver-trackingserversize"></a>
The size of the tracking server you want to create. You can choose between `"Small"`, `"Medium"`, and `"Large"`. The default MLflow Tracking Server configuration size is `"Small"`. You can choose a size depending on the projected use of the tracking server such as the volume of data logged, number of users, and frequency of use.
We recommend using a small tracking server for teams of up to 25 users, a medium tracking server for teams of up to 50 users, and a large tracking server for teams of up to 100 users.
*Required*: No
*Type*: String
*Allowed values*: `Small | Medium | Large`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeeklyMaintenanceWindowStart`  <a name="cfn-sagemaker-mlflowtrackingserver-weeklymaintenancewindowstart"></a>
The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: TUE:03:30.
*Required*: No
*Type*: String
*Pattern*: `^(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)$`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-mlflowtrackingserver-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-mlflowtrackingserver-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-mlflowtrackingserver-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-mlflowtrackingserver-return-values-fn--getatt-fn--getatt"></a>

`TrackingServerArn`  <a name="TrackingServerArn-fn::getatt"></a>
The ARN of the tracking server.
