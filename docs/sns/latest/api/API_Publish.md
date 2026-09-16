---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_Publish.html
---

# Publish
<a name="API_Publish"></a>

Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the `TargetArn`).

If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.

When a `messageId` is returned, the message is saved and Amazon SNS immediately delivers it to subscribers.

To use the `Publish` action for publishing a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the `CreatePlatformEndpoint` action. The second example below shows a request and response for publishing to a mobile endpoint.

For more information about formatting messages, see [Send Custom Platform-Specific Payloads in Messages to Mobile Devices](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html).

**Important**
You can publish messages only to topics and endpoints in the same AWS Region.

## Request Parameters
<a name="API_Publish_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Message **
The message you want to send.
If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the `MessageStructure` parameter to `json` and use a JSON object for the `Message` parameter. See the Examples section for the format of the JSON object.

Constraints:
+ With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).
+ For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters.

  If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren't truncated mid-word but are cut off at whole-word boundaries.

  The total size limit for a single SMS `Publish` action is 1,600 characters.
JSON-specific constraints:
+ Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.
+ The values will be parsed (unescaped) before they are used in outgoing messages.
+ Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).
+ Values have a minimum length of 0 (the empty string, "", is allowed).
+ Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).
+ Non-string values will cause the key to be ignored.
+ Keys that do not correspond to supported transport protocols are ignored.
+ Duplicate keys are not allowed.
+ Failure to parse or validate any key or value in the message will cause the `Publish` call to return an error (no partial delivery).
Type: String
Required: Yes

 **MessageAttributes** MessageAttributes.entry.N.Name (key)MessageAttributes.entry.N.Value (value)
Message attributes for Publish action.
Type: String to [MessageAttributeValue](API_MessageAttributeValue.md) object map
Required: No

 ** MessageDeduplicationId **
+ This parameter applies only to FIFO (first-in-first-out) topics. The `MessageDeduplicationId` can contain up to 128 alphanumeric characters `(a-z, A-Z, 0-9)` and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)`.
+ Every message must have a unique `MessageDeduplicationId`, which is a token used for deduplication of sent messages within the 5 minute minimum deduplication interval.
+ The scope of deduplication depends on the `FifoThroughputScope` attribute, when set to `Topic` the message deduplication scope is across the entire topic, when set to `MessageGroup` the message deduplication scope is within each individual message group.
+ If a message with a particular `MessageDeduplicationId` is sent successfully, subsequent messages within the deduplication scope and interval, with the same `MessageDeduplicationId`, are accepted successfully but aren't delivered.
+ Every message must have a unique `MessageDeduplicationId`:
  + You may provide a `MessageDeduplicationId` explicitly.
  + If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your topic, Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).
  + If you don't provide a `MessageDeduplicationId` and the topic doesn't have `ContentBasedDeduplication` set, the action fails with an error.
  + If the topic has a `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.
+ When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication scope and interval are treated as duplicates and only one copy of the message is delivered.
+ If you send one message with `ContentBasedDeduplication` enabled, and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates, within the deduplication scope and interval, and only one copy of the message is delivered.
Type: String
Required: No

 ** MessageGroupId **
The `MessageGroupId` can contain up to 128 alphanumeric characters `(a-z, A-Z, 0-9)` and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)`.
 For FIFO topics: The `MessageGroupId` is a tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). Every message must include a `MessageGroupId`.
 For standard topics: The `MessageGroupId` is optional and is forwarded only to Amazon SQS standard subscriptions to activate [fair queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html). The `MessageGroupId` is not used for, or sent to, any other endpoint types. When provided, the same validation rules apply as for FIFO topics.
Type: String
Required: No

 ** MessageStructure **
Set `MessageStructure` to `json` if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set `MessageStructure` to `json`, the value of the `Message` parameter must:
+ be a syntactically valid JSON object; and
+ contain at least a top-level JSON key of "default" with a value that is a string.
You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., "http").
Valid value: `json`
Type: String
Required: No

 ** PhoneNumber **
The phone number to which you want to deliver an SMS message. Use E.164 format.
If you don't specify a value for the `PhoneNumber` parameter, you must specify a value for the `TargetArn` or `TopicArn` parameters.
Type: String
Required: No

 ** Subject **
Optional parameter to be used as the "Subject" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.
Constraints: Subjects must be UTF-8 text with no line breaks or control characters, and less than 100 characters long.
Type: String
Required: No

 ** TargetArn **
If you don't specify a value for the `TargetArn` parameter, you must specify a value for the `PhoneNumber` or `TopicArn` parameters.
Type: String
Required: No

 ** TopicArn **
The topic you want to publish to.
If you don't specify a value for the `TopicArn` parameter, you must specify a value for the `PhoneNumber` or `TargetArn` parameters.
Type: String
Required: No

## Response Elements
<a name="API_Publish_ResponseElements"></a>

The following elements are returned by the service.

 ** MessageId **
Unique identifier assigned to the published message.
Length Constraint: Maximum 100 characters
Type: String

 ** SequenceNumber **
This response element applies only to FIFO (first-in-first-out) topics.
The sequence number is a large, non-consecutive number that Amazon SNS assigns to each message. The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to increase for each `MessageGroupId`.
Type: String

## Errors
<a name="API_Publish_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** EndpointDisabled **
Exception error indicating endpoint disabled.
 ** message **
Message for endpoint disabled.
HTTP Status Code: 400

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** InvalidSecurity **
The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.
HTTP Status Code: 403

 ** KMSAccessDenied **
The ciphertext references a key that doesn't exist or that you don't have access to.
HTTP Status Code: 400

 ** KMSDisabled **
The request was rejected because the specified AWS KMS key isn't enabled.
HTTP Status Code: 400

 ** KMSInvalidState **
The request was rejected because the state of the specified resource isn't valid for this request. For more information, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
HTTP Status Code: 400

 ** KMSNotFound **
The request was rejected because the specified entity or resource can't be found.
HTTP Status Code: 400

 ** KMSOptInRequired **
The AWS access key ID needs a subscription for the service.
HTTP Status Code: 403

 ** KMSThrottling **
The request was denied due to request throttling. For more information about throttling, see [Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) in the * AWS Key Management Service Developer Guide.*
HTTP Status Code: 400

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

 ** ParameterValueInvalid **
Indicates that a request parameter does not comply with the associated constraints.
 ** message **
The parameter of an entry in a request doesn't abide by the specification.
HTTP Status Code: 400

 ** PlatformApplicationDisabled **
Exception error indicating platform application disabled.
 ** message **
Message for platform application disabled.
HTTP Status Code: 400

 ** Validation **
Indicates that a parameter in the request is invalid.
HTTP Status Code: 400

## Examples
<a name="API_Publish_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_Publish_Example_1"></a>

This example illustrates one usage of Publish.

#### Sample Request
<a name="API_Publish_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=Publish
&TargetArn=arn%3Aaws%3Asns%3Aus-west-2%3A803981987763%3Aendpoint%2FAPNS_SANDBOX%2Fpushapp%2F98e9ced9-f136-3893-9d60-776547eafebb
&Message=%7B%22default%22%3A%22This+is+the+default+Message%22%2C%22APNS_SANDBOX%22%3A%22%7B+%5C%22aps%5C%22+%3A+%7B+%5C%22alert%5C%22+%3A+%5C%22You+have+got+email.%5C%22%2C+%5C%22badge%5C%22+%3A+9%2C%5C%22sound%5C%22+%3A%5C%22default%5C%22%7D%7D%22%7D
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_Publish_Example_1_Response"></a>

```
<PublishResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <PublishResult>
        <MessageId>567910cd-659e-55d4-8ccb-5aaf14679dc0</MessageId>
    </PublishResult>
    <ResponseMetadata>
        <RequestId>d74b8436-ae13-5ab4-a9ff-ce54dfea72a0</RequestId>
    </ResponseMetadata>
</PublishResponse>
```

### Example
<a name="API_Publish_Example_2"></a>

The following example publishes a different messages to each protocol:

The JSON format for `Message` is as follows:

```
{
    "default": "A message.",
    "email": "A message for email.",
    "email-json": "A message for email (JSON).",
    "http": "A message for HTTP.",
    "https": "A message for HTTPS.",
    "sqs": "A message for Amazon SQS."
}
```

#### Sample Request
<a name="API_Publish_Example_2_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=Publish
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A698519295917%3AMy-Topic
&Subject=My%20first%20message
&Message=Hello%20world%21
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_Publish_Example_2_Response"></a>

```
<PublishResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <PublishResult>
        <MessageId>94f20ce6-13c5-43a0-9a9e-ca52d816e90b</MessageId>
    </PublishResult>
    <ResponseMetadata>
        <RequestId>f187a3c1-376f-11df-8963-01868b7c937a</RequestId>
    </ResponseMetadata>
</PublishResponse>
```

### Example
<a name="API_Publish_Example_3"></a>

The following example allows you to specify different message content for different transport protocols (SMS, email, and push notification):

The JSON format for `MessageStructure` is as follows:

```
  "default": "This is the default message",
  "email": "This is the email message",
  "sms": "This is the SMS message",
  "app1": "This is the message for app1",
  "app2": "This is the message for app2"
}
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Request
<a name="API_Publish_Example_3_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=Publish
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A698519295917%3AMy-Topic
&Subject=My%20first%20message
&Message=Hello%20world%21
&MessageStructure=json
&Message={
  "default": "This is the default message",
  "email": "This is the email message",
  "sms": "This is the SMS message",
  "app1": "This is the message for app1",
  "app2": "This is the message for app2"
}
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_Publish_Example_3_Response"></a>

```
<PublishResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
  <PublishResult>
    <MessageId>95df01b4-ee98-5cb9-9069-4b046b850ca6</MessageId>
  </PublishResult>
  <ResponseMetadata>
    <RequestId>c6101522-8f6a-5d59-8e6e-cb9bc1bf0c9f</RequestId>
  </ResponseMetadata>
</PublishResponse>
```

## See Also
<a name="API_Publish_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/Publish)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/Publish)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/Publish)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/Publish)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/Publish)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/Publish)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/Publish)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/Publish)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/Publish)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/Publish)
