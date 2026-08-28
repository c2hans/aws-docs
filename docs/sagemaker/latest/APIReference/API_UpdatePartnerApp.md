---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePartnerApp.html
---

# UpdatePartnerApp
<a name="API_UpdatePartnerApp"></a>

Updates all of the SageMaker Partner AI Apps in an account.

## Request Syntax
<a name="API_UpdatePartnerApp_RequestSyntax"></a>

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
   "AppVersion": "{{string}}",
   "Arn": "{{string}}",
   "AuthType": "{{string}}",
   "ClientToken": "{{string}}",
   "EnableAutoMinorVersionUpgrade": {{boolean}},
   "EnableIamSessionBasedIdentity": {{boolean}},
   "IdcConfig": {
      "InstanceArn": "{{string}}"
   },
   "MaintenanceConfig": {
      "MaintenanceWindowStart": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Tier": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePartnerApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationConfig](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-ApplicationConfig"></a>
Configuration settings for the SageMaker Partner AI App.
Type: [PartnerAppConfig](API_PartnerAppConfig.md) object
Required: No

 ** [AppVersion](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-AppVersion"></a>
The semantic version to upgrade the SageMaker Partner AI App to. Must be the same semantic version returned in the `AvailableUpgrade` field from `DescribePartnerApp`. Version skipping and downgrades are not supported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `\d+\.\d+`
Required: No

 ** [Arn](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-Arn"></a>
The ARN of the SageMaker Partner AI App to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`
Required: Yes

 ** [AuthType](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-AuthType"></a>
The authorization type that users use to access the SageMaker Partner AI App. Use this parameter to migrate an existing SageMaker Partner AI App from `IAM` authorization to `IDC` authorization. Valid values:
+  `IAM`: Users access the SageMaker Partner AI App with their AWS IAM identity.
+  `IDC`: Users access the SageMaker Partner AI App with their AWS IAM Identity Center identity. Specify the Identity Center instance to use in `IdcConfig`.
Type: String
Valid Values: `IAM | IDC`
Required: No

 ** [ClientToken](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-ClientToken"></a>
A unique token that guarantees that the call to this API is idempotent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [EnableAutoMinorVersionUpgrade](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-EnableAutoMinorVersionUpgrade"></a>
When set to `TRUE`, the SageMaker Partner AI App is automatically upgraded to the latest minor version during the next scheduled maintenance window, if one is available.
Type: Boolean
Required: No

 ** [EnableIamSessionBasedIdentity](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-EnableIamSessionBasedIdentity"></a>
When set to `TRUE`, the SageMaker Partner AI App sets the AWS IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.
Type: Boolean
Required: No

 ** [IdcConfig](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-IdcConfig"></a>
Specifies the AWS IAM Identity Center configuration for the SageMaker Partner AI App. Specify this parameter when `AuthType` is `IDC`. Apps that use `IAM` authorization don't use this parameter.
Type: [IdcConfigInput](API_IdcConfigInput.md) object
Required: No

 ** [MaintenanceConfig](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-MaintenanceConfig"></a>
Maintenance configuration settings for the SageMaker Partner AI App.
Type: [PartnerAppMaintenanceConfig](API_PartnerAppMaintenanceConfig.md) object
Required: No

 ** [Tags](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-Tags"></a>
Each tag consists of a key and an optional value. Tag keys must be unique per resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Tier](#API_UpdatePartnerApp_RequestSyntax) **   <a name="sagemaker-UpdatePartnerApp-request-Tier"></a>
Indicates the instance type and size of the cluster attached to the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`
Required: No

## Response Syntax
<a name="API_UpdatePartnerApp_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_UpdatePartnerApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdatePartnerApp_ResponseSyntax) **   <a name="sagemaker-UpdatePartnerApp-response-Arn"></a>
The ARN of the SageMaker Partner AI App that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`

## Errors
<a name="API_UpdatePartnerApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePartnerApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdatePartnerApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdatePartnerApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
