---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetEvaluationFormValidation.html
---

# GetEvaluationFormValidation
<a name="API_GetEvaluationFormValidation"></a>

Retrieves the status and results of a validation process started by [StartEvaluationFormValidation](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEvaluationFormValidation.html). Returns the current execution status (`IN_PROGRESS`, `COMPLETED`, or `FAILED`), the validated form version, and when completed, a list of findings that identify structural issues and quality improvements for the evaluation form, and may include suggested fixes. If the validation failed, a reason is provided indicating the cause of the failure.

## Request Syntax
<a name="API_GetEvaluationFormValidation_RequestSyntax"></a>

```
GET /evaluation-forms/{{InstanceId}}/{{EvaluationFormId}}/validation-results?version={{EvaluationFormVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEvaluationFormValidation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationFormId](#API_GetEvaluationFormValidation_RequestSyntax) **   <a name="connect-GetEvaluationFormValidation-request-uri-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [EvaluationFormVersion](#API_GetEvaluationFormValidation_RequestSyntax) **   <a name="connect-GetEvaluationFormValidation-request-uri-EvaluationFormVersion"></a>
The version of the evaluation form to retrieve validation results for.

 ** [InstanceId](#API_GetEvaluationFormValidation_RequestSyntax) **   <a name="connect-GetEvaluationFormValidation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_GetEvaluationFormValidation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEvaluationFormValidation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationFormId": "string",
   "EvaluationFormVersion": number,
   "FailureReason": "string",
   "Findings": [
      {
         "Description": "string",
         "IssueCode": "string",
         "Items": [
            {
               "Property": "string",
               "RefId": "string"
            }
         ],
         "Severity": "string",
         "Suggestion": "string"
      }
   ],
   "StartedTime": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetEvaluationFormValidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationFormId](#API_GetEvaluationFormValidation_ResponseSyntax) **   <a name="connect-GetEvaluationFormValidation-response-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [EvaluationFormVersion](#API_GetEvaluationFormValidation_ResponseSyntax) **   <a name="connect-GetEvaluationFormValidation-response-EvaluationFormVersion"></a>
A version of the evaluation form.
Type: Integer

 ** [FailureReason](#API_GetEvaluationFormValidation_ResponseSyntax) **   <a name="connect-GetEvaluationFormValidation-response-FailureReason"></a>
The reason the validation failed. This field is populated only when the status is `FAILED`.
Type: String

 ** [Findings](#API_GetEvaluationFormValidation_ResponseSyntax) **   <a name="connect-GetEvaluationFormValidation-response-Findings"></a>
A list of findings from the validation process. Each finding identifies a structural issue or quality improvement for the evaluation form, and may include a suggested fix. This field is populated when the status is `COMPLETED`.
Type: Array of [EvaluationFormValidationFinding](API_EvaluationFormValidationFinding.md) objects

 ** [StartedTime](#API_GetEvaluationFormValidation_ResponseSyntax) **   <a name="connect-GetEvaluationFormValidation-response-StartedTime"></a>
The timestamp when the validation process was started.
Type: Timestamp

 ** [Status](#API_GetEvaluationFormValidation_ResponseSyntax) **   <a name="connect-GetEvaluationFormValidation-response-Status"></a>
The current status of the validation process. Valid values: `IN_PROGRESS`, `COMPLETED`, `FAILED`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`

## Errors
<a name="API_GetEvaluationFormValidation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_GetEvaluationFormValidation_Examples"></a>

### Example
<a name="API_GetEvaluationFormValidation_Example_1"></a>

The following example retrieves validation results for an evaluation form. The request does not have a request body.

#### Sample Response
<a name="API_GetEvaluationFormValidation_Example_1_Response"></a>

```
{
   "Status": "COMPLETED",
   "EvaluationFormVersion": 1,
   "EvaluationFormId": "[evaluation_form_id]",
   "StartedTime": "2026-04-20T16:00:15.015Z",
   "Findings": [
      {
         "IssueCode": "DUPLICATE_OPTION_TEXT",
         "Description": "All answer options for a question must have unique text",
         "Severity": "ERROR",
         "Items": [
            {
               "RefId": "question_1_1"
            }
         ]
      }
   ]
}
```

## See Also
<a name="API_GetEvaluationFormValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetEvaluationFormValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetEvaluationFormValidation)
