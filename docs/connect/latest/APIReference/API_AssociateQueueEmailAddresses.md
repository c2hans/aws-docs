---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateQueueEmailAddresses.html
---

# AssociateQueueEmailAddresses
<a name="API_AssociateQueueEmailAddresses"></a>

Associates a set of email addresses with a queue to enable agents to select different "From" (system) email addresses when replying to inbound email contacts or initiating outbound email contacts. This allows agents to handle email contacts across different brands and business units within the same queue.

 **Important things to know**
+ You can associate up to 49 additional email addresses with a single queue, plus 1 default outbound email address, for a total of 50.
+ The email addresses must already exist in the Connect Customer instance before they can be associated with a queue.
+ Agents will be able to select from these associated email addresses when handling email contacts in the queue.
+ For inbound email contacts, agents can select from email addresses associated with the queue where the contact was accepted.
+ For outbound email contacts, agents can select from email addresses associated with their default outbound queue configured in their routing profile.

## Request Syntax
<a name="API_AssociateQueueEmailAddresses_RequestSyntax"></a>

```
POST /queues/{{InstanceId}}/{{QueueId}}/associate-email-addresses HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "EmailAddressesConfig": [
      {
         "EmailAddressId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_AssociateQueueEmailAddresses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-AssociateQueueEmailAddresses-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [QueueId](#API_AssociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-AssociateQueueEmailAddresses-request-uri-QueueId"></a>
The identifier for the queue.
Required: Yes

## Request Body
<a name="API_AssociateQueueEmailAddresses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_AssociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-AssociateQueueEmailAddresses-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [EmailAddressesConfig](#API_AssociateQueueEmailAddresses_RequestSyntax) **   <a name="connect-AssociateQueueEmailAddresses-request-EmailAddressesConfig"></a>
Configuration list containing the email addresses to associate with the queue. Each configuration specifies an email address ID that should be linked to this queue for routing purposes.
Type: Array of [EmailAddressConfig](API_EmailAddressConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_AssociateQueueEmailAddresses_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateQueueEmailAddresses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateQueueEmailAddresses_Errors"></a>

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateQueueEmailAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateQueueEmailAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateQueueEmailAddresses)
