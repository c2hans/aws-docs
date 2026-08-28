---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

List all tags added to the specified Amazon SNS topic. For an overview, see [Amazon SNS Tags](https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html) in the *Amazon Simple Notification Service Developer Guide*.

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **
The ARN of the topic for which to list tags.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

The following element is returned by the service.

 **Tags.member.N**
The tags associated with the specified topic.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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

 ** TagPolicy **
The request doesn't comply with the IAM tag policy. Correct your request and then retry it.
HTTP Status Code: 400

## Examples
<a name="API_ListTagsForResource_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

#### Sample Request
<a name="API_ListTagsForResource_Example_1_Request"></a>

```
http://sns.us-west-2.amazonaws.com/&Action=ListTagsForResource
&ResourceArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Atagging
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListTagsForResource_Example_1_Response"></a>

```
<ListTagsForResourceResponse>
    <ListTagsForResourceResult>
        <Tags>
            <member>
                <Value>tagValue</Value>
                <Key>tagKey</Key>
            </member>
        </Tags>
    </ListTagsForResourceResult>
    <ResponseMetadata>
        <RequestId>123456a7-b8c9-01de-fg2h-3456i7j890k1</RequestId>
    </ResponseMetadata>
</ListTagsForResourceResponse>
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListTagsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
