---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEvaluationFormValidation.html
---

# StartEvaluationFormValidation
<a name="API_StartEvaluationFormValidation"></a>

Starts an asynchronous validation process for an evaluation form version in the specified Connect Customer instance. The validation first performs structural checks on the form content (such as verifying required fields, valid scoring configuration, and correct conditional logic), then asynchronously analyzes questions configured for generative AI evaluation against a set of best practices. Use [GetEvaluationFormValidation](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetEvaluationFormValidation.html) to retrieve the status and results once the validation completes.

## Request Syntax
<a name="API_StartEvaluationFormValidation_RequestSyntax"></a>

```
POST /evaluation-forms/{{InstanceId}}/{{EvaluationFormId}}/validate HTTP/1.1
Content-type: application/json

{
   "EvaluationFormVersion": {{number}}
}
```

## URI Request Parameters
<a name="API_StartEvaluationFormValidation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationFormId](#API_StartEvaluationFormValidation_RequestSyntax) **   <a name="connect-StartEvaluationFormValidation-request-uri-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_StartEvaluationFormValidation_RequestSyntax) **   <a name="connect-StartEvaluationFormValidation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_StartEvaluationFormValidation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EvaluationFormVersion](#API_StartEvaluationFormValidation_RequestSyntax) **   <a name="connect-StartEvaluationFormValidation-request-EvaluationFormVersion"></a>
The version of the evaluation form to validate.
Type: Integer
Required: Yes

## Response Syntax
<a name="API_StartEvaluationFormValidation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationFormArn": "string",
   "EvaluationFormId": "string",
   "EvaluationFormVersion": number
}
```

## Response Elements
<a name="API_StartEvaluationFormValidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationFormArn](#API_StartEvaluationFormValidation_ResponseSyntax) **   <a name="connect-StartEvaluationFormValidation-response-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the evaluation form resource.
Type: String

 ** [EvaluationFormId](#API_StartEvaluationFormValidation_ResponseSyntax) **   <a name="connect-StartEvaluationFormValidation-response-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [EvaluationFormVersion](#API_StartEvaluationFormValidation_ResponseSyntax) **   <a name="connect-StartEvaluationFormValidation-response-EvaluationFormVersion"></a>
A version of the evaluation form.
Type: Integer

## Errors
<a name="API_StartEvaluationFormValidation_Errors"></a>

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

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_StartEvaluationFormValidation_Examples"></a>

### Example
<a name="API_StartEvaluationFormValidation_Example_1"></a>

The following example starts a validation for version 1 of an evaluation form.

#### Sample Request
<a name="API_StartEvaluationFormValidation_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationFormId": "[evaluation_form_id]",
   "EvaluationFormVersion": 1
}
```

#### Sample Response
<a name="API_StartEvaluationFormValidation_Example_1_Response"></a>

```
{
   "EvaluationFormId": "[evaluation_form_id]",
   "EvaluationFormArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/evaluation-form/[evaluation_form_id]",
   "EvaluationFormVersion": 1
}
```

## See Also
<a name="API_StartEvaluationFormValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartEvaluationFormValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartEvaluationFormValidation)
