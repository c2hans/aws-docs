---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchWriteOperation.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchWriteOperation
<a name="API_BatchWriteOperation"></a>

Represents the output of a `BatchWrite` operation.

## Contents
<a name="API_BatchWriteOperation_Contents"></a>

 ** AddFacetToObject **   <a name="amazoncds-Type-BatchWriteOperation-AddFacetToObject"></a>
A batch operation that adds a facet to an object.
Type: [BatchAddFacetToObject](API_BatchAddFacetToObject.md) object
Required: No

 ** AttachObject **   <a name="amazoncds-Type-BatchWriteOperation-AttachObject"></a>
Attaches an object to a [Directory](API_Directory.md).
Type: [BatchAttachObject](API_BatchAttachObject.md) object
Required: No

 ** AttachPolicy **   <a name="amazoncds-Type-BatchWriteOperation-AttachPolicy"></a>
Attaches a policy object to a regular object. An object can have a limited number of attached policies.
Type: [BatchAttachPolicy](API_BatchAttachPolicy.md) object
Required: No

 ** AttachToIndex **   <a name="amazoncds-Type-BatchWriteOperation-AttachToIndex"></a>
Attaches the specified object to the specified index.
Type: [BatchAttachToIndex](API_BatchAttachToIndex.md) object
Required: No

 ** AttachTypedLink **   <a name="amazoncds-Type-BatchWriteOperation-AttachTypedLink"></a>
Attaches a typed link to a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchAttachTypedLink](API_BatchAttachTypedLink.md) object
Required: No

 ** CreateIndex **   <a name="amazoncds-Type-BatchWriteOperation-CreateIndex"></a>
Creates an index object. See [Indexing and search](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm) for more information.
Type: [BatchCreateIndex](API_BatchCreateIndex.md) object
Required: No

 ** CreateObject **   <a name="amazoncds-Type-BatchWriteOperation-CreateObject"></a>
Creates an object.
Type: [BatchCreateObject](API_BatchCreateObject.md) object
Required: No

 ** DeleteObject **   <a name="amazoncds-Type-BatchWriteOperation-DeleteObject"></a>
Deletes an object in a [Directory](API_Directory.md).
Type: [BatchDeleteObject](API_BatchDeleteObject.md) object
Required: No

 ** DetachFromIndex **   <a name="amazoncds-Type-BatchWriteOperation-DetachFromIndex"></a>
Detaches the specified object from the specified index.
Type: [BatchDetachFromIndex](API_BatchDetachFromIndex.md) object
Required: No

 ** DetachObject **   <a name="amazoncds-Type-BatchWriteOperation-DetachObject"></a>
Detaches an object from a [Directory](API_Directory.md).
Type: [BatchDetachObject](API_BatchDetachObject.md) object
Required: No

 ** DetachPolicy **   <a name="amazoncds-Type-BatchWriteOperation-DetachPolicy"></a>
Detaches a policy from a [Directory](API_Directory.md).
Type: [BatchDetachPolicy](API_BatchDetachPolicy.md) object
Required: No

 ** DetachTypedLink **   <a name="amazoncds-Type-BatchWriteOperation-DetachTypedLink"></a>
Detaches a typed link from a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchDetachTypedLink](API_BatchDetachTypedLink.md) object
Required: No

 ** RemoveFacetFromObject **   <a name="amazoncds-Type-BatchWriteOperation-RemoveFacetFromObject"></a>
A batch operation that removes a facet from an object.
Type: [BatchRemoveFacetFromObject](API_BatchRemoveFacetFromObject.md) object
Required: No

 ** UpdateLinkAttributes **   <a name="amazoncds-Type-BatchWriteOperation-UpdateLinkAttributes"></a>
Updates a given object's attributes.
Type: [BatchUpdateLinkAttributes](API_BatchUpdateLinkAttributes.md) object
Required: No

 ** UpdateObjectAttributes **   <a name="amazoncds-Type-BatchWriteOperation-UpdateObjectAttributes"></a>
Updates a given object's attributes.
Type: [BatchUpdateObjectAttributes](API_BatchUpdateObjectAttributes.md) object
Required: No

## See Also
<a name="API_BatchWriteOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWriteOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWriteOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWriteOperation)
