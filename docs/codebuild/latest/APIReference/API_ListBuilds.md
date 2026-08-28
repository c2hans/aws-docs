---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuilds.html
---

# ListBuilds
<a name="API_ListBuilds"></a>

Gets a list of build IDs, with each build ID representing a single build.

## Request Syntax
<a name="API_ListBuilds_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBuilds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [nextToken](#API_ListBuilds_RequestSyntax) **   <a name="CodeBuild-ListBuilds-request-nextToken"></a>
During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *nextToken*. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String
Required: No

 ** [sortOrder](#API_ListBuilds_RequestSyntax) **   <a name="CodeBuild-ListBuilds-request-sortOrder"></a>
The order to list build IDs. Valid values include:
+  `ASCENDING`: List the build IDs in ascending order by build ID.
+  `DESCENDING`: List the build IDs in descending order by build ID.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListBuilds_ResponseSyntax"></a>

```
{
   "ids": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBuilds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ids](#API_ListBuilds_ResponseSyntax) **   <a name="CodeBuild-ListBuilds-response-ids"></a>
A list of build IDs, with each build ID representing a single build.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

 ** [nextToken](#API_ListBuilds_ResponseSyntax) **   <a name="CodeBuild-ListBuilds-response-nextToken"></a>
If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a *nextToken*. To get the next batch of items in the list, call this operation again, adding the next token to the call.
Type: String

## Errors
<a name="API_ListBuilds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListBuilds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListBuilds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListBuilds)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
