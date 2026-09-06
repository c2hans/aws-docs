---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetCommandExecutions.html
---

# BatchGetCommandExecutions
<a name="API_BatchGetCommandExecutions"></a>

Gets information about the command executions.

## Request Syntax
<a name="API_BatchGetCommandExecutions_RequestSyntax"></a>

```
{
   "commandExecutionIds": [ "{{string}}" ],
   "sandboxId": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetCommandExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [commandExecutionIds](#API_BatchGetCommandExecutions_RequestSyntax) **   <a name="CodeBuild-BatchGetCommandExecutions-request-commandExecutionIds"></a>
A comma separated list of `commandExecutionIds`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [sandboxId](#API_BatchGetCommandExecutions_RequestSyntax) **   <a name="CodeBuild-BatchGetCommandExecutions-request-sandboxId"></a>
A `sandboxId` or `sandboxArn`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_BatchGetCommandExecutions_ResponseSyntax"></a>

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
   "commandExecutionsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetCommandExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commandExecutions](#API_BatchGetCommandExecutions_ResponseSyntax) **   <a name="CodeBuild-BatchGetCommandExecutions-response-commandExecutions"></a>
Information about the requested command executions.
Type: Array of [CommandExecution](API_CommandExecution.md) objects

 ** [commandExecutionsNotFound](#API_BatchGetCommandExecutions_ResponseSyntax) **   <a name="CodeBuild-BatchGetCommandExecutions-response-commandExecutionsNotFound"></a>
The IDs of command executions for which information could not be found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_BatchGetCommandExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetCommandExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/BatchGetCommandExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchGetCommandExecutions)
