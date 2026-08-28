---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchReadSuccessfulResponse.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchReadSuccessfulResponse
<a name="API_BatchReadSuccessfulResponse"></a>

Represents the output of a `BatchRead` success response operation.

## Contents
<a name="API_BatchReadSuccessfulResponse_Contents"></a>

 ** GetLinkAttributes **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-GetLinkAttributes"></a>
The list of attributes to retrieve from the typed link.
Type: [BatchGetLinkAttributesResponse](API_BatchGetLinkAttributesResponse.md) object
Required: No

 ** GetObjectAttributes **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-GetObjectAttributes"></a>
Retrieves attributes within a facet that are associated with an object.
Type: [BatchGetObjectAttributesResponse](API_BatchGetObjectAttributesResponse.md) object
Required: No

 ** GetObjectInformation **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-GetObjectInformation"></a>
Retrieves metadata about an object.
Type: [BatchGetObjectInformationResponse](API_BatchGetObjectInformationResponse.md) object
Required: No

 ** ListAttachedIndices **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListAttachedIndices"></a>
Lists indices attached to an object.
Type: [BatchListAttachedIndicesResponse](API_BatchListAttachedIndicesResponse.md) object
Required: No

 ** ListIncomingTypedLinks **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListIncomingTypedLinks"></a>
Returns a paginated list of all the incoming [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchListIncomingTypedLinksResponse](API_BatchListIncomingTypedLinksResponse.md) object
Required: No

 ** ListIndex **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListIndex"></a>
Lists objects attached to the specified index.
Type: [BatchListIndexResponse](API_BatchListIndexResponse.md) object
Required: No

 ** ListObjectAttributes **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListObjectAttributes"></a>
Lists all attributes that are associated with an object.
Type: [BatchListObjectAttributesResponse](API_BatchListObjectAttributesResponse.md) object
Required: No

 ** ListObjectChildren **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListObjectChildren"></a>
Returns a paginated list of child objects that are associated with a given object.
Type: [BatchListObjectChildrenResponse](API_BatchListObjectChildrenResponse.md) object
Required: No

 ** ListObjectParentPaths **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListObjectParentPaths"></a>
Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see [Directory Structure](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html).
Type: [BatchListObjectParentPathsResponse](API_BatchListObjectParentPathsResponse.md) object
Required: No

 ** ListObjectParents **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListObjectParents"></a>
The list of parent objects to retrieve.
Type: [BatchListObjectParentsResponse](API_BatchListObjectParentsResponse.md) object
Required: No

 ** ListObjectPolicies **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListObjectPolicies"></a>
Returns policies attached to an object in pagination fashion.
Type: [BatchListObjectPoliciesResponse](API_BatchListObjectPoliciesResponse.md) object
Required: No

 ** ListOutgoingTypedLinks **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListOutgoingTypedLinks"></a>
Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see [Typed Links](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink).
Type: [BatchListOutgoingTypedLinksResponse](API_BatchListOutgoingTypedLinksResponse.md) object
Required: No

 ** ListPolicyAttachments **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-ListPolicyAttachments"></a>
Returns all of the `ObjectIdentifiers` to which a given policy is attached.
Type: [BatchListPolicyAttachmentsResponse](API_BatchListPolicyAttachmentsResponse.md) object
Required: No

 ** LookupPolicy **   <a name="amazoncds-Type-BatchReadSuccessfulResponse-LookupPolicy"></a>
Lists all policies from the root of the [Directory](API_Directory.md) to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don't have the policies attached, it returns the `ObjectIdentifier` for such objects. If policies are present, it returns `ObjectIdentifier`, `policyId`, and `policyType`. Paths that don't lead to the root from the target object are ignored. For more information, see [Policies](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies).
Type: [BatchLookupPolicyResponse](API_BatchLookupPolicyResponse.md) object
Required: No

## See Also
<a name="API_BatchReadSuccessfulResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadSuccessfulResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadSuccessfulResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadSuccessfulResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
