---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchAttachObject.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchAttachObject
<a name="API_BatchAttachObject"></a>

Represents the output of an [AttachObject](API_AttachObject.md) operation.

## Contents
<a name="API_BatchAttachObject_Contents"></a>

 ** ChildReference **   <a name="amazoncds-Type-BatchAttachObject-ChildReference"></a>
The child object reference that is to be attached to the object.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** LinkName **   <a name="amazoncds-Type-BatchAttachObject-LinkName"></a>
The name of the link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`
Required: Yes

 ** ParentReference **   <a name="amazoncds-Type-BatchAttachObject-ParentReference"></a>
The parent object reference.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

## See Also
<a name="API_BatchAttachObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachObject)
