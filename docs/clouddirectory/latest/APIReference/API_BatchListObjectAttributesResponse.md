---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListObjectAttributesResponse.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListObjectAttributesResponse
<a name="API_BatchListObjectAttributesResponse"></a>

Represents the output of a [ListObjectAttributes](API_ListObjectAttributes.md) response operation.

## Contents
<a name="API_BatchListObjectAttributesResponse_Contents"></a>

 ** Attributes **   <a name="amazoncds-Type-BatchListObjectAttributesResponse-Attributes"></a>
The attributes map that is associated with the object. `AttributeArn` is the key; attribute value is the value.
Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md) objects
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListObjectAttributesResponse-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListObjectAttributesResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectAttributesResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectAttributesResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectAttributesResponse)
