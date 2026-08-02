---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_SchemaFacet.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# SchemaFacet
<a name="API_SchemaFacet"></a>

A facet.

## Contents
<a name="API_SchemaFacet_Contents"></a>

 ** FacetName **   <a name="amazoncds-Type-SchemaFacet-FacetName"></a>
The name of the facet. If this value is set, SchemaArn must also be set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** SchemaArn **   <a name="amazoncds-Type-SchemaFacet-SchemaArn"></a>
The ARN of the schema that contains the facet with no minor component. See [Arn Examples](arns.md) and [In-Place Schema Upgrade](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html) for a description of when to provide minor versions. If this value is set, FacetName must also be set.
Type: String
Required: No

## See Also
<a name="API_SchemaFacet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/SchemaFacet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/SchemaFacet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/SchemaFacet)
