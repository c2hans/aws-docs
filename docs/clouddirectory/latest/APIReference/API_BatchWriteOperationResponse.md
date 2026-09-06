---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchWriteOperationResponse.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchWriteOperationResponse
<a name="API_BatchWriteOperationResponse"></a>

Represents the output of a `BatchWrite` response operation.

## Contents
<a name="API_BatchWriteOperationResponse_Contents"></a>

 ** AddFacetToObject **   <a name="amazoncds-Type-BatchWriteOperationResponse-AddFacetToObject"></a>
The result of an add facet to object batch operation.
Type: [BatchAddFacetToObjectResponse](API_BatchAddFacetToObjectResponse.md) object
Required: No

 ** AttachObject **   <a name="amazoncds-Type-BatchWriteOperationResponse-AttachObject"></a>
Attaches an object to a [Directory](API_Directory.md).
Type: [BatchAttachObjectResponse](API_BatchAttachObjectResponse.md) object
Required: No

 ** AttachPolicy **   <a name="amazoncds-Type-BatchWriteOperationResponse-AttachPolicy"></a>
Attaches a policy object to a regular object. An object can have a limited number of attached policies.
Type: [BatchAttachPolicyResponse](API_BatchAttachPolicyResponse.md) object
Required: No

 ** AttachToIndex **   <a name="amazoncds-Type-BatchWriteOperationResponse-AttachToIndex"></a>
Attaches the specified object to the specified index.
Type: [BatchAttachToIndexResponse](API_BatchAttachToIndexResponse.md) object
Required: No

 ** AttachTypedLink **   <a name="amazoncds-Type-BatchWriteOperationResponse-AttachTypedLink"></a>
Attaches a typed link to a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchAttachTypedLinkResponse](API_BatchAttachTypedLinkResponse.md) object
Required: No

 ** CreateIndex **   <a name="amazoncds-Type-BatchWriteOperationResponse-CreateIndex"></a>
Creates an index object. See [Indexing and search](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm) for more information.
Type: [BatchCreateIndexResponse](API_BatchCreateIndexResponse.md) object
Required: No

 ** CreateObject **   <a name="amazoncds-Type-BatchWriteOperationResponse-CreateObject"></a>
Creates an object in a [Directory](API_Directory.md).
Type: [BatchCreateObjectResponse](API_BatchCreateObjectResponse.md) object
Required: No

 ** DeleteObject **   <a name="amazoncds-Type-BatchWriteOperationResponse-DeleteObject"></a>
Deletes an object in a [Directory](API_Directory.md).
Type: [BatchDeleteObjectResponse](API_BatchDeleteObjectResponse.md) object
Required: No

 ** DetachFromIndex **   <a name="amazoncds-Type-BatchWriteOperationResponse-DetachFromIndex"></a>
Detaches the specified object from the specified index.
Type: [BatchDetachFromIndexResponse](API_BatchDetachFromIndexResponse.md) object
Required: No

 ** DetachObject **   <a name="amazoncds-Type-BatchWriteOperationResponse-DetachObject"></a>
Detaches an object from a [Directory](API_Directory.md).
Type: [BatchDetachObjectResponse](API_BatchDetachObjectResponse.md) object
Required: No

 ** DetachPolicy **   <a name="amazoncds-Type-BatchWriteOperationResponse-DetachPolicy"></a>
Detaches a policy from a [Directory](API_Directory.md).
Type: [BatchDetachPolicyResponse](API_BatchDetachPolicyResponse.md) object
Required: No

 ** DetachTypedLink **   <a name="amazoncds-Type-BatchWriteOperationResponse-DetachTypedLink"></a>
Detaches a typed link from a specified source and target object. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchDetachTypedLinkResponse](API_BatchDetachTypedLinkResponse.md) object
Required: No

 ** RemoveFacetFromObject **   <a name="amazoncds-Type-BatchWriteOperationResponse-RemoveFacetFromObject"></a>
The result of a batch remove facet from object operation.
Type: [BatchRemoveFacetFromObjectResponse](API_BatchRemoveFacetFromObjectResponse.md) object
Required: No

 ** UpdateLinkAttributes **   <a name="amazoncds-Type-BatchWriteOperationResponse-UpdateLinkAttributes"></a>
Represents the output of a `BatchWrite` response operation.
Type: [BatchUpdateLinkAttributesResponse](API_BatchUpdateLinkAttributesResponse.md) object
Required: No

 ** UpdateObjectAttributes **   <a name="amazoncds-Type-BatchWriteOperationResponse-UpdateObjectAttributes"></a>
Updates a given object’s attributes.
Type: [BatchUpdateObjectAttributesResponse](API_BatchUpdateObjectAttributesResponse.md) object
Required: No

## See Also
<a name="API_BatchWriteOperationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWriteOperationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWriteOperationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWriteOperationResponse)
