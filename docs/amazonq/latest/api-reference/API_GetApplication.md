---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets information about an existing Amazon Q Business application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
GET /applications/{{applicationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetApplication_RequestSyntax) **   <a name="qbusiness-GetApplication-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "applicationId": "string",
   "attachmentsConfiguration": {
      "attachmentsControlMode": "string"
   },
   "autoSubscriptionConfiguration": {
      "autoSubscribe": "string",
      "defaultSubscriptionType": "string"
   },
   "clientIdsForOIDC": [ "string" ],
   "createdAt": number,
   "description": "string",
   "displayName": "string",
   "encryptionConfiguration": {
      "kmsKeyId": "string"
   },
   "error": {
      "errorCode": "string",
      "errorMessage": "string"
   },
   "iamIdentityProviderArn": "string",
   "identityCenterApplicationArn": "string",
   "identityType": "string",
   "personalizationConfiguration": {
      "personalizationControlMode": "string"
   },
   "qAppsConfiguration": {
      "qAppsControlMode": "string"
   },
   "quickSightConfiguration": {
      "clientNamespace": "string"
   },
   "roleArn": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-applicationArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [applicationId](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-applicationId"></a>
The identifier of the Amazon Q Business application.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [attachmentsConfiguration](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-attachmentsConfiguration"></a>
Settings for whether end users can upload files directly during chat.
Type: [AppliedAttachmentsConfiguration](API_AppliedAttachmentsConfiguration.md) object

 ** [autoSubscriptionConfiguration](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-autoSubscriptionConfiguration"></a>
Settings for auto-subscription behavior for this application. This is only applicable to SAML and OIDC applications.
Type: [AutoSubscriptionConfiguration](API_AutoSubscriptionConfiguration.md) object

 ** [clientIdsForOIDC](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-clientIdsForOIDC"></a>
The OIDC client ID for a Amazon Q Business application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.:/()*?=-]*`

 ** [createdAt](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-createdAt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
Type: Timestamp

 ** [description](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-description"></a>
A description for the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\s\S]*`

 ** [displayName](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-displayName"></a>
The name of the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

 ** [encryptionConfiguration](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-encryptionConfiguration"></a>
The identifier of the AWS AWS KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [error](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-error"></a>
If the `Status` field is set to `ERROR`, the `ErrorMessage` field contains a description of the error that caused the synchronization to fail.
Type: [ErrorDetail](API_ErrorDetail.md) object

 ** [iamIdentityProviderArn](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-iamIdentityProviderArn"></a>
The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:iam::\d{12}:(oidc-provider|saml-provider)/[a-zA-Z0-9_\.\/@\-]+`

 ** [identityCenterApplicationArn](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-identityCenterApplicationArn"></a>
The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance attached to your Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

 ** [identityType](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-identityType"></a>
The authentication type being used by a Amazon Q Business application.
Type: String
Valid Values: `AWS_IAM_IDP_SAML | AWS_IAM_IDP_OIDC | AWS_IAM_IDC | AWS_QUICKSIGHT_IDP | ANONYMOUS`

 ** [personalizationConfiguration](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-personalizationConfiguration"></a>
Configuration information about chat response personalization. For more information, see [Personalizing chat responses](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html).
Type: [PersonalizationConfiguration](API_PersonalizationConfiguration.md) object

 ** [qAppsConfiguration](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-qAppsConfiguration"></a>
Settings for whether end users can create and use Amazon Q Apps in the web experience.
Type: [QAppsConfiguration](API_QAppsConfiguration.md) object

 ** [quickSightConfiguration](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-quickSightConfiguration"></a>
The Amazon Quick authentication configuration for the Amazon Q Business application.
Type: [QuickSightConfiguration](API_QuickSightConfiguration.md) object

 ** [roleArn](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM with permissions to access your CloudWatch logs and metrics.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [status](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-status"></a>
The status of the Amazon Q Business application.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING`

 ** [updatedAt](#API_GetApplication_ResponseSyntax) **   <a name="qbusiness-GetApplication-response-updatedAt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
Type: Timestamp

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

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
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetApplication)
