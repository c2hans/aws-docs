---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html
---

# ListExecutions
<a name="API_ListExecutions"></a>

Lists all executions of a state machine or a Map Run. You can list all executions related to a state machine by specifying a state machine Amazon Resource Name (ARN), or those related to a Map Run by specifying a Map Run ARN. Using this API action, you can also list all [redriven](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html) executions.

You can also provide a state machine [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) ARN or [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) ARN to list the executions associated with a specific alias or version.

Results are sorted by time, with the most recent execution first. Running executions are sorted by their `startDate` or `redriveDate`, and other executions are sorted by their `stopDate`.

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

This API action is not supported by `EXPRESS` state machines. However, you may list `EXPRESS` children started by a map run using the `mapRunArn` parameter.

## Request Syntax
<a name="API_ListExecutions_RequestSyntax"></a>

```
{
   "mapRunArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "redriveFilter": "{{string}}",
   "stateMachineArn": "{{string}}",
   "statusFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_ListExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [mapRunArn](#API_ListExecutions_RequestSyntax) **   <a name="StepFunctions-ListExecutions-request-mapRunArn"></a>
The Amazon Resource Name (ARN) of the Map Run that started the child workflow executions. If the `mapRunArn` field is specified, a list of all of the child workflow executions started by a Map Run is returned. For more information, see [Examining Map Run](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html) in the * AWS Step Functions Developer Guide*.
You can specify either a `mapRunArn` or a `stateMachineArn`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** [maxResults](#API_ListExecutions_RequestSyntax) **   <a name="StepFunctions-ListExecutions-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListExecutions_RequestSyntax) **   <a name="StepFunctions-ListExecutions-request-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3096.
Required: No

 ** [redriveFilter](#API_ListExecutions_RequestSyntax) **   <a name="StepFunctions-ListExecutions-request-redriveFilter"></a>
Sets a filter to list executions based on whether or not they have been redriven.
For a Distributed Map, `redriveFilter` sets a filter to list child workflow executions based on whether or not they have been redriven.
If you do not provide a `redriveFilter`, Step Functions returns a list of both redriven and non-redriven executions.
If you provide a state machine ARN in `redriveFilter`, the API returns a validation exception.
Type: String
Valid Values: `REDRIVEN | NOT_REDRIVEN`
Required: No

 ** [stateMachineArn](#API_ListExecutions_RequestSyntax) **   <a name="StepFunctions-ListExecutions-request-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the state machine whose executions is listed.
You can specify either a `mapRunArn` or a `stateMachineArn`, but not both.
You can also return a list of executions associated with a specific [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) or [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html), by specifying an alias ARN or a version ARN in the `stateMachineArn` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [statusFilter](#API_ListExecutions_RequestSyntax) **   <a name="StepFunctions-ListExecutions-request-statusFilter"></a>
If specified, only list the executions whose current execution status matches the given filter.
If you provide a `PENDING_REDRIVE` statusFilter, you must specify `mapRunArn`. For more information, see [Child workflow execution redrive behaviour](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html#redrive-child-workflow-behavior) in the * AWS Step Functions Developer Guide*.
If you provide a stateMachineArn and a `PENDING_REDRIVE` statusFilter, the API returns a validation exception.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | ABORTED | PENDING_REDRIVE`
Required: No

## Response Syntax
<a name="API_ListExecutions_ResponseSyntax"></a>

```
{
   "executions": [
      {
         "executionArn": "string",
         "itemCount": number,
         "mapRunArn": "string",
         "name": "string",
         "redriveCount": number,
         "redriveDate": number,
         "startDate": number,
         "stateMachineAliasArn": "string",
         "stateMachineArn": "string",
         "stateMachineVersionArn": "string",
         "status": "string",
         "stopDate": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executions](#API_ListExecutions_ResponseSyntax) **   <a name="StepFunctions-ListExecutions-response-executions"></a>
The list of matching executions.
Type: Array of [ExecutionListItem](API_ExecutionListItem.md) objects

 ** [nextToken](#API_ListExecutions_ResponseSyntax) **   <a name="StepFunctions-ListExecutions-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3096.

## Errors
<a name="API_ListExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** InvalidToken **
The provided token is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

 ** StateMachineDoesNotExist **
The specified state machine does not exist.
HTTP Status Code: 400

 ** StateMachineTypeNotSupported **
State machine type is not supported.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/ListExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/ListExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ListExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/ListExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ListExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/ListExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/ListExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/ListExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/ListExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ListExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
