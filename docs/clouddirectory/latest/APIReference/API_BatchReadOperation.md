---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchReadOperation.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchReadOperation
<a name="API_BatchReadOperation"></a>

Represents the output of a `BatchRead` operation.

## Contents
<a name="API_BatchReadOperation_Contents"></a>

 ** GetLinkAttributes **   <a name="amazoncds-Type-BatchReadOperation-GetLinkAttributes"></a>
Retrieves attributes that are associated with a typed link.
Type: [BatchGetLinkAttributes](API_BatchGetLinkAttributes.md) object
Required: No

 ** GetObjectAttributes **   <a name="amazoncds-Type-BatchReadOperation-GetObjectAttributes"></a>
Retrieves attributes within a facet that are associated with an object.
Type: [BatchGetObjectAttributes](API_BatchGetObjectAttributes.md) object
Required: No

 ** GetObjectInformation **   <a name="amazoncds-Type-BatchReadOperation-GetObjectInformation"></a>
Retrieves metadata about an object.
Type: [BatchGetObjectInformation](API_BatchGetObjectInformation.md) object
Required: No

 ** ListAttachedIndices **   <a name="amazoncds-Type-BatchReadOperation-ListAttachedIndices"></a>
Lists indices attached to an object.
Type: [BatchListAttachedIndices](API_BatchListAttachedIndices.md) object
Required: No

 ** ListIncomingTypedLinks **   <a name="amazoncds-Type-BatchReadOperation-ListIncomingTypedLinks"></a>
Returns a paginated list of all the incoming [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchListIncomingTypedLinks](API_BatchListIncomingTypedLinks.md) object
Required: No

 ** ListIndex **   <a name="amazoncds-Type-BatchReadOperation-ListIndex"></a>
Lists objects attached to the specified index.
Type: [BatchListIndex](API_BatchListIndex.md) object
Required: No

 ** ListObjectAttributes **   <a name="amazoncds-Type-BatchReadOperation-ListObjectAttributes"></a>
Lists all attributes that are associated with an object.
Type: [BatchListObjectAttributes](API_BatchListObjectAttributes.md) object
Required: No

 ** ListObjectChildren **   <a name="amazoncds-Type-BatchReadOperation-ListObjectChildren"></a>
Returns a paginated list of child objects that are associated with a given object.
Type: [BatchListObjectChildren](API_BatchListObjectChildren.md) object
Required: No

 ** ListObjectParentPaths **   <a name="amazoncds-Type-BatchReadOperation-ListObjectParentPaths"></a>
Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see [Directory Structure](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html).
Type: [BatchListObjectParentPaths](API_BatchListObjectParentPaths.md) object
Required: No

 ** ListObjectParents **   <a name="amazoncds-Type-BatchReadOperation-ListObjectParents"></a>
Lists parent objects that are associated with a given object in pagination fashion.
Type: [BatchListObjectParents](API_BatchListObjectParents.md) object
Required: No

 ** ListObjectPolicies **   <a name="amazoncds-Type-BatchReadOperation-ListObjectPolicies"></a>
Returns policies attached to an object in pagination fashion.
Type: [BatchListObjectPolicies](API_BatchListObjectPolicies.md) object
Required: No

 ** ListOutgoingTypedLinks **   <a name="amazoncds-Type-BatchReadOperation-ListOutgoingTypedLinks"></a>
Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchListOutgoingTypedLinks](API_BatchListOutgoingTypedLinks.md) object
Required: No

 ** ListPolicyAttachments **   <a name="amazoncds-Type-BatchReadOperation-ListPolicyAttachments"></a>
Returns all of the `ObjectIdentifiers` to which a given policy is attached.
Type: [BatchListPolicyAttachments](API_BatchListPolicyAttachments.md) object
Required: No

 ** LookupPolicy **   <a name="amazoncds-Type-BatchReadOperation-LookupPolicy"></a>
Lists all policies from the root of the [Directory](API_Directory.md) to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don't have the policies attached, it returns the `ObjectIdentifier` for such objects. If policies are present, it returns `ObjectIdentifier`, `policyId`, and `policyType`. Paths that don't lead to the root from the target object are ignored. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies).
Type: [BatchLookupPolicy](API_BatchLookupPolicy.md) object
Required: No

## See Also
<a name="API_BatchReadOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadOperation)
