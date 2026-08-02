---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SubmitContactEvaluation.html
---

# SubmitContactEvaluation
<a name="API_SubmitContactEvaluation"></a>

Submits a contact evaluation in the specified Connect Customer instance. Answers included in the request are merged with existing answers for the given evaluation. If no answers or notes are passed, the evaluation is submitted with the existing answers and notes. You can delete an answer or note by passing an empty object (`{}`) to the question identifier.

If a contact evaluation is already in submitted state, this operation will trigger a resubmission.

## Request Syntax
<a name="API_SubmitContactEvaluation_RequestSyntax"></a>

```
POST /contact-evaluations/{{InstanceId}}/{{EvaluationId}}/submit HTTP/1.1
Content-type: application/json

{
   "Answers": {
      "{{string}}" : {
         "Value": { ... }
      }
   },
   "Notes": {
      "{{string}}" : {
         "Value": "{{string}}"
      }
   },
   "SubmittedBy": { ... }
}
```

## URI Request Parameters
<a name="API_SubmitContactEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationId](#API_SubmitContactEvaluation_RequestSyntax) **   <a name="connect-SubmitContactEvaluation-request-uri-EvaluationId"></a>
A unique identifier for the contact evaluation.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_SubmitContactEvaluation_RequestSyntax) **   <a name="connect-SubmitContactEvaluation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_SubmitContactEvaluation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Answers](#API_SubmitContactEvaluation_RequestSyntax) **   <a name="connect-SubmitContactEvaluation-request-Answers"></a>
A map of question identifiers to answer value.
Type: String to [EvaluationAnswerInput](API_EvaluationAnswerInput.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [Notes](#API_SubmitContactEvaluation_RequestSyntax) **   <a name="connect-SubmitContactEvaluation-request-Notes"></a>
A map of question identifiers to note value.
Type: String to [EvaluationNote](API_EvaluationNote.md) object map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [SubmittedBy](#API_SubmitContactEvaluation_RequestSyntax) **   <a name="connect-SubmitContactEvaluation-request-SubmittedBy"></a>
The ID of the user who submitted the contact evaluation.
Type: [EvaluatorUserUnion](API_EvaluatorUserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_SubmitContactEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationArn": "string",
   "EvaluationId": "string"
}
```

## Response Elements
<a name="API_SubmitContactEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationArn](#API_SubmitContactEvaluation_ResponseSyntax) **   <a name="connect-SubmitContactEvaluation-response-EvaluationArn"></a>
The Amazon Resource Name (ARN) for the contact evaluation resource.
Type: String

 ** [EvaluationId](#API_SubmitContactEvaluation_ResponseSyntax) **   <a name="connect-SubmitContactEvaluation-response-EvaluationId"></a>
A unique identifier for the contact evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_SubmitContactEvaluation_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_SubmitContactEvaluation_Examples"></a>

### Example
<a name="API_SubmitContactEvaluation_Example_1"></a>

The following example submits a previously started contact evaluation.

#### Sample Request
<a name="API_SubmitContactEvaluation_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationId": "[evaluation_id]"
}
```

#### Sample Response
<a name="API_SubmitContactEvaluation_Example_1_Response"></a>

```
{
   "EvaluationId": "[evaluation_id]",
   "EvaluationArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/contact-evaluation/[evaluation_id]"
}
```

## See Also
<a name="API_SubmitContactEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SubmitContactEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SubmitContactEvaluation)
