---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_OrganizationNode.html
---

# OrganizationNode
<a name="API_OrganizationNode"></a>

Information about the organization node.

## Contents
<a name="API_OrganizationNode_Contents"></a>

 ** Type **   <a name="servicecatalog-Type-OrganizationNode-Type"></a>
The organization node type.
Type: String
Valid Values: `ORGANIZATION | ORGANIZATIONAL_UNIT | ACCOUNT`
Required: No

 ** Value **   <a name="servicecatalog-Type-OrganizationNode-Value"></a>
The identifier of the organization node.
Type: String
Pattern: `(^[0-9]{12}$)|(^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32})|(^o-[a-z0-9]{10,32}$)|(^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}$)|(^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)`
Required: No

## See Also
<a name="API_OrganizationNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/OrganizationNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/OrganizationNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/OrganizationNode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
