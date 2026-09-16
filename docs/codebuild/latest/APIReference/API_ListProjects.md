---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListProjects.html
---

# ListProjects
<a name="API_ListProjects"></a>

Gets a list of build project names, with each build project name representing a single build project.

## Request Syntax
<a name="API_ListProjects_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [nextToken](#API_ListProjects_RequestSyntax) **   <a name="CodeBuild-ListProjects-request-nextToken"></a>
During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *nextToken*. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [sortBy](#API_ListProjects_RequestSyntax) **   <a name="CodeBuild-ListProjects-request-sortBy"></a>
The criterion to be used to list build project names. Valid values include:
+  `CREATED_TIME`: List based on when each build project was created.
+  `LAST_MODIFIED_TIME`: List based on when information about each build project was last changed.
+  `NAME`: List based on each build project's name.
Use `sortOrder` to specify in what order to list the build project names based on the preceding criteria.
Type: String
Valid Values: `NAME | CREATED_TIME | LAST_MODIFIED_TIME`
Required: No

 ** [sortOrder](#API_ListProjects_RequestSyntax) **   <a name="CodeBuild-ListProjects-request-sortOrder"></a>
The order in which to list build projects. Valid values include:
+  `ASCENDING`: List in ascending order.
+  `DESCENDING`: List in descending order.
Use `sortBy` to specify the criterion to be used to list build project names.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListProjects_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "projects": [ "string" ]
}
```

## Response Elements
<a name="API_ListProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProjects_ResponseSyntax) **   <a name="CodeBuild-ListProjects-response-nextToken"></a>
If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *nextToken*. To get the next batch of items in the list, call this operation again, adding the next token to the call.
Type: String

 ** [projects](#API_ListProjects_ResponseSyntax) **   <a name="CodeBuild-ListProjects-response-projects"></a>
The list of build project names, with each build project name representing a single build project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListProjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListProjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListProjects)
