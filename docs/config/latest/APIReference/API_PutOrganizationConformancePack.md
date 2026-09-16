---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html
---

# PutOrganizationConformancePack
<a name="API_PutOrganizationConformancePack"></a>

Deploys conformance packs across member accounts in an AWS Organization. For information on how many organization conformance packs and how many AWS Config rules you can have per account, see [**Service Limits**](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html) in the * AWS Config Developer Guide*.

Only a management account and a delegated administrator can call this API. When calling this API with a delegated administrator, you must ensure AWS Organizations `ListDelegatedAdministrator` permissions are added. An organization can have up to 3 delegated administrators.

**Important**
When you use `PutOrganizationConformancePack` to deploy conformance packs across member accounts, the operation can create AWS Config rules and remediation actions without requiring `config:PutConfigRule` or `config:PutRemediationConfigurations` permissions in member account IAM policies.
This API uses the `AWSServiceRoleForConfigConforms` service-linked role in each member account to create conformance pack resources. This service-linked role includes the permissions to create AWS Config rules and remediation configurations, even if member account IAM policies explicitly deny these actions.

This API enables organization service access for `config-multiaccountsetup.amazonaws.com` through the `EnableAWSServiceAccess` action and creates a service-linked role `AWSServiceRoleForConfigMultiAccountSetup` in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. To use this API with delegated administrator, register a delegated administrator by calling AWS Organization `register-delegate-admin` for `config-multiaccountsetup.amazonaws.com`.

**Note**
Prerequisite: Ensure you call `EnableAllFeatures` API to enable all features in an organization.
You must specify either the `TemplateS3Uri` or the `TemplateBody` parameter, but not both. If you provide both AWS Config uses the `TemplateS3Uri` parameter and ignores the `TemplateBody` parameter.
 AWS Config sets the state of a conformance pack to CREATE\_IN\_PROGRESS and UPDATE\_IN\_PROGRESS until the conformance pack is created or updated. You cannot update a conformance pack while it is in this state.

## Request Syntax
<a name="API_PutOrganizationConformancePack_RequestSyntax"></a>

```
{
   "ConformancePackInputParameters": [
      {
         "ParameterName": "{{string}}",
         "ParameterValue": "{{string}}"
      }
   ],
   "DeliveryS3Bucket": "{{string}}",
   "DeliveryS3KeyPrefix": "{{string}}",
   "ExcludedAccounts": [ "{{string}}" ],
   "OrganizationConformancePackName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TemplateBody": "{{string}}",
   "TemplateS3Uri": "{{string}}"
}
```

## Request Parameters
<a name="API_PutOrganizationConformancePack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConformancePackInputParameters](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-ConformancePackInputParameters"></a>
A list of `ConformancePackInputParameter` objects.
Type: Array of [ConformancePackInputParameter](API_ConformancePackInputParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** [DeliveryS3Bucket](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-DeliveryS3Bucket"></a>
The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
This field is optional. If used, it must be prefixed with `awsconfigconforms`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Required: No

 ** [DeliveryS3KeyPrefix](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-DeliveryS3KeyPrefix"></a>
The prefix for the Amazon S3 bucket.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ExcludedAccounts](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-ExcludedAccounts"></a>
A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** [OrganizationConformancePackName](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-OrganizationConformancePackName"></a>
Name of the organization conformance pack you want to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** [Tags](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-Tags"></a>
The tags for the organization conformance pack. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TemplateBody](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-TemplateBody"></a>
A string that contains the full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [TemplateS3Uri](#API_PutOrganizationConformancePack_RequestSyntax) **   <a name="config-PutOrganizationConformancePack-request-TemplateS3Uri"></a>
Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).
You must have access to read Amazon S3 bucket. In addition, in order to ensure a successful deployment, the template object must not be in an [archived storage class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) if this parameter is passed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://.*`
Required: No

## Response Syntax
<a name="API_PutOrganizationConformancePack_ResponseSyntax"></a>

```
{
   "OrganizationConformancePackArn": "string"
}
```

## Response Elements
<a name="API_PutOrganizationConformancePack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OrganizationConformancePackArn](#API_PutOrganizationConformancePack_ResponseSyntax) **   <a name="config-PutOrganizationConformancePack-response-OrganizationConformancePackArn"></a>
ARN of the organization conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_PutOrganizationConformancePack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPermissionsException **
Indicates one of the following errors:
+ For [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html), the rule cannot be created because the IAM role assigned to AWS Config lacks permissions to perform the config:Put\* action.
+ For [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html), the AWS Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.
+ For [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html), organization AWS Config rule cannot be created because you do not have permissions to call IAM `GetRole` action or create a service-linked role.
+ For [PutConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html) and [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html), a conformance pack cannot be created because you do not have the following permissions:
  + You do not have permission to call IAM `GetRole` action or create a service-linked role.
  + You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.
+ For [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html), a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM `CreateServiceLinkedRole`.
+ For [PutConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html), a connector cannot be created because you do not have the following permissions: IAM `CreateServiceLinkedRole`.
HTTP Status Code: 400

 ** MaxNumberOfOrganizationConformancePacksExceededException **
You have reached the limit of the number of organization conformance packs you can create in an account. For more information, see [**Service Limits**](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html) in the * AWS Config Developer Guide*.
HTTP Status Code: 400

 ** NoAvailableOrganizationException **
Organization is no longer available.
HTTP Status Code: 400

 ** OrganizationAccessDeniedException **
For `PutConfigurationAggregator` API, you can see this exception for the following reasons:
+ No permission to call `EnableAWSServiceAccess` API
+ The configuration aggregator cannot be updated because your AWS Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current AWS Organization.
+ The configuration aggregator is associated with a previous AWS Organization and AWS Config cannot aggregate data with current AWS Organization. Delete this aggregator and create a new one with the current AWS Organization.
+ You are not a registered delegated administrator for AWS Config with permissions to call `ListDelegatedAdministrators` API. Ensure that the management account registers delagated administrator for AWS Config service principal name before the delegated administrator creates an aggregator.
For all `OrganizationConfigRule` and `OrganizationConformancePack` APIs, AWS Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.
HTTP Status Code: 400

 ** OrganizationAllFeaturesNotEnabledException **
 AWS Config resource cannot be created because your organization does not have all features enabled.
HTTP Status Code: 400

 ** OrganizationConformancePackTemplateValidationException **
You have specified a template that is not valid or supported.
HTTP Status Code: 400

 ** ResourceInUseException **
You see this exception in the following cases:
+ For DeleteConfigRule, AWS Config is deleting this rule. Try your request again later.
+ For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.
+ For DeleteConfigRule, a remediation action is associated with the rule and AWS Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.
+ For PutConfigOrganizationRule, organization AWS Config rule deletion is in progress. Try your request again later.
+ For DeleteOrganizationConfigRule, organization AWS Config rule creation is in progress. Try your request again later.
+ For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
+ For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
HTTP Status Code: 400

 ** ValidationException **
The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.
For [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html), one of the following errors:
+ There are missing required fields.
+ The input value fails the validation.
+ You are trying to create more than 300 queries.
For [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html) and [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html), one of the following errors:
+ You have specified more than one configuration recorder.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.
+ One or more of the specified resource types are already associated or disassociated with the configuration recorder.
+ For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), one of the following errors:
+ You have provided both `Arn` and `ServicePrincipal`. Only one of `Arn` or `ServicePrincipal` can be specified.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
HTTP Status Code: 400

## See Also
<a name="API_PutOrganizationConformancePack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutOrganizationConformancePack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutOrganizationConformancePack)
