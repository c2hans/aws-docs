---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ObjectReference.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ObjectReference
<a name="API_ObjectReference"></a>

The reference that identifies an object.

## Contents
<a name="API_ObjectReference_Contents"></a>

 ** Selector **   <a name="amazoncds-Type-ObjectReference-Selector"></a>
A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see [Access Objects](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html). You can identify an object in one of the following ways:
+  *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes.
+  */some/path* - Identifies the object based on path
+  *\#SomeBatchReference* - Identifies the object in a batch call
Type: String
Required: No

## See Also
<a name="API_ObjectReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ObjectReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ObjectReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ObjectReference)
