---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSourceCredentials.html
---

# ListSourceCredentials
<a name="API_ListSourceCredentials"></a>

 Returns a list of `SourceCredentialsInfo` objects.

## Response Syntax
<a name="API_ListSourceCredentials_ResponseSyntax"></a>

```
{
   "sourceCredentialsInfos": [
      {
         "arn": "string",
         "authType": "string",
         "resource": "string",
         "serverType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSourceCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sourceCredentialsInfos](#API_ListSourceCredentials_ResponseSyntax) **   <a name="CodeBuild-ListSourceCredentials-response-sourceCredentialsInfos"></a>
 A list of `SourceCredentialsInfo` objects. Each `SourceCredentialsInfo` object includes the authentication type, token ARN, and type of source provider for one set of credentials.
Type: Array of [SourceCredentialsInfo](API_SourceCredentialsInfo.md) objects

## Errors
<a name="API_ListSourceCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListSourceCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListSourceCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListSourceCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
