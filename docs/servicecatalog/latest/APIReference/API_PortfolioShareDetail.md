---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_PortfolioShareDetail.html
---

# PortfolioShareDetail
<a name="API_PortfolioShareDetail"></a>

Information about the portfolio share.

## Contents
<a name="API_PortfolioShareDetail_Contents"></a>

 ** Accepted **   <a name="servicecatalog-Type-PortfolioShareDetail-Accepted"></a>
Indicates whether the shared portfolio is imported by the recipient account. If the recipient is in an organization node, the share is automatically imported, and the field is always set to true.
Type: Boolean
Required: No

 ** PrincipalARN **   <a name="servicecatalog-Type-PortfolioShareDetail-PrincipalARN"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** PrincipalId **   <a name="servicecatalog-Type-PortfolioShareDetail-PrincipalId"></a>
The identifier of the recipient entity that received the portfolio share. The recipient entity can be one of the following:
1. An external account.
2. An organziation member account.
3. An organzational unit (OU).
4. The organization itself. (This shares with every account in the organization).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** SharePrincipals **   <a name="servicecatalog-Type-PortfolioShareDetail-SharePrincipals"></a>
Indicates if `Principal` sharing is enabled or disabled for the portfolio share.
Type: Boolean
Required: No

 ** ShareTagOptions **   <a name="servicecatalog-Type-PortfolioShareDetail-ShareTagOptions"></a>
Indicates whether TagOptions sharing is enabled or disabled for the portfolio share.
Type: Boolean
Required: No

 ** Status **   <a name="servicecatalog-Type-PortfolioShareDetail-Status"></a>

Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`
Required: No

 ** Type **   <a name="servicecatalog-Type-PortfolioShareDetail-Type"></a>
The type of the portfolio share.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION | ORGANIZATIONAL_UNIT | ORGANIZATION_MEMBER_ACCOUNT`
Required: No

## See Also
<a name="API_PortfolioShareDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/PortfolioShareDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/PortfolioShareDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/PortfolioShareDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
