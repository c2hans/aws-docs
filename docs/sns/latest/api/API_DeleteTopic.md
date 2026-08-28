---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html
---

# DeleteTopic
<a name="API_DeleteTopic"></a>

Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.

## Request Parameters
<a name="API_DeleteTopic_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TopicArn **
The ARN of the topic you want to delete.
Type: String
Required: Yes

## Errors
<a name="API_DeleteTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** ConcurrentAccess **
Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.
HTTP Status Code: 400

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** InvalidState **
Indicates that the specified state is not a valid state for an event source.
HTTP Status Code: 400

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

 ** StaleTag **
A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.
HTTP Status Code: 400

 ** TagPolicy **
The request doesn't comply with the IAM tag policy. Correct your request and then retry it.
HTTP Status Code: 400

## Examples
<a name="API_DeleteTopic_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_DeleteTopic_Example_1"></a>

This example illustrates one usage of DeleteTopic.

#### Sample Request
<a name="API_DeleteTopic_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=DeleteTopic
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteTopic_Example_1_Response"></a>

```
<DeleteTopicResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>f3aa9ac9-3c3d-11df-8235-9dab105e9c32</RequestId>
    </ResponseMetadata>
</DeleteTopicResponse>
```

## See Also
<a name="API_DeleteTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/DeleteTopic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/DeleteTopic)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
