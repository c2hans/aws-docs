---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html
---

# ListSubscriptionsByTopic
<a name="API_ListSubscriptionsByTopic"></a>

Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a `NextToken` is also returned. Use the `NextToken` parameter in a new `ListSubscriptionsByTopic` call to get further results.

This action is throttled at 30 transactions per second (TPS).

## Request Parameters
<a name="API_ListSubscriptionsByTopic_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
Token returned by the previous `ListSubscriptionsByTopic` request.
Type: String
Required: No

 ** TopicArn **
The ARN of the topic for which you wish to find subscriptions.
Type: String
Required: Yes

## Response Elements
<a name="API_ListSubscriptionsByTopic_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
Token to pass along to the next `ListSubscriptionsByTopic` request. This element is returned if there are more subscriptions to retrieve.
Type: String

 **Subscriptions.member.N**
A list of subscriptions.
Type: Array of [Subscription](API_Subscription.md) objects

## Errors
<a name="API_ListSubscriptionsByTopic_Errors"></a>

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
<a name="API_ListSubscriptionsByTopic_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListSubscriptionsByTopic_Example_1"></a>

This example illustrates one usage of ListSubscriptionsByTopic.

#### Sample Request
<a name="API_ListSubscriptionsByTopic_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=ListSubscriptionsByTopic
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListSubscriptionsByTopic_Example_1_Response"></a>

```
<ListSubscriptionsByTopicResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ListSubscriptionsByTopicResult>
        <Subscriptions>
            <member>
                <TopicArn>arn:aws:sns:us-east-2:123456789012:My-Topic</TopicArn>
                <Protocol>email</Protocol>
                <SubscriptionArn>arn:aws:sns:us-east-2:123456789012:My-Topic:80289ba6-0fd4-4079-afb4-ce8c8260f0ca</SubscriptionArn>
                <Owner>123456789012</Owner>
                <Endpoint>example@amazon.com</Endpoint>
            </member>
        </Subscriptions>
    </ListSubscriptionsByTopicResult>
    <ResponseMetadata>
        <RequestId>b9275252-3774-11df-9540-99d0768312d3</RequestId>
    </ResponseMetadata>
</ListSubscriptionsByTopicResponse>
```

## See Also
<a name="API_ListSubscriptionsByTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListSubscriptionsByTopic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListSubscriptionsByTopic)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
