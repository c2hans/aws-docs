---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueOutboundCallerConfig.html
---

# UpdateQueueOutboundCallerConfig
<a name="API_UpdateQueueOutboundCallerConfig"></a>

Updates the outbound caller ID name, number, and outbound whisper flow for a specified queue.

**Important**
If the phone number is claimed to a traffic distribution group that was created in the same Region as the Connect Customer instance where you are calling this API, then you can use a full phone number ARN or a UUID for `OutboundCallerIdNumberId`. However, if the phone number is claimed to a traffic distribution group that is in one Region, and you are calling this API from an instance in another AWS Region that is associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a `ResourceNotFoundException`.
Only use the phone number ARN format that doesn't contain `instance` in the path, for example, `arn:aws:connect:us-east-1:1234567890:phone-number/uuid`. This is the same ARN format that is returned when you call the [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) API.
If you plan to use IAM policies to allow/deny access to this API for phone number resources claimed to a traffic distribution group, see [Allow or Deny queue API actions for phone numbers in a replica Region](https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_resource-level-policy-examples.html#allow-deny-queue-actions-replica-region).

## Request Syntax
<a name="API_UpdateQueueOutboundCallerConfig_RequestSyntax"></a>

```
POST /queues/{{InstanceId}}/{{QueueId}}/outbound-caller-config HTTP/1.1
Content-type: application/json

{
   "OutboundCallerConfig": {
      "OutboundCallerIdName": "{{string}}",
      "OutboundCallerIdNumberId": "{{string}}",
      "OutboundFlowId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateQueueOutboundCallerConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateQueueOutboundCallerConfig_RequestSyntax) **   <a name="connect-UpdateQueueOutboundCallerConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [QueueId](#API_UpdateQueueOutboundCallerConfig_RequestSyntax) **   <a name="connect-UpdateQueueOutboundCallerConfig-request-uri-QueueId"></a>
The identifier for the queue.
Required: Yes

## Request Body
<a name="API_UpdateQueueOutboundCallerConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [OutboundCallerConfig](#API_UpdateQueueOutboundCallerConfig_RequestSyntax) **   <a name="connect-UpdateQueueOutboundCallerConfig-request-OutboundCallerConfig"></a>
The outbound caller ID name, number, and outbound whisper flow.
Type: [OutboundCallerConfig](API_OutboundCallerConfig.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateQueueOutboundCallerConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateQueueOutboundCallerConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateQueueOutboundCallerConfig_Errors"></a>

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
<a name="API_UpdateQueueOutboundCallerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateQueueOutboundCallerConfig)
