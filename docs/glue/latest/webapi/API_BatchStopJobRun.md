---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchStopJobRun.html
---

# BatchStopJobRun
<a name="API_BatchStopJobRun"></a>

Stops one or more job runs for a specified job definition.

## Request Syntax
<a name="API_BatchStopJobRun_RequestSyntax"></a>

```
{
   "JobName": "{{string}}",
   "JobRunIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchStopJobRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobName](#API_BatchStopJobRun_RequestSyntax) **   <a name="Glue-BatchStopJobRun-request-JobName"></a>
The name of the job definition for which to stop job runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [JobRunIds](#API_BatchStopJobRun_RequestSyntax) **   <a name="Glue-BatchStopJobRun-request-JobRunIds"></a>
A list of the `JobRunIds` that should be stopped for that job definition.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchStopJobRun_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "ErrorDetail": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "JobName": "string",
         "JobRunId": "string"
      }
   ],
   "SuccessfulSubmissions": [
      {
         "JobName": "string",
         "JobRunId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchStopJobRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchStopJobRun_ResponseSyntax) **   <a name="Glue-BatchStopJobRun-response-Errors"></a>
A list of the errors that were encountered in trying to stop `JobRuns`, including the `JobRunId` for which each error was encountered and details about the error.
Type: Array of [BatchStopJobRunError](API_BatchStopJobRunError.md) objects

 ** [SuccessfulSubmissions](#API_BatchStopJobRun_ResponseSyntax) **   <a name="Glue-BatchStopJobRun-response-SuccessfulSubmissions"></a>
A list of the JobRuns that were successfully submitted for stopping.
Type: Array of [BatchStopJobRunSuccessfulSubmission](API_BatchStopJobRunSuccessfulSubmission.md) objects

## Errors
<a name="API_BatchStopJobRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchStopJobRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchStopJobRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchStopJobRun)
