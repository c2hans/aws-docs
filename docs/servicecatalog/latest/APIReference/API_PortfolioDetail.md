---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_PortfolioDetail.html
---

# PortfolioDetail
<a name="API_PortfolioDetail"></a>

Information about a portfolio.

## Contents
<a name="API_PortfolioDetail_Contents"></a>

 ** ARN **   <a name="servicecatalog-Type-PortfolioDetail-ARN"></a>
The ARN assigned to the portfolio.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

 ** CreatedTime **   <a name="servicecatalog-Type-PortfolioDetail-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** Description **   <a name="servicecatalog-Type-PortfolioDetail-Description"></a>
The description of the portfolio.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

 ** DisplayName **   <a name="servicecatalog-Type-PortfolioDetail-DisplayName"></a>
The name to use for display purposes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Id **   <a name="servicecatalog-Type-PortfolioDetail-Id"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProviderName **   <a name="servicecatalog-Type-PortfolioDetail-ProviderName"></a>
The name of the portfolio provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## See Also
<a name="API_PortfolioDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/PortfolioDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/PortfolioDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/PortfolioDetail)
