---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateNamespace.html
---

# UpdateNamespace
<a name="API_UpdateNamespace"></a>

Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both `adminUsername` and `adminUserPassword` to update either field, but you can't update both `kmsKeyId` and `logExports` in a single request.

Similarly, an S3 Tables log-publishing update (a request where `logDestinationType` is `s3table`) cannot be combined with any other namespace configuration change and must be submitted as its own request.

## Request Syntax
<a name="API_UpdateNamespace_RequestSyntax"></a>

```
{
   "adminPasswordSecretKmsKeyId": "{{string}}",
   "adminUsername": "{{string}}",
   "adminUserPassword": "{{string}}",
   "defaultIamRoleArn": "{{string}}",
   "iamRoles": [ "{{string}}" ],
   "kmsKeyId": "{{string}}",
   "logDestinationType": "{{string}}",
   "logExports": [ "{{string}}" ],
   "manageAdminPassword": {{boolean}},
   "namespaceName": "{{string}}",
   "s3TableAction": "{{string}}",
   "s3TableGranularity": "{{string}}",
   "s3TableKmsKeyId": "{{string}}",
   "s3TableNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [adminPasswordSecretKmsKeyId](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-adminPasswordSecretKmsKeyId"></a>
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if `manageAdminPassword` is true.
Type: String
Required: No

 ** [adminUsername](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-adminUsername"></a>
The username of the administrator for the first database created in the namespace. This parameter must be updated together with `adminUserPassword`.
Type: String
Required: No

 ** [adminUserPassword](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-adminUserPassword"></a>
The password of the administrator for the first database created in the namespace. This parameter must be updated together with `adminUsername`.
You can't use `adminUserPassword` if `manageAdminPassword` is true.
If your admin user account is locked, this operation also unlocks your account and resets the failed-login counter. This option is available only when account lockout security is enabled for the namespace.
Type: String
Required: No

 ** [defaultIamRoleArn](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-defaultIamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with `iamRoles`.
Type: String
Required: No

 ** [iamRoles](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-iamRoles"></a>
A list of IAM roles to associate with the namespace. This parameter must be updated together with `defaultIamRoleArn`.
Type: Array of strings
Required: No

 ** [kmsKeyId](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-kmsKeyId"></a>
The ID of the AWS Key Management Service key used to encrypt your data.
Type: String
Required: No

 ** [logDestinationType](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-logDestinationType"></a>
The destination for the log data. Valid values are `s3table` and `cloudwatch`.
Set this to `s3table` to manage Amazon S3 Tables system-table publishing for the namespace.
Type: String
Valid Values: `s3table | cloudwatch`
Required: No

 ** [logExports](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-logExports"></a>
The types of logs the namespace can export. The export types are `userlog`, `connectionlog`, and `useractivitylog`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Valid Values: `useractivitylog | userlog | connectionlog`
Required: No

 ** [manageAdminPassword](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-manageAdminPassword"></a>
If `true`, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials. You can't use `adminUserPassword` if `manageAdminPassword` is true. If `manageAdminPassword` is false or not set, Amazon Redshift uses `adminUserPassword` for the admin user account's password.
Type: Boolean
Required: No

 ** [namespaceName](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-namespaceName"></a>
The name of the namespace to update. You can't update the name of a namespace once it is created.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [s3TableAction](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-s3TableAction"></a>
Whether to enable or disable Amazon S3 Tables publishing. Valid values are `Enable` and `Disable`, matched case-insensitively.
When omitted, defaults to `Enable`. Valid only when `logDestinationType` is `s3table`.
Type: String
Valid Values: `Enable | Disable`
Required: No

 ** [s3TableGranularity](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-s3TableGranularity"></a>
The scope of the Amazon S3 Tables destination. Valid values are `namespace` and `account`, matched case-insensitively. `namespace` scopes the published tables to this namespace; `account` scopes them to the AWS account.
Required when enabling. Omitting this parameter or passing a blank value fails with `ValidationException`. Valid only when `logDestinationType` is `s3table`.
Type: String
Valid Values: `namespace | account`
Required: No

 ** [s3TableKmsKeyId](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-s3TableKmsKeyId"></a>
The identifier of the AWS Key Management Service key used to encrypt the published Amazon S3 Tables data. When omitted, the data is encrypted with SSE-S3 (Amazon S3 managed keys).
Valid only when `logDestinationType` is `s3table`.
Type: String
Required: No

 ** [s3TableNames](#API_UpdateNamespace_RequestSyntax) **   <a name="redshiftserverless-UpdateNamespace-request-s3TableNames"></a>
The system tables to publish (on enable) or to stop publishing (on disable). Each value is either a system table view name that begins with `sys_` or the keyword `all`.
Omitting this parameter, passing an empty list, or including `all` each select every current and future system table. Each name must be 1-128 characters, and the list can contain up to 256 names.
Valid only when `logDestinationType` is `s3table`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(all|sys_[a-z0-9_]+)`
Required: No

## Response Syntax
<a name="API_UpdateNamespace_ResponseSyntax"></a>

```
{
   "namespace": {
      "adminPasswordSecretArn": "string",
      "adminPasswordSecretKmsKeyId": "string",
      "adminUsername": "string",
      "catalogArn": "string",
      "creationDate": "string",
      "dbName": "string",
      "defaultIamRoleArn": "string",
      "iamRoles": [ "string" ],
      "kmsKeyId": "string",
      "lakehouseRegistrationStatus": "string",
      "logExports": [ "string" ],
      "namespaceArn": "string",
      "namespaceId": "string",
      "namespaceName": "string",
      "s3TablePublishStatus": {
         "enabledAll": boolean,
         "lastIngestionTimes": {
            "string" : "string"
         },
         "s3TableGranularity": "string",
         "s3TableNamespace": "string",
         "s3Tables": [ "string" ]
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_UpdateNamespace_ResponseSyntax) **   <a name="redshiftserverless-UpdateNamespace-response-namespace"></a>
A list of tag instances.
Type: [Namespace](API_Namespace.md) object

## Errors
<a name="API_UpdateNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/UpdateNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UpdateNamespace)
