---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html
---

# GetTopicAttributes
<a name="API_GetTopicAttributes"></a>

Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.

## Request Parameters
<a name="API_GetTopicAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TopicArn **
The ARN of the topic whose properties you want to get.
Type: String
Required: Yes

## Response Elements
<a name="API_GetTopicAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
A map of the topic's attributes. Attributes in this map include the following:
+  `DeliveryPolicy` – The JSON serialization of the topic's delivery policy.
+  `DisplayName` – The human-readable name used in the `From` field for notifications to `email` and `email-json` endpoints. For subscription confirmation and unsubscribe confirmation emails, the sender name is always "AWS Notifications" regardless of this attribute.
+  `EffectiveDeliveryPolicy` – The JSON serialization of the effective delivery policy, taking system defaults into account.
+  `Owner` – The AWS account ID of the topic's owner.
+  `Policy` – The JSON serialization of the topic's access control policy.
+  `SignatureVersion` – The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS.
  + By default, `SignatureVersion` is set to **1**. The signature is a Base64-encoded **SHA1withRSA** signature.
  + When you set `SignatureVersion` to **2**. Amazon SNS uses a Base64-encoded **SHA256withRSA** signature.
**Note**
If the API response does not include the `SignatureVersion` attribute, it means that the `SignatureVersion` for the topic has value **1**.
+  `SubscriptionsConfirmed` – The number of confirmed subscriptions for the topic.
+  `SubscriptionsDeleted` – The number of deleted subscriptions for the topic.
+  `SubscriptionsPending` – The number of subscriptions pending confirmation for the topic.
+  `TopicArn` – The topic's ARN.
+  `TracingConfig` – Tracing mode of an Amazon SNS topic. By default `TracingConfig` is set to `PassThrough`, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to `Active`, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.
The following attribute applies only to [server-side-encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html):
+  `KmsMasterKeyId` - The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms). For more examples, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the * AWS Key Management Service API Reference*.
The following attributes apply only to [FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html):
+  `ArchivePolicy` – The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.
+  `BeginningArchiveTime` – The earliest starting point at which a message in the topic’s archive can be replayed from. This point in time is based on the configured message retention period set by the topic’s message archiving policy.
+  `ContentBasedDeduplication` – Enables content-based deduplication for FIFO topics.
  + By default, `ContentBasedDeduplication` is set to `false`. If you create a FIFO topic and this attribute is `false`, you must specify a value for the `MessageDeduplicationId` parameter for the [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) action.
  + When you set `ContentBasedDeduplication` to `true`, Amazon SNS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    (Optional) To override the generated value, you can specify a value for the `MessageDeduplicationId` parameter for the `Publish` action.
+  `FifoTopic` – When this is set to `true`, a FIFO topic is created.
Type: String to string map

## Errors
<a name="API_GetTopicAttributes_Errors"></a>

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

 ** InvalidSecurity **
The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.
HTTP Status Code: 403

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_GetTopicAttributes_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_GetTopicAttributes_Example_1"></a>

This example illustrates one usage of GetTopicAttributes.

#### Sample Request
<a name="API_GetTopicAttributes_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=GetTopicAttributes
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetTopicAttributes_Example_1_Response"></a>

```
<GetTopicAttributesResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <GetTopicAttributesResult>
        <Attributes>
            <entry>
                <key>Owner</key>
                <value>123456789012</value>
            </entry>
            <entry>
                <key>Policy</key>
                <value>{&quot;Version&quot;:&quot;2008-10-17&quot;,&quot;Id&quot;:&quot;us-east-2/698519295917/test__default_policy_ID&quot;,&quot;Statement&quot;:[{&quot;Effect&quot;:&quot;Allow&quot;,&quot;Sid&quot;:&quot;us-east-2/698519295917/test__default_statement_ID&quot;,&quot;Principal&quot;:{&quot;AWS&quot;:&quot;*&quot;},&quot;Action&quot;:[&quot;SNS:GetTopicAttributes&quot;,&quot;SNS:SetTopicAttributes&quot;,&quot;SNS:AddPermission&quot;,&quot;SNS:RemovePermission&quot;,&quot;SNS:DeleteTopic&quot;,&quot;SNS:Subscribe&quot;,&quot;SNS:ListSubscriptionsByTopic&quot;,&quot;SNS:Publish&quot;],&quot;Resource&quot;:&quot;arn:aws:sns:us-east-2:698519295917:test&quot;,&quot;Condition&quot;:{&quot;StringLike&quot;:{&quot;AWS:SourceArn&quot;:&quot;arn:aws:*:*:698519295917:*&quot;}}}]}</value>
            </entry>
            <entry>
                <key>TopicArn</key>
                <value>arn:aws:sns:us-east-2:123456789012:My-Topic</value>
            </entry>
        </Attributes>
    </GetTopicAttributesResult>
    <ResponseMetadata>
        <RequestId>057f074c-33a7-11df-9540-99d0768312d3</RequestId>
    </ResponseMetadata>
</GetTopicAttributesResponse>
```

## See Also
<a name="API_GetTopicAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/GetTopicAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/GetTopicAttributes)
