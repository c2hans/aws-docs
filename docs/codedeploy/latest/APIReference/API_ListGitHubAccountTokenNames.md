---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListGitHubAccountTokenNames.html
---

# ListGitHubAccountTokenNames
<a name="API_ListGitHubAccountTokenNames"></a>

Lists the names of stored connections to GitHub accounts.

## Request Syntax
<a name="API_ListGitHubAccountTokenNames_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGitHubAccountTokenNames_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListGitHubAccountTokenNames_RequestSyntax) **   <a name="CodeDeploy-ListGitHubAccountTokenNames-request-nextToken"></a>
An identifier returned from the previous `ListGitHubAccountTokenNames` call. It can be used to return the next set of names in the list.
Type: String
Required: No

## Response Syntax
<a name="API_ListGitHubAccountTokenNames_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tokenNameList": [ "string" ]
}
```

## Response Elements
<a name="API_ListGitHubAccountTokenNames_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListGitHubAccountTokenNames_ResponseSyntax) **   <a name="CodeDeploy-ListGitHubAccountTokenNames-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent `ListGitHubAccountTokenNames` call to return the next set of names in the list.
Type: String

 ** [tokenNameList](#API_ListGitHubAccountTokenNames_ResponseSyntax) **   <a name="CodeDeploy-ListGitHubAccountTokenNames-response-tokenNameList"></a>
A list of names of connections to GitHub accounts.
Type: Array of strings

## Errors
<a name="API_ListGitHubAccountTokenNames_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The API used does not support the deployment.
HTTP Status Code: 400

 ** ResourceValidationException **
The specified resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_ListGitHubAccountTokenNames_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListGitHubAccountTokenNames)
