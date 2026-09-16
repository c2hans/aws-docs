---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an OAuth 2.0 customer managed application in IAM Identity Center for the given application provider.

**Note**
This API does not support creating SAML 2.0 customer managed applications or AWS managed applications. To learn how to create an AWS managed application, see the application user guide. You can create a SAML 2.0 customer managed application in the AWS Management Console only. See [Setting up customer managed SAML 2.0 applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html). For more information on these application types, see [AWS managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html).

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
{
   "ApplicationProviderArn": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "InstanceArn": "{{string}}",
   "Name": "{{string}}",
   "PortalOptions": {
      "SignInOptions": {
         "ApplicationUrl": "{{string}}",
         "Origin": "{{string}}"
      },
      "Visibility": "{{string}}"
   },
   "Status": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationProviderArn](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-ApplicationProviderArn"></a>
The ARN of the application provider under which the operation will run.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`
Required: Yes

 ** [ClientToken](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-ClientToken"></a>
Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [Description](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-Description"></a>
The description of the [Application](API_Application.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [InstanceArn](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-InstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [Name](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-Name"></a>
The name of the [Application](API_Application.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\S\s]*`
Required: Yes

 ** [PortalOptions](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-PortalOptions"></a>
A structure that describes the options for the portal associated with an application.
Type: [PortalOptions](API_PortalOptions.md) object
Required: No

 ** [Status](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-Status"></a>
Specifies whether the application is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Tags](#API_CreateApplication_RequestSyntax) **   <a name="singlesignon-CreateApplication-request-Tags"></a>
Specifies tags to be attached to the application.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 75 items.
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
{
   "ApplicationArn": "string",
   "IdentityStoreArn": "string",
   "InstanceArn": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArn](#API_CreateApplication_ResponseSyntax) **   <a name="singlesignon-CreateApplication-response-ApplicationArn"></a>
Specifies the ARN of the application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

 ** [IdentityStoreArn](#API_CreateApplication_ResponseSyntax) **   <a name="singlesignon-CreateApplication-response-IdentityStoreArn"></a>
The ARN of the identity store that is connected to the instance of IAM Identity Center.
Type: String

 ** [InstanceArn](#API_CreateApplication_ResponseSyntax) **   <a name="singlesignon-CreateApplication-response-InstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Indicates that the principal has crossed the permitted number of resources that can be created.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/CreateApplication)
