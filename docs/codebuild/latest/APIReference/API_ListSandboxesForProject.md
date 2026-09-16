---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxesForProject.html
---

# ListSandboxesForProject
<a name="API_ListSandboxesForProject"></a>

Gets a list of sandboxes for a given project.

## Request Syntax
<a name="API_ListSandboxesForProject_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "projectName": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSandboxesForProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [projectName](#API_ListSandboxesForProject_RequestSyntax) **   <a name="CodeBuild-ListSandboxesForProject-request-projectName"></a>
The AWS CodeBuild project name.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [maxResults](#API_ListSandboxesForProject_RequestSyntax) **   <a name="CodeBuild-ListSandboxesForProject-request-maxResults"></a>
The maximum number of sandbox records to be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSandboxesForProject_RequestSyntax) **   <a name="CodeBuild-ListSandboxesForProject-request-nextToken"></a>
The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.
Type: String
Required: No

 ** [sortOrder](#API_ListSandboxesForProject_RequestSyntax) **   <a name="CodeBuild-ListSandboxesForProject-request-sortOrder"></a>
The order in which sandbox records should be retrieved.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListSandboxesForProject_ResponseSyntax"></a>

```
{
   "ids": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSandboxesForProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ids](#API_ListSandboxesForProject_ResponseSyntax) **   <a name="CodeBuild-ListSandboxesForProject-response-ids"></a>
Information about the requested sandbox IDs.
Type: Array of strings
Length Constraints: Minimum length of 1.

 ** [nextToken](#API_ListSandboxesForProject_ResponseSyntax) **   <a name="CodeBuild-ListSandboxesForProject-response-nextToken"></a>
Information about the next token to get paginated results.
Type: String

## Errors
<a name="API_ListSandboxesForProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_ListSandboxesForProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListSandboxesForProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListSandboxesForProject)
