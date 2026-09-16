---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ImportSourceCredentials.html
---

# ImportSourceCredentials
<a name="API_ImportSourceCredentials"></a>

 Imports the source repository credentials for an AWS CodeBuild project that has its source code stored in a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository.

## Request Syntax
<a name="API_ImportSourceCredentials_RequestSyntax"></a>

```
{
   "authType": "{{string}}",
   "serverType": "{{string}}",
   "shouldOverwrite": {{boolean}},
   "token": "{{string}}",
   "username": "{{string}}"
}
```

## Request Parameters
<a name="API_ImportSourceCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [authType](#API_ImportSourceCredentials_RequestSyntax) **   <a name="CodeBuild-ImportSourceCredentials-request-authType"></a>
 The type of authentication used to connect to a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository. An OAUTH connection is not supported by the API and must be created using the AWS CodeBuild console.
Type: String
Valid Values: `OAUTH | BASIC_AUTH | PERSONAL_ACCESS_TOKEN | CODECONNECTIONS | SECRETS_MANAGER`
Required: Yes

 ** [serverType](#API_ImportSourceCredentials_RequestSyntax) **   <a name="CodeBuild-ImportSourceCredentials-request-serverType"></a>
 The source provider used for this project.
Type: String
Valid Values: `GITHUB | BITBUCKET | GITHUB_ENTERPRISE | GITLAB | GITLAB_SELF_MANAGED`
Required: Yes

 ** [token](#API_ImportSourceCredentials_RequestSyntax) **   <a name="CodeBuild-ImportSourceCredentials-request-token"></a>
 For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is either the access token or the app password. For the `authType` CODECONNECTIONS, this is the `connectionArn`. For the `authType` SECRETS\_MANAGER, this is the `secretArn`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [shouldOverwrite](#API_ImportSourceCredentials_RequestSyntax) **   <a name="CodeBuild-ImportSourceCredentials-request-shouldOverwrite"></a>
 Set to `false` to prevent overwriting the repository source credentials. Set to `true` to overwrite the repository source credentials. The default value is `true`.
Type: Boolean
Required: No

 ** [username](#API_ImportSourceCredentials_RequestSyntax) **   <a name="CodeBuild-ImportSourceCredentials-request-username"></a>
 The Bitbucket username when the `authType` is BASIC\_AUTH. This parameter is not valid for other types of source providers or connections.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ImportSourceCredentials_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_ImportSourceCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_ImportSourceCredentials_ResponseSyntax) **   <a name="CodeBuild-ImportSourceCredentials-response-arn"></a>
 The Amazon Resource Name (ARN) of the token.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ImportSourceCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountLimitExceededException **
An AWS service limit was exceeded for the calling AWS account.
HTTP Status Code: 400

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified AWS resource cannot be created, because an AWS resource with the same settings already exists.
HTTP Status Code: 400

## See Also
<a name="API_ImportSourceCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ImportSourceCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ImportSourceCredentials)
