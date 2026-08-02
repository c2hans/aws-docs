---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchCreateIndex.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchCreateIndex
<a name="API_BatchCreateIndex"></a>

Creates an index object inside of a [BatchRead](API_BatchRead.md) operation. For more information, see [CreateIndex](API_CreateIndex.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchCreateIndex_Contents"></a>

 ** IsUnique **   <a name="amazoncds-Type-BatchCreateIndex-IsUnique"></a>
Indicates whether the attribute that is being indexed has unique values or not.
Type: Boolean
Required: Yes

 ** OrderedIndexedAttributeList **   <a name="amazoncds-Type-BatchCreateIndex-OrderedIndexedAttributeList"></a>
Specifies the attributes that should be indexed on. Currently only a single attribute is supported.
Type: Array of [AttributeKey](API_AttributeKey.md) objects
Required: Yes

 ** BatchReferenceName **   <a name="amazoncds-Type-BatchCreateIndex-BatchReferenceName"></a>
The batch reference name. See [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html) for more information.
Type: String
Required: No

 ** LinkName **   <a name="amazoncds-Type-BatchCreateIndex-LinkName"></a>
The name of the link between the parent object and the index object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`
Required: No

 ** ParentReference **   <a name="amazoncds-Type-BatchCreateIndex-ParentReference"></a>
A reference to the parent object that contains the index object.
Type: [ObjectReference](API_ObjectReference.md) object
Required: No

## See Also
<a name="API_BatchCreateIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchCreateIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchCreateIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchCreateIndex)
