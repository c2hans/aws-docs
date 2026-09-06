---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html
---

# UpdateOrganizationConfiguration
<a name="API_UpdateOrganizationConfiguration"></a>

Configures the delegated administrator account with the provided values. You must provide a value for either `autoEnableOrganizationMembers` or `autoEnable`, but not both.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_UpdateOrganizationConfiguration_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/admin HTTP/1.1
Content-type: application/json

{
   "autoEnable": {{boolean}},
   "autoEnableOrganizationMembers": "{{string}}",
   "dataSources": {
      "kubernetes": {
         "auditLogs": {
            "autoEnable": {{boolean}}
         }
      },
      "malwareProtection": {
         "scanEc2InstanceWithFindings": {
            "ebsVolumes": {
               "autoEnable": {{boolean}}
            }
         }
      },
      "s3Logs": {
         "autoEnable": {{boolean}}
      }
   },
   "features": [
      {
         "additionalConfiguration": [
            {
               "autoEnable": "{{string}}",
               "name": "{{string}}"
            }
         ],
         "autoEnable": "{{string}}",
         "name": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateOrganizationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-UpdateOrganizationConfiguration-request-uri-DetectorId"></a>
The ID of the detector that configures the delegated administrator.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_UpdateOrganizationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoEnable](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-UpdateOrganizationConfiguration-request-autoEnable"></a>
 *This parameter has been deprecated.*
Represents whether to automatically enable member accounts in the organization. This applies to only new member accounts, not the existing member accounts. When a new account joins the organization, the chosen features will be enabled for them by default.
Even though this is still supported, we recommend using `AutoEnableOrganizationMembers` to achieve the similar results. You must provide a value for either `autoEnableOrganizationMembers` or `autoEnable`.
Type: Boolean
Required: No

 ** [autoEnableOrganizationMembers](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-UpdateOrganizationConfiguration-request-autoEnableOrganizationMembers"></a>
Indicates the auto-enablement configuration of GuardDuty for the member accounts in the organization. You must provide a value for either `autoEnableOrganizationMembers` or `autoEnable`.
Use one of the following configuration values for `autoEnableOrganizationMembers`:
+  `NEW`: Indicates that when a new account joins the organization, they will have GuardDuty enabled automatically.
+  `ALL`: Indicates that all accounts in the organization have GuardDuty enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.

  It may take up to 24 hours to update the configuration for all the member accounts.
+  `NONE`: Indicates that GuardDuty will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually.

  When you update the auto-enable setting from `ALL` or `NEW` to `NONE`, this action doesn't disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.
Type: String
Valid Values: `NEW | ALL | NONE`
Required: No

 ** [dataSources](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-UpdateOrganizationConfiguration-request-dataSources"></a>
 *This parameter has been deprecated.*
Describes which data sources will be updated.
Type: [OrganizationDataSourceConfigurations](API_OrganizationDataSourceConfigurations.md) object
Required: No

 ** [features](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-UpdateOrganizationConfiguration-request-features"></a>
A list of features that will be configured for the organization.
Type: Array of [OrganizationFeatureConfiguration](API_OrganizationFeatureConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_UpdateOrganizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateOrganizationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_UpdateOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/UpdateOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateOrganizationConfiguration)
