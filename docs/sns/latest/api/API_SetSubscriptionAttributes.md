---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html
---

# SetSubscriptionAttributes
<a name="API_SetSubscriptionAttributes"></a>

Allows a subscription owner to set an attribute of the subscription to a new value.

## Request Parameters
<a name="API_SetSubscriptionAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AttributeName **
A map of attributes with their corresponding values.
The following lists the names, descriptions, and values of the special request parameters that this action uses:
+  `DeliveryPolicy` – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
+  `FilterPolicy` – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.
+  `FilterPolicyScope` – This attribute lets you choose the filtering scope by using one of the following string value types:
  +  `MessageAttributes` (default) – The filter is applied on the message attributes.
  +  `MessageBody` – The filter is applied on the message body.
+  `RawMessageDelivery` – When set to `true`, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.
+  `RedrivePolicy` – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.
The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:
+  `SubscriptionRoleArn` – The ARN of the IAM role that has the following:
  + Permission to write to the Firehose delivery stream
  + Amazon SNS listed as a trusted entity

  Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see [Fanout to Firehose delivery streams](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html) in the *Amazon SNS Developer Guide*.
Type: String
Required: Yes

 ** AttributeValue **
The new value for the attribute in JSON format.
Type: String
Required: No

 ** SubscriptionArn **
The ARN of the subscription to modify.
Type: String
Required: Yes

## Errors
<a name="API_SetSubscriptionAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** FilterPolicyLimitExceeded **
Indicates that the number of filter polices in your AWS account exceeds the limit. To add more filter polices, submit an Amazon SNS Limit Increase case in the AWS Support Center.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

 ** ReplayLimitExceeded **
Indicates that the request parameter has exceeded the maximum number of concurrent message replays.
HTTP Status Code: 403

## Examples
<a name="API_SetSubscriptionAttributes_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_SetSubscriptionAttributes_Example_1"></a>

The following example sets the delivery policy to 5 retries.

The JSON format for `AttributeValue` is as follows. For more information on the `DeliveryPolicy` subscription attribute, see [Creating an HTTP/S delivery policy](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html#creating-delivery-policy).

```
{
    "healthyRetryPolicy": {
        "minDelayTarget": <int>,
        "maxDelayTarget": <int>,
        "numRetries": <int>,
        "numMaxDelayRetries": <int>,
        "backoffFunction": "<linear|arithmetic|geometric|exponential>"
    },
    "throttlePolicy": {
        "maxReceivesPerSecond": <int>
    },
    "requestPolicy" : {
        "headerContentType" : "<text/plain | application/json | application/xml>"
    }
}
```

#### Sample Request
<a name="API_SetSubscriptionAttributes_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=SetSubscriptionAttributes
&SubscriptionArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic%3A80289ba6-0fd4-4079-afb4-ce8c8260f0ca
&AttributeName=DeliveryPolicy
&AttributeValue={"healthyRetryPolicy":{"numRetries":5}}
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetSubscriptionAttributes_Example_1_Response"></a>

```
<SetSubscriptionAttributesResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>a8763b99-33a7-11df-a9b7-05d48da6f042</RequestId>
    </ResponseMetadata>
</SetSubscriptionAttributesResponse>
```

## See Also
<a name="API_SetSubscriptionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/SetSubscriptionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/SetSubscriptionAttributes)
