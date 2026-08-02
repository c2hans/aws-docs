---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-partnerapp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PartnerApp
<a name="aws-resource-sagemaker-partnerapp"></a>

The `AWS::SageMaker::PartnerApp` resource creates an Amazon SageMaker Partner AI App. For more information, see [Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html).

## Syntax
<a name="aws-resource-sagemaker-partnerapp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-partnerapp-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::PartnerApp",
  "Properties" : {
      "[ApplicationConfig](#cfn-sagemaker-partnerapp-applicationconfig)" : {{PartnerAppConfig}},
      "[AppVersion](#cfn-sagemaker-partnerapp-appversion)" : {{String}},
      "[AuthType](#cfn-sagemaker-partnerapp-authtype)" : {{String}},
      "[EnableAutoMinorVersionUpgrade](#cfn-sagemaker-partnerapp-enableautominorversionupgrade)" : {{Boolean}},
      "[EnableIamSessionBasedIdentity](#cfn-sagemaker-partnerapp-enableiamsessionbasedidentity)" : {{Boolean}},
      "[ExecutionRoleArn](#cfn-sagemaker-partnerapp-executionrolearn)" : {{String}},
      "[KmsKeyId](#cfn-sagemaker-partnerapp-kmskeyid)" : {{String}},
      "[MaintenanceConfig](#cfn-sagemaker-partnerapp-maintenanceconfig)" : {{PartnerAppMaintenanceConfig}},
      "[Name](#cfn-sagemaker-partnerapp-name)" : {{String}},
      "[Tags](#cfn-sagemaker-partnerapp-tags)" : {{[ Tag, ... ]}},
      "[Tier](#cfn-sagemaker-partnerapp-tier)" : {{String}},
      "[Type](#cfn-sagemaker-partnerapp-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-partnerapp-syntax.yaml"></a>

```
Type: AWS::SageMaker::PartnerApp
Properties:
  [ApplicationConfig](#cfn-sagemaker-partnerapp-applicationconfig): {{
    PartnerAppConfig}}
  [AppVersion](#cfn-sagemaker-partnerapp-appversion): {{String}}
  [AuthType](#cfn-sagemaker-partnerapp-authtype): {{String}}
  [EnableAutoMinorVersionUpgrade](#cfn-sagemaker-partnerapp-enableautominorversionupgrade): {{Boolean}}
  [EnableIamSessionBasedIdentity](#cfn-sagemaker-partnerapp-enableiamsessionbasedidentity): {{Boolean}}
  [ExecutionRoleArn](#cfn-sagemaker-partnerapp-executionrolearn): {{String}}
  [KmsKeyId](#cfn-sagemaker-partnerapp-kmskeyid): {{String}}
  [MaintenanceConfig](#cfn-sagemaker-partnerapp-maintenanceconfig): {{
    PartnerAppMaintenanceConfig}}
  [Name](#cfn-sagemaker-partnerapp-name): {{String}}
  [Tags](#cfn-sagemaker-partnerapp-tags): {{
    - Tag}}
  [Tier](#cfn-sagemaker-partnerapp-tier): {{String}}
  [Type](#cfn-sagemaker-partnerapp-type): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-partnerapp-properties"></a>

`ApplicationConfig`  <a name="cfn-sagemaker-partnerapp-applicationconfig"></a>
Configuration settings for the Partner AI App.
*Required*: No
*Type*: [PartnerAppConfig](aws-properties-sagemaker-partnerapp-partnerappconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppVersion`  <a name="cfn-sagemaker-partnerapp-appversion"></a>
The version of the Partner AI App. This property allows you to specify a particular version of the application to deploy.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthType`  <a name="cfn-sagemaker-partnerapp-authtype"></a>
Defines the authentication type used for the Partner AI App.
*Required*: Yes
*Type*: String
*Allowed values*: `IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableAutoMinorVersionUpgrade`  <a name="cfn-sagemaker-partnerapp-enableautominorversionupgrade"></a>
When set to `TRUE`, the SageMaker Partner AI App is automatically upgraded to the latest minor version during the next scheduled maintenance window, if one is available. Default is `FALSE`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableIamSessionBasedIdentity`  <a name="cfn-sagemaker-partnerapp-enableiamsessionbasedidentity"></a>
Enables IAM Session based Identity for PartnerApp.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-sagemaker-partnerapp-executionrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role of the user.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-sagemaker-partnerapp-kmskeyid"></a>
The AWS KMS customer managed key used to encrypt the data associated with the PartnerApp.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceConfig`  <a name="cfn-sagemaker-partnerapp-maintenanceconfig"></a>
A collection of settings that specify the maintenance schedule for the PartnerApp.
*Required*: No
*Type*: [PartnerAppMaintenanceConfig](aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-partnerapp-name"></a>
The name of the Partner AI App. This name must be unique within your account and region.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-partnerapp-tags"></a>
A list of tags to apply to the PartnerApp.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-partnerapp-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-sagemaker-partnerapp-tier"></a>
Specifies the tier or level of the Partner AI App. The tier size impacts the speed and capabilities of the application. For more information, see [Set up Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-app-onboard.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-sagemaker-partnerapp-type"></a>
Specifies the type of Partner AI App being created.
*Required*: Yes
*Type*: String
*Allowed values*: `lakera-guard | comet | deepchecks-llm-evaluation | fiddler`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-partnerapp-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-partnerapp-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-partnerapp-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-partnerapp-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Partner AI App.

`BaseUrl`  <a name="BaseUrl-fn::getatt"></a>
The AppServerUrl based on app and account-info.

`CurrentVersionEolDate`  <a name="CurrentVersionEolDate-fn::getatt"></a>
The end-of-life date for the current version of the Partner AI App.
