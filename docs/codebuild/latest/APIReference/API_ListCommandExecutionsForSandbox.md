---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCommandExecutionsForSandbox.html
---

# ListCommandExecutionsForSandbox
<a name="API_ListCommandExecutionsForSandbox"></a>

Gets a list of command executions for a sandbox.

## Request Syntax
<a name="API_ListCommandExecutionsForSandbox_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sandboxId": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCommandExecutionsForSandbox_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [sandboxId](#API_ListCommandExecutionsForSandbox_RequestSyntax) **   <a name="CodeBuild-ListCommandExecutionsForSandbox-request-sandboxId"></a>
A `sandboxId` or `sandboxArn`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [maxResults](#API_ListCommandExecutionsForSandbox_RequestSyntax) **   <a name="CodeBuild-ListCommandExecutionsForSandbox-request-maxResults"></a>
The maximum number of sandbox records to be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCommandExecutionsForSandbox_RequestSyntax) **   <a name="CodeBuild-ListCommandExecutionsForSandbox-request-nextToken"></a>
The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.
Type: String
Required: No

 ** [sortOrder](#API_ListCommandExecutionsForSandbox_RequestSyntax) **   <a name="CodeBuild-ListCommandExecutionsForSandbox-request-sortOrder"></a>
The order in which sandbox records should be retrieved.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListCommandExecutionsForSandbox_ResponseSyntax"></a>

```
{
   "commandExecutions": [
      {
         "command": "string",
         "endTime": number,
         "exitCode": "string",
         "id": "string",
         "logs": {
            "cloudWatchLogs": {
               "groupName": "string",
               "status": "string",
               "streamName": "string"
            },
            "cloudWatchLogsArn": "string",
            "deepLink": "string",
            "groupName": "string",
            "s3DeepLink": "string",
            "s3Logs": {
               "bucketOwnerAccess": "string",
               "encryptionDisabled": boolean,
               "location": "string",
               "status": "string"
            },
            "s3LogsArn": "string",
            "streamName": "string"
         },
         "sandboxArn": "string",
         "sandboxId": "string",
         "standardErrContent": "string",
         "standardOutputContent": "string",
         "startTime": number,
         "status": "string",
         "submitTime": number,
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCommandExecutionsForSandbox_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandExecutions](#API_ListCommandExecutionsForSandbox_ResponseSyntax) **   <a name="CodeBuild-ListCommandExecutionsForSandbox-response-commandExecutions"></a>
Information about the requested command executions.
Type: Array of [CommandExecution](API_CommandExecution.md) objects

 ** [nextToken](#API_ListCommandExecutionsForSandbox_ResponseSyntax) **   <a name="CodeBuild-ListCommandExecutionsForSandbox-response-nextToken"></a>
Information about the next token to get paginated results.
Type: String

## Errors
<a name="API_ListCommandExecutionsForSandbox_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_ListCommandExecutionsForSandbox_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListCommandExecutionsForSandbox)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListCommandExecutionsForSandbox)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
