---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePartnerApp.html
---

# CreatePartnerApp
<a name="API_CreatePartnerApp"></a>

Creates an Amazon SageMaker Partner AI App.

## Request Syntax
<a name="API_CreatePartnerApp_RequestSyntax"></a>

```
{
   "ApplicationConfig": {
      "AdminUsers": [ "{{string}}" ],
      "Arguments": {
         "{{string}}" : "{{string}}"
      },
      "AssignedGroupPatterns": [ "{{string}}" ],
      "RoleGroupAssignments": [
         {
            "GroupPatterns": [ "{{string}}" ],
            "RoleName": "{{string}}"
         }
      ]
   },
   "AuthType": "{{string}}",
   "ClientToken": "{{string}}",
   "EnableAutoMinorVersionUpgrade": {{boolean}},
   "EnableIamSessionBasedIdentity": {{boolean}},
   "ExecutionRoleArn": "{{string}}",
   "IdcConfig": {
      "InstanceArn": "{{string}}"
   },
   "KmsKeyId": "{{string}}",
   "MaintenanceConfig": {
      "MaintenanceWindowStart": "{{string}}"
   },
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Tier": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePartnerApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationConfig](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-ApplicationConfig"></a>
Configuration settings for the SageMaker Partner AI App.
Type: [PartnerAppConfig](API_PartnerAppConfig.md) object
Required: No

 ** [AuthType](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-AuthType"></a>
The authorization type that users use to access the SageMaker Partner AI App. Valid values:
+  `IAM`: Users access the SageMaker Partner AI App with their AWS IAM identity.
+  `IDC`: Users access the SageMaker Partner AI App with their AWS IAM Identity Center identity. Specify the Identity Center instance to use in `IdcConfig`.
Type: String
Valid Values: `IAM | IDC`
Required: Yes

 ** [ClientToken](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [EnableAutoMinorVersionUpgrade](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-EnableAutoMinorVersionUpgrade"></a>
When set to `TRUE`, the SageMaker Partner AI App is automatically upgraded to the latest minor version during the next scheduled maintenance window, if one is available. Default is `FALSE`.
Type: Boolean
Required: No

 ** [EnableIamSessionBasedIdentity](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-EnableIamSessionBasedIdentity"></a>
When set to `TRUE`, the SageMaker Partner AI App sets the AWS IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.
Type: Boolean
Required: No

 ** [ExecutionRoleArn](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-ExecutionRoleArn"></a>
The ARN of the IAM role that the partner application uses.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [IdcConfig](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-IdcConfig"></a>
Specifies the AWS IAM Identity Center configuration for the SageMaker Partner AI App. Specify this parameter when `AuthType` is `IDC`. Apps that use `IAM` authorization don't use this parameter.
Type: [IdcConfigInput](API_IdcConfigInput.md) object
Required: No

 ** [KmsKeyId](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-KmsKeyId"></a>
SageMaker Partner AI Apps uses AWS KMS to encrypt data at rest using an AWS managed key by default. For more control, specify a customer managed key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [MaintenanceConfig](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-MaintenanceConfig"></a>
Maintenance configuration settings for the SageMaker Partner AI App.
Type: [PartnerAppMaintenanceConfig](API_PartnerAppMaintenanceConfig.md) object
Required: No

 ** [Name](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-Name"></a>
The name to give the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** [Tags](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-Tags"></a>
Each tag consists of a key and an optional value. Tag keys must be unique per resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Tier](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-Tier"></a>
Indicates the instance type and size of the cluster attached to the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`
Required: Yes

 ** [Type](#API_CreatePartnerApp_RequestSyntax) **   <a name="sagemaker-CreatePartnerApp-request-Type"></a>
The type of SageMaker Partner AI App to create. Must be one of the following: `lakera-guard`, `comet`, `deepchecks-llm-evaluation`, or `fiddler`.
Type: String
Valid Values: `lakera-guard | comet | deepchecks-llm-evaluation | fiddler`
Required: Yes

## Response Syntax
<a name="API_CreatePartnerApp_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_CreatePartnerApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreatePartnerApp_ResponseSyntax) **   <a name="sagemaker-CreatePartnerApp-response-Arn"></a>
The ARN of the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`

## Errors
<a name="API_CreatePartnerApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreatePartnerApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePartnerApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePartnerApp)
