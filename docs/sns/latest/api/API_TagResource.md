---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Add tags to the specified Amazon SNS topic. For an overview, see [Amazon SNS Tags](https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html) in the *Amazon SNS Developer Guide*.

When you use topic tags, keep the following guidelines in mind:
+ Adding more than 50 tags to a topic isn't recommended.
+ Tags don't have any semantic meaning. Amazon SNS interprets tags as character strings.
+ Tags are case-sensitive.
+ A new tag with a key identical to that of an existing tag overwrites the existing tag.
+ Tagging actions are limited to 10 TPS per AWS account, per AWS Region. If your application requires a higher throughput, file a [technical support request](https://console.aws.amazon.com/support/home#/case/create?issueType=technical).

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **
The ARN of the topic to which to add tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 **Tags.member.N**
The tags to be added to the specified topic. A tag consists of a required key and an optional value.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** ConcurrentAccess **
Can't perform multiple operations on a tag simultaneously. Perform the operations sequentially.
HTTP Status Code: 400

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** ResourceNotFound **
Can’t perform the action on the specified resource. Make sure that the resource exists.
HTTP Status Code: 404

 ** StaleTag **
A tag has been added to a resource with the same ARN as a deleted resource. Wait a short while and then retry the operation.
HTTP Status Code: 400

 ** TagLimitExceeded **
Can't add more than 50 tags to a topic.
HTTP Status Code: 400

 ** TagPolicy **
The request doesn't comply with the IAM tag policy. Correct your request and then retry it.
HTTP Status Code: 400

## Examples
<a name="API_TagResource_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_TagResource_Example_1"></a>

This example illustrates one usage of TagResource.

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
http://sns.us-west-2.amazonaws.com/?&Action=TagResource
&ResourceArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Atagging
&Tags.Tag.1.Key=tagKey
&Tags.Tag.1.Value=tagValue
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
<TagResourceResponse>
    <TagResourceResult/>
    <ResponseMetadata>
        <RequestId>a1b2c3de-fg45-67h8-i9j0-k1lm234n5678</RequestId>
    </ResponseMetadata>
</TagResourceResponse>
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/TagResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/TagResource)
