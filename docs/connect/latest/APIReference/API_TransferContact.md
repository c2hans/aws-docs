---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TransferContact.html
---

# TransferContact
<a name="API_TransferContact"></a>

Transfers `TASK` or `EMAIL` contacts from one agent or queue to another agent or queue at any point after a contact is created. You can transfer a contact to another queue by providing the flow which orchestrates the contact to the destination queue. This gives you more control over contact handling and helps you adhere to the service level agreement (SLA) guaranteed to your customers.

Note the following requirements:
+ Transfer is only supported for `TASK` and `EMAIL` contacts.
+ Do not use both `QueueId` and `UserId` in the same call.
+ The following flow types are supported: Inbound flow, Transfer to agent flow, and Transfer to queue flow.
+ The `TransferContact` API can be called only on active contacts.
+ A contact cannot be transferred more than 11 times.

## Request Syntax
<a name="API_TransferContact_RequestSyntax"></a>

```
POST /contact/transfer HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ContactFlowId": "{{string}}",
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}",
   "QueueId": "{{string}}",
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TransferContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TransferContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_TransferContact_RequestSyntax) **   <a name="connect-TransferContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_TransferContact_RequestSyntax) **   <a name="connect-TransferContact-request-ContactFlowId"></a>
The identifier of the flow.
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** [ContactId](#API_TransferContact_RequestSyntax) **   <a name="connect-TransferContact-request-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_TransferContact_RequestSyntax) **   <a name="connect-TransferContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [QueueId](#API_TransferContact_RequestSyntax) **   <a name="connect-TransferContact-request-QueueId"></a>
The identifier for the queue.
Type: String
Required: No

 ** [UserId](#API_TransferContact_RequestSyntax) **   <a name="connect-TransferContact-request-UserId"></a>
The identifier for the user. This can be the ID or the ARN of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_TransferContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactArn": "string",
   "ContactId": "string"
}
```

## Response Elements
<a name="API_TransferContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_TransferContact_ResponseSyntax) **   <a name="connect-TransferContact-response-ContactArn"></a>
The Amazon Resource Name (ARN) of the contact.
Type: String

 ** [ContactId](#API_TransferContact_ResponseSyntax) **   <a name="connect-TransferContact-response-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_TransferContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_TransferContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/TransferContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/TransferContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TransferContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/TransferContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TransferContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/TransferContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/TransferContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/TransferContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/TransferContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TransferContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
