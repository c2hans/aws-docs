---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsProductDetails.html
---

# AwsProductDetails
<a name="API_AwsProductDetails"></a>

List of AWS services with program eligibility indicators (MAP, modernization pathways), cost estimates, and optimization recommendations.

## Contents
<a name="API_AwsProductDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Categories **   <a name="AWSPartnerCentral-Type-AwsProductDetails-Categories"></a>
List of program and pathway categories this product is eligible for.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** Optimizations **   <a name="AWSPartnerCentral-Type-AwsProductDetails-Optimizations"></a>
List of specific optimization recommendations for this product.
Type: Array of [AwsProductOptimization](API_AwsProductOptimization.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** ProductCode **   <a name="AWSPartnerCentral-Type-AwsProductDetails-ProductCode"></a>
AWS Partner Central product identifier used for opportunity association.
Type: String
Required: Yes

 ** Amount **   <a name="AWSPartnerCentral-Type-AwsProductDetails-Amount"></a>
Baseline service cost before optimizations.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: No

 ** OptimizedAmount **   <a name="AWSPartnerCentral-Type-AwsProductDetails-OptimizedAmount"></a>
Service cost after applying optimizations.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: No

 ** PotentialSavingsAmount **   <a name="AWSPartnerCentral-Type-AwsProductDetails-PotentialSavingsAmount"></a>
Service-specific cost reduction through optimizations.
Type: String
Pattern: `(0|([1-9][0-9]{0,30}))(\.[0-9]{0,2})?`
Required: No

 ** ServiceCode **   <a name="AWSPartnerCentral-Type-AwsProductDetails-ServiceCode"></a>
Pricing Calculator service code.
Type: String
Required: No

## See Also
<a name="API_AwsProductDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsProductDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsProductDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsProductDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
