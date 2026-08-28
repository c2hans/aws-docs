---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_FacetAttribute.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# FacetAttribute
<a name="API_FacetAttribute"></a>

An attribute that is associated with the [Facet](API_Facet.md).

## Contents
<a name="API_FacetAttribute_Contents"></a>

 ** Name **   <a name="amazoncds-Type-FacetAttribute-Name"></a>
The name of the facet attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** AttributeDefinition **   <a name="amazoncds-Type-FacetAttribute-AttributeDefinition"></a>
A facet attribute consists of either a definition or a reference. This structure contains the attribute definition. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.
Type: [FacetAttributeDefinition](API_FacetAttributeDefinition.md) object
Required: No

 ** AttributeReference **   <a name="amazoncds-Type-FacetAttribute-AttributeReference"></a>
An attribute reference that is associated with the attribute. See [Attribute References](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html) for more information.
Type: [FacetAttributeReference](API_FacetAttributeReference.md) object
Required: No

 ** RequiredBehavior **   <a name="amazoncds-Type-FacetAttribute-RequiredBehavior"></a>
The required behavior of the `FacetAttribute`.
Type: String
Valid Values: `REQUIRED_ALWAYS | NOT_REQUIRED`
Required: No

## See Also
<a name="API_FacetAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/FacetAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/FacetAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/FacetAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
