---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactEvaluation.html
---

# StartContactEvaluation
<a name="API_StartContactEvaluation"></a>

Starts an empty evaluation in the specified Connect Customer instance, using the given evaluation form for the particular contact. The evaluation form version used for the contact evaluation corresponds to the currently activated version. If no version is activated for the evaluation form, the contact evaluation cannot be started.

**Note**
Evaluations created through the public API do not contain answer values suggested from automation.

## Request Syntax
<a name="API_StartContactEvaluation_RequestSyntax"></a>

```
PUT /contact-evaluations/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "AutoEvaluationConfiguration": {
      "Enabled": {{boolean}}
   },
   "ClientToken": "{{string}}",
   "ContactId": "{{string}}",
   "EvaluationFormId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartContactEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_StartContactEvaluation_RequestSyntax) **   <a name="connect-StartContactEvaluation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_StartContactEvaluation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AutoEvaluationConfiguration](#API_StartContactEvaluation_RequestSyntax) **   <a name="connect-StartContactEvaluation-request-AutoEvaluationConfiguration"></a>
Whether automated evaluations are enabled.
Type: [AutoEvaluationConfiguration](API_AutoEvaluationConfiguration.md) object
Required: No

 ** [ClientToken](#API_StartContactEvaluation_RequestSyntax) **   <a name="connect-StartContactEvaluation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactId](#API_StartContactEvaluation_RequestSyntax) **   <a name="connect-StartContactEvaluation-request-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [EvaluationFormId](#API_StartContactEvaluation_RequestSyntax) **   <a name="connect-StartContactEvaluation-request-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [Tags](#API_StartContactEvaluation_RequestSyntax) **   <a name="connect-StartContactEvaluation-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartContactEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EvaluationArn": "string",
   "EvaluationId": "string"
}
```

## Response Elements
<a name="API_StartContactEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationArn](#API_StartContactEvaluation_ResponseSyntax) **   <a name="connect-StartContactEvaluation-response-EvaluationArn"></a>
The Amazon Resource Name (ARN) for the contact evaluation resource.
Type: String

 ** [EvaluationId](#API_StartContactEvaluation_ResponseSyntax) **   <a name="connect-StartContactEvaluation-response-EvaluationId"></a>
A unique identifier for the contact evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_StartContactEvaluation_Errors"></a>

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
<a name="API_StartContactEvaluation_Examples"></a>

### Example
<a name="API_StartContactEvaluation_Example_1"></a>

The following example starts a contact evaluation for a contact.

#### Sample Request
<a name="API_StartContactEvaluation_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationFormId": "[evaluation_form_id]",
   "ContactId": "[contact_id]"
}
```

#### Sample Response
<a name="API_StartContactEvaluation_Example_1_Response"></a>

```
{
   "EvaluationId": "[evaluation_id]",
   "EvaluationArn": "arn:aws:connect:[aws_region_code]:[account_id]:instance/[instance_id]/contact-evaluation/[evaluation_id]"
}
```

## See Also
<a name="API_StartContactEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartContactEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartContactEvaluation)
