---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxes.html
---

# ListSandboxes
<a name="API_ListSandboxes"></a>

Gets a list of sandboxes.

## Request Syntax
<a name="API_ListSandboxes_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSandboxes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [maxResults](#API_ListSandboxes_RequestSyntax) **   <a name="CodeBuild-ListSandboxes-request-maxResults"></a>
The maximum number of sandbox records to be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSandboxes_RequestSyntax) **   <a name="CodeBuild-ListSandboxes-request-nextToken"></a>
The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.
Type: String
Required: No

 ** [sortOrder](#API_ListSandboxes_RequestSyntax) **   <a name="CodeBuild-ListSandboxes-request-sortOrder"></a>
The order in which sandbox records should be retrieved.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListSandboxes_ResponseSyntax"></a>

```
{
   "ids": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSandboxes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ids](#API_ListSandboxes_ResponseSyntax) **   <a name="CodeBuild-ListSandboxes-response-ids"></a>
Information about the requested sandbox IDs.
Type: Array of strings
Length Constraints: Minimum length of 1.

 ** [nextToken](#API_ListSandboxes_ResponseSyntax) **   <a name="CodeBuild-ListSandboxes-response-nextToken"></a>
Information about the next token to get paginated results.
Type: String

## Errors
<a name="API_ListSandboxes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListSandboxes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListSandboxes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListSandboxes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
