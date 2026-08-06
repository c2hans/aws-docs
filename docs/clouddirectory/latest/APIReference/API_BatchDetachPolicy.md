---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchDetachPolicy.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchDetachPolicy
<a name="API_BatchDetachPolicy"></a>

Detaches the specified policy from the specified directory inside a [BatchWrite](API_BatchWrite.md) operation. For more information, see [DetachPolicy](API_DetachPolicy.md) and [BatchWrite:Operations](API_BatchWrite.md#amazoncds-BatchWrite-request-Operations).

## Contents
<a name="API_BatchDetachPolicy_Contents"></a>

 ** ObjectReference **   <a name="amazoncds-Type-BatchDetachPolicy-ObjectReference"></a>
Reference that identifies the object whose policy object will be detached.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** PolicyReference **   <a name="amazoncds-Type-BatchDetachPolicy-PolicyReference"></a>
Reference that identifies the policy object.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## See Also
<a name="API_BatchDetachPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchDetachPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchDetachPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchDetachPolicy)
