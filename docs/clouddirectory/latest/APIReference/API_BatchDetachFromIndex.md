---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchDetachFromIndex.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchDetachFromIndex
<a name="API_BatchDetachFromIndex"></a>

Detaches the specified object from the specified index inside a [BatchRead](API_BatchRead.md) operation. For more information, see [DetachFromIndex](API_DetachFromIndex.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchDetachFromIndex_Contents"></a>

 ** IndexReference **   <a name="amazoncds-Type-BatchDetachFromIndex-IndexReference"></a>
A reference to the index object.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** TargetReference **   <a name="amazoncds-Type-BatchDetachFromIndex-TargetReference"></a>
A reference to the object being detached from the index.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## See Also
<a name="API_BatchDetachFromIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchDetachFromIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchDetachFromIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchDetachFromIndex)
