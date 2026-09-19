---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_PublishBatch.html
---

# PublishBatch
<a name="API_PublishBatch"></a>

Publishes up to 10 messages to the specified topic in a single batch. This is a batch version of the `Publish` API. If you try to send more than 10 messages in a single batch request, you will receive a `TooManyEntriesInBatchRequest` exception.

For FIFO topics, multiple messages within a single batch are published in the order they are sent, and messages are deduplicated within the batch and across batches for five minutes.

The result of publishing each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.

By default, the maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KiB (262,144 bytes). To publish larger batches, set the topic's `MaximumMessageSize` attribute, which supports values up to 1 MiB (1,048,576 bytes). The combined size of all messages in the batch, including each message's body and attributes, must not exceed the topic's `MaximumMessageSize`.

For more information, see [Large message payloads](https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html) in the *Amazon SNS Developer Guide.*

**Important**
The `PublishBatch` API can send up to 10 messages at a time. If you attempt to send more than 10 messages in one request, you will encounter a `TooManyEntriesInBatchRequest` exception. In such cases, split your messages into multiple requests, each containing no more than 10 messages.

Some actions take lists of parameters. These lists are specified using the `param.n` notation. Values of `n` are integers starting from **1**. For example, a parameter list with two elements looks like this:

 `&AttributeName.1=first`

 `&AttributeName.2=second`

If you send a batch message to a topic, Amazon SNS publishes the batch message to each endpoint that is subscribed to the topic. The format of the batch message depends on the notification protocol for each subscribed endpoint.

When a `messageId` is returned, the batch message is saved, and Amazon SNS immediately delivers the message to subscribers.

## Request Parameters
<a name="API_PublishBatch_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **PublishBatchRequestEntries.member.N**
A list of `PublishBatch` request entries to be sent to the SNS topic.
Type: Array of [PublishBatchRequestEntry](API_PublishBatchRequestEntry.md) objects
Required: Yes

 ** TopicArn **
The Amazon resource name (ARN) of the topic you want to batch publish to.
Type: String
Required: Yes

## Response Elements
<a name="API_PublishBatch_ResponseElements"></a>

The following elements are returned by the service.

 **Failed.member.N**
A list of failed `PublishBatch` responses.
Type: Array of [BatchResultErrorEntry](API_BatchResultErrorEntry.md) objects

 **Successful.member.N**
A list of successful `PublishBatch` responses.
Type: Array of [PublishBatchResultEntry](API_PublishBatchResultEntry.md) objects

## Errors
<a name="API_PublishBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** BatchEntryIdsNotDistinct **
Two or more batch entries in the request have the same `Id`.
HTTP Status Code: 400

 ** BatchRequestTooLong **
The length of all the batch messages put together is more than the limit.
HTTP Status Code: 400

 ** EmptyBatchRequest **
The batch request doesn't contain any entries.
HTTP Status Code: 400

 ** EndpointDisabled **
Exception error indicating endpoint disabled.
 ** message **
Message for endpoint disabled.
HTTP Status Code: 400

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidBatchEntryId **
The `Id` of a batch entry in a batch request doesn't abide by the specification.
HTTP Status Code: 400

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

 ** TooManyEntriesInBatchRequest **
 The batch request contains more entries than permissible (more than 10).
HTTP Status Code: 400

 ** Validation **
Indicates that a parameter in the request is invalid.
HTTP Status Code: 400

## See Also
<a name="API_PublishBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/PublishBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/PublishBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/PublishBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/PublishBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/PublishBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/PublishBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/PublishBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/PublishBatch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/PublishBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/PublishBatch)
