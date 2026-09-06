---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_StartCalculationExecution.html
---

# StartCalculationExecution
<a name="API_StartCalculationExecution"></a>

Submits calculations for execution within a session. You can supply the code to run as an inline code block within the request.

**Note**
The request syntax requires the [StartCalculationExecution:CodeBlock](#athena-StartCalculationExecution-request-CodeBlock) parameter or the [CalculationConfiguration:CodeBlock](API_CalculationConfiguration.md#athena-Type-CalculationConfiguration-CodeBlock) parameter, but not both. Because [CalculationConfiguration:CodeBlock](API_CalculationConfiguration.md#athena-Type-CalculationConfiguration-CodeBlock) is deprecated, use the [StartCalculationExecution:CodeBlock](#athena-StartCalculationExecution-request-CodeBlock) parameter instead.

## Request Syntax
<a name="API_StartCalculationExecution_RequestSyntax"></a>

```
{
   "CalculationConfiguration": {
      "CodeBlock": "{{string}}"
   },
   "ClientRequestToken": "{{string}}",
   "CodeBlock": "{{string}}",
   "Description": "{{string}}",
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartCalculationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CalculationConfiguration](#API_StartCalculationExecution_RequestSyntax) **   <a name="athena-StartCalculationExecution-request-CalculationConfiguration"></a>
 *This parameter has been deprecated.*
Contains configuration information for the calculation.
Type: [CalculationConfiguration](API_CalculationConfiguration.md) object
Required: No

 ** [ClientRequestToken](#API_StartCalculationExecution_RequestSyntax) **   <a name="athena-StartCalculationExecution-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure the request to create the calculation is idempotent (executes only once). If another `StartCalculationExecutionRequest` is received, the same response is returned and another calculation is not created. If a parameter has changed, an error is returned.
This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [CodeBlock](#API_StartCalculationExecution_RequestSyntax) **   <a name="athena-StartCalculationExecution-request-CodeBlock"></a>
A string that contains the code of the calculation. Use this parameter instead of [CalculationConfiguration:CodeBlock](API_CalculationConfiguration.md#athena-Type-CalculationConfiguration-CodeBlock), which is deprecated.
Type: String
Length Constraints: Maximum length of 68000.
Required: No

 ** [Description](#API_StartCalculationExecution_RequestSyntax) **   <a name="athena-StartCalculationExecution-request-Description"></a>
A description of the calculation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SessionId](#API_StartCalculationExecution_RequestSyntax) **   <a name="athena-StartCalculationExecution-request-SessionId"></a>
The session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_StartCalculationExecution_ResponseSyntax"></a>

```
{
   "CalculationExecutionId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_StartCalculationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CalculationExecutionId](#API_StartCalculationExecution_ResponseSyntax) **   <a name="athena-StartCalculationExecution-response-CalculationExecutionId"></a>
The calculation execution UUID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [State](#API_StartCalculationExecution_ResponseSyntax) **   <a name="athena-StartCalculationExecution-response-State"></a>
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
<a name="API_StartCalculationExecution_Errors"></a>

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
<a name="API_StartCalculationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/StartCalculationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/StartCalculationExecution)
