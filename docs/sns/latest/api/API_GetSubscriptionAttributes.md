---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html
---

# GetSubscriptionAttributes
<a name="API_GetSubscriptionAttributes"></a>

Returns all of the properties of a subscription.

## Request Parameters
<a name="API_GetSubscriptionAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SubscriptionArn **
The ARN of the subscription whose properties you want to get.
Type: String
Required: Yes

## Response Elements
<a name="API_GetSubscriptionAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
A map of the subscription's attributes. Attributes in this map include the following:
+  `ConfirmationWasAuthenticated` – `true` if the subscription confirmation request was authenticated.
+  `DeliveryPolicy` – The JSON serialization of the subscription's delivery policy.
+  `EffectiveDeliveryPolicy` – The JSON serialization of the effective delivery policy that takes into account the topic delivery policy and account system defaults.
+  `FilterPolicy` – The filter policy JSON that is assigned to the subscription. For more information, see [Amazon SNS Message Filtering](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html) in the *Amazon SNS Developer Guide*.
+  `FilterPolicyScope` – This attribute lets you choose the filtering scope by using one of the following string value types:
  +  `MessageAttributes` (default) – The filter is applied on the message attributes.
  +  `MessageBody` – The filter is applied on the message body.
+  `Owner` – The AWS account ID of the subscription's owner.
+  `PendingConfirmation` – `true` if the subscription hasn't been confirmed. To confirm a pending subscription, call the `ConfirmSubscription` action with a confirmation token.
+  `RawMessageDelivery` – `true` if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints.
+  `RedrivePolicy` – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.
+  `SubscriptionArn` – The subscription's ARN.
+  `TopicArn` – The topic ARN that the subscription is associated with.
The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:
+  `SubscriptionRoleArn` – The ARN of the IAM role that has the following:
  + Permission to write to the Firehose delivery stream
  + Amazon SNS listed as a trusted entity

  Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see [Fanout to Firehose delivery streams](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html) in the *Amazon SNS Developer Guide*.
Type: String to string map

## Errors
<a name="API_GetSubscriptionAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
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

## Examples
<a name="API_GetSubscriptionAttributes_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_GetSubscriptionAttributes_Example_1"></a>

This example illustrates one usage of GetSubscriptionAttributes.

#### Sample Request
<a name="API_GetSubscriptionAttributes_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=GetSubscriptionAttributes
&SubscriptionArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic%3A80289ba6-0fd4-4079-afb4-ce8c8260f0ca
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetSubscriptionAttributes_Example_1_Response"></a>

```
<GetSubscriptionAttributesResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <GetSubscriptionAttributesResult>
        <Attributes>
            <entry>
                <key>Owner</key>
                <value>123456789012</value>
            </entry>
            <entry>
                <key>DeliveryPolicy</key>
                <value>{&quot;healthyRetryPolicy&quot;:{&quot;numRetries&quot;:10}}</value>
            </entry>
            <entry>
                <key>SubscriptionArn</key>
                <value>arn:aws:sns:us-east-2:123456789012:My-Topic:80289ba6-0fd4-4079-afb4-ce8c8260f0ca</value>
            </entry>
        </Attributes>
    </GetSubscriptionAttributesResult>
    <ResponseMetadata>
        <RequestId>057f074c-33a7-11df-9540-99d0768312d3</RequestId>
    </ResponseMetadata>
</GetSubscriptionAttributesResponse>
```

## See Also
<a name="API_GetSubscriptionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/GetSubscriptionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/GetSubscriptionAttributes)
