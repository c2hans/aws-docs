---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_FacetAttributeReference.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
