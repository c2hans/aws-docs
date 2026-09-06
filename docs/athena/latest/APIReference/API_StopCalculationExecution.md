---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_StopCalculationExecution.html
---

# StopCalculationExecution
<a name="API_StopCalculationExecution"></a>

Requests the cancellation of a calculation. A `StopCalculationExecution` call on a calculation that is already in a terminal state (for example, `STOPPED`, `FAILED`, or `COMPLETED`) succeeds but has no effect.

**Note**
Cancelling a calculation is done on a best effort basis. If a calculation cannot be cancelled, you can be charged for its completion. If you are concerned about being charged for a calculation that cannot be cancelled, consider terminating the session in which the calculation is running.

## Request Syntax
<a name="API_StopCalculationExecution_RequestSyntax"></a>

```
{
   "CalculationExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopCalculationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CalculationExecutionId](#API_StopCalculationExecution_RequestSyntax) **   <a name="athena-StopCalculationExecution-request-CalculationExecutionId"></a>
The calculation execution UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Response Syntax
<a name="API_StopCalculationExecution_ResponseSyntax"></a>

```
{
   "State": "string"
}
```

## Response Elements
<a name="API_StopCalculationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [State](#API_StopCalculationExecution_ResponseSyntax) **   <a name="athena-StopCalculationExecution-response-State"></a>
 `CREATING` - The calculation is in the process of being created.
 `CREATED` - The calculation has been created and is ready to run.
 `QUEUED` - The calculation has been queued for processing.
 `RUNNING` - The calculation is running.
 `CANCELING` - A request to cancel the calculation has been received and the system is working to stop it.
 `CANCELED` - The calculation is no longer running as the result of a cancel request.
 `COMPLETED` - The calculation has completed without error.
 `FAILED` - The calculation failed and is no longer running.
Type: String
Valid Values: `CREATING | CREATED | QUEUED | RUNNING | CANCELING | CANCELED | COMPLETED | FAILED`

## Errors
<a name="API_StopCalculationExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_StopCalculationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/StopCalculationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/StopCalculationExecution)
