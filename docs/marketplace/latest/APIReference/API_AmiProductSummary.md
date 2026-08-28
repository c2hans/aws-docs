---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_AmiProductSummary.html
---

# AmiProductSummary
<a name="API_AmiProductSummary"></a>

Object that contains summarized information about an AMI product.

## Contents
<a name="API_AmiProductSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-AmiProductSummary-ProductTitle"></a>
The title of the AMI product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-AmiProductSummary-Visibility"></a>
The lifecycle of the AMI product.
Type: String
Valid Values: `Limited | Public | Restricted | Draft`
Required: No

## See Also
<a name="API_AmiProductSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/AmiProductSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/AmiProductSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/AmiProductSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
