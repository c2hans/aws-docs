---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateQueueEmailAddresses.html
---

# DisassociateQueueEmailAddresses
<a name="API_DisassociateQueueEmailAddresses"></a>

Removes the association between a set of email addresses and a queue. After disassociation, agents will no longer be able to select these email addresses as "From" addresses when replying to inbound email contacts or initiating outbound email contacts in this queue.

 **Important things to know**
+ Agents will no longer see these email addresses in their "From" address selection options for this queue.
+ The email addresses themselves are not deleted from the instance, only their availability for agent selection in this queue is removed.
+ Changes take effect immediately and will affect the agent experience in the Contact Control Panel (CCP).

## Request Syntax
<a name="API_DisassociateQueueEmailAddresses_RequestSyntax"></a>

```
POST /queues/{{InstanceId}}/{{QueueId}}/disassociate-email-addresses HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "EmailAddressesId": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DisassociateQueueEmailAddresses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DisassociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-DisassociateQueueEmailAddresses-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [QueueId](#API_DisassociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-DisassociateQueueEmailAddresses-request-uri-QueueId"></a>
The identifier for the queue.
Required: Yes

## Request Body
<a name="API_DisassociateQueueEmailAddresses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_DisassociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-DisassociateQueueEmailAddresses-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [EmailAddressesId](#API_DisassociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-DisassociateQueueEmailAddresses-request-EmailAddressesId"></a>
List of email address identifiers to disassociate from the queue. These are the unique identifiers of email addresses that should no longer be routed to this queue.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Response Syntax
<a name="API_DisassociateQueueEmailAddresses_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateQueueEmailAddresses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateQueueEmailAddresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_DisassociateQueueEmailAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateQueueEmailAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateQueueEmailAddresses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
