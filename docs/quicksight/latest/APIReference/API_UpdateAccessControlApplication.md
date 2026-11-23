---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccessControlApplication.html
---

# UpdateAccessControlApplication

Updates an access control application. You can change its name, description, status, IdP settings such as the client ID and issuer URL, and its Quick Sight authentication settings such as redirect URIs.

You can't change the `IdpAuthorizingType`, the `QuickAuthenticationType`, or the trusted token issuer after the application is created. To manage client secrets, use `CreateAccessControlApplicationSecret`, `UpdateAccessControlApplicationSecret`, and `DeleteAccessControlApplicationSecret`.

## Request Syntax
<a name="API_UpdateAccessControlApplication_RequestSyntax"></a>

```
PATCH /accounts/{{AwsAccountId}}/access-control-applications/{{ApplicationId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "IdpAuthorizingConfiguration": {
      "IdcTrustedTokenIssuerConfiguration": {
         "IdcTrustedTokenIssuerArn": "{{string}}"
      },
      "IdpAuthorizingConfigurationDetailInput": { ... },
      "IdpAuthorizingType": "{{string}}"
   },
   "Name": "{{string}}",
   "QuickAuthenticationConfiguration": {
      "QuickAuthenticationConfigurationDetailInput": { ... },
      "QuickAuthenticationType": "{{string}}"
   },
   "Status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAccessControlApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-uri-ApplicationId"></a>
The ID of the access control application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAccessControlApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-Description"></a>
The new description of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** [IdpAuthorizingConfiguration](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-IdpAuthorizingConfiguration"></a>
The identity provider settings to update, such as the client ID and issuer URL. You can't change the `IdpAuthorizingType` or the trusted token issuer. To manage client secrets, use the client secret operations.
Type: [IdpAuthorizingConfigUpdateInput](API_IdpAuthorizingConfigUpdateInput.md) object
Required: No

 ** [Name](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-Name"></a>
The new name of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [QuickAuthenticationConfiguration](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-QuickAuthenticationConfiguration"></a>
The Quick Sight authentication settings to update, such as redirect URIs. You can't change the `QuickAuthenticationType`.
Type: [QuickAuthenticationConfigInput](API_QuickAuthenticationConfigInput.md) object
Required: No

 ** [Status](#API_UpdateAccessControlApplication_RequestSyntax) **   <a name="QS-UpdateAccessControlApplication-request-Status"></a>
The new status of the access control application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateAccessControlApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccessControlApplicationStatus": "string",
   "ApplicationId": "string",
   "Arn": "string",
   "LastUpdatedTime": number,
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateAccessControlApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateAccessControlApplication_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccessControlApplicationStatus](#API_UpdateAccessControlApplication_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplication-response-AccessControlApplicationStatus"></a>
The status of the access control application.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [ApplicationId](#API_UpdateAccessControlApplication_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplication-response-ApplicationId"></a>
The ID of the access control application.
Type: String

 ** [Arn](#API_UpdateAccessControlApplication_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplication-response-Arn"></a>
The ARN of the access control application.
Type: String

 ** [LastUpdatedTime](#API_UpdateAccessControlApplication_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplication-response-LastUpdatedTime"></a>
The time when the access control application was last updated.
Type: Timestamp

 ** [RequestId](#API_UpdateAccessControlApplication_ResponseSyntax) **   <a name="QS-UpdateAccessControlApplication-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateAccessControlApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateAccessControlApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAccessControlApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAccessControlApplication)
