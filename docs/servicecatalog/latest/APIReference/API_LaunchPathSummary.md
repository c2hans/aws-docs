---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_LaunchPathSummary.html
---

# LaunchPathSummary
<a name="API_LaunchPathSummary"></a>

Summary information about a product path for a user.

## Contents
<a name="API_LaunchPathSummary_Contents"></a>

 ** ConstraintSummaries **   <a name="servicecatalog-Type-LaunchPathSummary-ConstraintSummaries"></a>
The constraints on the portfolio-product relationship.
Type: Array of [ConstraintSummary](API_ConstraintSummary.md) objects
Required: No

 ** Id **   <a name="servicecatalog-Type-LaunchPathSummary-Id"></a>
The identifier of the product path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Name **   <a name="servicecatalog-Type-LaunchPathSummary-Name"></a>
The name of the portfolio that contains the product.
Type: String
Required: No

 ** Tags **   <a name="servicecatalog-Type-LaunchPathSummary-Tags"></a>
The tags associated with this product path.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_LaunchPathSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/LaunchPathSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/LaunchPathSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/LaunchPathSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
