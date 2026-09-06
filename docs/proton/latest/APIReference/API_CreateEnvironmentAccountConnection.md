---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentAccountConnection.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateEnvironmentAccountConnection
<a name="API_CreateEnvironmentAccountConnection"></a>

Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.

An environment account connection is a secure bi-directional connection between a *management account* and an *environment account* that maintains authorization and permissions. For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the * AWS Proton User guide*.

## Request Syntax
<a name="API_CreateEnvironmentAccountConnection_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "codebuildRoleArn": "{{string}}",
   "componentRoleArn": "{{string}}",
   "environmentName": "{{string}}",
   "managementAccountId": "{{string}}",
   "roleArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateEnvironmentAccountConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-clientToken"></a>
When included, if two identical requests are made with the same client token, AWS Proton returns the environment account connection that the first request created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [codebuildRoleArn](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-codebuildRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [componentRoleArn](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.
You must specify `componentRoleArn` to allow directly defined components to be associated with any environments running in this account.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [environmentName](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-environmentName"></a>
The name of the AWS Proton environment that's created in the associated management account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [managementAccountId](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-managementAccountId"></a>
The ID of the management account that accepts or rejects the environment account connection. You create and manage the AWS Proton environment in this account. If the management account accepts the environment account connection, AWS Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** [roleArn](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. AWS Proton uses this role to provision infrastructure resources in the associated environment account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [tags](#API_CreateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton environment account connection. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateEnvironmentAccountConnection_ResponseSyntax"></a>

```
{
   "environmentAccountConnection": {
      "arn": "string",
      "codebuildRoleArn": "string",
      "componentRoleArn": "string",
      "environmentAccountId": "string",
      "environmentName": "string",
      "id": "string",
      "lastModifiedAt": number,
      "managementAccountId": "string",
      "requestedAt": number,
      "roleArn": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_CreateEnvironmentAccountConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentAccountConnection](#API_CreateEnvironmentAccountConnection_ResponseSyntax) **   <a name="proton-CreateEnvironmentAccountConnection-response-environmentAccountConnection"></a>
The environment account connection detail data that's returned by AWS Proton.
Type: [EnvironmentAccountConnection](API_EnvironmentAccountConnection.md) object

## Errors
<a name="API_CreateEnvironmentAccountConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
A quota was exceeded. For more information, see [AWS Proton Quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html) in the * AWS Proton User Guide*.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironmentAccountConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateEnvironmentAccountConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateEnvironmentAccountConnection)
