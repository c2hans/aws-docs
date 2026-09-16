---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateQueue.html
---

# CreateQueue
<a name="API_CreateQueue"></a>

Creates a new queue for the specified Connect Customer instance.

**Important**
If the phone number is claimed to a traffic distribution group that was created in the same Region as the Connect Customer instance where you are calling this API, then you can use a full phone number ARN or a UUID for `OutboundCallerIdNumberId`. However, if the phone number is claimed to a traffic distribution group that is in one Region, and you are calling this API from an instance in another AWS Region that is associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a `ResourceNotFoundException`.
Only use the phone number ARN format that doesn't contain `instance` in the path, for example, `arn:aws:connect:us-east-1:1234567890:phone-number/uuid`. This is the same ARN format that is returned when you call the [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) API.
If you plan to use IAM policies to allow/deny access to this API for phone number resources claimed to a traffic distribution group, see [Allow or Deny queue API actions for phone numbers in a replica Region](https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_resource-level-policy-examples.html#allow-deny-queue-actions-replica-region).

## Request Syntax
<a name="API_CreateQueue_RequestSyntax"></a>

```
PUT /queues/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "EmailAddressesConfig": [
      {
         "EmailAddressId": "{{string}}"
      }
   ],
   "HoursOfOperationId": "{{string}}",
   "MaxContacts": {{number}},
   "Name": "{{string}}",
   "OutboundCallerConfig": {
      "OutboundCallerIdName": "{{string}}",
      "OutboundCallerIdNumberId": "{{string}}",
      "OutboundFlowId": "{{string}}"
   },
   "OutboundEmailConfig": {
      "OutboundEmailAddressId": "{{string}}"
   },
   "QuickConnectIds": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateQueue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateQueue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-Description"></a>
The description of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [EmailAddressesConfig](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-EmailAddressesConfig"></a>
Configuration list containing the email addresses to associate with the queue during creation. Each configuration specifies an email address ID that agents can select when handling email contacts in this queue.
Type: Array of [EmailAddressConfig](API_EmailAddressConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [HoursOfOperationId](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-HoursOfOperationId"></a>
The identifier for the hours of operation.
Type: String
Required: Yes

 ** [MaxContacts](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-MaxContacts"></a>
The maximum number of contacts that can be in the queue before it is considered full.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Name](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-Name"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [OutboundCallerConfig](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-OutboundCallerConfig"></a>
The outbound caller ID name, number, and outbound whisper flow.
Type: [OutboundCallerConfig](API_OutboundCallerConfig.md) object
Required: No

 ** [OutboundEmailConfig](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-OutboundEmailConfig"></a>
The outbound email address ID for a specified queue.
Type: [OutboundEmailConfig](API_OutboundEmailConfig.md) object
Required: No

 ** [QuickConnectIds](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-QuickConnectIds"></a>
The quick connects available to agents who are working the queue.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [Tags](#API_CreateQueue_RequestSyntax) **   <a name="connect-CreateQueue-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateQueue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "QueueArn": "string",
   "QueueId": "string"
}
```

## Response Elements
<a name="API_CreateQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueueArn](#API_CreateQueue_ResponseSyntax) **   <a name="connect-CreateQueue-response-QueueArn"></a>
The Amazon Resource Name (ARN) of the queue.
Type: String

 ** [QueueId](#API_CreateQueue_ResponseSyntax) **   <a name="connect-CreateQueue-response-QueueId"></a>
The identifier for the queue.
Type: String

## Errors
<a name="API_CreateQueue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
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
<a name="API_CreateQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateQueue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateQueue)
