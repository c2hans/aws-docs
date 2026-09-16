---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Remove tags from the specified Amazon SNS topic. For an overview, see [Amazon SNS Tags](https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html) in the *Amazon SNS Developer Guide*.

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **
The ARN of the topic from which to remove tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 **TagKeys.member.N**
The list of tag keys to remove from the specified topic.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Errors
<a name="API_UntagResource_Errors"></a>

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
<a name="API_UntagResource_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_UntagResource_Example_1"></a>

This example illustrates one usage of UntagResource.

#### Sample Request
<a name="API_UntagResource_Example_1_Request"></a>

```
http://sns.us-east-2.amazonaws.com/?Action=UntagResource
&ResourceArn=arn%3Aaws%3Asns%3Aus-east-1%3A123456789012%3Atagging
&TagKeys.TagKey.1=tagKey
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_UntagResource_Example_1_Response"></a>

```
<UntagResourceResponse>
    <UntagResourceResult/>
    <ResponseMetadata>
        <RequestId>1a34f567-8bc9-01de-f234-g567h8908i12</RequestId>
    </ResponseMetadata>
</UntagResourceResponse>
```

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/UntagResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/UntagResource)
