---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html
---

# ListSubscriptions
<a name="API_ListSubscriptions"></a>

Returns a list of the requester's subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a `NextToken` is also returned. Use the `NextToken` parameter in a new `ListSubscriptions` call to get further results.

This action is throttled at 30 transactions per second (TPS).

## Request Parameters
<a name="API_ListSubscriptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
Token returned by the previous `ListSubscriptions` request.
Type: String
Required: No

## Response Elements
<a name="API_ListSubscriptions_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
Token to pass along to the next `ListSubscriptions` request. This element is returned if there are more subscriptions to retrieve.
Type: String

 **Subscriptions.member.N**
A list of subscriptions.
Type: Array of [Subscription](API_Subscription.md) objects

## Errors
<a name="API_ListSubscriptions_Errors"></a>

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

## Examples
<a name="API_ListSubscriptions_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListSubscriptions_Example_1"></a>

This example illustrates one usage of ListSubscriptions.

#### Sample Request
<a name="API_ListSubscriptions_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=ListSubscriptions
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListSubscriptions_Example_1_Response"></a>

```
<ListSubscriptionsResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ListSubscriptionsResult>
        <Subscriptions>
            <member>
                <TopicArn>arn:aws:sns:us-east-2:698519295917:My-Topic</TopicArn>
                <Protocol>email</Protocol>
                <SubscriptionArn>arn:aws:sns:us-east-2:123456789012:My-Topic:80289ba6-0fd4-4079-afb4-ce8c8260f0ca</SubscriptionArn>
                <Owner>123456789012</Owner>
                <Endpoint>example@amazon.com</Endpoint>
            </member>
        </Subscriptions>
    </ListSubscriptionsResult>
    <ResponseMetadata>
        <RequestId>384ac68d-3775-11df-8963-01868b7c937a</RequestId>
    </ResponseMetadata>
</ListSubscriptionsResponse>
```

## See Also
<a name="API_ListSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListSubscriptions)
