---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsOpportunityRelatedEntities.html
---

# AwsOpportunityRelatedEntities
<a name="API_AwsOpportunityRelatedEntities"></a>

Represents other entities related to the AWS opportunity, such as AWS products, partner solutions, and marketplace offers. These associations help build a complete picture of the solution being sold.

## Contents
<a name="API_AwsOpportunityRelatedEntities_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsMarketplaceProducts **   <a name="AWSPartnerCentral-Type-AwsOpportunityRelatedEntities-AwsMarketplaceProducts"></a>
The AWS Marketplace product ARNs associated with this opportunity.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** AwsMarketplaceSolutions **   <a name="AWSPartnerCentral-Type-AwsOpportunityRelatedEntities-AwsMarketplaceSolutions"></a>
The AWS Marketplace solution ARNs associated with this opportunity.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** AwsProducts **   <a name="AWSPartnerCentral-Type-AwsOpportunityRelatedEntities-AwsProducts"></a>
Specifies the AWS products associated with the opportunity. This field helps track the specific products that are part of the proposed solution.
Type: Array of strings
Required: No

 ** Solutions **   <a name="AWSPartnerCentral-Type-AwsOpportunityRelatedEntities-Solutions"></a>
Specifies the partner solutions related to the opportunity. These solutions represent the partner's offerings that are being positioned as part of the overall AWS opportunity.
Type: Array of strings
Pattern: `S-[0-9]{1,19}`
Required: No

## See Also
<a name="API_AwsOpportunityRelatedEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsOpportunityRelatedEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsOpportunityRelatedEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsOpportunityRelatedEntities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
