---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html
---

# ConfirmSubscription
<a name="API_ConfirmSubscription"></a>

Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier `Subscribe` action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the `AuthenticateOnUnsubscribe` flag is set to "true".

## Request Parameters
<a name="API_ConfirmSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AuthenticateOnUnsubscribe **
Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is `true` and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication.
Type: String
Required: No

 ** Token **
Short-lived token sent to an endpoint during the `Subscribe` action.
Type: String
Required: Yes

 ** TopicArn **
The ARN of the topic for which you wish to confirm a subscription.
Type: String
Required: Yes

## Response Elements
<a name="API_ConfirmSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** SubscriptionArn **
The ARN of the created subscription.
Type: String

## Errors
<a name="API_ConfirmSubscription_Errors"></a>

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

 ** SubscriptionLimitExceeded **
Indicates that the customer already owns the maximum allowed number of subscriptions.
HTTP Status Code: 403

## Examples
<a name="API_ConfirmSubscription_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ConfirmSubscription_Example_1"></a>

This example illustrates one usage of ConfirmSubscription.

#### Sample Request
<a name="API_ConfirmSubscription_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=ConfirmSubscription
&TopicArn=arn%3aws%3sns%3us-east-2%3123456789012%3My-Topic
&Token=51b2ff3edb475b7d91550e0ab6edf0c1de2a34e6ebaf6c2262a001bcb7e051c43aa00022ceecce70bd2a67b2042da8d8eb47fef7a4e4e942d23e7fa56146b9ee35da040b4b8af564cc4184a7391c834cb75d75c22981f776ad1ce8805e9bab29da2329985337bb8095627907b46c8577c8440556b6f86582a954758026f41fc62041c4b3f67b0f5921232b5dae5aaca1
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ConfirmSubscription_Example_1_Response"></a>

```
<ConfirmSubscriptionResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ConfirmSubscriptionResult>
        <SubscriptionArn>arn:aws:sns:us-east-2:123456789012:My-Topic:80289ba6-0fd4-4079-afb4-ce8c8260f0ca</SubscriptionArn>
    </ConfirmSubscriptionResult>
    <ResponseMetadata>
        <RequestId>7a50221f-3774-11df-a9b7-05d48da6f042</RequestId>
    </ResponseMetadata>
</ConfirmSubscriptionResponse>
```

## See Also
<a name="API_ConfirmSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ConfirmSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ConfirmSubscription)
