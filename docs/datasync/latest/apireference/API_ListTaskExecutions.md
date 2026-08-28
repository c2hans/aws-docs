---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ListTaskExecutions.html
---

# ListTaskExecutions
<a name="API_ListTaskExecutions"></a>

Returns a list of executions for an AWS DataSync transfer task.

## Request Syntax
<a name="API_ListTaskExecutions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTaskExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTaskExecutions_RequestSyntax) **   <a name="DataSync-ListTaskExecutions-request-MaxResults"></a>
Specifies how many results you want in the response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTaskExecutions_RequestSyntax) **   <a name="DataSync-ListTaskExecutions-request-NextToken"></a>
Specifies an opaque string that indicates the position at which to begin the next list of results in the response.
Type: String
Length Constraints: Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [TaskArn](#API_ListTaskExecutions_RequestSyntax) **   <a name="DataSync-ListTaskExecutions-request-TaskArn"></a>
Specifies the Amazon Resource Name (ARN) of the task that you want execution information about.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`
Required: No

## Response Syntax
<a name="API_ListTaskExecutions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TaskExecutions": [
      {
         "Status": "string",
         "TaskExecutionArn": "string",
         "TaskMode": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTaskExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTaskExecutions_ResponseSyntax) **   <a name="DataSync-ListTaskExecutions-response-NextToken"></a>
The opaque string that indicates the position to begin the next list of results in the response.
Type: String
Length Constraints: Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

 ** [TaskExecutions](#API_ListTaskExecutions_ResponseSyntax) **   <a name="DataSync-ListTaskExecutions-response-TaskExecutions"></a>
A list of the task's executions.
Type: Array of [TaskExecutionListEntry](API_TaskExecutionListEntry.md) objects

## Errors
<a name="API_ListTaskExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_ListTaskExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/ListTaskExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ListTaskExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
