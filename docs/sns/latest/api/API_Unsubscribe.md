---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html
---

# Unsubscribe
<a name="API_Unsubscribe"></a>

Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the `Unsubscribe` call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the `Unsubscribe` request was unintended.

This action is throttled at 100 transactions per second (TPS).

## Request Parameters
<a name="API_Unsubscribe_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SubscriptionArn **
The ARN of the subscription to be deleted.
Type: String
Required: Yes

## Errors
<a name="API_Unsubscribe_Errors"></a>

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
<a name="API_Unsubscribe_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_Unsubscribe_Example_1"></a>

This example illustrates one usage of Unsubscribe.

#### Sample Request
<a name="API_Unsubscribe_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe
&SubscriptionArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic%3A80289ba6-0fd4-4079-afb4-ce8c8260f0ca
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_Unsubscribe_Example_1_Response"></a>

```
<UnsubscribeResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>18e0ac39-3776-11df-84c0-b93cc1666b84</RequestId>
    </ResponseMetadata>
</UnsubscribeResponse>
```

## See Also
<a name="API_Unsubscribe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/Unsubscribe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/Unsubscribe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
