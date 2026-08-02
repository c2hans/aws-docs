---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteContactEvaluation.html
---

# DeleteContactEvaluation
<a name="API_DeleteContactEvaluation"></a>

Deletes a contact evaluation in the specified Connect Customer instance.

## Request Syntax
<a name="API_DeleteContactEvaluation_RequestSyntax"></a>

```
DELETE /contact-evaluations/{{InstanceId}}/{{EvaluationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteContactEvaluation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EvaluationId](#API_DeleteContactEvaluation_RequestSyntax) **   <a name="connect-DeleteContactEvaluation-request-uri-EvaluationId"></a>
A unique identifier for the contact evaluation.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_DeleteContactEvaluation_RequestSyntax) **   <a name="connect-DeleteContactEvaluation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DeleteContactEvaluation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteContactEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteContactEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteContactEvaluation_Errors"></a>

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
<a name="API_DeleteContactEvaluation_Examples"></a>

### Example
<a name="API_DeleteContactEvaluation_Example_1"></a>

The following example deletes a contact evaluation.

#### Sample Request
<a name="API_DeleteContactEvaluation_Example_1_Request"></a>

```
{
   "InstanceId": "[instance_id]",
   "EvaluationId": "[evaluation_id]"
}
```

#### Sample Response
<a name="API_DeleteContactEvaluation_Example_1_Response"></a>

```
(empty response)
```

## See Also
<a name="API_DeleteContactEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteContactEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteContactEvaluation)
