---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html
---

# UpdateUser
<a name="API_UpdateUser"></a>

Updates an Amazon Quick Sight user.

## Request Syntax
<a name="API_UpdateUser_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/users/{{UserName}} HTTP/1.1
Content-type: application/json

{
   "CustomFederationProviderUrl": "{{string}}",
   "CustomPermissionsName": "{{string}}",
   "Email": "{{string}}",
   "ExternalLoginFederationProviderType": "{{string}}",
   "ExternalLoginId": "{{string}}",
   "Role": "{{string}}",
   "UnapplyCustomPermissions": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-uri-AwsAccountId"></a>
The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon Quick Sight account.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [Namespace](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-uri-Namespace"></a>
The namespace. Currently, you should set this to `default`.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

 ** [UserName](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-uri-UserName"></a>
The Amazon Quick Sight user name that you want to update.
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: Yes

## Request Body
<a name="API_UpdateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Email](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-Email"></a>
The email address of the user that you want to update.
Type: String
Required: Yes

 ** [Role](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-Role"></a>
The Amazon Quick Sight role of the user. The role can be one of the following default security cohorts:
+  `READER`: A user who has read-only access to dashboards.
+  `AUTHOR`: A user who can create data sources, datasets, analyses, and dashboards.
+  `ADMIN`: A user who is an author, who can also manage Amazon Quick Sight settings.
+  `READER_PRO`: Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Quick Sight, can build stories with Amazon Q, and can generate executive summaries from dashboards.
+  `AUTHOR_PRO`: Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.
+  `ADMIN_PRO`: Admin Pros are Author Pros who can also manage Amazon Quick Sight administrative settings. Admin Pro users are billed at Author Pro pricing.
The name of the Quick Sight role is invisible to the user except for the console screens dealing with permissions.
Type: String
Valid Values: `ADMIN | AUTHOR | READER | RESTRICTED_AUTHOR | RESTRICTED_READER | ADMIN_PRO | AUTHOR_PRO | READER_PRO`
Required: Yes

 ** [CustomFederationProviderUrl](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-CustomFederationProviderUrl"></a>
The URL of the custom OpenID Connect (OIDC) provider that provides identity to let a user federate into Quick Sight with an associated AWS Identity and Access Management(IAM) role. This parameter should only be used when `ExternalLoginFederationProviderType` parameter is set to `CUSTOM_OIDC`.
Type: String
Required: No

 ** [CustomPermissionsName](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-CustomPermissionsName"></a>
(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a user's access by restricting access the following operations:
+ Create and update data sources
+ Create and update datasets
+ Create and update email reports
+ Subscribe to email reports
A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the Quick Sight console. Then, you use the `RegisterUser` API operation to assign the named set of permissions to a Quick Sight user.
Quick Sight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning Quick Sight users to one of the default security cohorts in Quick Sight (admin, author, reader).
This feature is available only to Quick Sight Enterprise edition subscriptions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`
Required: No

 ** [ExternalLoginFederationProviderType](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-ExternalLoginFederationProviderType"></a>
The type of supported external login provider that provides identity to let a user federate into Quick Sight with an associated AWS Identity and Access Management(IAM) role. The type of supported external login provider can be one of the following.
+  `COGNITO`: Amazon Cognito. The provider URL is cognito-identity.amazonaws.com. When choosing the `COGNITO` provider type, don’t use the "CustomFederationProviderUrl" parameter which is only needed when the external provider is custom.
+  `CUSTOM_OIDC`: Custom OpenID Connect (OIDC) provider. When choosing `CUSTOM_OIDC` type, use the `CustomFederationProviderUrl` parameter to provide the custom OIDC provider URL.
+  `NONE`: This clears all the previously saved external login information for a user. Use the ` [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html) ` API operation to check the external login information.
Type: String
Required: No

 ** [ExternalLoginId](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-ExternalLoginId"></a>
The identity ID for a user in the external login provider.
Type: String
Required: No

 ** [UnapplyCustomPermissions](#API_UpdateUser_RequestSyntax) **   <a name="QS-UpdateUser-request-UnapplyCustomPermissions"></a>
A flag that you use to indicate that you want to remove all custom permissions from this user. Using this parameter resets the user to the state it was in before a custom permissions profile was applied. This parameter defaults to NULL and it doesn't accept any other value.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateUser_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "User": {
      "Active": boolean,
      "Arn": "string",
      "CustomPermissionsName": "string",
      "Email": "string",
      "ExternalLoginFederationProviderType": "string",
      "ExternalLoginFederationProviderUrl": "string",
      "ExternalLoginId": "string",
      "IdentityType": "string",
      "PrincipalId": "string",
      "Role": "string",
      "UserName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateUser_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateUser_ResponseSyntax) **   <a name="QS-UpdateUser-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateUser_ResponseSyntax) **   <a name="QS-UpdateUser-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [User](#API_UpdateUser_ResponseSyntax) **   <a name="QS-UpdateUser-response-User"></a>
The Amazon Quick Sight user.
Type: [User](API_User.md) object

## Errors
<a name="API_UpdateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** PreconditionNotMetException **
One or more preconditions aren't met.
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

 ** ResourceUnavailableException **
This resource is currently unavailable.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateUser)
