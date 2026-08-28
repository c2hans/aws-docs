---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteGitHubAccountToken.html
---

# DeleteGitHubAccountToken
<a name="API_DeleteGitHubAccountToken"></a>

Deletes a GitHub account connection.

## Request Syntax
<a name="API_DeleteGitHubAccountToken_RequestSyntax"></a>

```
{
   "tokenName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteGitHubAccountToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [tokenName](#API_DeleteGitHubAccountToken_RequestSyntax) **   <a name="CodeDeploy-DeleteGitHubAccountToken-request-tokenName"></a>
The name of the GitHub account connection to delete.
Type: String
Required: No

## Response Syntax
<a name="API_DeleteGitHubAccountToken_ResponseSyntax"></a>

```
{
   "tokenName": "string"
}
```

## Response Elements
<a name="API_DeleteGitHubAccountToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tokenName](#API_DeleteGitHubAccountToken_ResponseSyntax) **   <a name="CodeDeploy-DeleteGitHubAccountToken-response-tokenName"></a>
The name of the GitHub account connection that was deleted.
Type: String

## Errors
<a name="API_DeleteGitHubAccountToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GitHubAccountTokenDoesNotExistException **
No GitHub account connection exists with the named specified in the call.
HTTP Status Code: 400

 ** GitHubAccountTokenNameRequiredException **
The call is missing a required GitHub account connection name.
HTTP Status Code: 400

 ** InvalidGitHubAccountTokenNameException **
The format of the specified GitHub account connection name is invalid.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The API used does not support the deployment.
HTTP Status Code: 400

 ** ResourceValidationException **
The specified resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DeleteGitHubAccountToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/DeleteGitHubAccountToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeleteGitHubAccountToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
