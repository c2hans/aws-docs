---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TypedLinkFacet.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# TypedLinkFacet
<a name="API_TypedLinkFacet"></a>

Defines the typed links structure and its attributes. To create a typed link facet, use the [CreateTypedLinkFacet](API_CreateTypedLinkFacet.md) API.

## Contents
<a name="API_TypedLinkFacet_Contents"></a>

 ** Attributes **   <a name="amazoncds-Type-TypedLinkFacet-Attributes"></a>
A set of key-value pairs associated with the typed link. Typed link attributes are used when you have data values that are related to the link itself, and not to one of the two objects being linked. Identity attributes also serve to distinguish the link from others of the same type between the same objects.
Type: Array of [TypedLinkAttributeDefinition](API_TypedLinkAttributeDefinition.md) objects
Required: Yes

 ** IdentityAttributeOrder **   <a name="amazoncds-Type-TypedLinkFacet-IdentityAttributeOrder"></a>
The set of attributes that distinguish links made from this facet from each other, in the order of significance. Listing typed links can filter on the values of these attributes. See [ListOutgoingTypedLinks](API_ListOutgoingTypedLinks.md) and [ListIncomingTypedLinks](API_ListIncomingTypedLinks.md) for details.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** Name **   <a name="amazoncds-Type-TypedLinkFacet-Name"></a>
The unique name of the typed link facet.
Type: String
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## See Also
<a name="API_TypedLinkFacet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkFacet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkFacet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkFacet)
