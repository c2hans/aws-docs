---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_Facet.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Facet
<a name="API_Facet"></a>

A structure that contains `Name`, `ARN`, `Attributes`, ` Rules`, and `ObjectTypes`. See [Facets](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_whatarefacets.html) for more information.

## Contents
<a name="API_Facet_Contents"></a>

 ** FacetStyle **   <a name="amazoncds-Type-Facet-FacetStyle"></a>
There are two different styles that you can define on any given facet, `Static` and `Dynamic`. For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.
Type: String
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** Name **   <a name="amazoncds-Type-Facet-Name"></a>
The name of the [Facet](#API_Facet).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** ObjectType **   <a name="amazoncds-Type-Facet-ObjectType"></a>
The object type that is associated with the facet. See [CreateFacet:ObjectType](API_CreateFacet.md#amazoncds-CreateFacet-request-ObjectType) for more details.
Type: String
Valid Values: `NODE | LEAF_NODE | POLICY | INDEX`
Required: No

## See Also
<a name="API_Facet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/Facet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/Facet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/Facet)
