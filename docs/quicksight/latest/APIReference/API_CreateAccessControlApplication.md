---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAccessControlApplication.html
---

# CreateAccessControlApplication

Creates an access control application in an Amazon Quick Sight account. You use an access control application to define how an external client signs in to Quick Sight with OAuth 2.0.

To connect a client to Quick Sight through an inbound connector, associate the access control application with the connector by using the `UpdateInboundConnectorApplicationAssociations` operation.

## Request Syntax
<a name="API_CreateAccessControlApplication_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/access-control-applications HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "AuthenticationType": "{{string}}",
   "Description": "{{string}}",
   "IdpAuthorizingConfiguration": {
      "IdcTrustedTokenIssuerConfiguration": {
         "IdcTrustedTokenIssuerArn": "{{string}}"
      },
      "IdpAuthorizingConfigurationDetailInput": { ... },
      "IdpAuthorizingType": "{{string}}"
   },
   "Name": "{{string}}",
   "Namespace": "{{string}}",
   "QuickAuthenticationConfiguration": {
      "QuickAuthenticationConfigurationDetailInput": { ... },
      "QuickAuthenticationType": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAccessControlApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_CreateAccessControlApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-ApplicationId"></a>
The ID for the access control application. This ID is unique per AWS Region for each AWS account.
Quick Sight reserves IDs that start with `quick-aca-` for the access control application of the Quick Sight desktop application. To create one, the ID must be `quick-aca-` followed by your AWS account ID and the namespace, separated by a hyphen. For example, `quick-aca-111122223333-default`. In addition, `QuickAuthenticationType` must be `QUICK_MANAGED_PUBLIC_AUTH_CODE` with `http://localhost:18080` as the only redirect URI, and `IdpAuthorizingType` must be `IDC_AUTH_CODE` or `QUICK_MANAGED_AUTH_CODE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AuthenticationType](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-AuthenticationType"></a>
The authentication protocol that the access control application uses.
Type: String
Valid Values: `OIDC`
Required: Yes

 ** [IdpAuthorizingConfiguration](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-IdpAuthorizingConfiguration"></a>
The identity provider configuration of the access control application.
Type: [IdpAuthorizingConfigInput](API_IdpAuthorizingConfigInput.md) object
Required: Yes

 ** [Name](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-Name"></a>
The name of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [Namespace](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-Namespace"></a>
The Quick Sight namespace for the access control application.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

 ** [QuickAuthenticationConfiguration](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-QuickAuthenticationConfiguration"></a>
The Quick Sight authentication configuration of the access control application. You provide redirect URIs, and Quick Sight generates the client ID.
Type: [QuickAuthenticationConfigInput](API_QuickAuthenticationConfigInput.md) object
Required: Yes

 ** [Description](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-Description"></a>
The description of the access control application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

 ** [Tags](#API_CreateAccessControlApplication_RequestSyntax) **   <a name="QS-CreateAccessControlApplication-request-Tags"></a>
The tags to assign to the access control application.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateAccessControlApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccessControlApplicationStatus": "string",
   "ApplicationId": "string",
   "Arn": "string",
   "CreatedTime": number,
   "IdcApplicationArn": "string",
   "QuickAuthenticationConfiguration": {
      "QuickAuthenticationConfigurationDetailCreateOutput": { ... },
      "QuickAuthenticationType": "string"
   },
   "RequestId": "string",
   "TenantUrl": "string"
}
```

## Response Elements
<a name="API_CreateAccessControlApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccessControlApplicationStatus](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-AccessControlApplicationStatus"></a>
The status of the access control application. A new application is always `ENABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [ApplicationId](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-ApplicationId"></a>
The ID of the access control application.
Type: String

 ** [Arn](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-Arn"></a>
The ARN of the access control application.
Type: String

 ** [CreatedTime](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-CreatedTime"></a>
The time when the access control application was created.
Type: Timestamp

 ** [RequestId](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TenantUrl](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-TenantUrl"></a>
The tenant URL of the access control application.
Type: String

 ** [IdcApplicationArn](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-IdcApplicationArn"></a>
The ARN of the AWS IAM Identity Center application that Quick Sight manages for this access control application. This value is present when the `IdpAuthorizingType` is `IDC_AUTH_CODE`, or when a trusted token issuer is configured.
Type: String

 ** [QuickAuthenticationConfiguration](#API_CreateAccessControlApplication_ResponseSyntax) **   <a name="QS-CreateAccessControlApplication-response-QuickAuthenticationConfiguration"></a>
The generated Quick Sight authentication configuration. It contains the generated client ID.
Type: [QuickAuthenticationConfigCreateOutput](API_QuickAuthenticationConfigCreateOutput.md) object

## Errors
<a name="API_CreateAccessControlApplication_Errors"></a>

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

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
<a name="API_CreateAccessControlApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateAccessControlApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateAccessControlApplication)
