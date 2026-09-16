---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateNamespace.html
---

# UpdateNamespace
<a name="API_UpdateNamespace"></a>

Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both `adminUsername` and `adminUserPassword` to update either field, but you can't update both `kmsKeyId` and `logExports` in a single request.

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
   "logExports": [ "{{string}}" ],
   "manageAdminPassword": {{boolean}},
   "namespaceName": "{{string}}"
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
