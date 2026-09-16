---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentAccountConnection.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateEnvironmentAccountConnection
<a name="API_UpdateEnvironmentAccountConnection"></a>

In an environment account, update an environment account connection to use a new IAM role.

For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the * AWS Proton User guide*.

## Request Syntax
<a name="API_UpdateEnvironmentAccountConnection_RequestSyntax"></a>

```
{
   "codebuildRoleArn": "{{string}}",
   "componentRoleArn": "{{string}}",
   "id": "{{string}}",
   "roleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEnvironmentAccountConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [codebuildRoleArn](#API_UpdateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-UpdateEnvironmentAccountConnection-request-codebuildRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [componentRoleArn](#API_UpdateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-UpdateEnvironmentAccountConnection-request-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.
The environment account connection must have a `componentRoleArn` to allow directly defined components to be associated with any environments running in the account.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [id](#API_UpdateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-UpdateEnvironmentAccountConnection-request-id"></a>
The ID of the environment account connection to update.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [roleArn](#API_UpdateEnvironmentAccountConnection_RequestSyntax) **   <a name="proton-UpdateEnvironmentAccountConnection-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

## Response Syntax
<a name="API_UpdateEnvironmentAccountConnection_ResponseSyntax"></a>

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
<a name="API_UpdateEnvironmentAccountConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentAccountConnection](#API_UpdateEnvironmentAccountConnection_ResponseSyntax) **   <a name="proton-UpdateEnvironmentAccountConnection-response-environmentAccountConnection"></a>
The environment account connection detail data that's returned by AWS Proton.
Type: [EnvironmentAccountConnection](API_EnvironmentAccountConnection.md) object

## Errors
<a name="API_UpdateEnvironmentAccountConnection_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEnvironmentAccountConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateEnvironmentAccountConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateEnvironmentAccountConnection)
