---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePartnerApp.html
---

# DescribePartnerApp
<a name="API_DescribePartnerApp"></a>

Gets information about a SageMaker Partner AI App.

## Request Syntax
<a name="API_DescribePartnerApp_RequestSyntax"></a>

```
{
   "Arn": "{{string}}",
   "IncludeAvailableUpgrade": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribePartnerApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_DescribePartnerApp_RequestSyntax) **   <a name="sagemaker-DescribePartnerApp-request-Arn"></a>
The ARN of the SageMaker Partner AI App to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`
Required: Yes

 ** [IncludeAvailableUpgrade](#API_DescribePartnerApp_RequestSyntax) **   <a name="sagemaker-DescribePartnerApp-request-IncludeAvailableUpgrade"></a>
When set to `TRUE`, the response includes available upgrade information for the SageMaker Partner AI App. Default is `FALSE`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribePartnerApp_ResponseSyntax"></a>

```
{
   "ApplicationConfig": {
      "AdminUsers": [ "string" ],
      "Arguments": {
         "string" : "string"
      },
      "AssignedGroupPatterns": [ "string" ],
      "RoleGroupAssignments": [
         {
            "GroupPatterns": [ "string" ],
            "RoleName": "string"
         }
      ]
   },
   "Arn": "string",
   "AuthType": "string",
   "AvailableUpgrade": {
      "ReleaseNotes": [ "string" ],
      "Version": "string"
   },
   "BaseUrl": "string",
   "CreationTime": number,
   "CurrentVersionEolDate": number,
   "EnableAutoMinorVersionUpgrade": boolean,
   "EnableIamSessionBasedIdentity": boolean,
   "Error": {
      "Code": "string",
      "Reason": "string"
   },
   "ExecutionRoleArn": "string",
   "IdcConfig": {
      "ApplicationArn": "string",
      "InstanceArn": "string"
   },
   "KmsKeyId": "string",
   "LastModifiedTime": number,
   "MaintenanceConfig": {
      "MaintenanceWindowStart": "string"
   },
   "Name": "string",
   "Status": "string",
   "Tier": "string",
   "Type": "string",
   "Version": "string"
}
```

## Response Elements
<a name="API_DescribePartnerApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationConfig](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-ApplicationConfig"></a>
Configuration settings for the SageMaker Partner AI App.
Type: [PartnerAppConfig](API_PartnerAppConfig.md) object

 ** [Arn](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Arn"></a>
The ARN of the SageMaker Partner AI App that was described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`

 ** [AuthType](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-AuthType"></a>
The authorization type that users use to access the SageMaker Partner AI App. Valid values:
+  `IAM`: Users access the SageMaker Partner AI App with their AWS IAM identity.
+  `IDC`: Users access the SageMaker Partner AI App with their AWS IAM Identity Center identity.
Type: String
Valid Values: `IAM | IDC`

 ** [AvailableUpgrade](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-AvailableUpgrade"></a>
A map of available minor version upgrades for the SageMaker Partner AI App. The key is the semantic version number, and the value is a list of release notes for that version. A null value indicates no upgrades are available.
Type: [AvailableUpgrade](API_AvailableUpgrade.md) object

 ** [BaseUrl](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-BaseUrl"></a>
The URL of the SageMaker Partner AI App that the Application SDK uses to support in-app calls for the user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [CreationTime](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-CreationTime"></a>
The time that the SageMaker Partner AI App was created.
Type: Timestamp

 ** [CurrentVersionEolDate](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-CurrentVersionEolDate"></a>
The end-of-life date for the current version of the SageMaker Partner AI App.
Type: Timestamp

 ** [EnableAutoMinorVersionUpgrade](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-EnableAutoMinorVersionUpgrade"></a>
Indicates whether the SageMaker Partner AI App is configured for automatic minor version upgrades during scheduled maintenance windows.
Type: Boolean

 ** [EnableIamSessionBasedIdentity](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-EnableIamSessionBasedIdentity"></a>
When set to `TRUE`, the SageMaker Partner AI App sets the AWS IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.
Type: Boolean

 ** [Error](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Error"></a>
This is an error field object that contains the error code and the reason for an operation failure.
Type: [ErrorInfo](API_ErrorInfo.md) object

 ** [ExecutionRoleArn](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-ExecutionRoleArn"></a>
The ARN of the IAM role associated with the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [IdcConfig](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-IdcConfig"></a>
Contains the AWS IAM Identity Center configuration for the SageMaker Partner AI App, including the Identity Center instance and the Identity Center application that SageMaker creates for the app. The service returns this field for apps that use `IDC` authorization.
Type: [IdcConfigOutput](API_IdcConfigOutput.md) object

 ** [KmsKeyId](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-KmsKeyId"></a>
The AWS KMS customer managed key used to encrypt the data at rest associated with SageMaker Partner AI Apps.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [LastModifiedTime](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-LastModifiedTime"></a>
The time that the SageMaker Partner AI App was last modified.
Type: Timestamp

 ** [MaintenanceConfig](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-MaintenanceConfig"></a>
Maintenance configuration settings for the SageMaker Partner AI App.
Type: [PartnerAppMaintenanceConfig](API_PartnerAppMaintenanceConfig.md) object

 ** [Name](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Name"></a>
The name of the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]+`

 ** [Status](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Status"></a>
The status of the SageMaker Partner AI App.
+ Creating: SageMaker AI is creating the partner AI app. The partner AI app is not available during creation.
+ Updating: SageMaker AI is updating the partner AI app. The partner AI app is not available when updating.
+ Deleting: SageMaker AI is deleting the partner AI app. The partner AI app is not available during deletion.
+ Available: The partner AI app is provisioned and accessible.
+ Failed: The partner AI app is in a failed state and isn't available. SageMaker AI is investigating the issue. For further guidance, contact AWS Support.
+ UpdateFailed: The partner AI app couldn't be updated but is available.
+ Deleted: The partner AI app is permanently deleted and not available.
Type: String
Valid Values: `Creating | Updating | Deleting | Available | Failed | UpdateFailed | Deleted`

 ** [Tier](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Tier"></a>
The instance type and size of the cluster attached to the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`

 ** [Type](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Type"></a>
The type of SageMaker Partner AI App. Must be one of the following: `lakera-guard`, `comet`, `deepchecks-llm-evaluation`, or `fiddler`.
Type: String
Valid Values: `lakera-guard | comet | deepchecks-llm-evaluation | fiddler`

 ** [Version](#API_DescribePartnerApp_ResponseSyntax) **   <a name="sagemaker-DescribePartnerApp-response-Version"></a>
The version of the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`

## Errors
<a name="API_DescribePartnerApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePartnerApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribePartnerApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribePartnerApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
