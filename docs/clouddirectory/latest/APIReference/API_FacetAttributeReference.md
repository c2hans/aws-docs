---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_FacetAttributeReference.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# FacetAttributeReference
<a name="API_FacetAttributeReference"></a>

The facet attribute reference that specifies the attribute definition that contains the attribute facet name and attribute name.

## Contents
<a name="API_FacetAttributeReference_Contents"></a>

 ** TargetAttributeName **   <a name="amazoncds-Type-FacetAttributeReference-TargetAttributeName"></a>
The target attribute name that is associated with the facet reference. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** TargetFacetName **   <a name="amazoncds-Type-FacetAttributeReference-TargetFacetName"></a>
The target facet name that is associated with the facet reference. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: Yes

## See Also
<a name="API_FacetAttributeReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttributeReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttributeReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttributeReference)
