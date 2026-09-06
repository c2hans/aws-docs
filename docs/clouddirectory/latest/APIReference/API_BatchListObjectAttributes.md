---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListObjectAttributes.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListObjectAttributes
<a name="API_BatchListObjectAttributes"></a>

Represents the output of a [ListObjectAttributes](API_ListObjectAttributes.md) operation.

## Contents
<a name="API_BatchListObjectAttributes_Contents"></a>

 ** ObjectReference **   <a name="amazoncds-Type-BatchListObjectAttributes-ObjectReference"></a>
Reference of the object whose attributes need to be listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** FacetFilter **   <a name="amazoncds-Type-BatchListObjectAttributes-FacetFilter"></a>
Used to filter the list of object attributes that are associated with a certain facet.
Type: [SchemaFacet](API_SchemaFacet.md) object
Required: No

 ** MaxResults **   <a name="amazoncds-Type-BatchListObjectAttributes-MaxResults"></a>
The maximum number of items to be retrieved in a single call. This is an approximate number.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListObjectAttributes-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListObjectAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectAttributes)
