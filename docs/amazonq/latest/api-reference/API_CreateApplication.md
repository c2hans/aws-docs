---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates an Amazon Q Business application.

**Note**
There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on what's included in Amazon Q Business Lite and what's included in Amazon Q Business Pro, see [Amazon Q Business tiers](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers). You must use the Amazon Q Business console to assign subscription tiers to users.
An Amazon Q Apps service linked role will be created if it's absent in the AWS account when `QAppsConfiguration` is enabled in the request. For more information, see [ Using service-linked roles for Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html).
When you create an application, Amazon Q Business may securely transmit data for processing from your selected AWS region, but within your geography. For more information, see [Cross region inference in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html).

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /applications HTTP/1.1
Content-type: application/json

{
   "attachmentsConfiguration": {
      "attachmentsControlMode": "{{string}}"
   },
   "clientIdsForOIDC": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "displayName": "{{string}}",
   "encryptionConfiguration": {
      "kmsKeyId": "{{string}}"
   },
   "iamIdentityProviderArn": "{{string}}",
   "identityCenterInstanceArn": "{{string}}",
   "identityType": "{{string}}",
   "personalizationConfiguration": {
      "personalizationControlMode": "{{string}}"
   },
   "qAppsConfiguration": {
      "qAppsControlMode": "{{string}}"
   },
   "quickSightConfiguration": {
      "clientNamespace": "{{string}}"
   },
   "roleArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attachmentsConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-attachmentsConfiguration"></a>
An option to allow end users to upload files directly during chat.
Type: [AttachmentsConfiguration](API_AttachmentsConfiguration.md) object
Required: No

 ** [clientIdsForOIDC](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-clientIdsForOIDC"></a>
The OIDC client ID for a Amazon Q Business application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.:/()*?=-]*`
Required: No

 ** [clientToken](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-clientToken"></a>
A token that you provide to identify the request to create your Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [description](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-description"></a>
A description for the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\s\S]*`
Required: No

 ** [displayName](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-displayName"></a>
A name for the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [encryptionConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-encryptionConfiguration"></a>
The identifier of the AWS KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [iamIdentityProviderArn](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-iamIdentityProviderArn"></a>
The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:iam::\d{12}:(oidc-provider|saml-provider)/[a-zA-Z0-9_\.\/@\-]+`
Required: No

 ** [identityCenterInstanceArn](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-identityCenterInstanceArn"></a>
 The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** [identityType](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-identityType"></a>
The authentication type being used by a Amazon Q Business application.
Type: String
Valid Values: `AWS_IAM_IDP_SAML | AWS_IAM_IDP_OIDC | AWS_IAM_IDC | AWS_QUICKSIGHT_IDP | ANONYMOUS`
Required: No

 ** [personalizationConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-personalizationConfiguration"></a>
Configuration information about chat response personalization. For more information, see [Personalizing chat responses](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html)
Type: [PersonalizationConfiguration](API_PersonalizationConfiguration.md) object
Required: No

 ** [qAppsConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-qAppsConfiguration"></a>
An option to allow end users to create and use Amazon Q Apps in the web experience.
Type: [QAppsConfiguration](API_QAppsConfiguration.md) object
Required: No

 ** [quickSightConfiguration](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-quickSightConfiguration"></a>
The Amazon Quick configuration for an Amazon Q Business application that uses Quick for authentication. This configuration is required if your application uses Quick as the identity provider. For more information, see [Creating an Amazon Quick integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html).
Type: [QuickSightConfiguration](API_QuickSightConfiguration.md) object
Required: No

 ** [roleArn](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-roleArn"></a>
 The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a [service linked role (SLR)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions) and use it as the application's role.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [tags](#API_CreateApplication_RequestSyntax) **   <a name="qbusiness-CreateApplication-request-tags"></a>
A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "applicationId": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_CreateApplication_ResponseSyntax) **   <a name="qbusiness-CreateApplication-response-applicationArn"></a>
 The Amazon Resource Name (ARN) of the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [applicationId](#API_CreateApplication_ResponseSyntax) **   <a name="qbusiness-CreateApplication-response-applicationId"></a>
The identifier of the Amazon Q Business application.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateApplication)
