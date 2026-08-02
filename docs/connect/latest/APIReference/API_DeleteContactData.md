---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteContactData.html
---

# DeleteContactData
<a name="API_DeleteContactData"></a>

Deletes the specified fields containing personally identifiable information (PII) from a contact in the specified Connect Customer instance. We redact PII (such as customer endpoints, additional email recipients, and the email subject) from the contact and its associated contact trace record (CTR). The contact must be in a terminated state.

**Important**
 **This deletion is permanent and cannot be undone.** Performing this operation permanently deletes the specified PII. There is no retention period; you cannot recover the data after deletion. We remove only the fields that Connect Customer identifies and stores as PII. Any PII that you place in fields outside the scope of this operation remains your responsibility to remove.

## Request Syntax
<a name="API_DeleteContactData_RequestSyntax"></a>

```
POST /contact/delete/{{InstanceId}}/{{ContactId}} HTTP/1.1
Content-type: application/json

{
   "ContactFields": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeleteContactData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_DeleteContactData_RequestSyntax) **   <a name="connect-DeleteContactData-request-uri-ContactId"></a>
The identifier of the contact. You can delete PII only from a contact that has been disconnected (is in a terminated state).
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DeleteContactData_RequestSyntax) **   <a name="connect-DeleteContactData-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DeleteContactData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactFields](#API_DeleteContactData_RequestSyntax) **   <a name="connect-DeleteContactData-request-ContactFields"></a>
The categories of PII to redact from the contact. Specify one or more of the following values:
+  `CUSTOMER_ENDPOINT` – The customer's contact endpoint.
+  `ADDITIONAL_EMAIL_RECIPIENTS` – Additional recipients on an email contact (email channel only).
+  `EMAIL_SUBJECT` – The subject line of an email contact (email channel only).
Type: Array of strings
Valid Values: `CUSTOMER_ENDPOINT | ADDITIONAL_EMAIL_RECIPIENTS | EMAIL_SUBJECT`
Required: Yes

## Response Syntax
<a name="API_DeleteContactData_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteContactData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteContactData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ContactNotTerminatedException **
The contact has not been disconnected and is not in a terminated state. To delete PII, disconnect the contact first. Wait for it to reach the terminated state, then retry the request.
HTTP Status Code: 409

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

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DeleteContactData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteContactData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteContactData)
