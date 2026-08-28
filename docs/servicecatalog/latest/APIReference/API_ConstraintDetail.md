---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ConstraintDetail.html
---

# ConstraintDetail
<a name="API_ConstraintDetail"></a>

Information about a constraint.

## Contents
<a name="API_ConstraintDetail_Contents"></a>

 ** ConstraintId **   <a name="servicecatalog-Type-ConstraintDetail-ConstraintId"></a>
The identifier of the constraint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Description **   <a name="servicecatalog-Type-ConstraintDetail-Description"></a>
The description of the constraint.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

 ** Owner **   <a name="servicecatalog-Type-ConstraintDetail-Owner"></a>
The owner of the constraint.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** PortfolioId **   <a name="servicecatalog-Type-ConstraintDetail-PortfolioId"></a>
The identifier of the portfolio the product resides in. The constraint applies only to the instance of the product that lives within this portfolio.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProductId **   <a name="servicecatalog-Type-ConstraintDetail-ProductId"></a>
The identifier of the product the constraint applies to. Note that a constraint applies to a specific instance of a product within a certain portfolio.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Type **   <a name="servicecatalog-Type-ConstraintDetail-Type"></a>
The type of constraint.
+  `LAUNCH`
+  `NOTIFICATION`
+ STACKSET
+  `TEMPLATE`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ConstraintDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ConstraintDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ConstraintDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ConstraintDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
