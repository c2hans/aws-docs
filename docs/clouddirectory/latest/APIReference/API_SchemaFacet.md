---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_SchemaFacet.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
