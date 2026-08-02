---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchDetachObject.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchDetachObject
<a name="API_BatchDetachObject"></a>

Represents the output of a [DetachObject](API_DetachObject.md) operation.

## Contents
<a name="API_BatchDetachObject_Contents"></a>

 ** LinkName **   <a name="amazoncds-Type-BatchDetachObject-LinkName"></a>
The name of the link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`
Required: Yes

 ** ParentReference **   <a name="amazoncds-Type-BatchDetachObject-ParentReference"></a>
Parent reference from which the object with the specified link name is detached.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** BatchReferenceName **   <a name="amazoncds-Type-BatchDetachObject-BatchReferenceName"></a>
The batch reference name. See [Transaction Support](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html) for more information.
Type: String
Required: No

## See Also
<a name="API_BatchDetachObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchDetachObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchDetachObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchDetachObject)
