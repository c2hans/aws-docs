---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListObjectChildren.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListObjectChildren
<a name="API_BatchListObjectChildren"></a>

Represents the output of a [ListObjectChildren](API_ListObjectChildren.md) operation.

## Contents
<a name="API_BatchListObjectChildren_Contents"></a>

 ** ObjectReference **   <a name="amazoncds-Type-BatchListObjectChildren-ObjectReference"></a>
Reference of the object for which child objects are being listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** MaxResults **   <a name="amazoncds-Type-BatchListObjectChildren-MaxResults"></a>
Maximum number of items to be retrieved in a single call. This is an approximate number.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListObjectChildren-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListObjectChildren_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectChildren)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectChildren)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectChildren)
