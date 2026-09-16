---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html
---

# PutConformancePack
<a name="API_PutConformancePack"></a>

Creates or updates a conformance pack. A conformance pack is a collection of AWS Config rules that can be easily deployed in an account and a region and across an organization. For information on how many conformance packs you can have per account, see [**Service Limits**](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html) in the * AWS Config Developer Guide*.

**Important**
When you use `PutConformancePack` to deploy conformance packs in your account, the operation can create AWS Config rules and remediation actions without requiring `config:PutConfigRule` or `config:PutRemediationConfigurations` permissions in your account IAM policies.
This API uses the `AWSServiceRoleForConfigConforms` service-linked role in your account to create conformance pack resources. This service-linked role includes the permissions to create AWS Config rules and remediation configurations, even if your account IAM policies explicitly deny these actions.

This API creates a service-linked role `AWSServiceRoleForConfigConforms` in your account. The service-linked role is created only when the role does not exist in your account.

**Note**
You must specify only one of the follow parameters: `TemplateS3Uri`, `TemplateBody` or `TemplateSSMDocumentDetails`.

**Note**
 **Tags are added at creation and cannot be updated with this operation**
 `PutConformancePack` is an idempotent API. Subsequent requests won't create a duplicate resource if one was already created. If a following request has different `tags` values, AWS Config will ignore these differences and treat it as an idempotent request of the previous. In this case, `tags` will not be updated, even if they are different.
Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

## Request Syntax
<a name="API_PutConformancePack_RequestSyntax"></a>

```
{
   "ConformancePackInputParameters": [
      {
         "ParameterName": "{{string}}",
         "ParameterValue": "{{string}}"
      }
   ],
   "ConformancePackName": "{{string}}",
   "DeliveryS3Bucket": "{{string}}",
   "DeliveryS3KeyPrefix": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TemplateBody": "{{string}}",
   "TemplateS3Uri": "{{string}}",
   "TemplateSSMDocumentDetails": {
      "DocumentName": "{{string}}",
      "DocumentVersion": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_PutConformancePack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConformancePackInputParameters](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-ConformancePackInputParameters"></a>
A list of `ConformancePackInputParameter` objects.
Type: Array of [ConformancePackInputParameter](API_ConformancePackInputParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** [ConformancePackName](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-ConformancePackName"></a>
The unique name of the conformance pack you want to deploy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

 ** [DeliveryS3Bucket](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-DeliveryS3Bucket"></a>
The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Required: No

 ** [DeliveryS3KeyPrefix](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-DeliveryS3KeyPrefix"></a>
The prefix for the Amazon S3 bucket.
This field is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Tags](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-Tags"></a>
The tags for the conformance pack. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TemplateBody](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-TemplateBody"></a>
A string that contains the full conformance pack template body. The structure containing the template body has a minimum length of 1 byte and a maximum length of 51,200 bytes.
You can use a YAML template with two resource types: AWS Config rule (`AWS::Config::ConfigRule`) and remediation action (`AWS::Config::RemediationConfiguration`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [TemplateS3Uri](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-TemplateS3Uri"></a>
The location of the file containing the template body (`s3://bucketname/prefix`). The uri must point to a conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket in the same Region as the conformance pack.
You must have access to read Amazon S3 bucket. In addition, in order to ensure a successful deployment, the template object must not be in an [archived storage class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) if this parameter is passed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://.*`
Required: No

 ** [TemplateSSMDocumentDetails](#API_PutConformancePack_RequestSyntax) **   <a name="config-PutConformancePack-request-TemplateSSMDocumentDetails"></a>
An object of type `TemplateSSMDocumentDetails`, which contains the name or the Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.
Type: [TemplateSSMDocumentDetails](API_TemplateSSMDocumentDetails.md) object
Required: No

## Response Syntax
<a name="API_PutConformancePack_ResponseSyntax"></a>

```
{
   "ConformancePackArn": "string"
}
```

## Response Elements
<a name="API_PutConformancePack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConformancePackArn](#API_PutConformancePack_ResponseSyntax) **   <a name="config-PutConformancePack-response-ConformancePackArn"></a>
ARN of the conformance pack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_PutConformancePack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConformancePackTemplateValidationException **
You have specified a template that is not valid or supported.
HTTP Status Code: 400

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

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** MaxNumberOfConformancePacksExceededException **
You have reached the limit of the number of conformance packs you can create in an account. For more information, see [**Service Limits**](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html) in the * AWS Config Developer Guide*.
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

## See Also
<a name="API_PutConformancePack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutConformancePack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutConformancePack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutConformancePack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutConformancePack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutConformancePack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutConformancePack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutConformancePack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutConformancePack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutConformancePack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutConformancePack)
