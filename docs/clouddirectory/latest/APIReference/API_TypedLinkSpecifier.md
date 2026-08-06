---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TypedLinkSpecifier.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# TypedLinkSpecifier
<a name="API_TypedLinkSpecifier"></a>

Contains all the information that is used to uniquely identify a typed link. The parameters discussed in this topic are used to uniquely specify the typed link being operated on. The [AttachTypedLink](API_AttachTypedLink.md) API returns a typed link specifier while the [DetachTypedLink](API_DetachTypedLink.md) API accepts one as input. Similarly, the [ListIncomingTypedLinks](API_ListIncomingTypedLinks.md) and [ListOutgoingTypedLinks](API_ListOutgoingTypedLinks.md) API operations provide typed link specifiers as output. You can also construct a typed link specifier from scratch.

## Contents
<a name="API_TypedLinkSpecifier_Contents"></a>

 ** IdentityAttributeValues **   <a name="amazoncds-Type-TypedLinkSpecifier-IdentityAttributeValues"></a>
Identifies the attribute value to update.
Type: Array of [AttributeNameAndValue](API_AttributeNameAndValue.md) objects
Required: Yes

 ** SourceObjectReference **   <a name="amazoncds-Type-TypedLinkSpecifier-SourceObjectReference"></a>
Identifies the source object that the typed link will attach to.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** TargetObjectReference **   <a name="amazoncds-Type-TypedLinkSpecifier-TargetObjectReference"></a>
Identifies the target object that the typed link will attach to.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** TypedLinkFacet **   <a name="amazoncds-Type-TypedLinkSpecifier-TypedLinkFacet"></a>
Identifies the typed link facet that is associated with the typed link.
Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md) object
Required: Yes

## See Also
<a name="API_TypedLinkSpecifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkSpecifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkSpecifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkSpecifier)
